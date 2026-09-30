import os
import codecs
import pytest
from brain.memory import MovieState, TranscriptSegment
from core.subtitle_builder import write_srt_file
from core.capcut_pack import export_capcut_package
from agents.audio_agent import AudioAgent


def test_write_srt_file_with_bom(tmp_path):
    srt_path = str(tmp_path / "test.srt")
    segments = [
        {"start_s": 0.0, "end_s": 2.5, "burmese": "မင်္ဂလာပါ ခင်ဗျာ။"},
        {"start_s": 2.5, "end_s": 5.0, "burmese": "ဒီနေ့ ရုပ်ရှင်ဇာတ်လမ်းကတော့ စိတ်လှုပ်ရှားစရာပါ။"}
    ]
    res_path = write_srt_file(srt_path, segments, with_bom=True)
    assert os.path.exists(res_path)

    with open(res_path, "rb") as f:
        content_bytes = f.read()

    # Verify UTF-8 BOM signature (\xef\xbb\xbf)
    assert content_bytes.startswith(codecs.BOM_UTF8)
    text_content = content_bytes.decode("utf-8-sig")
    assert "မင်္ဂလာပါ ခင်ဗျာ" in text_content
    assert "00:00:00,000 --> 00:00:02,500" in text_content


def test_export_capcut_package(tmp_path):
    output_dir = str(tmp_path / "outputs")
    os.makedirs(output_dir, exist_ok=True)

    movie_name = "test_movie_action"
    project_slug = movie_name
    proj_dir = os.path.join(output_dir, project_slug)
    os.makedirs(proj_dir, exist_ok=True)

    # Create dummy source video
    dummy_video = os.path.join(proj_dir, "clean_source.mp4")
    with open(dummy_video, "wb") as f:
        f.write(b"fake_mp4_bytes")

    # Create dummy thumbnail
    dummy_thumb = os.path.join(proj_dir, "thumbnail.jpg")
    with open(dummy_thumb, "wb") as f:
        f.write(b"fake_jpg_bytes")

    # Create dummy audio / sfx
    dummy_sfx = os.path.join(proj_dir, "dummy_sfx.mp3")
    with open(dummy_sfx, "wb") as f:
        f.write(b"fake_sfx_mp3_bytes")

    dummy_vo = os.path.join(proj_dir, "final_recap_speech.mp3")
    with open(dummy_vo, "wb") as f:
        f.write(b"fake_voiceover_mp3_bytes")

    state = MovieState(movie_name=movie_name)
    state.movie_path = dummy_video
    state.thumbnail_path = dummy_thumb
    state.sfx_path = dummy_sfx
    state.voiceover_path = dummy_vo
    state.duration_sec = 60.0
    state.transcript = [
        TranscriptSegment(start=0.0, end=3.0, text="လူဆိုးကြီးက မြို့ထဲကို ရောက်လာခဲ့ပါတယ်။")
    ]
    state.generated_script = [
        {
            "speaker": "Narrator",
            "start_sec": 0.0,
            "end_sec": 3.0,
            "narration": "လူဆိုးကြီးက မြို့ထဲကို ရောက်လာခဲ့ပါတယ်။"
        }
    ]
    state.seo_metadata = {
        "title": "Action Movie Recap",
        "description": "စိတ်လှုပ်ရှားဖွယ် ဇာတ်လမ်းတွဲ",
        "hashtags": ["#Action", "#Recap"]
    }

    result = export_capcut_package(state, output_dir, movie_path=dummy_video)

    assert os.path.isdir(result["pack_dir"])
    assert os.path.isfile(result["zip_path"])

    files = result["files"]
    assert "01_video" in files and os.path.exists(files["01_video"])
    assert "02_voiceover" in files and os.path.exists(files["02_voiceover"])
    assert "03_background_sfx" in files and os.path.exists(files["03_background_sfx"])
    assert "04_subtitles" in files and os.path.exists(files["04_subtitles"])
    assert "05_script" in files and os.path.exists(files["05_script"])
    assert "06_thumbnail" in files and os.path.exists(files["06_thumbnail"])
    assert "07_upload_info" in files and os.path.exists(files["07_upload_info"])

    # Verify subtitle BOM
    with open(files["04_subtitles"], "rb") as sf:
        assert sf.read().startswith(codecs.BOM_UTF8)

    # Verify state updated
    assert state.capcut_pack_dir == result["pack_dir"]
    assert state.capcut_zip_path == result["zip_path"]


def test_audio_agent_extract_sfx_nonexistent():
    agent = AudioAgent()
    res = agent.extract_sfx("non_existent_audio.wav", "outputs")
    assert res is None


def test_web_ui_capcut_mode_dispatch():
    from unittest.mock import patch
    from fastapi.testclient import TestClient
    from web_ui import app

    client = TestClient(app)
    with patch("web_ui._resolve_input_source", return_value="dummy.mp4"):
        with patch("os.path.exists", return_value=True):
            with patch("threading.Thread") as mock_thread:
                resp = client.post("/api/start", json={
                    "input": "dummy.mp4",
                    "engine_mode": "capcut"
                })
                assert resp.status_code == 200
                data = resp.json()
                assert "job_id" in data
                assert mock_thread.called
                call_args = mock_thread.call_args[1]["args"]
                # In pipeline_worker args, eff_render_video is at index 31
                # Check that render_video is False
                assert call_args[31] is False

                # Clean up memory
                import web_ui
                with web_ui.jobs_lock:
                    web_ui.jobs.pop(data["job_id"], None)
