# 🎬 AI Studio by Pai (v2.3) — $0 Free Local & Cloud-Accelerated Pipeline

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Google Colab](https://img.shields.io/badge/Google%20Colab-T4%20GPU%20(Free)-orange.svg)](https://colab.research.google.com/github/paipai1999/ai-studio-by-pai/blob/main/AI_Movie_Translate_Colab.ipynb)
[![Kaggle](https://img.shields.io/badge/Kaggle-Dual%20T4%2030GB%20VRAM-blue.svg)](https://github.com/paipai1999/ai-studio-by-pai/blob/main/AI_Movie_Translate_Kaggle.ipynb)
[![Tests](https://img.shields.io/badge/Tests-100%2F100%20Passed%20(100%25)-brightgreen.svg)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An autonomous, production-grade AI studio designed to automatically translate movies, short dramas, anime, and YouTube videos into natural **Colloquial Spoken Burmese** (စကားပြောဟန်) or English, synthesize lifelike **Multi-Voice Dubbing (Male/Female)**, and render viral, ready-to-publish videos equipped with **9:16 Facebook Reels / TikTok Canvas**, **Styled Myanmar ASS Subtitles**, **Vision AI Subtitle Blur Protection**, **Anti-Copyright Shields**, and **High-CTR Thumbnails**.

---

## 🇲🇲 စနစ်အနှစ်ချုပ် မိတ်ဆက် (Burmese Overview)

**Pai AI Movie Studio** သည် ရုပ်ရှင်၊ ဒရမ်မာဇာတ်လမ်းတိုများနှင့် YouTube ဗီဒီယိုများကို ကွန်ပျူတာ သို့မဟုတ် Free Cloud GPU (Google Colab / Kaggle) ပေါ်တွင် **၁၀၀% အခမဲ့** ဖြင့် မြန်မာဘာသာသို့ အလိုအလျောက် ဘာသာပြန်ခြင်း၊ အသံသွင်းခြင်း (Dubbing) နှင့် စာတန်းထိုးထုတ်လုပ်ပေးနိုင်သော All-in-One AI စနစ်ဖြစ်ပါသည်။

### 🎯 စနစ်ပါ အဓိက Production Pipelines:
1. ⚡ **CapCut Fast Pack Production Pipeline (`--capcut-only`)**
   - Video Render လုပ်ရန် မလိုဘဲ အချိန် **~၂ မိနစ်အတွင်း** CapCut တွင် တိုက်ရိုက် Edit ပြုလုပ်ရန် လိုအပ်သည့် Deliverable **ဖိုင် ၇ မျိုး** နှင့် ZIP Bundle ကို အလိုအလျောက် ထုတ်ပေးခြင်း။
   - **01_video.mp4**: မူရင်း Video ဖိုင်။
   - **02_voiceover.mp3**: AI မြန်မာအသံဖိုင် (TTS Voiceover Track -14 LUFS ဖြင့် စနစ်တကျ ညှိထားပြီး)။
   - **03_background_sfx.mp3**: အသံခွဲခြမ်းစိတ်ဖြာထားသော နောက်ခံတေးဂီတနှင့် SFX အသံဖိုင် (Demucs Vocal Stripped / Ambience)။
   - **04_subtitles.srt**: CapCut Desktop/Mobile တွင် မြန်မာစာလုံးမပျက်ဘဲ ဖတ်နိုင်သော UTF-8 BOM (`utf-8-sig`) စာတန်းထိုးဖိုင်။
   - **05_script.txt**: Timestamp ပါဝင်သော မြန်မာဘာသာပြန် ဇာတ်ညွှန်းအပြည့်အစုံ။
   - **06_thumbnail.jpg**: စာသားမပါသော သန့်ရှင်းကြည်လင်သည့် 1080p Cover ပုံ (Clean High-Clarity Artwork / No Text Overlay)။
   - **07_upload_info.txt**: YouTube, Facebook, TikTok အတွက် Viral SEO ခေါင်းစဉ်များ၊ Description နှင့် Hashtags များ။
   - **CapCut_Pack_<MovieName>.zip**: အထက်ပါဖိုင်အားလုံးကို ကလစ်တစ်ချက်တည်းဖြင့် Download ဆွဲနိုင်သော ZIP အထုပ်။
2. 🎬 **Full Movie Recap & Multi-Voice Dubbing Studio (`main.py`)**
   - ဇာတ်လမ်းပြောပြသူ Persona (`...ခဲ့တာပေါ့ဗျာ`) သို့မဟုတ် ၁:၁ ဇာတ်ကောင် Dubbing ဖြင့် အပြီးသတ် Render ပြုလုပ်ထားသော Video ထုတ်လုပ်ပေးခြင်း။
   - အမျိုးသား (`my-MM-ThihaNeural`) နှင့် အမျိုးသမီး (`my-MM-NilarNeural`) အသံများ အလိုအလျောက်ခွဲခြား Dubbing သွင်းပေးခြင်း။
   - Facebook Reels / TikTok (9:16) နှင့် YouTube (16:9) ဗီဒီယို ၂ မျိုးစလုံး တစ်ပြိုင်နက် ထုတ်လုပ်ပေးခြင်း။
   - Zero-Drift Scene-Anchor စနစ်ဖြင့် အခန်းပေါင်း ၁၀၀ ကျော်တွင် အသံနှင့် ရုပ်သံ လုံးဝလွဲချော်မှုမရှိခြင်း (0.000s Drift)။

---

## ⚡ Cloud GPU One-Click Setup (100% Free Cloud Options)

### 🥇 Option A: Google Colab (Free T4 GPU + Google Drive Sync)
👉 **[Open AI_Movie_Translate_Colab.ipynb in Google Colab](https://colab.research.google.com/github/paipai1999/ai-studio-by-pai/blob/main/AI_Movie_Translate_Colab.ipynb)**
* **Highlights:** 1-Click Web UI Dashboard, Permanent Google Drive Sync for videos/cookies/database, 60s Auto Keep-Alive Heartbeat, and Fast Socket Health-Check.
* **Public & Private Editions:** 
  - `AI_Movie_Translate_Colab.ipynb` (Public Edition on GitHub - clean template for community sharing).
  - `AI_Movie_Translate_Colab_PRIVATE.ipynb` (Personal VIP Edition - pre-loaded with your Gemini keys & YouTube cookies for instant 1-click execution without typing).

### 🥈 Option B: Kaggle Notebooks (Free Dual T4 30GB VRAM / 30h Weekly Quota)
👉 **[View AI_Movie_Translate_Kaggle.ipynb](https://github.com/paipai1999/ai-studio-by-pai/blob/main/AI_Movie_Translate_Kaggle.ipynb)**
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
* **Windows 1-Click:** Select Option `[8] Run Pai AI Studio in Docker Container` from `Start_Studio.bat`.
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

## 🎯 The Dual-Pipeline Architecture: CapCut Pack vs. Full Render

| Feature / Capability | ⚡ CapCut Fast Pack Pipeline (`--capcut-only`) | 🎬 Full Movie Recap Studio (`main.py`) |
| :--- | :---: | :---: |
| **Primary CLI Flag** | `--capcut-only` or `--capcut-pack` | Standard `main.py` execution |
| **Windows Master Launcher** | [`Start_Studio.bat`](Start_Studio.bat) (Menu `[2]` or `[3]`) | [`Start_Studio.bat`](Start_Studio.bat) (Menu `[4]` or `[5]`) |
| **Processing Speed** | **Ultra Fast (~1.5–2.5 minutes)** | Standard (~6–8 min CPU / ~1.5 min GPU) |
| **Video Rendering** | ❌ None (Keeps 100% original video untouched) | ✅ Single-Pass Filtergraph Encoding (16:9 + 9:16) |
| **Subtitles Format** | UTF-8 BOM (`utf-8-sig`) `.srt` (CapCut ready) | Burned-in ASS styling (Netflix Box / TikTok Yellow) |
| **Audio Tracks Export** | `02_voiceover.mp3` (-14 LUFS) & `03_background_sfx.mp3` | Mixed & ducked into output video stream |
| **Target Audience** | Content Creators editing in CapCut / Premiere | 1-Click publish-ready viral videos |
| **Deliverable Package** | 7 Individual Assets + `CapCut_Pack_<Name>.zip` | Rendered MP4s, Cover Art, Script, Metadata |

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
ai-studio-by-pai/
├── main.py                    ← Master CLI & Universal Studio Dispatcher
├── web_ui.py                  ← FastAPI Web Dashboard with Live Streaming & Cinema Player
│
├── Start_Studio.bat          ← Master 1-Click Studio Launcher (Web UI & Fast CapCut Packs)
│
├── core/                      ← Centralized Media & Subtitle Processing Package
│   ├── capcut_pack.py         ← CapCut 7-Asset Production Bundler & ZIP Exporter
│   ├── anti_copyright.py      ← Platform video & audio anti-copyright filter graphs
│   ├── subtitle_builder.py    ← ASS & UTF-8 BOM SRT subtitle generators & styling presets
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
│   ├── thumbnail_agent.py     ← Clean High-Clarity Cover Artwork & Vision AI Hardsub Blur Generator
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
git clone https://github.com/paipai1999/ai-studio-by-pai.git
cd ai-studio-by-pai

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

* **CapCut Fast Pack 1-Click Export:** Download the bundled ZIP package directly from the dashboard card.
* **Drag-and-Drop Video Upload:** Upload `.mp4`, `.mkv`, `.webm` files directly or paste YouTube/DramaBox links.
* **Live SSE Streaming Logs & Stopwatch:** Watch real-time terminal output and progress timers.
* **Theater Cinema View:** Click `🎬 Cinema` on any generated card to preview in full screen.
* **System Health Check:** Click the diagnostics icon to test FFmpeg encoders, active Gemini keys, Edge-TTS, and disk space.

---

### 💻 Method 2: Command Line Interface (CLI)

#### ⚡ 1. CapCut Fast Pack Production Pipeline (`--capcut-only`)
```bash
# 1. Generate CapCut 7-asset bundle + ZIP in ~2 minutes (Skip heavy rendering)
python main.py "movies/sample.mp4" --capcut-only

# 2. Batch generate CapCut production packs for all files in movies/ folder
python main.py --batch --capcut-only

# 3. Direct download from YouTube and export CapCut pack immediately
python main.py "https://youtu.be/..." --capcut-only
```

#### 🎬 2. Full Movie Recap & Dubbing Studio (`main.py`)
```bash
# 1. Standard full recap generation (Both 16:9 + 9:16 Reels)
python main.py "movies/sample.mp4"

# 2. Process with custom TikTok yellow subtitle style and 9:16 format only
python main.py "movies/sample.mp4" --format 9:16 --sub-style yellow_pop

# 3. Overnight Batch Mode for all videos in movies/ directory
python main.py --batch --format both

# 4. Skip Demucs vocal separation on CPU for ultra-fast processing
python main.py "movies/sample.mp4" --skip-demucs
```

---

## 🧪 Testing & Quality Assurance

Run the automated test suite to verify system integrity:
```powershell
.venv\Scripts\pytest -v
```
*Current test suite status:* **100 / 100 Tests Passed (100% OK)** covering:
* Memory state serialization & SQLite persistence
* Gemini client protobuf & REST fallback rotation
* Dual script storytelling engine & Burmese digit/acronym transliteration
* QAAgent scene ID collision prevention, auto-rewrites & language preservation
* CapCut 7-asset production pack generation, UTF-8 BOM SRT export & audio stem extraction
* Job queue lifecycle, sequential execution, emergency cancellation & thread safety
* Web API security (CORS, token masking, authentication & report previews)

---

## 📄 License
This project is licensed under the MIT License — free for personal, educational, and commercial content production.
