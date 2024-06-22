import telebot
from config import telegram_token

bot = telebot.TeleBot(telegram_token)


@bot.message_handler(commands=['start', 'main', 'hello'])
def start(message):
    bot.send_message(message.chat.id, f'Helloko, {message.chat.first_name} {message.chat.last_name}')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, '<b>Help</b> <em><u>information</u></em>', parse_mode="html")


bot.polling(none_stop=True)
