import telebot

from telebot import types

bot = telebot.TeleBot('')


@bot.message_handler(commands=['start'])
def send_welcome(message):

    kbrd = types.ReplyKeyboardMarkup(resize_keyboard=True)
    lang = types.KeyboardButton("Мова")
    info = types.KeyboardButton("Інформація")
    food = types.KeyboardButton("Їдальня")
    lost = types.KeyboardButton("Відсутні")

    kbrd.add(food, lost, lang, info)

    bot.reply_to(message, f'Привіт, це бот Краматорського закладу середньої освіти №22 з профільним навчанням ім. М.М.Крупченка', reply_markup=kbrd)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':

        markup = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Учень🧑🏼‍🎓", callback_data='pupil')
        item2 = types.InlineKeyboardButton("Викладач👩🏼‍🏫", callback_data='teacher')

        markup.add(item1, item2)

        bot.send_message(message.chat.id, 'Хто ти?', reply_markup=markup)
    elif message.text.lower() == 'інформація':
        bot.send_message(message.from_user.id, 'Телеграм бот КЗЗСО №22 з профільним навчанням ім. М.М.Крупченка. \n' +
                                               '\n' +
                                               'Увесь вихідний код на GitHub: \n' +
                                               'https://github.com/Raleyph/school_bot \n' +
                                               '\n' +
                                               'Версія: 0.0.1 Pre-Alpha')
    elif message.text.lower() == 'Відсутні':
    else:
        bot.send_message(message.from_user.id, 'Не розумію')


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    try:
        if call.message:
            if call.data == 'pupil':
                bot.send_message(call.message.chat.id, 'Ви учень!')
            elif call.data == 'teacher':
                bot.send_message(call.message.chat.id, 'Ви викладач!')

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Хто ти?", reply_markup=None)

    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)
