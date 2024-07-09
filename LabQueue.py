import telebot
from telebot import types

bot = telebot.TeleBot("6396123776:AAFKb5Fji0SW_uYCzzsg2pLO46w73MRlZzU")

@bot.message_handler(commands = ["start"])
def start(m, res = False):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton("Lab 4")
    item2 = types.KeyboardButton("Lab 5")
    markup.add(item1, item2)
    bot.send_message(m.chat.id, "Choose what you want to do", reply_markup = markup)

@bot.message_handler(content_types = ["text"])
def handle_text(message):
    if (message.text.strip() == "Lab 4"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = types.KeyboardButton("Записаться в очередь на Lab 4")
        item2 = types.KeyboardButton("Посмотреть очередь на Lab 4")
        item3 = types.KeyboardButton("Вернуться в главное меню")
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, "Choose action", reply_markup = markup)
    elif (message.text.strip() == "Lab 5"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = types.KeyboardButton("Записаться в очередь на Lab 5")
        item2 = types.KeyboardButton("Посмотреть очередь на Lab 5")
        item3 = types.KeyboardButton("Вернуться в главное меню")
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, "Choose action", reply_markup = markup)
    elif (message.text.strip() == "Записаться в очередь на Lab 4"):
        f3 = open("Lab4.txt", "r+", encoding = "UTF-8")
        lab4 = f3.read().split("\n")
        for name in lab4:
            if name == message.from_user.first_name:
                bot.send_message(message.chat.id, "You have already stayed in queue")
                break
            else:
                f3.seek(0, 2)
                f3.write(message.from_user.first_name + "\n")
                f = open("Lab4Queue.txt", "r+", encoding = "UTF-8")
                f2 = open("CurrentQueueLab4.txt", "r+", encoding = "UTF-8")
                number = f2.read()
                f.seek(0, 2)
                f.write(number + '. ' + message.from_user.first_name + "\n")
                number = int(number) + 1
                f2.seek(0)
                f2.write(str(number))
                f.close
                f2.close
        f3.close
    elif (message.text.strip() == "Посмотреть очередь на Lab 4"):
        f = open("Lab4Queue.txt", 'r', encoding = "UTF-8")
        lab4 = f.read()
        f.close
        bot.send_message(message.chat.id, lab4)
    elif (message.text.strip() == "Записаться в очередь на Lab 5"):
        f3 = open("Lab5.txt", "r+", encoding = "UTF-8")
        lab4 = f3.read().split("\n")
        for name in lab4:
            if name == message.from_user.first_name:
                bot.send_message(message.chat.id, "You have already stayed in queue")
                break
            else:
                f3.seek(0, 2)
                f3.write(message.from_user.first_name + "\n")
                f = open("Lab5Queue.txt", "r+", encoding = "UTF-8")
                f2 = open("CurrentQueueLab5.txt", "r+", encoding = "UTF-8")
                number = f2.read()
                f.seek(0, 2)
                f.write(number + '. ' + message.from_user.first_name + "\n")
                number = int(number) + 1
                f2.seek(0)
                f2.write(str(number))
                f.close
                f2.close
        f3.close
    elif (message.text.strip() == "Посмотреть очередь на Lab 5"):
        f = open("Lab5Queue.txt", 'r', encoding = "UTF-8")
        lab5 = f.read()
        f.close
        bot.send_message(message.chat.id, lab5)
    elif (message.text.strip() == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        item1 = types.KeyboardButton("Lab 4")
        item2 = types.KeyboardButton("Lab 5")
        markup.add(item1, item2)
        bot.send_message(message.chat.id, "Choose what you want to do", reply_markup = markup)
    else:
        bot.send_message(message.chat.id, "There is no such action")

bot.polling(none_stop = True, interval = 0)
