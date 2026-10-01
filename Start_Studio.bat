@echo off
setlocal EnableDelayedExpansion
chcp 65001 >nul
cd /d "%~dp0"
title AI Studio by Pai (v2.3) - Master Launcher
color 0B

:: 1. Python Environment Detection
set "PYTHON_EXE=%~dp0.venv\Scripts\python.exe"
if not exist "%PYTHON_EXE%" set "PYTHON_EXE=python"

set "CLI_MODE="
if not "%~1"=="" set "CLI_MODE=1"

:: 2. Command-Line Arguments & Shortcuts Dispatcher
if "%~1"=="" goto MENU
if /i "%~1"=="--web" goto WEBUI
if /i "%~1"=="web" goto WEBUI
if /i "%~1"=="1" goto WEBUI
if /i "%~1"=="--capcut" goto CAPCUT_MODE
if /i "%~1"=="capcut" goto CAPCUT_MODE
if /i "%~1"=="2" goto CAPCUT_MODE
if /i "%~1"=="c" goto CAPCUT_MODE
if /i "%~1"=="--capcut-batch" goto CAPCUT_BATCH
if /i "%~1"=="3" goto CAPCUT_BATCH
if /i "%~1"=="--recap" goto RECAP_SINGLE
if /i "%~1"=="recap" goto RECAP_SINGLE
if /i "%~1"=="4" goto RECAP_SINGLE
if /i "%~1"=="--batch" goto RECAP_BATCH
if /i "%~1"=="batch" goto RECAP_BATCH
if /i "%~1"=="5" goto RECAP_BATCH
if /i "%~1"=="--clean" goto CLEAN
if /i "%~1"=="clean" goto CLEAN
if /i "%~1"=="6" goto CLEAN
if /i "%~1"=="--health" goto HEALTH
if /i "%~1"=="health" goto HEALTH
if /i "%~1"=="7" goto HEALTH
if /i "%~1"=="--test" goto TEST
if /i "%~1"=="test" goto TEST
if /i "%~1"=="8" goto TEST
if /i "%~1"=="--update" goto UPDATE
if /i "%~1"=="update" goto UPDATE
if /i "%~1"=="9" goto UPDATE
if /i "%~1"=="--docker" goto DOCKER
if /i "%~1"=="docker" goto DOCKER
if /i "%~1"=="10" goto DOCKER

:: Drag-and-drop file onto Start_Studio.bat
if exist "%~1" (
    set "DRAG_FILE=%~1"
    goto DRAG_MENU
)

set "input_src=%~1"
set "cc_input=%~1"
goto CAPCUT_DIRECT

:DRAG_MENU
cls
echo ===============================================================================
echo            AI STUDIO BY PAI - FILE DETECTED
echo ===============================================================================
echo.
echo Input File: "%DRAG_FILE%"
echo.
echo Select Processing Pipeline for this file:
echo.
echo    [1] CapCut Fast Pack (7 Assets + ZIP in ~2 mins - Recommended)
echo    [2] Full Movie Recap Render (AI Dubbing + Subtitles Burned In)
echo    [0] Return to Main Menu
echo.
echo ===============================================================================
set "dd_choice="
set /p "dd_choice=Select Option [1-2, Default=1]: "
if not defined dd_choice set "dd_choice=1"
if "%dd_choice%"=="1" (
    set "cc_input=%DRAG_FILE%"
    goto CAPCUT_DIRECT
)
if "%dd_choice%"=="2" (
    set "input_src=%DRAG_FILE%"
    goto RECAP_DIRECT
)
goto MENU

:MENU
cls
echo ===============================================================================
echo            AI STUDIO BY PAI (v2.3) - CAPCUT PRODUCTION PIPELINE
echo ===============================================================================
echo.
echo    [1] Launch Interactive Web UI Dashboard (Recommended / Default: Enter)
echo    [2] CapCut Fast Pack Mode (Single Video / URL - 7 Assets in ~2 mins)
echo    [3] CapCut Fast Pack Batch Mode (Process all in "movies/" folder)
echo    [4] Full Movie Recap Render for Single Video / URL
echo    [5] Full Movie Recap Render (Batch Mode)
echo    [6] Open Studio Cleanup Utility (Delete cache / old outputs)
echo    [7] Run System Health and Hardware Diagnostics
echo    [8] Run Automated Test Suite (pytest verification)
echo    [9] Check & Pull Latest Updates from GitHub (git pull)
echo    [10] Run AI Studio in Docker Container
echo    [0] Exit
echo.
echo ===============================================================================
set "choice="
set /p "choice=Select an option [0-10, press Enter for Web UI]: "

