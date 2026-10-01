"""
Original Audio & Burmese Hardsub Studio Engine Wrapper
======================================================
Provides backward-compatibility for Google Colab, Kaggle, and CLI callers
by routing hardsub production directly to main.py / MasterAgent with 100% original audio.
"""
import sys
import subprocess

if __name__ == "__main__":
    args = sys.argv[1:]
    cmd = [sys.executable, "main.py"]
    has_audio_mode = any(a == "--audio-mode" for a in args)
    if not has_audio_mode:
        cmd.extend(["--audio-mode", "original"])

    has_mode = any(a in ("--mode", "--script-engine") for a in args)
    if not has_mode:
        cmd.extend(["--mode", "translate"])

    has_sub_mode = any(a in ("--sub-mode", "--subtitle-mode") for a in args)
    if not has_sub_mode:
        cmd.extend(["--sub-mode", "burn"])

    cmd.extend(args)
    sys.exit(subprocess.call(cmd))
