import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

BOT_TOKEN = os.environ.get('BOT_TOKEN', "8790836425:8790836425:AAEuHfvdz1z6mehn7ainA3zjcxBSvTipTJQ")
ADMIN_ID = 7005005023

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_text(f"👋 Привет, {user.first_name}!")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ Бот запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()
