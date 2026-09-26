import os
import sys
import unittest
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agents.downloader_agent import DownloaderAgent
import web_ui


class TestDownloaderFeature(unittest.TestCase):

    def test_is_url(self):
        """Verify URL validation patterns."""
        self.assertTrue(DownloaderAgent.is_url("https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
        self.assertTrue(DownloaderAgent.is_url("https://youtu.be/dQw4w9WgXcQ"))
        self.assertTrue(DownloaderAgent.is_url("http://example.com/video.mp4"))
        self.assertFalse(DownloaderAgent.is_url("local_movie.mp4"))
        self.assertFalse(DownloaderAgent.is_url("movies/trailer.mp4"))

    def test_clean_url(self):
        """Verify tracking parameters are cleaned from YouTube URLs."""
        dirty = "https://www.youtube.com/watch?v=dQw4w9WgXcQ&feature=share&si=abc123xyz"
        clean = DownloaderAgent._clean_url(dirty)
        self.assertEqual(clean, "https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    def test_download_video_signature_and_resolution(self):
        """Verify download_video supports resolution and custom_filename options."""
        dl = DownloaderAgent(output_dir="temp_test_dl")
        with patch("yt_dlp.YoutubeDL") as mock_ydl:
            mock_inst = MagicMock()
            mock_ydl.return_value.__enter__.return_value = mock_inst
            mock_inst.extract_info.return_value = {"title": "TestVideo", "ext": "mp4"}
            mock_inst.prepare_filename.return_value = os.path.join("temp_test_dl", "TestVideo.mp4")

            # Mock file existence and size
            with patch("os.path.exists", return_value=True), patch("os.path.getsize", return_value=5000):
                res_path = dl.download_video(
                    "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                    resolution="720p",
                    custom_filename="CustomTest"
                )
                self.assertTrue(res_path.endswith(".mp4"))
                # Check options passed to YoutubeDL
                call_opts = mock_ydl.call_args[0][0]
                self.assertIn("720", call_opts["format"])
                self.assertIn("CustomTest", call_opts["outtmpl"])

    def test_web_ui_download_request_schema(self):
        """Verify DownloadVideoRequest validation."""
        req = web_ui.DownloadVideoRequest(
            url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
            resolution="1080p",
            custom_name="MyMovie"
        )
        self.assertEqual(req.url, "https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        self.assertEqual(req.resolution, "1080p")
        self.assertEqual(req.custom_name, "MyMovie")


if __name__ == "__main__":
    unittest.main()
