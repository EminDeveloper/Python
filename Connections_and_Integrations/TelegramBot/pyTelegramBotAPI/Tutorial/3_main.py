import telebot
from config import telegram_token
import requests
import json

bot = telebot.TeleBot(telegram_token)
API = '3d9de74844d28377e81415151cbe6a66'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Xosh gelmisiniz. Hansi seherin hava durumun isteyirsiniz?')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Indi hava: {temp}')
        image = 'sunny.png' if temp > 5.0 else 'sun.png'
        file = open('./' + image, 'rb')
        bot.send_photo(message.chat.id, file)
    else:
        bot.reply_to(message, f'Duzgun sheher adi girmediniz. Zehmet olmasa duzgun sheher adi giriniz.')


bot.polling(none_stop=True)