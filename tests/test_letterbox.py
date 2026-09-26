import os
import unittest
import subprocess
from agents.video_merger_agent import _get_ffmpeg_bin
from core.letterbox import detect_letterbox_crop


class TestLetterboxDetection(unittest.TestCase):
    """Unit tests for CinemaScope and letterbox auto-detection."""

    @classmethod
    def setUpClass(cls):
        cls.ffmpeg_bin = _get_ffmpeg_bin()
        cls.temp_dir = os.path.abspath("temp")
        os.makedirs(cls.temp_dir, exist_ok=True)
        cls.clean_169 = os.path.join(cls.temp_dir, "test_clean_169.mp4")
        cls.letterboxed_219 = os.path.join(cls.temp_dir, "test_letterboxed_219.mp4")

        # 1. Synthesize clean 16:9 (1280x720) without black bars
        cmd1 = [
            cls.ffmpeg_bin, "-y",
            "-f", "lavfi", "-i", "testsrc=duration=1:size=1280x720:rate=24",
            "-c:v", "libx264", "-preset", "ultrafast",
            cls.clean_169
        ]
        subprocess.run(cmd1, capture_output=True)

        # 2. Synthesize 21:9 CinemaScope letterbox (1280x540 inside 1280x720 black container)
        flt = "color=c=black:s=1280x720:d=1[bg];testsrc=duration=1:size=1280x540:rate=24[fg];[bg][fg]overlay=0:90[out]"
        cmd2 = [
            cls.ffmpeg_bin, "-y",
            "-f", "lavfi", "-i", "nullsrc=s=1280x720:d=1",
            "-filter_complex", flt,
            "-map", "[out]",
            "-c:v", "libx264", "-preset", "ultrafast",
            cls.letterboxed_219
        ]
        subprocess.run(cmd2, capture_output=True)

    @classmethod
    def tearDownClass(cls):
        for p in [cls.clean_169, cls.letterboxed_219]:
            if p and os.path.exists(p):
                try:
                    os.remove(p)
                except Exception:
                    pass

    def test_clean_169_returns_none(self):
        """A full-frame 16:9 video should not be detected as letterboxed."""
        res = detect_letterbox_crop(self.clean_169, ffmpeg_bin=self.ffmpeg_bin, sample_timestamps=[0.5])
        self.assertIsNone(res)

    def test_letterboxed_219_detected(self):
        """A 21:9 letterboxed video should be accurately detected with crop coordinates."""
        res = detect_letterbox_crop(self.letterboxed_219, ffmpeg_bin=self.ffmpeg_bin, sample_timestamps=[0.5])
        self.assertIsNotNone(res)
        self.assertEqual(res["orig_w"], 1280)
        self.assertEqual(res["orig_h"], 720)
        # Active area is 1280x540 at (0, 90)
        self.assertAlmostEqual(res["w"], 1280, delta=16)
        self.assertAlmostEqual(res["h"], 540, delta=16)
        self.assertAlmostEqual(res["y"], 90, delta=16)
        self.assertTrue(res["crop_str"].startswith("crop="))


if __name__ == "__main__":
    unittest.main()
