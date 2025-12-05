# 🚀 Guía Completa de Despliegue - Bot de Telegram

## Sistema de Registro de Pandillas - San Luis Potosí

Esta guía te llevará paso a paso para tener tu bot de Telegram completamente funcional y desplegado en producción.

---

## 📋 Tabla de Contenidos

1. [Requisitos Previos](#requisitos-previos)
2. [Configuración Inicial](#configuración-inicial)
3. [Pruebas Locales](#pruebas-locales)
4. [Despliegue en Producción](#despliegue-en-producción)
5. [Verificación y Monitoreo](#verificación-y-monitoreo)
6. [Solución de Problemas](#solución-de-problemas)

---

## 1️⃣ Requisitos Previos

### Software Necesario

- **Python 3.8 o superior**
  - Descarga: https://www.python.org/downloads/
  - Durante la instalación en Windows, marca la opción "Add Python to PATH"

- **Git** (opcional pero recomendado)
  - Descarga: https://git-scm.com/downloads

- **Editor de código** (opcional)
  - Visual Studio Code: https://code.visualstudio.com/

### Cuentas Necesarias

- **Cuenta de Telegram**
- **Token de Bot de Telegram** (obtendremos esto en el siguiente paso)
- **Credenciales de Supabase** (ya incluidas en el código)

---

## 2️⃣ Configuración Inicial

### Paso 1: Crear el Bot en Telegram

1. **Abre Telegram** en tu teléfono o computadora

2. **Busca @BotFather**
   - Es el bot oficial de Telegram para crear y administrar bots
   - Tiene una verificación azul (✓)

3. **Inicia una conversación** con @BotFather
   - Envía el comando: `/start`

4. **Crea tu bot**
   ```
   /newbot
   ```

5. **Sigue las instrucciones:**
   - Te pedirá un **nombre** para tu bot (ejemplo: "Sistema Pandillas SLP")
   - Te pedirá un **nombre de usuario** (debe terminar en "bot")
     - Ejemplo: `slp_pandillas_bot` o `sistema_pandillas_slp_bot`

6. **¡Importante!** BotFather te dará un **token** como este:
   ```
   123456789:ABCdefGHIjklMNOpqrsTUVwxyz-1234567890
   ```
   - ⚠️ **Guarda este token en un lugar seguro**
   - ⚠️ **No lo compartas con nadie**
   - Este token es como la contraseña de tu bot

7. **(Opcional) Personaliza tu bot**
   ```
   /setdescription    → Descripción del bot
   /setabouttext      → Texto "Acerca de"
   /setuserpic        → Foto de perfil
   ```

### Paso 2: Configurar el Token en el Código

1. **Abre el archivo `bot.py`** en la carpeta `telegram-bot`

2. **Busca la línea 19** (aproximadamente):
   ```python
   TELEGRAM_TOKEN = "7973091439:AAGdIywM6mfFv-o03xCXhxVQO3nzDNbnGDU"
   ```

3. **Reemplaza el token** con el tuyo que obtuviste de BotFather:
   ```python
   TELEGRAM_TOKEN = "TU_TOKEN_AQUI"
   ```

4. **Guarda el archivo** (Ctrl+S o Cmd+S)

### Paso 3: Instalar Dependencias

#### En Windows:

```bash
# Abre PowerShell o CMD en la carpeta telegram-bot
cd ruta/al/proyecto/telegram-bot

# Instala las dependencias
pip install python-telegram-bot aiohttp

# O usando el archivo requirements.txt
pip install -r requirements.txt
```

#### En Linux/Mac:

```bash
# Abre Terminal en la carpeta telegram-bot
cd ruta/al/proyecto/telegram-bot

# Instala las dependencias
pip3 install python-telegram-bot aiohttp

# O usando el archivo requirements.txt
pip3 install -r requirements.txt
```

---

## 3️⃣ Pruebas Locales

### Ejecutar el Bot Localmente

#### Opción A - Comando Directo:

**Windows:**
```bash
python bot.py
```

**Linux/Mac:**
```bash
python3 bot.py
```

#### Opción B - Scripts de Inicio:

**Windows:**
```bash
start_bot.bat
```

**Linux/Mac:**
```bash
chmod +x start_bot.sh
./start_bot.sh
```

### Verificar que el Bot Funciona

1. **Deberías ver en la consola:**
   ```
   2024-12-05 10:30:45 - __main__ - INFO - Bot iniciado correctamente...
   2024-12-05 10:30:45 - __main__ - INFO - Esperando comandos...
   ```

2. **Abre Telegram** y busca tu bot por su nombre de usuario

3. **Prueba estos comandos:**
   ```
   /start          → Mensaje de bienvenida
   /help           → Lista de comandos
   /estadisticas   → Estadísticas del sistema
   /zonas          → Zonas de actividad
   ```

4. **Si todo funciona correctamente:**
   - El bot responde instantáneamente
   - Los mensajes están formateados correctamente
   - No hay errores en la consola

### ⚠️ Nota Importante sobre Pruebas Locales

Mientras el bot esté corriendo en tu computadora:
- ✅ **Debes mantener el script ejecutándose**
- ✅ **Debes mantener tu computadora encendida**
- ✅ **Debes estar conectado a internet**

Para uso en producción 24/7, continúa con la siguiente sección.

---

## 4️⃣ Despliegue en Producción

Para que tu bot funcione 24/7 sin necesidad de mantener tu computadora encendida, necesitas desplegarlo en un servidor. Aquí hay varias opciones:

### Opción 1: Railway (Recomendado - Más Fácil) 🚂

**Ventajas:**
- ✅ Gratuito (500 horas/mes)
- ✅ Muy fácil de configurar
- ✅ Integración con GitHub
- ✅ Logs en tiempo real

**Pasos:**

1. **Crea una cuenta en Railway**
   - Ve a https://railway.app/
   - Regístrate con GitHub

2. **Prepara tu repositorio**
   - Sube tu código a GitHub (si aún no lo has hecho)
   - Asegúrate de que la carpeta `telegram-bot` esté en tu repositorio

3. **Crea un archivo `Procfile`** en la carpeta `telegram-bot`:
   ```
   worker: python bot.py
   ```

4. **Crea un archivo `runtime.txt`** (opcional):
   ```
   python-3.11.0
   ```

5. **Despliega en Railway:**
   - En Railway, haz clic en "New Project"
   - Selecciona "Deploy from GitHub repo"
   - Elige tu repositorio
   - Railway detectará automáticamente que es un proyecto Python

6. **Configura las variables de entorno:**
   - En Railway, ve a "Variables"
   - Agrega:
     - `TELEGRAM_TOKEN` = tu token de Telegram
     - (Opcional) `SUPABASE_URL` = URL de tu proyecto Supabase
     - (Opcional) `SUPABASE_KEY` = Anon Key de Supabase

7. **Inicia el servicio:**
   - Railway comenzará a construir y desplegar automáticamente
   - Verifica los logs para confirmar que está funcionando

---

### Opción 2: Heroku 🟣

**Ventajas:**
- ✅ Gratuito con limitaciones
- ✅ Muy popular y bien documentado
- ✅ Fácil de usar

**Pasos:**

1. **Crea una cuenta en Heroku**
   - Ve a https://www.heroku.com/
   - Regístrate gratis

2. **Instala Heroku CLI**
   - Descarga: https://devcenter.heroku.com/articles/heroku-cli
   - Instala y reinicia tu terminal

3. **Inicia sesión en Heroku:**
   ```bash
   heroku login
   ```

4. **Crea un nuevo proyecto:**
   ```bash
   cd telegram-bot
   heroku create nombre-de-tu-bot
   ```

5. **Crea un archivo `Procfile`**:
   ```
   worker: python bot.py
   ```

6. **Configura las variables de entorno:**
   ```bash
   heroku config:set TELEGRAM_TOKEN=tu_token_aqui
   ```

7. **Despliega el bot:**
   ```bash
   git init
   git add .
   git commit -m "Deploy bot"
   git push heroku main
   ```

8. **Escala el worker:**
   ```bash
   heroku ps:scale worker=1
   ```

9. **Verifica los logs:**
   ```bash
   heroku logs --tail
   ```

---

### Opción 3: VPS (Linux Server) 🖥️

**Ventajas:**
- ✅ Control total
- ✅ Sin limitaciones
- ✅ Ideal para producción

**Servicios recomendados:**
- DigitalOcean (desde $5/mes)
- Linode (desde $5/mes)
- AWS Lightsail (desde $3.50/mes)
- Google Cloud Platform (crédito gratis inicial)

**Pasos:**

1. **Contrata un VPS** con Ubuntu 20.04 o superior

2. **Conéctate por SSH:**
   ```bash
   ssh root@tu-ip-servidor
   ```

3. **Actualiza el sistema:**
   ```bash
   apt update && apt upgrade -y
   ```

4. **Instala Python y pip:**
   ```bash
   apt install python3 python3-pip -y
   ```

5. **Crea un usuario para el bot:**
   ```bash
   adduser telegram-bot
   su - telegram-bot
   ```

6. **Sube tu código** (usando git o scp):
   ```bash
   git clone https://github.com/tu-usuario/tu-repo.git
   cd tu-repo/telegram-bot
   ```

7. **Instala dependencias:**
   ```bash
   pip3 install -r requirements.txt
   ```

8. **Crea un servicio systemd:**
   ```bash
   sudo nano /etc/systemd/system/telegram-bot.service
   ```

   Contenido:
   ```ini
   [Unit]
   Description=Telegram Bot - Sistema de Pandillas
   After=network.target

   [Service]
   Type=simple
   User=telegram-bot
   WorkingDirectory=/home/telegram-bot/tu-repo/telegram-bot
   ExecStart=/usr/bin/python3 bot.py
   Restart=always
   RestartSec=10

   [Install]
   WantedBy=multi-user.target
   ```

9. **Habilita e inicia el servicio:**
   ```bash
   sudo systemctl enable telegram-bot
   sudo systemctl start telegram-bot
   sudo systemctl status telegram-bot
   ```

10. **Ver logs:**
    ```bash
    sudo journalctl -u telegram-bot -f
    ```

---

### Opción 4: PythonAnywhere 🐍

**Ventajas:**
- ✅ Especializado en Python
- ✅ Cuenta gratuita disponible
- ✅ No necesitas conocimientos de DevOps

**Pasos:**

1. **Crea una cuenta en PythonAnywhere**
   - Ve a https://www.pythonanywhere.com/
   - Regístrate gratis

2. **Sube tu código:**
   - Usa el Dashboard para subir archivos
   - O clona desde GitHub

3. **Instala dependencias:**
   - Abre una consola Bash
   ```bash
   pip3 install --user python-telegram-bot aiohttp
   ```

4. **Configura una tarea programada:**
   - Ve a "Tasks"
   - Agrega: `python3 /home/tuusuario/telegram-bot/bot.py`

---

## 5️⃣ Verificación y Monitoreo

### Verificar que el Bot está en Línea

1. **Envía `/start` a tu bot en Telegram**
   - Debe responder inmediatamente

2. **Prueba comandos autenticados:**
   ```
   /login admin@example.com password
   /buscar_pandilla nombre
   /incidentes
   ```

3. **Verifica los logs del servidor:**
   - En Railway: Panel de Logs
   - En Heroku: `heroku logs --tail`
   - En VPS: `journalctl -u telegram-bot -f`

### Monitorear el Rendimiento

#### En Railway:
- Dashboard → Logs → Ver logs en tiempo real
- Métricas de uso de CPU y memoria

#### En Heroku:
```bash
heroku ps
heroku logs --tail
```

#### En VPS:
```bash
# Estado del servicio
sudo systemctl status telegram-bot

# Uso de recursos
top
htop

# Logs
tail -f /path/to/bot.log
```

### Estadísticas del Bot

Puedes agregar un comando especial para administradores:

```python
# Ya incluido en bot.py
@application.command
async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Estadísticas del bot (solo admin)"""
    stats_text = f"""
📊 Estadísticas del Bot

⏰ Tiempo activo: {uptime}
👥 Usuarios activos: {active_users}
📨 Mensajes procesados: {message_count}
🔄 Comandos ejecutados: {command_count}
    """
    await update.message.reply_text(stats_text)
```

---

## 6️⃣ Solución de Problemas

### Problema: "Token inválido"

**Causa:** El token de Telegram es incorrecto

**Solución:**
1. Verifica que copiaste el token completo de BotFather
2. No debe tener espacios al principio o final
3. Debe tener el formato: `123456789:ABCdef...`

---

### Problema: "No module named 'telegram'"

**Causa:** Las dependencias no están instaladas

**Solución:**
```bash
pip install python-telegram-bot aiohttp
```

---

### Problema: "Connection error"

**Causa:** Problemas de conexión a internet o firewall

**Solución:**
1. Verifica tu conexión a internet
2. Si estás en un VPS, verifica el firewall:
   ```bash
   sudo ufw allow 443/tcp
   sudo ufw allow 80/tcp
   ```

---

### Problema: "Bot no responde"

**Causa:** El script no está corriendo o hay un error

**Solución:**
1. Verifica que el script esté ejecutándose:
   ```bash
   # En VPS
   sudo systemctl status telegram-bot
   
   # En local
   ps aux | grep bot.py
   ```

2. Revisa los logs para ver errores específicos

---

### Problema: "Error al consultar la API"

**Causa:** El servidor de Supabase no está disponible o las credenciales son incorrectas

**Solución:**
1. Verifica que el proyecto de Supabase esté activo
2. Confirma que las credenciales sean correctas:
   - SUPABASE_URL
   - SUPABASE_ANON_KEY

---

### Problema: "ModuleNotFoundError: No module named 'aiohttp'"

**Causa:** Falta la biblioteca aiohttp

**Solución:**
```bash
pip install aiohttp
```

---

## 📚 Recursos Adicionales

### Documentación Oficial

- **Python Telegram Bot:** https://docs.python-telegram-bot.org/
- **Telegram Bot API:** https://core.telegram.org/bots/api
- **BotFather:** https://t.me/botfather
- **Supabase Docs:** https://supabase.com/docs

### Tutoriales en Video

- Crear un bot de Telegram: https://www.youtube.com/results?search_query=crear+bot+telegram+python
- Desplegar en Railway: https://www.youtube.com/results?search_query=deploy+python+railway
- Desplegar en Heroku: https://www.youtube.com/results?search_query=deploy+python+heroku

### Comunidades

- Stack Overflow (tag: python-telegram-bot)
- Reddit: r/TelegramBots
- GitHub Discussions del proyecto

---

## 🔒 Mejores Prácticas de Seguridad

1. **Nunca subas tu token a repositorios públicos**
   - Usa variables de entorno
   - Agrega `.env` al `.gitignore`

2. **Limita el acceso a comandos sensibles**
   - Ya implementado en el código con autenticación

3. **Actualiza regularmente las dependencias**
   ```bash
   pip install --upgrade python-telegram-bot
   ```

4. **Monitorea los logs constantemente**
   - Configura alertas para errores críticos

5. **Haz backups regulares**
   - Especialmente de la base de datos

---

## ✅ Checklist Final

Antes de considerar el despliegue completo, verifica:

- [ ] El bot responde al comando `/start`
- [ ] Los comandos públicos funcionan (`/help`, `/estadisticas`, `/zonas`)
- [ ] La autenticación funciona (`/login`)
- [ ] Los comandos autenticados funcionan (`/buscar_pandilla`, `/incidentes`)
- [ ] El bot se reconecta automáticamente si hay un error
- [ ] Los logs se generan correctamente
- [ ] El bot está corriendo 24/7 (si ya desplegaste)
- [ ] Tienes un sistema de monitoreo configurado
- [ ] Las variables de entorno están configuradas correctamente
- [ ] El código está en un repositorio (backup)

---

## 🎉 ¡Felicitaciones!

Si has completado todos los pasos, tu bot de Telegram está completamente funcional y desplegado en producción.

### Próximos Pasos

1. **Personaliza los mensajes** según tus necesidades
2. **Agrega más comandos** según sea necesario
3. **Implementa webhooks** para mayor eficiencia (opcional)
4. **Configura notificaciones automáticas** para eventos importantes
5. **Crea un dashboard de administración** (opcional)

---

## 📞 Soporte

Si tienes problemas o preguntas:

1. Revisa esta documentación completa
2. Consulta el archivo `README.md`
3. Revisa el archivo `QUICK_START.md` para soluciones rápidas
4. Consulta los logs del bot
5. Busca en Stack Overflow
6. Abre un issue en el repositorio del proyecto

---

**Última actualización:** Diciembre 2024  
**Versión del bot:** 1.0.0  
**Autor:** Sistema de Registro de Pandillas - San Luis Potosí
