import telebot
import os

# Убедитесь, что вы получаете токен из переменных окружения или замените его своим токеном
TOKEN = os.getenv('TELEGRAM_TOKEN', '7240803057:AAHg-vv5-OYhosfjdRwsIuF93D6wtPUAlBo')

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello!')

def main():
    bot.polling()

if __name__ == '__main__':
    main() 
