# 🚀 Guía Rápida - Bot de Telegram

## Inicio Rápido en 3 Pasos

### 1️⃣ Instalar Dependencias

**Windows:**
```bash
pip install python-telegram-bot aiohttp
```

**Linux/Mac:**
```bash
pip3 install python-telegram-bot aiohttp
```

O usando el archivo de requisitos:
```bash
pip install -r requirements.txt
```

---

### 2️⃣ Ejecutar el Bot

**Opción A - Comando directo:**

```bash
# Windows
python bot.py

# Linux/Mac
python3 bot.py
```

**Opción B - Script de inicio:**

```bash
# Windows
start_bot.bat

# Linux/Mac
chmod +x start_bot.sh
./start_bot.sh
```

---

### 3️⃣ Probar el Bot en Telegram

1. Busca tu bot en Telegram
2. Envía el comando `/start`
3. Deberías ver el mensaje de bienvenida

---

## ✅ Verificar que Funciona

### Comandos de Prueba:

```
/start          → Mensaje de bienvenida
/help           → Lista de comandos
/estadisticas   → Estadísticas del sistema
/zonas          → Zonas de actividad
```

### Comandos Autenticados:

```
/login email@example.com password
/buscar_pandilla Los Tigres
/incidentes
/logout
```

---

## 🔧 Si Algo No Funciona

### Python no está instalado
→ Descarga desde: https://www.python.org/downloads/

### Error "No module named 'telegram'"
→ Ejecuta: `pip install python-telegram-bot`

### Error "No module named 'aiohttp'"
→ Ejecuta: `pip install aiohttp`

### El bot no responde
→ Verifica que el script esté corriendo
→ Revisa el archivo `bot.log`

---

## 📱 Ejemplo de Uso

```
Usuario: /start
Bot: 🛡️ Bienvenido al Sistema de Registro de Pandillas...

Usuario: /estadisticas
Bot: 📊 Estadísticas Generales
     🎯 Pandillas Registradas: 5
     ...

Usuario: /login admin@example.com password123
Bot: ✅ Sesión iniciada correctamente
     👤 Usuario: Admin User
     🔐 Rol: Administrador

Usuario: /buscar_pandilla Los Tigres
Bot: 🔍 Información de Pandilla
     📛 Nombre: Los Tigres
     👤 Líder: Juan Pérez
     ...
```

---

## 📚 Documentación Completa

Consulta `README.md` para instrucciones detalladas sobre:
- Configuración avanzada
- Despliegue en producción
- Troubleshooting completo
- Gestión de logs

---

**¡Listo! Tu bot está funcionando** 🎉
