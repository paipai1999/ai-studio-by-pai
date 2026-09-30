"""
CapCut Editing Package Bundler (CapCut အသင့်သုံး ပရောဂျက် ထုတ်လုပ်မှုစနစ်)
========================================================================
Packages all essential assets for direct drag-and-drop editing in CapCut:
  01_video.mp4          -> Original / downloaded raw high-clarity video
  02_voiceover.mp3      -> AI Burmese voiceover audio track (-14 LUFS normalized)
  03_background_sfx.mp3 -> Isolated background sound effects & ambient music (vocals stripped)
  04_subtitles.srt      -> UTF-8 BOM Burmese subtitles for instant CapCut auto-captioning
  05_script.txt         -> Complete Burmese script transcript with timestamps & speakers
  06_thumbnail.jpg      -> High-CTR cover thumbnail artwork
  07_upload_info.txt    -> SEO Titles, Description, and Viral Hashtags for social platforms
Also bundles the entire package into a single CapCut_Pack_<Name>.zip for 1-click download.
"""

import os
import shutil
import zipfile
import subprocess
from typing import Dict, Any, Optional, List
from brain.memory import MovieState
from core.subtitle_builder import write_srt_file, format_srt_timestamp
from brain.burmese_utils import strip_trailing_subtitle_punctuation, normalize_standard_burmese_spelling


def _get_ffmpeg_bin() -> str:
    bin_path = shutil.which("ffmpeg") or os.environ.get("IMAGEIO_FFMPEG_EXE")
    if not bin_path:
        try:
            from imageio_ffmpeg import get_ffmpeg_exe
            bin_path = get_ffmpeg_exe()
        except Exception:
            bin_path = "ffmpeg"
    return bin_path