if not defined choice set "choice=1"
if "%choice%"=="1" goto WEBUI
if "%choice%"=="2" goto CAPCUT_MODE
if /i "%choice%"=="c" goto CAPCUT_MODE
if "%choice%"=="3" goto CAPCUT_BATCH
if "%choice%"=="4" goto RECAP_SINGLE
if "%choice%"=="5" goto RECAP_BATCH
if "%choice%"=="6" goto CLEAN
if "%choice%"=="7" goto HEALTH
if "%choice%"=="8" goto TEST
if "%choice%"=="9" goto UPDATE
if "%choice%"=="10" goto DOCKER
if "%choice%"=="0" goto EXIT
goto MENU

:WEBUI
cls
echo ===============================================================================
echo LAUNCHING AI STUDIO BY PAI - WEB UI DASHBOARD...
echo ===============================================================================
echo.
echo [*] Checking Port 5000 availability...
powershell -NoProfile -Command "Get-NetTCPConnection -LocalPort 5000 -State Listen -ErrorAction SilentlyContinue | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force -ErrorAction SilentlyContinue }" >nul 2>&1

echo [*] Opening Browser at http://localhost:5000 ...
start /b "" "%PYTHON_EXE%" -c "import socket, time, webbrowser; exec('for _ in range(30):\n time.sleep(1)\n try:\n  with socket.create_connection((\x27127.0.0.1\x27, 5000), timeout=0.5):\n   webbrowser.open(\x27http://localhost:5000\x27)\n   break\n except OSError:\n  pass')" >nul 2>&1

echo.
echo ===============================================================================
echo  Dashboard Link : http://localhost:5000
echo  To Stop Server : Press Ctrl + C in this window
echo ===============================================================================
echo.

"%PYTHON_EXE%" web_ui.py
if errorlevel 1 (
    echo.
    echo [ERROR] Web UI stopped with an error code.
    pause
)
if defined CLI_MODE exit /b 0
goto MENU

:RECAP_BATCH
cls
echo ===============================================================================
echo STARTING BATCH MOVIE RECAP GENERATION FOR "movies/" FOLDER...
echo ===============================================================================
"%PYTHON_EXE%" main.py --batch
if defined CLI_MODE exit /b 0
echo.
echo ===============================================================================
echo Batch Processing Complete! Press any key to return to menu...
pause >nul
goto MENU

:RECAP_SINGLE
cls
echo ===============================================================================
echo ENTER VIDEO URL OR LOCAL FILE PATH:
echo ===============================================================================
echo Tip: Paste a full YouTube link or local file path (e.g. C:\videos\movie.mp4)
set "input_src="
set /p "input_src=Input URL or File Path: "
if not defined input_src goto MENU

echo.
echo Select Narration / Translation Style:
echo    [1] Movie Recap Storyteller (Default)
echo    [2] Chinese Drama Audio Novel (တရုတ်ဒရမ်မာ အသံထွက်ဝတ္ထုဟန်)
echo    [3] Wuxia / Cultivation (သိုင်းကား / ကျင့်ကြံရေး)
echo    [4] Cinematic Persona Dubbing
set "rc_style_choice="
set /p "rc_style_choice=Choice [1-4, Enter for Recap]: "
set "rc_style=recap"
if "%rc_style_choice%"=="2" set "rc_style=drama_novel"
if "%rc_style_choice%"=="3" set "rc_style=wuxia"
if "%rc_style_choice%"=="4" set "rc_style=persona"

:RECAP_DIRECT
cls
if not defined rc_style set "rc_style=recap"
set "input_src=!input_src:"=!"
echo ===============================================================================
echo PROCESSING: !input_src! [Style: %rc_style%]
echo ===============================================================================
"%PYTHON_EXE%" main.py "!input_src!" --style "%rc_style%"
if defined CLI_MODE exit /b 0
echo.
echo ===============================================================================
echo Processing Complete! Press any key to return to menu...
pause >nul
goto MENU

:CAPCUT_BATCH
cls
echo ===============================================================================
echo STARTING BATCH CAPCUT FAST PACK PRODUCTION FOR "movies/" FOLDER...
echo ===============================================================================
echo Exports 7 assets + ZIP bundle for every video without heavy rendering (~2 mins each).
echo.
"%PYTHON_EXE%" main.py --batch --capcut-only
if defined CLI_MODE exit /b 0
echo.
echo ===============================================================================
echo Batch CapCut Processing Complete! Press any key to return to menu...
pause >nul
goto MENU

:CLEAN
cls
echo ===============================================================================
echo STUDIO CLEANUP UTILITY
echo ===============================================================================
"%PYTHON_EXE%" main.py --clean
if defined CLI_MODE exit /b 0
echo.
echo Press any key to return to menu...
pause >nul
goto MENU

