import telebot
from config import telegram_token
from currency_converter import CurrencyConverter
from telebot import types

bot = telebot.TeleBot(telegram_token)
currency = CurrencyConverter()
amount = 0


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Salam, meblegi daxil edin')
    bot.register_next_step_handler(message, summa)


def summa(message):
    global amount
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Yalnish formatda mebleg daxil edilmisdir.')
        bot.register_next_step_handler(message, summa)
        return

    if amount > 0:
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
        btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
        btn3 = types.InlineKeyboardButton('USD/GBP', callback_data='usd/gbp')
        btn4 = types.InlineKeyboardButton('Diger deyer', callback_data='else')
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, 'Bir valyuta cutu secin', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Daxil edilen eded 0 dan boyuk olmalidir')
        bot.register_next_step_handler(message, summa)


@bot.callback_query_handlers(func=lambda call: True)
def callback(call):
    values = call.data.upper().split('/')
    res = currency.convert(amount)



bot.polling(none_stop=True)
