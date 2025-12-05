@echo off
REM Script de inicio rápido para el Bot de Telegram (Windows)
REM Sistema de Registro de Pandillas - San Luis Potosí

echo.
echo ================================================
echo   Bot de Telegram - Sistema de Pandillas SLP
echo ================================================
echo.

REM Verificar que Python está instalado
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python no esta instalado
    echo         Instalalo desde https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [OK] Python encontrado
echo.

REM Verificar dependencias
echo Verificando dependencias...
echo.

python -c "import telegram" >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] python-telegram-bot no esta instalado
    echo     Instalando dependencias...
    pip install -r requirements.txt
) else (
    echo [OK] python-telegram-bot instalado
)

python -c "import aiohttp" >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] aiohttp no esta instalado
    echo     Instalando dependencias...
    pip install -r requirements.txt
) else (
    echo [OK] aiohttp instalado
)

echo.
echo ================================================
echo   Iniciando bot...
echo ================================================
echo.
echo Presiona Ctrl+C para detener el bot
echo.

REM Ejecutar el bot
python bot.py

pause
