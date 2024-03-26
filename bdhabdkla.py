import telebot
import random


token = "7043472916:AAE4VE3JPaLS46uSruhmleSRpguMjEK7E4k"
bot = telebot.TeleBot(token=token)
notes = {}

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
    global num_random
    user_id = message.chat.id
    msg = bot.send_message(user_id, "Угадай число")
    num_random = random.randint(1, 10)
    bot.register_next_step_handler(msg, compare)


@bot.message_handler(content_types=['text'])
def compare(message):
    user_id = message.chat.id
    notes[user_id] = message.text
    if num_random > int(message.text):
        more = bot.send_message(user_id, "Больше!")
        bot.register_next_step_handler(more, compare)
    elif num_random < int(message.text):
        less = bot.send_message(user_id, "Меньше!")
        bot.register_next_step_handler(less, compare)
    elif num_random == int(message.text):         
        msg1 = bot.send_message(user_id, "Вам удалось отгадать число,это в самом деле,", num_random)
        bot.register_next_step_handler(msg1, priv)


bot.polling(none_stop=True)