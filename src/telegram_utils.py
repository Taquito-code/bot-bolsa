import os
import requests

def enviar_telegram(texto: str) -> bool:
    token = os.environ["TELEGRAM_TOKEN"]
    chat_id = os.environ["TELEGRAM_CHAT_ID"]
    r = requests.post(
        f"https://api.telegram.org/bot8877459710:AAEGDNiMVgtyhmP9FBxAso7WkXH_WKvm4TA/sendMessage",
        json={"chat_id": 1805813672, "text": texto},
        timeout=15,
    )
    if not r.ok:
        print("Error Telegram:", r.text)
    return r.ok