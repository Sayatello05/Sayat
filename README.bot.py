# Sayatimport logging
from telegram.ext import Updater, CommandHandler

TOKEN = "ВСТАВЬ_СЮДА_СВОЙ_ТОКЕН"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def start(update, context):
    update.message.reply_text("✅ Бот активирован!")

def ping(update, context):
    update.message.reply_text("✅ Online")

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("ping", ping))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
