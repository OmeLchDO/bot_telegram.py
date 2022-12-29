import telebot
from telebot import types
from Config import tg_bot_token
from datetime import datetime, date

from API import buy_usd, sale_usd, buy_eur, sale_eur

bot = telebot.TeleBot(tg_bot_token)
current_datetime = datetime.now().date()


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Курсы валют')
    markup.add(item1)
    bot.send_message(message.chat.id, 'Привет, {0.full_name}!'.format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Курсы валют':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            bot.send_message(message.chat.id, 'Актуальные курсы на: ' + str(date.today()))

            back = types.KeyboardButton('Назад')
            markup.add(back)
            bot.send_message(message.chat.id, f"Доллар США:\n {buy_usd} / {sale_usd}\nЕвро:\n {buy_eur} / {sale_eur}", reply_markup=markup)

        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('Курсы валют')
            markup.add(item1)
            bot.send_message(message.chat.id, 'Назад', reply_markup=markup)


bot.polling(none_stop=True)
