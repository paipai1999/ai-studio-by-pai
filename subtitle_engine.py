"""
Subtitle & Transcript Engine (Burmese Subtitle Engine Wrapper)
=============================================================
Provides backward-compatibility for Google Colab, Kaggle, and CLI callers
by routing subtitle/transcript production directly to main.py / MasterAgent.
"""
import sys
import subprocess

if __name__ == "__main__":
    args = sys.argv[1:]
    cmd = [sys.executable, "main.py"]
    # If -i was provided as first arg, map it cleanly
    clean_args = []
    i = 0
    while i < len(args):
        if args[i] == "-i" and i + 1 < len(args):
            clean_args.append(args[i + 1])
            i += 2
        else:
            clean_args.append(args[i])
            i += 1

    has_mode = any(a in ("--mode", "--script-engine") for a in clean_args)
    if not has_mode:
        cmd.extend(["--mode", "translate"])

    has_sub_mode = any(a in ("--sub-mode", "--subtitle-mode") for a in clean_args)
    if not has_sub_mode and "--no-render" in clean_args:
        cmd.extend(["--sub-mode", "none"])

    cmd.extend(clean_args)
    sys.exit(subprocess.call(cmd))
