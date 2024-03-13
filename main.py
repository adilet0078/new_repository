
# import telebot
# from telebot import types
# import random


# token = '6515198023:AAEjjgVNI2LZSi_qPwR6aTdjaQ5dxyXL9vg'

# bot = telebot.TeleBot(token)
# Keyboard = types.ReplyKeyboardMarkup()
# btn1 = types.KeyboardButton('играть!')
# btn2 = types.KeyboardButton('Нет, я Пас!')
# Keyboard.add(btn1, btn2)



# @bot.message_handler(commands=['start','game'])
# def start_message(message):
#     bot_message = bot.send_message(message.chat.id, 'Привет Чемпион, начнем игру?',reply_markup=Keyboard)
#     bot.register_next_step_handler(bot_message, check_answer)


# def check_answer(message):
#     if message.text == 'играть!':
#       bot.send_message(message.chat.id, 'Ok, тогда лови правила игры:\nНужно угадать число, которое я загадаю в диапазоне от 1 до 10 вкючительно! У тебя будет 3 попытки! Если не угадаешь я тебя повешу! :)')
#       number = random.randint(1, 10)
#       print(number)
#       game(message, 3, number)
#     elif message.text == 'Нет, я Пас!':
#       bot.send_message(message.chat.id, 'Ok, пока!')
#     else:
#       bot_message = bot.send_message(message.chat.id, 'Вы ввели неправильное значение!\n попробуйте еще раз!',reply_markup=Keyboard)
#       bot.register_next_step_handler(bot_message, check_answer)

# def game(message, attempts, number):
#     message_bot = bot.send_message(message.chat.id, 'Угадай число!')
#     bot.register_next_step_handler(message_bot, check_number, attempts-1, number)

# def check_number(message, attempts, number):
#     if message.text == str(number):
#       bot.send_message(message.chat.id, 'Ты угадал! Поздравляю!')
#     elif attempts == 0:
#       bot.send_message(message.chat.id, 'keep moving forward until you win!')
#     else:
#       bot.send_message(message.chat.id, 'Ты не угадал! Попробуй еще раз!')
#       game(message, attempts, number)


# bot.polling()




