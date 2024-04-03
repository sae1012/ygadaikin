import telebot
import random
from telebot import types



token = "TOKEN"
bot = telebot.TeleBot(token=token)
numbers = {}

'''
@bot.message_handler(commands=['remind'])
def remind(message):
    user_id = message.chat.id
    if user_id not in notes:
        bot.send_message(user_id, "Вы мне еще не писали.")
    else:
        bot.send_message(user_id, notes[user_id])

@bot.message_handler(content_types=['text'])
def remember(message):
    user_id = message.chat.id
    notes[user_id] = message.text
'''

@bot.message_handler(commands=['start'])
def priv(message):
    user_id = message.chat.id
    numbers[user_id] = random.randint(1, 10)
    bot.send_message(user_id, "Угадай число")


@bot.message_handler(content_types=['text'])
def compare(message):
    user_id = message.chat.id
    guess = int(message.text)
    if numbers[user_id] > guess:
        more = bot.send_message(user_id, "Больше!")
        bot.register_next_step_handler(more, compare)
    if numbers[user_id] < guess:
        less = bot.send_message(user_id, "Меньше!")
        bot.register_next_step_handler(less, compare)
    if numbers[user_id] == int(message.text):
        msg1 = bot.send_message(user_id, "Вам удалось отгадать число, это в самом деле, " + str(numbers[user_id]))
        keyboard = types.InlineKeyboardMarkup()
        button1 = types.InlineKeyboardButton(text="Да", callback_data="button1")
        button2 = types.InlineKeyboardButton(text="Нет", callback_data="button2")
        keyboard.add(button1, button2)
        bot.send_message(user_id,'Еще Раз?', reply_markup=keyboard)

 
@bot.callback_query_handler(func=lambda call: True)
def choice(call):
    if call.message:
        if call.data == "button1":
            chic = bot.send_message(call.message.chat.id, "Ура!")
            priv(call.message)
        if call.data == "button2":
            bot.send_message(call.message.chat.id, "=(")


bot.polling(none_stop=True)
