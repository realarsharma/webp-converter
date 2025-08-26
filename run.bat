@echo off
setlocal

REM Set project folder
set "PROJECT_DIR=%~dp0"

REM VENV folder
set "VENV_DIR=%PROJECT_DIR%webp-converter-env"

REM Check if venv exists, if not, create it
if not exist "%VENV_DIR%" (
    echo Creating virtual environment...
    python -m venv "%VENV_DIR%"
    if %errorlevel% neq 0 (
        echo ⚠️ Failed to create virtual environment.
        pause
        exit /b 1
    )
)

REM Set venv python and pip paths
set "VENV_PYTHON=%VENV_DIR%\Scripts\python.exe"
set "VENV_PIP=%VENV_DIR%\Scripts\pip.exe"

REM Debug: Show which python and pip will be used
echo Using Python: %VENV_PYTHON%
echo Using Pip: %VENV_PIP%
"%VENV_PYTHON%" --version
"%VENV_PIP%" --version

REM Upgrade pip
echo Upgrading pip...
"%VENV_PIP%" install --upgrade pip

REM Install dependencies if requirements.txt exists
if exist "%PROJECT_DIR%requirements.txt" (
    echo Installing required packages...
    "%VENV_PIP%" install -r "%PROJECT_DIR%requirements.txt"
)

REM Run run.py or main.py using venv python
if exist "%PROJECT_DIR%run.py" (
    echo Running run.py...
    "%VENV_PYTHON%" "%PROJECT_DIR%run.py"
) else (
    echo Running main.py...
    "%VENV_PYTHON%" "%PROJECT_DIR%main.py"
)

REM Always pause to see output
echo.
echo Press any key to exit...
pause