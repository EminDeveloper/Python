import telebot
from config import telegram_token
from telebot import types

bot = telebot.TeleBot(telegram_token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("️Go to️")
    markup.row(btn1)
    btn2 = types.KeyboardButton("Delete photo")
    btn3 = types.KeyboardButton("Edit Text")
    markup.row(btn2, btn3)
    file = open('./photo.jpg', 'rb')
    # bot.send_photo(message.chat.id, file, reply_markup=markup)
    # bot.send_message(message.chat.id, 'Hi', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == "Go to️":
        bot.send_message(message.chat.id, "Website is open")
    elif message.text == "Delete photo":
        bot.send_message(message.chat.id, "Deleted")

@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Go to site', url='https://google.com')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Delete photo', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Edit Text', callback_data='edit')
    markup.row(btn2, btn3)
    bot.reply_to(message, 'Good Photo', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_query(callback):
    if callback.data == 'delete':
        bot.delete_messages(callback.message.chat.id, callback.message.message_id - 2)
    elif callback.data == 'edit':
        bot.edit_message_reply_markup(callback.message.chat.id, callback.message.message_id)


bot.polling(none_stop=True)
