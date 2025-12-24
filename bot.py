from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import os

TOKEN = os.getenv("BOT_TOKEN")

def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "🎬 Welcome to AI Video Bot!\nSend me any text prompt."
    )

def reply_text(update: Update, context: CallbackContext):
    text = update.message.text
    update.message.reply_text(f"✅ You sent:\n{text}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_text))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
    