"""
Automated tests verifying comprehensive audit fixes.
"""
import unittest
from unittest.mock import patch, MagicMock
from brain.memory import MovieState, TranscriptSegment
from brain.gemini_client import _FALLBACK_MODELS
from agents.qa_agent import QAAgent
from agents.audio_agent import AudioAgent


class TestAuditFixes(unittest.TestCase):

    def test_movie_state_subtitles_burned_flag(self):
        """Verify subtitles_burned exists on MovieState and defaults to False."""
        state = MovieState(movie_name="AuditTest")
        self.assertFalse(state.subtitles_burned)
        state.subtitles_burned = True
        self.assertTrue(state.subtitles_burned)

    def test_gemini_fallback_models_include_production(self):
        """Verify _FALLBACK_MODELS includes standard Google AI Studio production models."""
        for required_model in ["gemini-3.5-flash-lite", "gemini-3.1-flash-lite", "gemini-3.5-flash"]:
            self.assertIn(required_model, _FALLBACK_MODELS)

    def test_qa_agent_scene_id_collision_prevention(self):
        """Verify QAAgent does not collide 'scene_1' and 'action_bridge_1' into '1'."""
        qa = QAAgent()
        state = MovieState(movie_name="CollisionTest")
        state.language = "english"
        state.generated_script = [
            {
                "scene_id": "scene_1",
                "narration": "Original narration for main scene 1 which is very long and needs to be shortened significantly to fit timing.",
                "start_sec": 0.0,
                "end_sec": 2.0,
            },
            {
                "scene_id": "action_bridge_1",
                "narration": "Original narration for bridge 1 which is also quite long and exceeds the allowed duration.",
                "start_sec": 2.0,
                "end_sec": 4.0,
            }
        ]

        fake_llm_response = """
        [
            {"scene_id": "scene_1", "rewritten_narration": "Short scene 1."},
            {"scene_id": "action_bridge_1", "rewritten_narration": "Short bridge 1."}
        ]
        """
        with patch("brain.gemini_client.call_gemini", return_value=(fake_llm_response, None)):
            with patch("brain.config.load_config", return_value={"gemini": {"enabled": True, "api_keys": ["fake-key"]}}):
                updated_state = qa.enforce_duration_constraints(state)

        # Both should have their OWN distinct rewritten narration
        script = updated_state.generated_script
        self.assertEqual(script[0]["narration"], "Short scene 1.")
        self.assertEqual(script[1]["narration"], "Short bridge 1.")

    def test_audio_agent_correct_transcript_preserves_all_segments(self):
        """Verify correct_transcript does not truncate large transcripts and preserves all segments."""
        state = MovieState(movie_name="TruncationTest")
        # Create 150 segments (which would previously exceed 40000 chars if long or get truncated)
        original_segments = [
            TranscriptSegment(start=float(i * 3), end=float(i * 3 + 2.5), text=f"Dialogue segment {i}")
            for i in range(150)
        ]
        state.transcript = list(original_segments)

        # Mock call_gemini to simulate a batch returning corrected text for each chunk
        def mock_call_gemini(sys_p, user_p, api_key, model=None, temperature=None):
            import re
            lines = re.findall(r'\[([\d.]+)-([\d.]+)\]\s*(.*)', user_p)
            segments_json = [{"start": float(l[0]), "end": float(l[1]), "text": f"Corrected {l[2]}"} for l in lines]
            import json
            return json.dumps(segments_json), None

        with patch("brain.gemini_client.call_gemini", side_effect=mock_call_gemini):
            with patch("brain.config.load_config", return_value={"gemini": {"enabled": True, "api_keys": ["fake-key"]}}):
                audio_agent = AudioAgent("dummy_path.mp4")
                res_state = audio_agent.correct_transcript(state)

        self.assertEqual(len(res_state.transcript), 150)
        self.assertTrue(res_state.transcript[0].text.startswith("Corrected Dialogue segment 0"))
        self.assertTrue(res_state.transcript[149].text.startswith("Corrected Dialogue segment 149"))

    def test_downloader_agent_none_filename_guard(self):
        """Verify DownloaderAgent handles None filename without raising TypeError."""
        from agents.downloader_agent import DownloaderAgent
        dl = DownloaderAgent(output_dir="temp_test_dl")
        with patch("yt_dlp.YoutubeDL") as mock_ydl_cls:
            mock_instance = MagicMock()
            mock_ydl_cls.return_value.__enter__.return_value = mock_instance
            mock_instance.extract_info.return_value = {"title": "dummy_video"}
            mock_instance.prepare_filename.return_value = None

            with self.assertRaises(FileNotFoundError) as ctx:
                dl.download_video("https://youtube.com/watch?v=dummy123")
            self.assertIn("Download seemed to succeed but file not found", str(ctx.exception))

    def test_qa_agent_review_model_workhorse_defined(self):
        """Verify QAAgent.review does not raise NameError for model_workhorse during language check."""
        qa = QAAgent()
        state = MovieState(movie_name="ModelWorkhorseTest")
        state.generated_script = [{"scene_id": "1", "narration": "မင်္ဂလာပါ။"}]
        cfg_mock = {
            "gemini": {
                "enabled": True,
                "api_keys": ["fake-key"],
                "models": {"workhorse": "gemini-3.5-flash-lite"}
            },
            "qa": {
                "enabled": True,
                "skip_video_qa": True,
                "language_check": True,
                "sync_check": False
            }
        }
        with patch("brain.config.load_config", return_value=cfg_mock):
            with patch.object(qa, "_run_language_check", return_value={"overall_language_score": 8, "blocks": []}):
                with patch.object(qa, "_save_reports"):
                    reviewed = qa.review(state, "dummy_orig.mp4", "dummy_recap.mp4")
                    self.assertIsNotNone(reviewed.qa_results)
                    self.assertEqual(reviewed.qa_results.get("language", {}).get("overall_language_score"), 8)

    def test_anti_copyright_zoom_independent_of_color_grading(self):
        """Verify zoom/crop is preserved even when color_grading=False."""
        from core.anti_copyright import build_video_anti_copyright_filters
        filters_no_color = build_video_anti_copyright_filters(mirror=False, color_grading=False)
        self.assertTrue(any("scale=1.02*iw:1.02*ih" in f for f in filters_no_color))
        self.assertFalse(any("eq=contrast" in f for f in filters_no_color))

    def test_video_blur_even_dimensions_truncation(self):
        """Verify build_boxblur_filter uses trunc(.../2)*2 for even pixel dimensions in FFmpeg."""
        from core.video_blur import build_boxblur_filter
        crop_blur, overlay_pos = build_boxblur_filter(start_y_pct=0.82, height_pct=0.18)
        self.assertIn("trunc(ih*", crop_blur)
        self.assertIn("/2)*2", crop_blur)
        self.assertIn("trunc(H*", overlay_pos)

    def test_gemini_fallback_models_include_requested_and_active(self):
        """Verify _FALLBACK_MODELS contains both active 3.6/3-preview and legacy requested models."""
        from brain.gemini_client import _FALLBACK_MODELS
        expected_models = [
            "gemini-3.6-flash",
            "gemini-3-flash-preview",
            "gemini-2.5-flash",
            "gemini-2.0-flash",
            "gemini-1.5-flash",
        ]
        for m in expected_models:
            self.assertIn(m, _FALLBACK_MODELS)

    def test_web_ui_and_services_state_synchronization(self):
        """Verify web_ui and services share identical state references."""
        import web_ui
        import services.job_manager
        import services.queue_manager
        self.assertIs(web_ui.jobs, services.job_manager.jobs)
        self.assertIs(web_ui.jobs_lock, services.job_manager.jobs_lock)
        self.assertIs(web_ui.job_queue, services.queue_manager.job_queue)
        self.assertIs(web_ui.queue_lock, services.queue_manager.queue_lock)

    def test_foreign_script_detection_and_particle_sanitization(self):
        """Verify foreign script detection and Burmese dialogue particle sanitization."""
        from brain.burmese_utils import has_untranslated_foreign_script, sanitize_dialogue_persona_particles
        # Foreign script checks
        self.assertTrue(has_untranslated_foreign_script("你好，这是测试"))
        self.assertTrue(has_untranslated_foreign_script("မင်္ဂလာပါ 姑娘"))
        self.assertTrue(has_untranslated_foreign_script("こんにちは"))
        self.assertTrue(has_untranslated_foreign_script("안녕하세요"))
        self.assertFalse(has_untranslated_foreign_script("မင်္ဂလာပါ ခင်ဗျာ။"))
        self.assertFalse(has_untranslated_foreign_script("Hello world!"))

        # Dialogue persona particle sanitization (remove robotic polite particles before/after !)
        cleaned_threat = sanitize_dialogue_persona_particles("သေစမ်းပါ ခင်ဗျာ!")
        self.assertNotIn("ခင်ဗျာ!", cleaned_threat)
        self.assertIn("!", cleaned_threat)

        cleaned_female = sanitize_dialogue_persona_particles("သွားစမ်းပါ ရှင့်!")
        self.assertNotIn("ရှင့်!", cleaned_female)

        cleaned_negative = sanitize_dialogue_persona_particles("မလုပ်နဲ့ ခင်ဗျာ")
        self.assertNotIn("ခင်ဗျာ", cleaned_negative)

    @patch("hardsub_engine.call_gemini")
    def test_hardsub_engine_auto_repairs_foreign_leakage(self, mock_gemini):
        """Verify HardsubEngine detects foreign script leakage and auto-repairs via Gemini."""
        from hardsub_engine import HardsubEngine
        engine = HardsubEngine()
        engine.config_data = {"gemini": {"api_keys": ["fake-key"]}}

        segments = [
            {"id": 1, "original": "姑娘，你没事吧？", "burmese": "姑娘，你没事吧？"},
            {"id": 2, "original": "谢谢你。", "burmese": "ကျေးဇူးတင်ပါတယ် ခင်ဗျာ။"}
        ]
        # Repair pass returns pure Myanmar
        mock_gemini.return_value = ('[{"id": 1, "burmese": "မိန်းကလေး၊ ဘာမှမဖြစ်ဘူးမဟုတ်လား။", "speaker_gender": "male"}]', 0)

        repaired = engine._audit_and_repair_untranslated(segments, translation_style="wuxia")
        self.assertEqual(repaired[0]["burmese"], "မိန်းကလေး၊ ဘာမှမဖြစ်ဘူးမဟုတ်လား")
        self.assertEqual(repaired[1]["burmese"], "ကျေးဇူးတင်ပါတယ် ခင်ဗျာ")
        self.assertEqual(engine.last_damaged_count, 1)
        self.assertEqual(engine.last_repaired_count, 1)

    def test_strip_trailing_subtitle_punctuation(self):
        """Verify trailing punctuation marks ( ၊ , ။ ) are stripped from subtitle line endings."""
        from brain.burmese_utils import strip_trailing_subtitle_punctuation
        # Burmese period (double danda) stripped at end
        self.assertEqual(strip_trailing_subtitle_punctuation("မင်္ဂလာပါ ခင်ဗျာ။"), "မင်္ဂလာပါ ခင်ဗျာ")
        # Burmese comma stripped at end
        self.assertEqual(strip_trailing_subtitle_punctuation("ဒါပေမဲ့၊"), "ဒါပေမဲ့")
        # English comma stripped at end
        self.assertEqual(strip_trailing_subtitle_punctuation("ဟုတ်ကဲ့ပါ,"), "ဟုတ်ကဲ့ပါ")
        # Multiple trailing punctuation / spaces stripped
        self.assertEqual(strip_trailing_subtitle_punctuation("ကျေးဇူးတင်ပါတယ် ခင်ဗျာ။   "), "ကျေးဇူးတင်ပါတယ် ခင်ဗျာ")
        # Internal commas preserved for natural speech flow
        self.assertEqual(strip_trailing_subtitle_punctuation("မင်္ဂလာပါ၊ ကျနော်ကတော့ မင်းသားပါ။"), "မင်္ဂလာပါ၊ ကျနော်ကတော့ မင်းသားပါ")
        # Exclamation and question marks preserved
        self.assertEqual(strip_trailing_subtitle_punctuation("မင်း သေချင်နေတာလား!"), "မင်း သေချင်နေတာလား!")
        self.assertEqual(strip_trailing_subtitle_punctuation("ဘယ်သူလဲ?"), "ဘယ်သူလဲ?")
        # Multi-line with \n and \N
        self.assertEqual(
            strip_trailing_subtitle_punctuation("အဲဒီအချိန်မှာ၊\nသူမ ရောက်လာခဲ့တယ်။"),
            "အဲဒီအချိန်မှာ\nသူမ ရောက်လာခဲ့တယ်"
        )
        self.assertEqual(
            strip_trailing_subtitle_punctuation("ပထမစာကြောင်း၊\\Nဒုတိယစာကြောင်း။"),
            "ပထမစာကြောင်း\\Nဒုတိယစာကြောင်း"
        )

    def test_format_dual_speaker_subtitles(self):
        """Verify dual-speaker dialogue dashes are cleanly formatted with \\N and stripped punctuation."""
        from brain.burmese_utils import format_dual_speaker_subtitles
        res1 = format_dual_speaker_subtitles("- Are you ready? - Yes, I am.")
        self.assertEqual(res1, "- Are you ready?\\N- Yes, I am.")

        res2 = format_dual_speaker_subtitles("- အဆင်သင့်ဖြစ်ပြီလား? - ဟုတ်ကဲ့၊ အဆင်သင့်ပါပဲ။")
        self.assertEqual(res2, "- အဆင်သင့်ဖြစ်ပြီလား?\\N- ဟုတ်ကဲ့၊ အဆင်သင့်ပါပဲ")

        single = format_dual_speaker_subtitles("မင်္ဂလာပါ ခင်ဗျာ။")
        self.assertEqual(single, "မင်္ဂလာပါ ခင်ဗျာ")

    def test_merge_short_gap_segments(self):
        """Verify micro-gap fragmented subtitle segments are merged into coherent lines."""
        from brain.burmese_utils import merge_short_gap_segments
        segs = [
            {"id": 1, "start": 1.0, "end": 2.0, "original": "Wait for me"},
            {"id": 2, "start": 2.1, "end": 3.2, "original": "I am coming"},
            {"id": 3, "start": 5.0, "end": 6.5, "original": "Longer pause here."},
            {"id": 4, "start": 6.6, "end": 7.5, "original": "After sentence end"},
        ]
        merged = merge_short_gap_segments(segs, max_gap=0.25, max_combined_dur=5.0)
        self.assertEqual(len(merged), 3)
        self.assertEqual(merged[0]["original"], "Wait for me I am coming")
        self.assertEqual(merged[0]["start"], 1.0)
        self.assertEqual(merged[0]["end"], 3.2)
        # Sentence ending with '.' was not merged even with short gap
        self.assertEqual(merged[1]["original"], "Longer pause here.")
        self.assertEqual(merged[2]["original"], "After sentence end")

    def test_localize_common_idioms(self):
        """Verify common movie idioms and insults are localized naturally."""
        from brain.burmese_utils import localize_common_idioms
        self.assertIn("ငါ့နောက်ကသာ ပြေးလိုက်ခဲ့တော့", localize_common_idioms("Eat my dust!"))
        self.assertIn("အသေပဲ", localize_common_idioms("You are dead meat!"))
        self.assertIn("ပါးစပ်ပိတ်ထား", localize_common_idioms("Just shut up!"))
        self.assertIn("ငါ့ကို အရင်သတ်သွားလိုက်", localize_common_idioms("Over my dead body."))


if __name__ == "__main__":
    unittest.main()
