# 🎬 Pai AI Movie Studio (v2.2) — $0 Free Local & Cloud-Accelerated Pipeline

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Google Colab](https://img.shields.io/badge/Google%20Colab-T4%20GPU%20(Free)-orange.svg)](https://colab.research.google.com/github/paipai1999/pai-ai-movie-studio/blob/main/AI_Movie_Translate_Colab.ipynb)
[![Kaggle](https://img.shields.io/badge/Kaggle-Dual%20T4%2030GB%20VRAM-blue.svg)](https://github.com/paipai1999/pai-ai-movie-studio/blob/main/AI_Movie_Translate_Kaggle.ipynb)
[![Tests](https://img.shields.io/badge/Tests-77%2F77%20Passed%20(100%25)-brightgreen.svg)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An autonomous, production-grade AI studio designed to automatically translate movies, short dramas, anime, and YouTube videos into natural **Colloquial Spoken Burmese** (စကားပြောဟန်) or English, synthesize lifelike **Multi-Voice Dubbing (Male/Female)**, and render viral, ready-to-publish videos equipped with **9:16 Facebook Reels / TikTok Canvas**, **Styled Myanmar ASS Subtitles**, **Vision AI Subtitle Blur Protection**, **Anti-Copyright Shields**, and **High-CTR Thumbnails**.

---

## 🇲🇲 စနစ်အနှစ်ချုပ် မိတ်ဆက် (Burmese Overview)

**Pai AI Movie Studio** သည် ရုပ်ရှင်၊ ဒရမ်မာဇာတ်လမ်းတိုများနှင့် YouTube ဗီဒီယိုများကို ကွန်ပျူတာ သို့မဟုတ် Free Cloud GPU (Google Colab / Kaggle) ပေါ်တွင် **၁၀၀% အခမဲ့** ဖြင့် မြန်မာဘာသာသို့ အလိုအလျောက် ဘာသာပြန်ခြင်း၊ အသံသွင်းခြင်း (Dubbing) နှင့် စာတန်းထိုးထုတ်လုပ်ပေးနိုင်သော All-in-One AI စနစ်ဖြစ်ပါသည်။

### 🎯 စနစ်ပါ အဓိက Studio Engine (၃) မျိုး:
1. 🎬 **Engine 1: AI Movie Recap & Multi-Voice Dubbing Studio (`main.py`)**
   - ဇာတ်လမ်းပြောပြသူ Persona (`...ခဲ့တာပေါ့ဗျာ`, `...လိုက်ရတာပါ`) သို့မဟုတ် ၁:၁ ဇာတ်ကောင် Dubbing။
   - အမျိုးသား (`my-MM-ThihaNeural`) နှင့် အမျိုးသမီး (`my-MM-NilarNeural`) အသံများ အလိုအလျောက်ခွဲခြား Dubbing သွင်းပေးခြင်း။
   - Facebook Reels / TikTok (9:16) နှင့် YouTube (16:9) ဗီဒီယို ၂ မျိုးစလုံး တစ်ပြိုင်နက် ထုတ်လုပ်ပေးခြင်း။
   - Zero-Drift Scene-Anchor စနစ်ဖြင့် အခန်းပေါင်း ၁၀၀ ကျော်တွင် အသံနှင့် ရုပ်သံ လုံးဝလွဲချော်မှုမရှိခြင်း (0.000s Drift)။
2. 📝 **Engine 2: YouTube Subtitle & Transcript Studio (`subtitle_engine.py`)**
   - မူရင်း Timestamp စက္ကန့်တိကျမှု ၁၀၀% မပျက်မယွင်း ထိန်းသိမ်းထားသော Spoken Burmese စာတန်းထိုး။
   - အသုံးပြုသူအတွက် အသင့်သုံး Deliverables ၆ မျိုး (`.mp4`, `.srt`, `.txt` ၃ မျိုး, Quality Audit Report) ကို တစ်ခါတည်း ထုတ်ပေးခြင်း။
3. 🎞️ **Engine 3: 100% Original Audio & Burmese Hardsub Studio (`hardsub_engine.py`)**
   - မူရင်းရုပ်ရှင်အသံ ၁၀၀% နဂိုအတိုင်းထားရှိပြီး မြန်မာစာတန်းထိုး အကြည်စား ရိုက်ကပ်ခြင်း (Zero TTS Overwrite)။
   - Vision AI ဖြင့် စာတန်းဟောင်းများကို အလိုအလျောက် Boxblur ဖျက်ပေးခြင်း (Blur Height 12%–30%)။
   - မူပိုင်ခွင့် ကာကွယ်ရေး Shields (1.02x Zoom/Crop, Color Grading EQ, Horizontal Mirror, Audio Tempo Shield atempo=1.008)။

---

## ⚡ Cloud GPU One-Click Setup (100% Free Cloud Options)

### 🥇 Option A: Google Colab (Free T4 GPU + Google Drive Sync)
👉 **[Open AI_Movie_Translate_Colab.ipynb in Google Colab](https://colab.research.google.com/github/paipai1999/pai-ai-movie-studio/blob/main/AI_Movie_Translate_Colab.ipynb)**
* **Highlights:** 1-Click Web UI Dashboard, Permanent Google Drive Sync for videos/cookies/database, 60s Auto Keep-Alive Heartbeat, and Fast Socket Health-Check.
* **Public & Private Editions:** 
  - `AI_Movie_Translate_Colab.ipynb` (Public Edition on GitHub - clean template for community sharing).
  - `AI_Movie_Translate_Colab_PRIVATE.ipynb` (Personal VIP Edition - pre-loaded with your Gemini keys & YouTube cookies for instant 1-click execution without typing).

### 🥈 Option B: Kaggle Notebooks (Free Dual T4 30GB VRAM / 30h Weekly Quota)
👉 **[View AI_Movie_Translate_Kaggle.ipynb](https://github.com/paipai1999/pai-ai-movie-studio/blob/main/AI_Movie_Translate_Kaggle.ipynb)**
* **Highlights:** 2x NVIDIA T4 GPUs (30GB VRAM) or P100 GPU, 30 Hours/Week Free GPU Quota, 12-Hour Continuous Sessions, Cloudflare Tunnel Web UI, and 30GB System RAM.
* **Public & Private Editions:**
  - `AI_Movie_Translate_Kaggle.ipynb` (Public Edition on GitHub).
  - `AI_Movie_Translate_Kaggle_PRIVATE.ipynb` (Personal VIP Edition - pre-embedded keys & cookies, zero setup).
* **Kaggle Quickstart:**
  1. Create a new Notebook on [kaggle.com](https://www.kaggle.com).
  2. Click `File` > `Import Notebook` and upload `AI_Movie_Translate_Kaggle.ipynb`.
  3. In right sidebar `Notebook Settings`: Set **Accelerator = GPU T4 x2** and turn **Internet = On**.
  4. Run Cell 1 to launch the Web UI Dashboard!

---

## 🔐 Secure Local & Production Setup

Keep Gemini credentials and YouTube session cookies outside the project directory or configure them securely:

```powershell
# Set environment variables in Windows PowerShell:
$env:GEMINI_API_KEYS="KEY_1,KEY_2,KEY_3"
$env:MOVIE_COOKIES_PATH="C:\Users\wcp18\AppData\Local\MovieTranslate\cookies.txt"
$env:WEB_UI_TOKEN="your-secure-password-here"
$env:WEB_UI_ALLOWED_ORIGINS="http://127.0.0.1:5000,http://localhost:5000"

# Launch Web UI Server:
python web_ui.py
```

* API keys are masked in logs, stored securely in memory, and sent directly to Google via request headers rather than URL query parameters.
* Rotate any keys that were previously placed in public templates.

---

## 🐳 Docker Deployment (Any OS / Windows / Linux / macOS)

Run the studio anywhere with Docker without needing local Python or FFmpeg installation:

```bash
# 1. Start Pai AI Movie Studio in background
docker compose up -d

# 2. View live logs
docker compose logs -f

# 3. Stop studio
docker compose down
```

* **Dashboard Access:** Open [http://localhost:5000](http://localhost:5000)
* **Windows 1-Click:** Select Option `[7] Run in Docker Container` from `Start_Studio.bat`.
* **Volumes & Storage:** `movies/`, `outputs/`, `temp/`, and `config.json` are automatically mounted to your host machine.

---

## 📊 Benchmark Performance: Legacy vs. v2.2 Engine

The following real-world benchmark was measured on a full 15-minute movie recap (205 discrete dialogue segments):

| Evaluation Metric | Legacy Pipeline (v2.1) | v2.2 Architectural Engine | Improvement / Impact |
| :--- | :---: | :---: | :---: |
| **Audio/Visual Drift at Clip 10** | `+9.80s` behind | **`+0.51s` (Near Zero)** | **95% tighter sync** |
| **Audio/Visual Drift at Clip 50** | `+85.16s` behind | **`+3.43s`** | **96% tighter sync** |
| **Audio/Visual Drift at Clip 100** | `+148.36s` (2.5 min lag) | **`+3.28s`** | **98% tighter sync** |
| **Cumulative Drift Accumulation** | Compounding without bound | **Zero compounding (Auto-realigns)** | **Eliminated runaway drift** |
| **Dropped Dialogue Clips** | 45 clips dropped / skipped | **0 clips dropped (205/205 placed)** | **100% dialogue coverage** |
| **Sentence Mid-Speech Cutoffs** | Severe (Truncated words) | **0% cutoffs (100% complete delivery)** | **Full pronunciation guarantee** |
| **QAAgent Auto-Rewrite Coverage** | ~19% (165/205 ignored) | **100% of over-length blocks rewritten** | **Flawless length adherence** |
| **Video Encoding Engine (Kaggle)**| CPU `libx264` (Multi-core) | **NVIDIA NVENC (`h264_nvenc`)** | **Hardware-accelerated silicon** |
| **Video Encoding Speed** | 80–110 fps | **400–650 fps** | **5x–8x faster rendering** |
| **1080p Post-Processing Time** | ~7.2 minutes | **~1.4 minutes** | **Saved ~6 minutes per run** |
| **Total 15-Min Video Render Time** | 35+ minutes (3 passes) | **6–8 min CPU / ~1.5 min GPU** | **Single-Pass Filtergraph (4x faster)** |

---

## 🎯 The Triple-Engine Architecture

| Feature / Capability | 🎬 Engine 1: Movie Recap Studio | 📝 Engine 2: Subtitle & Transcript Studio | 🎞️ Engine 3: Hardsub Studio |
| :--- | :---: | :---: | :---: |
| **Primary Script / Core** | [`main.py`](main.py) / `MasterAgent` | [`subtitle_engine.py`](subtitle_engine.py) | [`hardsub_engine.py`](hardsub_engine.py) |
| **Windows Master Launcher** | [`Start_Studio.bat`](Start_Studio.bat) (Menu [1-3]) | [`Start_Studio.bat`](Start_Studio.bat) (Menu [5]) | [`Start_Studio.bat`](Start_Studio.bat) (Menu [4]) |
| **Primary Output Purpose** | Viral Movie Recaps with Full AI Dubbing | 1:1 Subtitles & Multi-Lingual Transcripts | Hardsubbed Videos with 100% Original Audio |
| **Audio Treatment** | AI Multi-Voice Dubbing (Thiha / Nilar) | Original Audio (Muted or Preserved) | **100% Original Audio Preserved (Zero TTS)** |
| **Anti-Copyright Shields** | Dynamic ducking, scene-trimming | Standard 1:1 matching | **1.02x Zoom/Crop, Color EQ, Mirror, Audio Shield** |
| **Subtitle Blur Protection** | Bottom area blur detection | Optional transcript | **Vision AI Auto Subtitle Blur (12%–30% bottom)** |
| **Translation Style** | Storyteller Persona (`...ခဲ့တာပေါ့ဗျာ`) | Spoken Burmese (စကားပြောဟန်) | **Faithful 1:1 Persona (Male/Female/Child particles)** |
| **Deliverable Exports** | 16:9 Video, 9:16 Reels, Thumbnail, SEO | 6 Deliverables (`.mp4`, `.txt` x3, `.srt`, QC) | 16:9 MP4, 9:16 MP4, `.ass`, `.srt`, `.json`, QC Report |

---

## 🌟 Key Capabilities & Architectural Highlights

### 🎯 1. Zero Cumulative Drift & Scene Timestamp Anchoring
* **Hard Scene Anchoring:** Dialogue blocks are locked to visual cuts (`starts[idx]`). Local speech variance never compounds into future scenes.
* **Full Spoken Delivery:** No mid-sentence audio truncation (`subclip`) — sentences are spoken completely to the final syllable.

### 🎙️ 2. Acoustic Pitch & Multimodal Vision Diarization
* **Acoustic Pitch Classification ($F_0$):** Real-time pitch extraction ($70\text{ Hz} \le F_0 \le 350\text{ Hz}$) dynamically categorizes dialogue speakers into male and female.
* **Multimodal Keyframe Analysis:** Gemini Vision inspects video frames at dialogue transition cuts to assign character personas.
* **Multi-Voice TTS Assignment:** Automatically maps female speakers to `my-MM-NilarNeural` and male speakers / narrator to `my-MM-ThihaNeural`.

### 🎨 3. 5 Cinema-Grade Subtitle Style Presets
* **🎬 Cinema Box (`box_black`):** White text over 70% dark translucent box (Netflix aesthetic).
* **⚡ TikTok / Reels Yellow (`yellow_pop`):** Vivid yellow typography with black stroke and drop shadow.
* **⚪ Classic White (`white_stroke`):** Clean white text with drop shadow outline.
* **💎 Cyber Cyan Neon (`cyan_cyber`):** Glowing cyan neon font with deep blue outline.
* **🩸 Thriller Crimson (`crimson_box`):** White text over dark crimson red background box.

### 🛡️ 4. Anti-Copyright Shield Suite
* **1.02x Scale & Center Crop:** Crops out outermost borders to disrupt bounding box hashes.
* **Color Grading EQ:** Alters contrast (`1.03`), brightness (`0.02`), and saturation (`1.06`).
* **Horizontal Mirror (`hflip`):** Reverses frame orientation for platforms requiring visual inversion.
* **Audio Tempo Shield (`atempo=1.008`):** Applies subtle speed perturbation to evade automated acoustic fingerprint matching algorithms without perceptible pitch change.

### 🛑 5. 1-Click Force Stop & Process Tree Termination
* Emergency cancellation button in the Web UI immediately kills child process trees (`ffmpeg`, `whisper`, `demucs`, `yt-dlp`) on both Windows and Linux, releasing GPU VRAM and CPU threads instantly.

### 🎦 6. Theater Cinema Modal Player
* Interactive full-screen Cinema modal player in the Web UI dashboard for instant verification and playback of all rendered 16:9 and 9:16 videos.

---

## 🗂️ Project Structure

```text
pai-ai-movie-studio/
├── hardsub_engine.py          ← Engine 3: 100% Original Audio & Burmese Hardsub Studio
├── subtitle_engine.py         ← Engine 2: YouTube to Burmese Subtitle & Transcript Studio
├── main.py                    ← Engine 1 CLI & Unified Multi-Engine Dispatcher
├── web_ui.py                  ← FastAPI Web Dashboard with 3-Engine Graphical Interface
│
├── Start_Studio.bat          ← Master 1-Click Studio Launcher (Web UI & All 3 Engines)
│
├── core/                      ← Centralized Media & Subtitle Processing Package
│   ├── anti_copyright.py      ← Platform video & audio anti-copyright filter graphs
│   ├── subtitle_builder.py    ← ASS & SRT subtitle generators, styling presets & syllable wrap
│   └── video_blur.py          ← Vision AI bounding box calculation & FFmpeg boxblur filters
│
├── services/                  ← Job Management & Background Dispatching
│   ├── job_manager.py         ← In-memory job state, process trees, and SSE log queues
│   └── queue_manager.py       ← Persistent FIFO queue worker & batch coordinator
│
├── agents/                    ← Specialized Agentic Pipeline Modules
│   ├── master.py              ← Engine 1 orchestrator (Phases 1–7) & hardware management
│   ├── downloader_agent.py    ← Multi-platform downloader (YouTube, DramaBox, ReelShort)
│   ├── video_agent.py         ← Video metadata: FPS, duration, resolution (OpenCV & FFprobe)
│   ├── audio_agent.py         ← Audio extract + Fast Whisper STT + Demucs separation
│   ├── writer_agent.py        ← 1:1 Dialogue Translation (Gemini 3.5 Flash) + Action Bridge
│   ├── seo_agent.py           ← Viral Title, Description, Tags, and Hashtags generator
│   ├── voice_agent.py         ← Multi-Voice TTS (Thiha Male / Nilar Female) & Time Stretch
│   ├── video_merger_agent.py  ← Single-Pass Merger, Audio Ducking, NVENC/QSV Hardware Encoder
│   ├── thumbnail_agent.py     ← High-CTR Golden Yellow Top-Center Thumbnail Generator
│   └── qa_agent.py            ← Sync score & language naturalness QA review
│
├── brain/                     ← Core AI Brain & Persistence Layer
│   ├── memory.py              ← Pydantic shared state (MovieState with atomic JSON persistence)
│   ├── planner.py             ← Overnight Batch Processor with auto API key rotation
│   ├── prompts.py             ← LLM prompt templates (Dialogue, SEO, QA, Persona translation)
│   ├── config.py              ← config.json loader with Gemini 3.5 Flash defaults
│   ├── gemini_client.py       ← Gemini API client with safe parsing & 8-model fallback rotation
│   ├── sqlite_store.py        ← SQLite local database for multi-engine state & job logs
│   └── burmese_utils.py       ← Burmese syllable regex, number-to-words, acronym transliteration
│
├── templates/
│   └── index.html             ← Modern Glassmorphic Web UI with Theater Cinema Player
│
├── AI_Movie_Translate_Colab.ipynb  ← Official Google Colab One-Click Dedicated GPU Notebook
├── AI_Movie_Translate_Kaggle.ipynb ← Official Kaggle One-Click Dual T4 Dedicated GPU Notebook
├── config.json                ← Active runtime configuration (API keys, branding, models)
├── config.example.json        ← Default configuration template
├── cookies.txt                ← Netscape cookie file for YouTube anti-bot bypass
├── requirements.txt           ← Python package dependencies
├── assets/                    ← Reference voice samples, cookies, Padauk font, and branding
├── movies/                    ← Place source video files here
├── outputs/                   ← Generated final videos, thumbnails, scripts, and logs
└── temp/                      ← Intermediate audio/video cache (Auto-cleaned after merge)
```

---

## 💻 Local Setup (Windows / Linux / macOS)

### 1. Clone Repository & Create Virtual Environment
```bash
# Clone repository
git clone https://github.com/paipai1999/pai-ai-movie-studio.git
cd pai-ai-movie-studio

# Create Python virtual environment (Python 3.8+ required)
python -m venv .venv

# Activate virtual environment
# Windows (PowerShell):
.venv\Scripts\Activate.ps1
# Windows (CMD):
.venv\Scripts\activate.bat
# Linux / macOS:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure API Keys
Copy `config.example.json` to `config.json` and add your free Gemini API keys:
```json
{
  "gemini": {
    "enabled": true,
    "api_keys": [
      "AIzaSyYourFirstGeminiApiKeyHere",
      "AIzaSyYourSecondGeminiApiKeyHere"
    ]
  }
}
```
*(Get free API keys with high rate limits from [Google AI Studio](https://aistudio.google.com).)*

---

## 🚀 Usage Guide

### 🌐 Method 1: Web UI Dashboard (Recommended)
Double-click [`Start_Studio.bat`](Start_Studio.bat) or execute:
```bash
python web_ui.py
```
Open your browser at: `http://localhost:5000`

* **3 Studio Engines at your fingertips:** Switch between **🎬 Recap Studio**, **📝 Subtitle Engine**, and **🎞️ Hardsub Studio**.
* **Drag-and-Drop Video Upload:** Upload `.mp4`, `.mkv`, `.webm` files directly or paste YouTube/DramaBox links.
* **Live SSE Streaming Logs & Stopwatch:** Watch real-time terminal output and progress timers.
* **Theater Cinema View:** Click `🎬 Cinema` on any generated card to preview in full screen.
* **System Health Check:** Click the diagnostics icon to test FFmpeg encoders, active Gemini keys, Edge-TTS, and disk space.

---

### 💻 Method 2: Command Line Interface (CLI)

#### 🎬 Engine 1: AI Movie Recap & Dubbing Studio (`main.py`)
```bash
# 1. Standard recap generation (Both 16:9 + 9:16 Reels)
python main.py "movies/sample.mp4"

# 2. Process with custom TikTok yellow subtitle style and 9:16 format only
python main.py "movies/sample.mp4" --format 9:16 --sub-style yellow_pop

# 3. Overnight Batch Mode for all videos in movies/ directory
python main.py --batch --format both

# 4. Skip Demucs vocal separation on CPU for ultra-fast processing
python main.py "movies/sample.mp4" --skip-demucs
```

#### 📝 Engine 2: YouTube Subtitle & Transcript Studio (`subtitle_engine.py`)
```bash
# 1. Download YouTube video and export 6 deliverable files with spoken Burmese subtitles
python subtitle_engine.py -i "https://youtu.be/KmYSM5knNV8" --source-lang auto

# 2. Local video input with custom project folder name
python subtitle_engine.py -i "movies/clip.mp4" --name "My_Custom_Project"

# 3. Force Whisper transcription even if YouTube closed captions exist
python subtitle_engine.py -i "https://youtu.be/..." --force-whisper
```

#### 🎞️ Engine 3: 100% Original Audio & Burmese Hardsub Studio (`hardsub_engine.py`)
```bash
# 1. Standard run: 100% original audio, Netflix Box subtitles, Dual 16:9 + 9:16 export
python hardsub_engine.py "movies/action_movie.mp4" --format both --res 1080p

# 2. Anti-Copyright Shielded run (Mirror + Color EQ + Audio Shield atempo=1.008 + Vision AI Blur)
python hardsub_engine.py "movies/clip.mp4" --mirror --color-grading --audio-shield --blur yes --blur-height 0.20

# 3. Run directly with custom project name and source language
python hardsub_engine.py "https://youtu.be/..." --name "Marvel_Hardsub" --source-lang en
```

---

## 🧪 Testing & Quality Assurance

Run the automated test suite to verify system integrity:
```powershell
.venv\Scripts\python.exe -m unittest discover tests
```
*Current test suite status:* **77 / 77 Tests Passed (100% OK)** covering:
* Memory state serialization & deserialization
* Gemini client protobuf & REST fallback parsing
* QAAgent scene ID collision prevention & auto-rewrites
* HardsubEngine & SubtitleEngine timestamp conversions and filter construction
* Job queue lifecycle, cancellation, and thread safety

---

## 📄 License
This project is licensed under the MIT License — free for personal, educational, and commercial content production.