def _assemble_voiceover_if_needed(state: MovieState, target_path: str, project_dir_path: str) -> Optional[str]:
    """Assembles discrete scene speech clips into a single normalized -14 LUFS MP3 track."""
    # Check if voiceover is already unified
    if getattr(state, "voiceover_path", None) and os.path.exists(state.voiceover_path):
        try:
            shutil.copyfile(state.voiceover_path, target_path)
            return target_path
        except Exception:
            pass

    # Check voiceover folder for scene clips
    vo_dir = os.path.join(project_dir_path, "voiceover")
    clips_with_timing: List[tuple] = []

    # Priority A: Check state.subtitle_timings
    sub_timings = getattr(state, "subtitle_timings", None) or []
    if os.path.exists(vo_dir):
        files = sorted(os.listdir(vo_dir))
        for idx, fname in enumerate(files):
            if fname.lower().endswith((".mp3", ".wav")):
                fpath = os.path.join(vo_dir, fname)
                place_time = 0.0
                if idx < len(sub_timings):
                    place_time = float(sub_timings[idx][0])
                else:
                    # Estimate based on index * 3s
                    place_time = float(idx * 3.0)
                clips_with_timing.append((fpath, place_time, 3.0))

    if not clips_with_timing and getattr(state, "generated_script", None):
        for block in state.generated_script:
            audio_file = block.get("audio_file") or block.get("audio_path")
            if audio_file and os.path.exists(audio_file):
                start_s = float(block.get("start_sec") or 0.0)
                clips_with_timing.append((audio_file, start_s, 3.0))

    if not clips_with_timing:
        return None

    try:
        from agents.video_merger_agent import _assemble_voiceover_track
        total_dur = getattr(state, "duration_sec", 0.0) or (clips_with_timing[-1][1] + 5.0)
        temp_wav = os.path.join(project_dir_path, "temp_vo_assembled.wav")
        _assemble_voiceover_track(clips_with_timing, total_dur, temp_wav)

        ffmpeg_bin = _get_ffmpeg_bin()
        # Loudness normalize to standard -14 LUFS for CapCut / YouTube
        cmd = [
            ffmpeg_bin, "-y", "-i", temp_wav,
            "-af", "loudnorm=I=-14:LRA=7:tp=-1.5",
            "-c:a", "libmp3lame", "-b:a", "192k",
            target_path
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
        if os.path.exists(temp_wav):
            try:
                os.remove(temp_wav)
            except Exception:
                pass
        return target_path
    except Exception as e:
        print(f"[!] CapCutPack: Error assembling voiceover track: {e}")
        return None


def export_capcut_package(
    state: MovieState,
    output_dir: str,
    movie_path: Optional[str] = None
) -> Dict[str, Any]:
    """
    Builds the CapCut editing production package with 7 standardized assets and a ZIP bundle.
    """
    project_slug = getattr(state, "project_dir", None) or state.movie_name.replace(" ", "_")
    project_dir_path = os.path.join(output_dir, project_slug)
    pack_name = f"CapCut_Pack_{state.movie_name}"
    pack_dir = os.path.join(project_dir_path, pack_name)
    os.makedirs(pack_dir, exist_ok=True)

    print(f"\n{'='*60}")
    print(f"🎬 [CapCut Pack] Exporting Production Bundle: {pack_name}")
    print(f"{'='*60}")

    created_files: Dict[str, str] = {}
    ffmpeg_bin = _get_ffmpeg_bin()

    # 1. 01_video.mp4 (Raw downloaded or clean video)
    src_video = (
        getattr(state, "clean_video_path", None)
        or movie_path
        or getattr(state, "movie_path", None)
        or getattr(state, "file_path", None)
        or os.path.join(project_dir_path, "final_recap_clean.mp4")
    )
    target_video = os.path.join(pack_dir, "01_video.mp4")
    if src_video and os.path.exists(src_video):
        try:
            # Quick copy or symlink
            if not os.path.exists(target_video) or os.path.getsize(target_video) != os.path.getsize(src_video):
                shutil.copyfile(src_video, target_video)
            created_files["01_video"] = target_video
            print(f"   ✓ [01_video.mp4] Attached source video ({round(os.path.getsize(target_video)/(1024*1024), 1)} MB)")
        except Exception as e:
            print(f"   [!] Failed copying source video: {e}")

    # 2. 02_voiceover.mp3 (AI Burmese voiceover audio track -14 LUFS)
    target_vo = os.path.join(pack_dir, "02_voiceover.mp3")
    vo_result = _assemble_voiceover_if_needed(state, target_vo, project_dir_path)
    if vo_result and os.path.exists(vo_result):
        state.voiceover_path = vo_result
        created_files["02_voiceover"] = vo_result
        print(f"   ✓ [02_voiceover.mp3] Formatted -14 LUFS AI voiceover track")
    else:
        # Check if project directory has final_recap_speech.mp3 or similar
        candidate_vo = os.path.join(project_dir_path, "final_recap_speech.mp3")
        if os.path.exists(candidate_vo):
            shutil.copyfile(candidate_vo, target_vo)
            state.voiceover_path = target_vo
            created_files["02_voiceover"] = target_vo
            print(f"   ✓ [02_voiceover.mp3] Reused existing final speech track")

    # 3. 03_background_sfx.mp3 (Isolated SFX / ambient track without vocals)
    target_sfx = os.path.join(pack_dir, "03_background_sfx.mp3")
    sfx_src = getattr(state, "sfx_path", None)
    if not sfx_src or not os.path.exists(sfx_src):
        # Fallback to audio agent extraction
        from agents.audio_agent import AudioAgent
        raw_audio = getattr(state, "audio_path", None)
        if raw_audio and os.path.exists(raw_audio):
            sfx_src = AudioAgent().extract_sfx(raw_audio, project_dir_path)
            state.sfx_path = sfx_src

    if sfx_src and os.path.exists(sfx_src):
        try:
            if sfx_src.lower().endswith(".mp3"):
                shutil.copyfile(sfx_src, target_sfx)
            else:
                # Convert WAV stem to MP3
                cmd = [ffmpeg_bin, "-y", "-i", sfx_src, "-c:a", "libmp3lame", "-b:a", "192k", target_sfx]
                subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            created_files["03_background_sfx"] = target_sfx
            print(f"   ✓ [03_background_sfx.mp3] Isolated SFX & ambient audio track")
        except Exception as e:
            print(f"   [!] Failed preparing SFX audio: {e}")

    # 4. 04_subtitles.srt (UTF-8 BOM Burmese subtitles for instant CapCut recognition)
    target_srt = os.path.join(pack_dir, "04_subtitles.srt")
    sub_timings = getattr(state, "subtitle_timings", None) or []
    srt_segments: List[Dict[str, Any]] = []

    if sub_timings:
        for item in sub_timings:
            start_s = float(item[0])
            dur_s = float(item[1])
            text_val = str(item[2])
            srt_segments.append({
                "start_s": start_s,
                "end_s": start_s + max(dur_s, 0.8),
                "burmese": text_val
            })
    elif getattr(state, "generated_script", None):
        for block in state.generated_script:
            if isinstance(block, dict):
                start_s = float(block.get("start_sec") or 0.0)
                end_s = float(block.get("end_sec") or (start_s + 3.0))
                txt = str(block.get("narration") or block.get("text") or "").strip()
                if txt:
                    srt_segments.append({
                        "start_s": start_s,
                        "end_s": max(end_s, start_s + 0.8),
                        "burmese": txt
                    })
    elif getattr(state, "transcript", None):
        for t in state.transcript:
            s_s = getattr(t, "start_sec", getattr(t, "start", 0.0))
            e_s = getattr(t, "end_sec", getattr(t, "end", float(s_s) + 2.0))
            srt_segments.append({
                "start_s": float(s_s),
                "end_s": float(e_s),
                "burmese": t.text
            })

    if srt_segments:
        write_srt_file(target_srt, srt_segments, with_bom=True)
        created_files["04_subtitles"] = target_srt
        print(f"   ✓ [04_subtitles.srt] Built CapCut-ready UTF-8 BOM Burmese subtitles ({len(srt_segments)} cues)")

    # 5. 05_script.txt (Full Burmese script transcript)
    target_script = os.path.join(pack_dir, "05_script.txt")
    script_lines = []
    script_lines.append(f"🎬 Movie / Video: {state.movie_name}")
    script_lines.append(f"📅 Export Date: {state.end_time or 'Current Session'}")
    script_lines.append(f"⏱️ Duration: {getattr(state, 'duration_sec', 0.0):.1f}s")
    script_lines.append("="*60 + "\n")

    if getattr(state, "generated_script", None):
        for idx, block in enumerate(state.generated_script, 1):
            speaker = block.get("speaker") or block.get("character") or "Narrator"
            start_s = block.get("start_sec", 0.0)
            end_s = block.get("end_sec", 0.0)
            text_val = block.get("narration") or block.get("text") or ""
            norm_text = strip_trailing_subtitle_punctuation(normalize_standard_burmese_spelling(text_val))
            script_lines.append(f"[{format_srt_timestamp(float(start_s))} --> {format_srt_timestamp(float(end_s))}] {speaker}:")
            script_lines.append(f"   {norm_text}\n")
    elif getattr(state, "transcript", None):
        for idx, t in enumerate(state.transcript, 1):
            norm_text = strip_trailing_subtitle_punctuation(normalize_standard_burmese_spelling(t.text))
            s_s = getattr(t, "start_sec", getattr(t, "start", 0.0))
            e_s = getattr(t, "end_sec", getattr(t, "end", float(s_s) + 2.0))
            script_lines.append(f"[{format_srt_timestamp(float(s_s))} --> {format_srt_timestamp(float(e_s))}]")
            script_lines.append(f"   {norm_text}\n")

    with open(target_script, "w", encoding="utf-8") as f:
        f.write("\n".join(script_lines))
    created_files["05_script"] = target_script
    print(f"   ✓ [05_script.txt] Exported readable dialogue/narration script")

    # 6. 06_thumbnail.jpg (High-CTR artwork)
    thumb_src = getattr(state, "thumbnail_path", None) or os.path.join(project_dir_path, "thumbnail.jpg")
    target_thumb = os.path.join(pack_dir, "06_thumbnail.jpg")
    if thumb_src and os.path.exists(thumb_src):
        shutil.copyfile(thumb_src, target_thumb)
        created_files["06_thumbnail"] = target_thumb
        print(f"   ✓ [06_thumbnail.jpg] High-CTR thumbnail cover attached")

    # 7. 07_upload_info.txt (Viral SEO Titles, Description, Hashtags)
    target_upload_info = os.path.join(pack_dir, "07_upload_info.txt")
    seo = getattr(state, "seo_metadata", None) or {}
    upload_info_lines = []
    upload_info_lines.append("="*60)
    upload_info_lines.append("🚀 SOCIAL MEDIA PUBLISHING METADATA (ကူးယူအသုံးပြုရန် အသင့်သုံး)")
    upload_info_lines.append("="*60 + "\n")
    upload_info_lines.append("📌 1. VIRAL TITLES (ခေါင်းစဉ် ရွေးချယ်စရာများ):")
    main_title = seo.get("title") or state.movie_name
    upload_info_lines.append(f"   • Option A: {main_title}")
    if seo.get("alternative_titles"):
        for i, alt in enumerate(seo.get("alternative_titles")[:3], 2):
            upload_info_lines.append(f"   • Option {chr(64+i)}: {alt}")
    else:
        upload_info_lines.append(f"   • Option B: {state.movie_name} မြန်မာစာတန်းထိုးနှင့် အသံထွက် ဇာတ်လမ်းအကျဉ်း")

    upload_info_lines.append("\n📝 2. DESCRIPTION (ဖော်ပြချက် စာသား):")
    desc = seo.get("description") or f"{state.movie_name} ရုပ်ရှင်ဇာတ်လမ်းကို မြန်မာဘာသာဖြင့် ကြည်လင်ပြတ်သားစွာ တင်ဆက်ထားပါသည်။"
    upload_info_lines.append(desc)

    upload_info_lines.append("\n🏷️ 3. HASHTAGS (အများဆုံးရှာဖွေသော Hashtag များ):")
    hashtags = seo.get("hashtags") or ["#MovieRecap", "#MyanmarMovie", "#AiStudioByPai", "#CapCutEdit", "#MyanmarSubtitles"]
    if isinstance(hashtags, list):
        upload_info_lines.append(" ".join(hashtags))
    else:
        upload_info_lines.append(str(hashtags))

    with open(target_upload_info, "w", encoding="utf-8") as f:
        f.write("\n".join(upload_info_lines))
    created_files["07_upload_info"] = target_upload_info
    print(f"   ✓ [07_upload_info.txt] Viral titles, description & hashtags generated")

    # 8. Create unified ZIP archive
    zip_path = os.path.join(output_dir, f"{pack_name}.zip")
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, _, files in os.walk(pack_dir):
            for file in files:
                abs_f = os.path.join(root, file)
                rel_f = os.path.join(pack_name, os.path.relpath(abs_f, pack_dir))
                zf.write(abs_f, rel_f)

    # Also keep a copy inside project directory for persistent job manager retrieval
    proj_zip_path = os.path.join(project_dir_path, f"{pack_name}.zip")
    try:
        shutil.copyfile(zip_path, proj_zip_path)
    except Exception:
        pass

    state.capcut_pack_dir = pack_dir
    state.capcut_zip_path = zip_path

    print(f"\n📦 [CapCut Pack Ready] 7 Assets organized into:")
    print(f"   Folder: {pack_dir}")
    print(f"   ZIP   : {zip_path} ({round(os.path.getsize(zip_path)/(1024*1024), 1)} MB)")
    print(f"{'='*60}\n")

    return {
        "pack_name": pack_name,
        "pack_dir": pack_dir,
        "zip_path": zip_path,
        "files": created_files
    }
