from telethon import TelegramClient, events
import time

api_id = 32933179
api_hash = "6c15743033e839a2582848930d581583"

client = TelegramClient('session', api_id, api_hash)

MENSAJE = """Hola bb ¿Deseas mi contenido?
Ahí te envío mis precios 🔥

💎PACK BÁSICO – S/15
🎥 3 videos 
📸 5 fotos 
━━━━━━━━━━━━━━
🚀 PACK PREMIUM – S/30 ⭐ (El más pedido)
🎥 7 videos 
📸 10 fotos 
━━━━━━━━━━━━━━
👑 PACK VIP – S/50
🎥 12 videos 
📸 40 fotos

Siempre cumplo 🔥
¿Cuál deseas amor?"""

# 👇 guardamos el último envío por usuario
usuarios = {}

TIEMPO_ESPERA = 86400  # 24 horas en segundos

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if event.out:
        return

    user_id = event.sender_id
    ahora = time.time()

    # 👇 si el usuario no existe o ya pasaron 24h
    if user_id not in usuarios or (ahora - usuarios[user_id]) > TIEMPO_ESPERA:
        await client.send_message(event.chat_id, MENSAJE)
        usuarios[user_id] = ahora
    else:
        # opcional: no hacer nada o ignorar
        pass

client.start()
print("🔥 BOT CON CONTROL DE 24H")
client.run_until_disconnected()