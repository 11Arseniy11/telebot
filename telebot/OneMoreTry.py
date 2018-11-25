# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 11:09:30 2018

@author: Арсений
"""

import telebot
from telebot import apihelper
token = ''
bot = telebot.TeleBot(token)

apihelper.proxy = {'http':'http://12.65.38.80:443'}

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Мир тебе, входящему! Я мини-бот. Цель моего существования пока не определена. С помощью нейросетей я могу оценивать ваши картинки. Просто загрузите картинку. А если вы напишите /go, то я спрошу, сколько вам лет! Здорово)")

@bot.message_handler(content_types=['photo'])
def text_handler(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Красиво!')

@bot.message_handler(commands=['go'])
def start_handler(message):
    global isRunning
    if not isRunning:
        chat_id = message.chat.id
        msg = bot.send_message(chat_id, 'Сколько вам лет?')
        bot.register_next_step_handler(msg, askAge) #askSource
        isRunning = True

def askAge(message):
    chat_id = message.chat.id
    text = message.text
    if not text.isdigit():
        msg = bot.send_message(chat_id, 'Возраст должен быть числом, введите ещё раз.')
        bot.register_next_step_handler(msg, askAge) #askSource
        return
    msg = bot.send_message(chat_id, 'Спасибо, я запомнил что вам ' + text + ' лет. Зачем мне это? Я и сам не знаю')
    isRunning = False

bot.polling(none_stop=True, interval=0)
     


#@bot.message_handler(content_types=["text"])
#def handle_text(message):
 #   if message.text == "Hi":
  #      bot.send_message(message.from_user.id, "Hello!")
    
   # elif message.text == "How are you?" or message.text == "How are u?":
      #  bot.send_message(message.from_user.id, "I'm fine, thanks. And you?")
    
    #else:
     #   bot.send_message(message.from_user.id, "Привет, Вика! Очень рад тебя видеть! Как тебе этот бот?) Теперь можем писать все, что угодно!")