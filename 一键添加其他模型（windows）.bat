@echo off
setlocal
cd /d "%~dp0"
set "PY=%~dp0codex-add-models\scripts\install_ccai_catalog.py"
where python >nul 2>nul
if %errorlevel%==0 (
  python "%PY%"
  goto :eof
)
where py >nul 2>nul
if %errorlevel%==0 (
  py -3 "%PY%"
  goto :eof
)
echo Python not found. Install Python 3 and retry.
pause
exit /b 1
