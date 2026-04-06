@echo off
title Bookshelf4MD

echo.
echo ========================================
echo   Bookshelf4MD - Markdown Bookshelf
echo ========================================
echo.

REM Check if .venv exists
if not exist ".venv" (
    echo [ERROR] Virtual environment not found
    echo Please run: python -m venv .venv
    pause
    exit /b 1
)

REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Check if Flask is installed
python -c "import flask" 2>nul
if errorlevel 1 (
    echo [INFO] Installing required packages...
    pip install -r requirements.txt
    echo.
)

REM Create mds directory if not exists
if not exist "mds" mkdir mds

echo [INFO] Starting server...
echo [INFO] Open http://localhost:5000 in your browser
echo.
echo [INFO] Press Ctrl+C to stop the server
echo ========================================
echo.

python app.py

pause
