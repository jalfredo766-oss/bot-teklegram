from telethon import TelegramClient, events

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

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if event.out:
        return

    # 👇 mensaje limpio, sin responder al anterior
    await client.send_message(event.chat_id, MENSAJE)

client.start()
print("🔥 BOT FUNCIONANDO SIN RESPUESTA")
client.run_until_disconnected()