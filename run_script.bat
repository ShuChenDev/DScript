@echo off
setlocal
call "%~dp0\venv\Scripts\activate.bat"
python "%~dp0\main.py"
deactivate
