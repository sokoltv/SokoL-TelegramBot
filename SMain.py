"""
This software is completely open source and is distributed under the GNU GPLv3 license as is.

Copyright 2017-2018, sokoltv
"""
import telebot
import SStrings

# Втыкаем бота, втыкаем значение в отдельный файл и выцыганиваем их.
bot = telebot.TeleBot(SStrings.SToken)

# Оно получает обновы
upd = bot.get_updates()

# А оно забират последнее
last_upd = upd[-1]

# А вот оно уже выводит это последнее в консоль
message_from_user = last_upd
print(last_upd)


print(bot.get_me)

def log(messange, answer):
    print("\n ~~~~~")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от [0] [1]. (id = [2]) \n Текст - [3]".format(messange.from_user.first_name,
                                                                   messange.from_user.last_name,
                                                                   str(messange.from_user.id), messange.text))
    print(answer)


# Тут что-то пошло не так
"""
Не работает

@bot.message_handler(content_types=["start"])
def handle_command(messange):
    print("Пришла команда")
    bot.send_message(messange.chat.id, SStrings.SAnswerHZ)
"""

# Блок определения
@bot.message_handler(content_types=["text"])
def handle_command(messange):
    print("Пришло ПТС")
    if messange.text == "Привет" or messange.text == "Привет!" or messange.text == "Здаров" \
            or messange.text == "Здарово" or messange.text == "Здравствуй" or messange.text == "Здравствуйте" \
            or messange.text == "Привки" or messange.text == "Приветики" or messange.text == "Привифки" \
            or messange.text == "привет":
        answer = SStrings.SAnswerPriv
        bot.send_message(messange.chat.id, SStrings.SAnswerPriv)
        log(messange, answer)
    elif messange.text == "/start":
        answer = SStrings.SAnswerHZ
        bot.send_message(messange.chat.id, SStrings.SAnswerHZ)
        log(messange, answer)
    elif messange.text == "/end":
        answer = SStrings.SAnswerHZ
        bot.send_message(messange.chat.id, SStrings.SAnswerHZ)
        log(messange, answer)
    elif messange.text == "/setting":
        answer = SStrings.SAnswerHZ
        bot.send_message(messange.chat.id, SStrings.SAnswerHZ)
        log(messange, answer)
    elif messange.text == "/help":
        answer = SStrings.SAnswerHZ
        bot.send_message(messange.chat.id, SStrings.SAnswerHZ)
        log(messange, answer)
    elif messange.text == "/acrtion":     # Очепятка
        answer = SStrings.SAnswerHZ
        bot.send_message(messange.chat.id, SStrings.SAnswerHZ)
        log(messange, answer)
    else:
        answer = SStrings.SAnswerErr
        bot.send_message(messange.chat.id, SStrings.SAnswerErr)
        log(messange, answer)

@bot.message_handler(content_types=["document"])
def handle_command(messange):
    print("Пришли Доки")
    answer = SStrings.SAnswerDoc
    bot.send_message(messange.chat.id, SStrings.SAnswerDoc)
    log(messange, answer)


@bot.message_handler(content_types=["audio"])
def handle_command(messange):
    print("Пришло МиАС")
    answer = SStrings.SAnswerHZ
    bot.send_message(messange.chat.id, SStrings.SAnswerHZ)
    log(messange, answer)

@bot.message_handler(content_types=["photo"])
def handle_command(messange):
    print("Пришло ЗВИИ")
    answer = SStrings.SAnswerHZ
    bot.send_message(messange.chat.id, SStrings.SAnswerHZ)
    log(messange, answer)

@bot.message_handler(content_types=["sticker"])
def handle_command(messange):
    print("Пришло ЗВБИ")
    answer = SStrings.SAnswerHZ2
    bot.send_message(messange.chat.id, SStrings.SAnswerHZ2)
    log(messange, answer)


bot.polling(none_stop=True, interval=0)

