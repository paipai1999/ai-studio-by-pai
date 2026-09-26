@echo off
setlocal EnableDelayedExpansion
chcp 65001 >nul
cd /d "%~dp0"
title Pai AI Movie Studio (v2.3)
color 0B

:: 1. Python Environment Detection
set "PYTHON_EXE="
if exist "%~dp0.venv\Scripts\python.exe" (
    set "PYTHON_EXE=%~dp0.venv\Scripts\python.exe"
) else (
    where python >nul 2>&1
    if not errorlevel 1 set "PYTHON_EXE=python"
)

if not defined PYTHON_EXE (
    echo.
    echo ===============================================================================
    echo [ERROR] Python 3.8+ or virtual environment not found!
    echo Please make sure Python is installed and added to PATH.
    echo ===============================================================================
    echo.
    pause
    exit /b 1
)

:MENU
cls
echo ===============================================================================
echo            PAI AI MOVIE STUDIO (v2.3) - MASTER LAUNCHER
echo ===============================================================================
echo.
echo    [1] Launch Interactive Web UI Dashboard (Recommended)
echo    [2] Run Movie Recap Studio (Auto-Process videos in "movies" folder)
echo    [3] Run Movie Recap Studio for a Single URL or Video File
echo    [4] Run Original Audio and Burmese Hardsub Studio (Engine 3)
echo    [5] Run YouTube Subtitle and Transcript Studio (Engine 2)
echo    [6] Run Comprehensive System Health Check
echo    [7] Run in Docker Container (docker compose up)
echo    [0] Exit
echo.
echo ===============================================================================
set "choice="
set /p choice="Select an option [0-7, press Enter for Web UI]: "

if not defined choice set "choice=1"
if "%choice%"=="1" goto WEBUI
if "%choice%"=="2" goto RECAP_BATCH
if "%choice%"=="3" goto RECAP_SINGLE
if "%choice%"=="4" goto HARDSUB
if "%choice%"=="5" goto SUBTITLE
if "%choice%"=="6" goto HEALTH
if "%choice%"=="7" goto DOCKER
if "%choice%"=="0" goto EXIT
goto MENU

:WEBUI
cls
echo ===============================================================================
echo LAUNCHING PAI AI MOVIE STUDIO - WEB UI DASHBOARD...
echo ===============================================================================
echo [*] Checking Port 5000 availability...
powershell -NoProfile -Command "Get-NetTCPConnection -LocalPort 5000 -State Listen -ErrorAction SilentlyContinue | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force -ErrorAction SilentlyContinue }" >nul 2>&1

echo [*] Opening Browser at http://localhost:5000 ...
start http://localhost:5000

echo.
echo ===============================================================================
echo  Dashboard Link : http://localhost:5000
echo  To Stop Server : Press Ctrl + C in this terminal window
echo ===============================================================================
echo.

"%PYTHON_EXE%" web_ui.py
if errorlevel 1 (
    echo.
    echo [ERROR] Web UI stopped with an error code.
    pause
)
goto MENU

:RECAP_BATCH
cls
echo ===============================================================================
echo STARTING BATCH MOVIE RECAP GENERATION FOR "movies" FOLDER...
echo ===============================================================================
"%PYTHON_EXE%" main.py --batch
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
set "input_src="
set /p "input_src=Input URL or File Path: "
if not defined input_src goto MENU
cls
echo ===============================================================================
echo PROCESSING: !input_src!
echo ===============================================================================
"%PYTHON_EXE%" main.py "!input_src!"
echo.
echo ===============================================================================
echo Processing Complete! Press any key to return to menu...
pause >nul
goto MENU

:HARDSUB
cls
echo ===============================================================================
echo ORIGINAL AUDIO AND BURMESE HARDSUB STUDIO
echo ===============================================================================
set "hs_input="
set /p "hs_input=Enter Video URL or File Path: "
if not defined hs_input goto MENU

echo.
echo Select Format: [1] Both 16:9 + 9:16 (Default) | [2] 16:9 Only | [3] 9:16 Only
set "hs_fmt_choice=1"
set /p "hs_fmt_choice=Choice [1-3, Enter for Both]: "
set "hs_fmt=both"
if "%hs_fmt_choice%"=="2" set "hs_fmt=16:9"
if "%hs_fmt_choice%"=="3" set "hs_fmt=9:16"

echo.
echo Select Subtitle Style: [1] Cinema Box (Default) | [2] TikTok Yellow | [3] Classic White
set "hs_style_choice=1"
set /p "hs_style_choice=Choice [1-3, Enter for Box Black]: "
set "hs_style=box_black"
if "%hs_style_choice%"=="2" set "hs_style=yellow_pop"
if "%hs_style_choice%"=="3" set "hs_style=white_stroke"

cls
echo ===============================================================================
echo [*] Running Hardsub Studio Engine...
echo ===============================================================================
"%PYTHON_EXE%" hardsub_engine.py "!hs_input!" --format "%hs_fmt%" --style "%hs_style%" --blur auto --color-grading
echo.
echo ===============================================================================
echo Hardsub Studio Complete! Press any key to return to menu...
pause >nul
goto MENU

:SUBTITLE
cls
echo ===============================================================================
echo YOUTUBE SUBTITLE AND TRANSCRIPT STUDIO
echo ===============================================================================
set "sub_input="
set /p "sub_input=Enter YouTube URL or Video File: "
if not defined sub_input goto MENU

cls
echo ===============================================================================
echo [*] Running Subtitle Engine...
echo ===============================================================================
"%PYTHON_EXE%" subtitle_engine.py -i "!sub_input!" --source-lang auto
echo.
echo ===============================================================================
echo Subtitle Engine Complete! Press any key to return to menu...
pause >nul
goto MENU

:HEALTH
cls
echo ===============================================================================
echo RUNNING SYSTEM HEALTH CHECK...
echo ===============================================================================
"%PYTHON_EXE%" -c "import sys, brain.config as cfg; from agents.video_merger_agent import detect_hardware_encoder, _get_ffmpeg_bin; ff = _get_ffmpeg_bin(); enc = detect_hardware_encoder(); keys = cfg.load_config().get('gemini', {}).get('api_keys', []); print('[*] Python Version :', sys.version.split()[0]); print('[*] FFmpeg Binary  :', ff or 'NOT FOUND'); print('[*] Video Encoder  :', enc.get('label', 'Unknown'), '(' + enc.get('codec', 'libx264') + ')'); print('[*] Gemini Keys    :', len(keys), 'key(s) configured in config.json')"
echo.
echo ===============================================================================
echo Press any key to return to menu...
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

:EXIT
exit /b 0
