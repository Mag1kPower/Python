
import telebot
from telebot import types
import requests


bot = telebot.TeleBot('6971427533:AAERXsqI1HdTU0m0HgB8EVnEJTyAxEIA_po')
owner_id = "-4100559442"



@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Привет бот!")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Ничего не бойся, я помогу тебе во всем разобраться и все подскажу!", reply_markup=markup)



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.copy_message(chat_id="-4100559442", from_chat_id=message.chat.id, message_id=message.id)
    if message.text == '👋 Привет бот!':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('да')
        btn2 = types.KeyboardButton('нет')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, '❓ Как на счет отдохнуть от работы и сходить на свидание?', reply_markup=markup)
    if message.text == 'да':
        bot.send_message(message.from_user.id, "Отличный выбор! Я горжусь тобой!", parse_mode="html")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Суббота')
        btn2 = types.KeyboardButton('Воскресенье')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, 'Какой день выберем?', reply_markup=markup)
    if message.text == 'Суббота':
        bot.send_message(message.from_user.id, "Великолепно! За тобой приедет этот Тигр \U0001F61C", parse_mode="html")
        photo = open("photo.jpg", "rb")
        bot.send_photo(message.chat.id, photo)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # создание новых кнопок
        btn1 = types.KeyboardButton('Отменить все это безобразие!')
        markup.add(btn1)
        bot.send_message(message.from_user.id, 'Он безупречен, не правда ли??',reply_markup=markup)
    if message.text == 'Воскресенье':
        bot.send_message(message.from_user.id, "Детка, соберись! Давай еще разок!", parse_mode="html")
    if message.text == 'нет':
        bot.send_message(message.from_user.id, "Подумай еще раз! Это важный выбор!", parse_mode="html")
    if message.text == 'Отменить все это безобразие!':
        bot.send_message(message.from_user.id, "Такая ты наивная! \U0001F618", parse_mode="html")
        photo = open("photo1.jpg", "rb")
        bot.send_photo(message.chat.id, photo)
#@bot.message_handler(content_types=['text'])# Тут ловим все текстовые сообщения от пользователя
#def some_funtion(message): #Название функции неважно Код не нужен
    #bot.copy_message(chat_id="-4100559442", from_chat_id=message.chat.id, message_id=message.id)


bot.polling(none_stop=True, interval=0)