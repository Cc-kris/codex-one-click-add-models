@echo off
chcp 65001 >nul
setlocal
cd /d "%~dp0"
where python >nul 2>nul
if %errorlevel%==0 (
  python "%~dp0install_ccai_catalog.py"
  goto :eof
)
where py >nul 2>nul
if %errorlevel%==0 (
  py -3 "%~dp0install_ccai_catalog.py"
  goto :eof
)
echo Python 3 not found. Install Python 3 and retry.
pause
exit /b 1
