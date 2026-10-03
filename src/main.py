import sys
from telegram_utils import enviar_telegram

if __name__ == "__main__":
    ok = enviar_telegram("✅ Bot de bolsa conectado correctamente")
    print("Enviado:", ok)
    if not ok:
        sys.exit(1)