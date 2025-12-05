import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    CallbackQueryHandler,
    filters,
)
import asyncio
from datetime import datetime, timedelta

# Configuración
TELEGRAM_TOKEN = "8321947546:AAF5N2AXZvpPD_sRYG9Vr_cynt3VKHEjkKM"

# Configuración de Supabase - CORREGIDA
SUPABASE_PROJECT_ID = "uapxsrbetmyshfscqpot"
SUPABASE_URL = f"https://uapxsrbetmyshfscqpot.supabase.co"
SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVhcHhzcmJldG15c2hmc2NxcG90Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjI0Nzg5NTQsImV4cCI6MjA3ODA1NDk1NH0.nfYp3Ugygrohex_lyM20G71unIOu94HrmJrbZ0xdEXg"
SUPABASE_FUNCTION_URL = f"https://uapxsrbetmyshfscqpot.supabase.co/functions/v1/make-server-98a674d7"

# Configurar logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers=[
        logging.FileHandler("bot.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Almacenar sesiones de usuarios (en producción, usar Redis o base de datos)
user_sessions = {}


# === COMANDOS BÁSICOS ===

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /start - Inicia el bot"""
    welcome_message = """
🛡️ *Bienvenido al Sistema de Registro de Pandillas*
_San Luis Potosí_

Comandos disponibles:

*Para todos los usuarios:*
/help - Mostrar ayuda
/estadisticas - Ver estadísticas generales
/zonas - Zonas con mayor actividad

*Para usuarios autenticados:*
/login - Iniciar sesión
/buscar_pandilla - Buscar pandilla
/buscar_integrante - Buscar integrante
/incidentes - Incidentes recientes
/logout - Cerrar sesión

⚠️ *Nota:* Algunas funciones requieren autenticación
    """
    await update.message.reply_text(welcome_message, parse_mode="Markdown")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /help - Muestra ayuda"""
    user_id = update.effective_user.id
    session = user_sessions.get(user_id)
    
    help_text = """
📖 *Ayuda - Sistema de Registro de Pandillas*

*Comandos Públicos:*
• `/estadisticas` - Muestra estadísticas generales
• `/zonas` - Consulta zonas de mayor actividad

*Comandos Autenticados:*
• `/login <email> <password>` - Iniciar sesión
  _Ejemplo: /login usuario@email.com mipassword_

• `/buscar_pandilla <nombre>` - Buscar una pandilla
  _Ejemplo: /buscar_pandilla Los Tigres_

• `/buscar_integrante <nombre>` - Buscar un integrante
  _Ejemplo: /buscar_integrante Juan Pérez_

• `/incidentes` - Ver incidentes de los últimos 7 días

• `/logout` - Cerrar sesión actual

*Estado actual:* """
    
    if session:
        help_text += f"✅ Sesión activa ({session['role']})"
    else:
        help_text += "❌ Sin sesión activa"
    
    await update.message.reply_text(help_text, parse_mode="Markdown")


# === AUTENTICACIÓN ===

async def login(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /login - Iniciar sesión"""
    user_id = update.effective_user.id
    
    # Verificar si ya hay sesión activa
    if user_id in user_sessions:
        await update.message.reply_text(
            "⚠️ Ya tienes una sesión activa. Usa /logout para cerrarla primero."
        )
        return
    
    # Verificar argumentos
    if len(context.args) < 2:
        await update.message.reply_text(
            "❌ Uso incorrecto. Formato: /login <email> <password>"
        )
        return
    
    email = context.args[0]
    password = " ".join(context.args[1:])
    
    try:
        # Llamada a API de autenticación
        import aiohttp
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{SUPABASE_FUNCTION_URL}/login",
                json={"email": email, "password": password},
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {SUPABASE_ANON_KEY}"
                }
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    
                    # Guardar sesión
                    user_sessions[user_id] = {
                        "token": data["accessToken"],
                        "user": data["user"],
                        "role": data["user"]["role"],
                        "login_time": datetime.now(),
                    }
                    
                    await update.message.reply_text(
                        f"✅ Sesión iniciada correctamente\n"
                        f"👤 Usuario: {data['user']['firstName']} {data['user']['lastName']}\n"
                        f"🔐 Rol: {data['user']['role'].capitalize()}"
                    )
                else:
                    await update.message.reply_text(
                        "❌ Error de autenticación. Verifica tus credenciales."
                    )
    
    except Exception as e:
        logger.error(f"Error en login: {e}")
        await update.message.reply_text(
            "❌ Error al conectar con el servidor. Intenta más tarde."
        )


async def logout(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /logout - Cerrar sesión"""
    user_id = update.effective_user.id
    
    if user_id in user_sessions:
        del user_sessions[user_id]
        await update.message.reply_text("✅ Sesión cerrada correctamente")
    else:
        await update.message.reply_text("⚠️ No tienes ninguna sesión activa")


# === CONSULTAS PÚBLICAS ===

async def estadisticas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /estadisticas - Muestra estadísticas generales"""
    try:
        # Llamada a API para obtener estadísticas
        import aiohttp
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{SUPABASE_FUNCTION_URL}/stats",
                headers={"Authorization": f"Bearer {SUPABASE_ANON_KEY}"}
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    
                    stats_text = f"""
📊 *Estadísticas Generales*

🎯 *Pandillas Registradas:* {data.get('totalGangs', 0)}
  • Alta peligrosidad: {data.get('highDanger', 0)}
  • Media peligrosidad: {data.get('mediumDanger', 0)}
  • Baja peligrosidad: {data.get('lowDanger', 0)}

👥 *Integrantes:* {data.get('totalMembers', 0)}

📋 *Incidentes (último mes):* {data.get('recentIncidents', 0)}

_Última actualización: {datetime.now().strftime('%d/%m/%Y %H:%M')}_
                    """
                    
                    await update.message.reply_text(stats_text, parse_mode="Markdown")
                else:
                    await update.message.reply_text(
                        "❌ Error al obtener estadísticas"
                    )
    
    except Exception as e:
        logger.error(f"Error en estadísticas: {e}")
        await update.message.reply_text(
            "❌ Error al conectar con el servidor"
        )


async def zonas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /zonas - Muestra zonas de mayor actividad"""
    zonas_text = """
📍 *Zonas con Mayor Actividad Pandilleril*

1. 🔴 *Colonia Centro*
   • 5 pandillas activas
   • Nivel de peligrosidad: Alto

2. 🟡 *Fraccionamiento Satélite*
   • 3 pandillas activas
   • Nivel de peligrosidad: Medio

3. 🟡 *Colonia Morales*
   • 3 pandillas activas
   • Nivel de peligrosidad: Medio

4. 🟢 *Zona Industrial*
   • 2 pandillas activas
   • Nivel de peligrosidad: Bajo

⚠️ *Recomendaciones:*
• Evita transitar solo por zonas de alta peligrosidad
• Reporta actividad sospechosa a las autoridades
• Mantente informado de incidentes recientes
    """
    
    await update.message.reply_text(zonas_text, parse_mode="Markdown")


# === CONSULTAS AUTENTICADAS ===

def require_auth(func):
    """Decorador para verificar autenticación"""
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.effective_user.id
        
        if user_id not in user_sessions:
            await update.message.reply_text(
                "🔒 Necesitas iniciar sesión para usar este comando.\n"
                "Usa: /login <email> <password>"
            )
            return
        
        # Verificar timeout de sesión (24 horas)
        session = user_sessions[user_id]
        if datetime.now() - session["login_time"] > timedelta(hours=24):
            del user_sessions[user_id]
            await update.message.reply_text(
                "⏰ Tu sesión ha expirado. Por favor inicia sesión nuevamente."
            )
            return
        
        return await func(update, context)
    
    return wrapper


@require_auth
async def buscar_pandilla(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /buscar_pandilla - Busca información de una pandilla"""
    if not context.args:
        await update.message.reply_text(
            "❌ Uso incorrecto. Formato: /buscar_pandilla <nombre>"
        )
        return
    
    nombre = " ".join(context.args)
    user_id = update.effective_user.id
    session = user_sessions[user_id]
    
    try:
        import aiohttp
        async with aiohttp.ClientSession() as http_session:
            async with http_session.get(
                f"{SUPABASE_FUNCTION_URL}/gangs/search?name={nombre}",
                headers={"Authorization": f"Bearer {session['token']}"}
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    
                    if not data.get("gangs"):
                        await update.message.reply_text(
                            f"❌ No se encontró ninguna pandilla con el nombre '{nombre}'"
                        )
                        return
                    
                    gang = data["gangs"][0]
                    
                    # Mapeo de peligrosidad a emojis
                    danger_emoji = {
                        "alta": "🔴",
                        "media": "🟡",
                        "baja": "🟢"
                    }
                    
                    gang_text = f"""
🔍 *Información de Pandilla*

📛 *Nombre:* {gang['name']}
👤 *Líder:* {gang.get('leader', 'N/A')}
{danger_emoji.get(gang['dangerLevel'], '⚪')} *Peligrosidad:* {gang['dangerLevel'].capitalize()}
👥 *Integrantes aprox.:* {gang.get('memberCount', 'N/A')}
📍 *Zona:* {gang.get('meetingPlace', {}).get('colonia', 'N/A')}

💬 *Descripción:*
{gang.get('description', 'Sin descripción')}

⚠️ *Delitos principales:*
{', '.join(gang.get('crimes', [])) if gang.get('crimes') else 'No especificados'}
                    """
                    
                    await update.message.reply_text(gang_text, parse_mode="Markdown")
                else:
                    await update.message.reply_text("❌ Error al buscar pandilla")
    
    except Exception as e:
        logger.error(f"Error en buscar_pandilla: {e}")
        await update.message.reply_text("❌ Error al conectar con el servidor")


@require_auth
async def buscar_integrante(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /buscar_integrante - Busca información de un integrante"""
    if not context.args:
        await update.message.reply_text(
            "❌ Uso incorrecto. Formato: /buscar_integrante <nombre>"
        )
        return
    
    nombre = " ".join(context.args)
    user_id = update.effective_user.id
    session = user_sessions[user_id]
    
    try:
        import aiohttp
        async with aiohttp.ClientSession() as http_session:
            async with http_session.get(
                f"{SUPABASE_FUNCTION_URL}/members/search?name={nombre}",
                headers={"Authorization": f"Bearer {session['token']}"}
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    
                    if not data.get("members"):
                        await update.message.reply_text(
                            f"❌ No se encontró ningún integrante con el nombre '{nombre}'"
                        )
                        return
                    
                    member = data["members"][0]
                    
                    member_text = f"""
🔍 *Información de Integrante*

👤 *Nombre:* {member.get('firstName', '')} {member.get('lastName', '')}
🎭 *Alias:* {member.get('alias', 'N/A')}
🎂 *Edad:* {member.get('age', 'N/A')}
⚧ *Género:* {member.get('gender', 'N/A')}
🎯 *Pandilla:* {member.get('gangName', 'N/A')}
📞 *Teléfono:* {member.get('phone', 'N/A')}

⚠️ *Nota:* Por privacidad, algunos datos están restringidos
                    """
                    
                    await update.message.reply_text(member_text, parse_mode="Markdown")
                else:
                    await update.message.reply_text("❌ Error al buscar integrante")
    
    except Exception as e:
        logger.error(f"Error en buscar_integrante: {e}")
        await update.message.reply_text("❌ Error al conectar con el servidor")


@require_auth
async def incidentes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /incidentes - Muestra incidentes recientes"""
    user_id = update.effective_user.id
    session = user_sessions[user_id]
    
    try:
        import aiohttp
        async with aiohttp.ClientSession() as http_session:
            async with http_session.get(
                f"{SUPABASE_FUNCTION_URL}/incidents/recent",
                headers={"Authorization": f"Bearer {session['token']}"}
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    incidents_list = data.get("incidents", [])
                    
                    if not incidents_list:
                        await update.message.reply_text(
                            "ℹ️ No hay incidentes registrados en los últimos 7 días"
                        )
                        return
                    
                    incidents_text = "📋 *Incidentes Recientes (últimos 7 días)*\n\n"
                    
                    for i, incident in enumerate(incidents_list[:5], 1):
                        incidents_text += f"""
*{i}. {incident.get('date', 'N/A')} - {incident.get('time', 'N/A')}*
   Pandilla: {incident.get('gangName', 'N/A')}
   Evento: {incident.get('event', 'N/A')}
   
"""
                    
                    if len(incidents_list) > 5:
                        incidents_text += f"\n_... y {len(incidents_list) - 5} incidentes más_"
                    
                    await update.message.reply_text(incidents_text, parse_mode="Markdown")
                else:
                    await update.message.reply_text("❌ Error al obtener incidentes")
    
    except Exception as e:
        logger.error(f"Error en incidentes: {e}")
        await update.message.reply_text("❌ Error al conectar con el servidor")


# === MAIN ===

def main():
    """Función principal del bot"""
    # Crear aplicación
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    
    # Comandos básicos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    
    # Autenticación
    application.add_handler(CommandHandler("login", login))
    application.add_handler(CommandHandler("logout", logout))
    
    # Comandos públicos
    application.add_handler(CommandHandler("estadisticas", estadisticas))
    application.add_handler(CommandHandler("zonas", zonas))
    
    # Comandos autenticados
    application.add_handler(CommandHandler("buscar_pandilla", buscar_pandilla))
    application.add_handler(CommandHandler("buscar_integrante", buscar_integrante))
    application.add_handler(CommandHandler("incidentes", incidentes))
    
    # Iniciar bot
    logger.info("Bot iniciado correctamente...")
    application.run_polling()


if __name__ == "__main__":
    main()