:HEALTH
cls
echo ===============================================================================
echo RUNNING SYSTEM HEALTH AND HARDWARE DIAGNOSTICS...
echo ===============================================================================
"%PYTHON_EXE%" -c "import sys, os, brain.config as cfg; from agents.video_merger_agent import detect_hardware_encoder, _get_ffmpeg_bin; ff = _get_ffmpeg_bin(); enc = detect_hardware_encoder(); c = cfg.load_config(); keys = c.get('gemini', {}).get('api_keys', []); models = c.get('gemini', {}).get('models', {}); model = models.get('workhorse') or c.get('gemini', {}).get('model', 'Unknown'); print('  [*] Python Version     :', sys.version.split()[0]); print('  [*] Active FFmpeg      :', ff or 'NOT FOUND'); print('  [*] Video Accelerator  :', enc.get('label', 'Default'), '[' + enc.get('codec', 'libx264') + ']'); print('  [*] Gemini Model       :', model); print('  [*] Configured API Keys:', len(keys), 'key(s)'); print('  [*] Working Directory  :', os.getcwd())"
if defined CLI_MODE exit /b 0
echo.
echo ===============================================================================
echo Press any key to return to menu...
pause >nul
goto MENU

:TEST
cls
echo ===============================================================================
echo RUNNING AUTOMATED UNIT AND INTEGRATION TEST SUITE (pytest)...
echo ===============================================================================
echo.
set "PYTEST_EXE=%~dp0.venv\Scripts\pytest.exe"
if exist "%PYTEST_EXE%" (
    "%PYTEST_EXE%" -v
) else (
    "%PYTHON_EXE%" -m pytest -v
)
if defined CLI_MODE exit /b 0
echo.
echo ===============================================================================
echo Test run complete! Press any key to return to menu...
echo ===============================================================================
pause >nul
goto MENU

:DOCKER
cls
echo ===============================================================================
echo LAUNCHING PAI AI MOVIE STUDIO IN DOCKER CONTAINER...
echo ===============================================================================
where docker >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Docker was not detected on this system!
    echo Please install Docker Desktop: https://www.docker.com/products/docker-desktop/
    echo.
    pause
    goto MENU
)
echo [*] Starting Studio containers via Docker Compose...
docker compose up -d
if errorlevel 1 (
    echo.
    echo [ERROR] Failed to start Docker container.
    pause
    goto MENU
)
echo.
echo [*] Docker container is active and running!
echo [*] Opening Browser at http://localhost:5000 ...
start http://localhost:5000
echo.
echo Press any key to return to menu...
pause >nul
goto MENU

:UPDATE
cls
echo ===============================================================================
echo CHECKING AND PULLING LATEST UPDATES FROM GITHUB...
echo ===============================================================================
where git >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Git was not detected on this system!
    echo Please install Git from https://git-scm.com/
    pause
    goto MENU
)
echo [*] Fetching and pulling latest changes from origin/main...
git pull origin main
if errorlevel 1 (
    echo [WARN] git pull returned an error. Please check your network or local changes.
) else (
    echo [OK] Code updated successfully!
)
echo.
echo [*] Checking Python dependencies...
"%PYTHON_EXE%" -m pip install -r requirements.txt --quiet
echo [OK] Dependencies check completed.
echo.
echo ===============================================================================
echo Update completed! Press any key to return to menu...
echo ===============================================================================
pause >nul
goto MENU

:CAPCUT_MODE
cls
echo ===============================================================================
echo RUN CAPCUT FAST PACK PRODUCTION MODE (SKIP HEAVY VIDEO RENDER)
echo ===============================================================================
echo.
echo Exports 7 assets: Video, Voiceover (-14 LUFS), SFX/BGM, UTF-8 BOM SRT, Script,
echo Cover Thumbnail (Clean Artwork), and Social Metadata + 1-Click ZIP bundle in ~2 mins.
echo.
set "cc_input="
set /p "cc_input=Enter Video File Path or YouTube URL: "
if not defined cc_input goto MENU

:CAPCUT_DIRECT
if not defined cc_input set "cc_input=!input_src!"
set "cc_input=!cc_input:"=!"
echo.
echo [*] Executing CapCut Fast Pack Pipeline for: !cc_input!
"%PYTHON_EXE%" main.py "!cc_input!" --capcut-only
echo.
echo ===============================================================================
echo CapCut Pack complete! Check outputs/ folder for CapCut_Pack ZIP bundle.
echo ===============================================================================
pause
if defined CLI_MODE exit /b 0
goto MENU

:EXIT
exit /b 0
