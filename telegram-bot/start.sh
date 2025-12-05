#!/bin/bash

# Script de inicio rápido para el Bot de Telegram
# Sistema de Registro de Pandillas - San Luis Potosí

echo "🤖 Iniciando Bot de Telegram..."
echo "================================"
echo ""

# Verificar que Python está instalado
if ! command -v python3 &> /dev/null
then
    echo "❌ Error: Python 3 no está instalado"
    echo "   Instálalo desde https://www.python.org/downloads/"
    exit 1
fi

echo "✅ Python encontrado: $(python3 --version)"
echo ""

# Verificar dependencias
echo "📦 Verificando dependencias..."

if ! python3 -c "import telegram" 2>/dev/null
then
    echo "⚠️  python-telegram-bot no está instalado"
    echo "   Instalando dependencias..."
    pip3 install -r requirements.txt
else
    echo "✅ python-telegram-bot instalado"
fi

if ! python3 -c "import aiohttp" 2>/dev/null
then
    echo "⚠️  aiohttp no está instalado"
    echo "   Instalando dependencias..."
    pip3 install -r requirements.txt
else
    echo "✅ aiohttp instalado"
fi

echo ""
echo "🚀 Iniciando bot..."
echo "================================"
echo ""
echo "Presiona Ctrl+C para detener el bot"
echo ""

# Ejecutar el bot
python3 bot.py
