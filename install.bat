@echo off
REM Wakeon Voice Assistant Installation Script for Windows

echo 🎙️  Wakeon Voice Assistant - Installation
echo ==========================================

REM Check if Python 3 is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.8 or higher.
    pause
    exit /b 1
)

echo ✅ Python detected

REM Create virtual environment
echo 📦 Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Upgrade pip
echo ⬆️  Upgrading pip...
python -m pip install --upgrade pip

REM Install requirements
echo 📚 Installing dependencies...
pip install -r requirements.txt

REM Create necessary directories
echo 📁 Creating directories...
if not exist models mkdir models
if not exist logs mkdir logs
if not exist audio_output mkdir audio_output

REM Copy environment file
if not exist .env (
    echo ⚙️  Creating .env file from template...
    copy env.example .env
    echo 📝 Please edit .env file with your configuration
)

echo.
echo 🎉 Installation completed successfully!
echo.
echo Next steps:
echo 1. Edit .env file with your OpenAI API key
echo 2. Download Vosk model: https://alphacephei.com/vosk/models
echo 3. Run tests: python test_wakeon.py
echo 4. Start Wakeon: python wakeon.py
echo.
echo To activate the virtual environment in the future:
echo venv\Scripts\activate.bat
pause 