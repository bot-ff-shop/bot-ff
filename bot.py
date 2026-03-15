import logging
import os

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Логи
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Токен из переменных Railway
BOT_TOKEN = os.environ.get("BOT_TOKEN")

ADMIN_ID = 7005005023


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    await update.message.reply_text(
        f"👋 Привет, {user.first_name}!\n\n"
        "Добро пожаловать в магазин Free Fire 🔥\n"
        "Используй команды:\n"
        "/shop — открыть магазин\n"
        "/help — помощь"
    )


async def shop(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = (
        "🛒 Магазин Free Fire\n\n"
        "💎 100 Diamonds — 1$\n"
        "💎 310 Diamonds — 3$\n"
        "💎 520 Diamonds — 5$\n\n"
        "Напишите админу для покупки."
    )

    await update.message.reply_text(text)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "ℹ️ Помощь\n\n"
        "/start — запуск бота\n"
        "/shop — магазин\n"
        "/help — помощь"
    )


def main():

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("shop", shop))
    app.add_handler(CommandHandler("help", help_command))

    print("✅ Бот запущен!")

    app.run_polling()


if __name__ == "__main__":
    main()
