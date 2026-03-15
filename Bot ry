Bot ryimport logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
import os

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Токен бота (из переменных окружения или запасной)
BOT_TOKEN = os.environ.get('BOT_TOKEN', "8790836425:AAEuHfvdz1z6mehn7ainA3zjcxBSvTipTJQ")
ADMIN_ID = 7005005023

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    # Создаем кнопки
    keyboard = [
        [InlineKeyboardButton("🛒 Каталог", callback_data="catalog")],
        [InlineKeyboardButton("🎁 Бесплатно", callback_data="free")],
        [InlineKeyboardButton("ℹ️ О боте", callback_data="about")]
    ]
    # Отправляем сообщение с кнопками
    await update.message.reply_text(
        f"👋 Привет, {user.first_name}!\nДобро пожаловать в VIRUSFF SHOP",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# Обработчик кнопки "Каталог"
async def catalog(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("🛒 Здесь будут платные настройки")

# Обработчик кнопки "Бесплатно"
async def free(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("🎁 Бесплатные настройки:\n\n• Обычные настройки")

# Обработчик кнопки "О боте"
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    text = """
ℹ️ VIRUSFF SHOP

🆓 Обычные - Бесплатно
🔰 Средние - 300₽
💎 Фулл - 600₽

✅ Оплата: СБП
✅ Мгновенная выдача
    """
    await query.edit_message_text(text)

# Запуск бота
def main():
    app = Application.builder().token(BOT_TOKEN).build()
    
    # Добавляем обработчики
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(catalog, pattern="catalog"))
    app.add_handler(CallbackQueryHandler(free, pattern="free"))
    app.add_handler(CallbackQueryHandler(about, pattern="about"))
    
    print("✅ Бот запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()
