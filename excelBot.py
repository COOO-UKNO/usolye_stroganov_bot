import pandas as pd
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Чтение данных из Excel
def read_excel_data(file_path='data.xlsx'):
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"Ошибка при чтении Excel: {e}")
        return None

# Обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я бот для работы с Excel. Используй команду /getdata для получения данных."
    )

# Обработчик команды /getdata
async def get_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        df = read_excel_data()
        
        if df is None or df.empty:
            await update.message.reply_text("Файл Excel пуст или не найден.")
            return
        
        # Отправляем текстовые данные
        text_data = df.to_string(index=False)
        await update.message.reply_text(f"Данные из Excel:\n\n{text_data}")
        
        # Проверяем есть ли столбец с картинками
        if 'image_path' in df.columns:
            for _, row in df.iterrows():
                if pd.notna(row['image_path']) and os.path.exists(row['image_path']):
                    try:
                        with open(row['image_path'], 'rb') as photo:
                            await update.message.reply_photo(
                                photo, 
                                caption=f"Фото для {row.get('name', '')}"
                            )
                    except Exception as e:
                        print(f"Ошибка при отправке фото: {e}")
                        await update.message.reply_text(
                            f"Не удалось отправить фото: {row['image_path']}"
                        )
        
    except Exception as e:
        await update.message.reply_text(f"Произошла ошибка: {str(e)}")

# Основная функция
def main(token):
    # Токен вашего бота

    # Создаем Application
    application = Application.builder().token(token).build()
    
    # Регистрация обработчиков команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("getdata", get_data))
    
    # Запуск бота
    application.run_polling()

