# Bot de Telegram - Sistema de Registro de Pandillas
## San Luis Potosí

Bot de Telegram oficial para consultar información del Sistema de Registro de Pandillas de San Luis Potosí.

---

## 📋 Requisitos Previos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Token de Bot de Telegram (obtenido de @BotFather)
- Acceso al proyecto de Supabase

---

## 🚀 Instalación

### 1. Instalar Python

Asegúrate de tener Python instalado:

```bash
python --version
# o
python3 --version
```

Si no tienes Python instalado, descárgalo desde [python.org](https://www.python.org/downloads/)

### 2. Instalar Dependencias

Navega a la carpeta del bot e instala las bibliotecas necesarias:

```bash
cd telegram-bot
pip install python-telegram-bot aiohttp
```

O si estás en Linux/Mac:

```bash
pip3 install python-telegram-bot aiohttp
```

### 3. Configuración

El archivo `bot.py` ya está configurado con las credenciales correctas de Supabase. No necesitas modificar nada.

**Configuración incluida:**
- ✅ Token de Telegram
- ✅ URL del proyecto Supabase
- ✅ Clave de API (Anon Key)
- ✅ Endpoints de la API

---

## ▶️ Ejecución

Para iniciar el bot, ejecuta:

```bash
python bot.py
```

O en Linux/Mac:

```bash
python3 bot.py
```

Deberías ver un mensaje similar a:

```
2024-XX-XX XX:XX:XX - __main__ - INFO - Bot iniciado correctamente...
```

El bot ahora está en línea y esperando comandos.

---

## 📱 Uso del Bot en Telegram

### Comandos Públicos (sin autenticación)

- `/start` - Muestra el mensaje de bienvenida
- `/help` - Muestra la ayuda completa
- `/estadisticas` - Muestra estadísticas generales del sistema
- `/zonas` - Consulta las zonas de mayor actividad pandilleril

### Comandos Autenticados (requieren login)

Primero debes autenticarte:

```
/login usuario@email.com tupassword
```

Luego podrás usar:

- `/buscar_pandilla <nombre>` - Buscar información de una pandilla
  - Ejemplo: `/buscar_pandilla Los Tigres`
  
- `/buscar_integrante <nombre>` - Buscar información de un integrante
  - Ejemplo: `/buscar_integrante Juan Pérez`
  
- `/incidentes` - Ver incidentes de los últimos 7 días

- `/logout` - Cerrar sesión actual

---

## 🔧 Funcionalidades

### ✅ Comandos que funcionan actualmente:

1. **Comandos básicos:**
   - ✅ `/start` - Bienvenida
   - ✅ `/help` - Ayuda
   - ✅ `/zonas` - Zonas de actividad (datos estáticos)

2. **Autenticación:**
   - ✅ `/login` - Inicio de sesión
   - ✅ `/logout` - Cierre de sesión

3. **Consultas (requieren API activa):**
   - ✅ `/estadisticas` - Conecta con la API
   - ✅ `/buscar_pandilla` - Busca en la base de datos
   - ✅ `/buscar_integrante` - Busca en la base de datos
   - ✅ `/incidentes` - Consulta incidentes recientes

---

## 🛠️ Troubleshooting

### Error: "ModuleNotFoundError: No module named 'telegram'"

**Solución:**
```bash
pip install python-telegram-bot
```

### Error: "ModuleNotFoundError: No module named 'aiohttp'"

**Solución:**
```bash
pip install aiohttp
```

### El bot no responde a comandos

**Posibles causas:**
1. El script no está en ejecución
2. El token de Telegram es incorrecto
3. No tienes conexión a internet

**Solución:**
- Verifica que el script esté corriendo sin errores
- Revisa los logs en `bot.log`

### Error al conectar con la API

**Posibles causas:**
1. El proyecto de Supabase no está desplegado
2. Las credenciales de Supabase son incorrectas
3. Los endpoints de la API no están disponibles

**Solución:**
- Verifica que el proyecto de Supabase esté activo
- Confirma que las credenciales en `bot.py` sean correctas
- Prueba los endpoints directamente en el navegador

---

## 📝 Logs

El bot genera logs automáticamente en el archivo `bot.log`. Puedes consultarlo para ver:

- Errores de conexión
- Comandos ejecutados
- Problemas de autenticación
- Excepciones del sistema

Para ver los logs en tiempo real:

```bash
# En Windows
type bot.log

# En Linux/Mac
tail -f bot.log
```

---

## 🌐 Despliegue en Producción

Para mantener el bot ejecutándose 24/7, considera usar:

### Opción 1: Heroku
```bash
# Requiere crear un Procfile
echo "worker: python bot.py" > Procfile
```

### Opción 2: Railway
1. Conecta tu repositorio a Railway
2. Railway detectará automáticamente el proyecto Python

### Opción 3: VPS (Linux Server)

Usar `systemd` para ejecutar como servicio:

```bash
# Crear archivo de servicio
sudo nano /etc/systemd/system/telegram-bot.service
```

Contenido:
```ini
[Unit]
Description=Telegram Bot - Sistema de Pandillas
After=network.target

[Service]
Type=simple
User=tu_usuario
WorkingDirectory=/ruta/al/telegram-bot
ExecStart=/usr/bin/python3 bot.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Activar el servicio:
```bash
sudo systemctl enable telegram-bot
sudo systemctl start telegram-bot
sudo systemctl status telegram-bot
```

---

## 📚 Recursos Adicionales

- [Documentación de python-telegram-bot](https://docs.python-telegram-bot.org/)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [BotFather - Crear y gestionar bots](https://t.me/botfather)
- [Supabase Documentation](https://supabase.com/docs)

---

## 🆘 Soporte

Si tienes problemas con el bot:

1. Revisa el archivo `bot.log` para ver errores específicos
2. Verifica que todas las dependencias estén instaladas
3. Confirma que las credenciales de Supabase sean correctas
4. Consulta el panel de administración en la aplicación web

---

## ⚙️ Configuración Avanzada

El archivo `config.example.py` contiene opciones de configuración adicionales:

- Nivel de logging (DEBUG, INFO, WARNING, ERROR)
- Timeout de sesión
- IDs de administradores con permisos especiales

Para usar un archivo de configuración personalizado:

```bash
cp config.example.py config.py
# Edita config.py con tus preferencias
```

---

## 📄 Licencia

Este bot es parte del Sistema de Registro de Pandillas de San Luis Potosí.

---

**Última actualización:** Diciembre 2024
