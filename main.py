import os
import telebot

TOKEN = os.getenv("TELEGRAM_TOKEN")  # берем токен из переменных окружения
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Бот работает ✅")


@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, f"Ты написал: {message.text}")


if __name__ == "__main__":
    print("Бот запущен...")
    bot.polling(none_stop=True)
