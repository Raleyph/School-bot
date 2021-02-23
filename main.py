import telebot

from telebot import types

bot = telebot.TeleBot('1506257040:AAH5DunpqOf38JPrsIv2MFwpfjVlSafhwnI')


@bot.message_handler(commands=['start'])
def send_welcome(message):

    kbrd = types.ReplyKeyboardMarkup(resize_keyboard=True)
    lang = types.KeyboardButton("Мова")
    info = types.KeyboardButton("Інформація")
    food = types.KeyboardButton("Їдальня")
    lost = types.KeyboardButton("Відсутні")
    covid = types.KeyboardButton("Стоп COVID-19")

    kbrd.add(food, lost, lang, covid, info)

    lg = types.InlineKeyboardMarkup(row_width=3)
    ua = types.InlineKeyboardButton('🇺🇦')
    ru = types.InlineKeyboardButton('🇷🇺')
    en = types.InlineKeyboardButton('🇬🇧')

    lg.add(ua, ru, en)

    bot.reply_to(message, f'Привіт, це бот Краматорського закладу середньої освіти №22 з профільним навчанням ім. М.М.Крупченка \n' +
                          f'\n' +
                          f'Виберіть мову користування:\n', reply_markup=kbrd)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привіт!👋🏻')
    elif message.text.lower() == 'інформація':
        bot.send_message(message.from_user.id, 'ℹ️Телеграм бот КЗЗСО №22 з профільним навчанням ім. М.М.Крупченка. \n' +
                                               '\n' +
                                               '📥Увесь вихідний код на GitHub: \n' +
                                               'https://github.com/Raleyph/school_bot \n' +
                                               '\n' +
                                               'ℹ️Версія: 0.0.1 Pre-Alpha \n' +
                                               '\n' +
                                               '❗️Просимо вибачення за відсутність можливості вибору ім\'я учня під час сдачі відсутніх, адже ми піклуємося про персональні дані та конфіденціальність!')
    elif message.text.lower() == 'відсутні':

        lost_pupils = types.InlineKeyboardMarkup(row_width=3)
        # первые классы
        c1_a = types.InlineKeyboardButton("1-А", callback_data='1a')
        c1_b = types.InlineKeyboardButton("1-Б", callback_data='1b')
        c1_v = types.InlineKeyboardButton("1-В", callback_data='1v')
        # вторые классы
        c2_a = types.InlineKeyboardButton("2-А", callback_data='2a')
        c2_b = types.InlineKeyboardButton("2-Б", callback_data='2b')
        c2_v = types.InlineKeyboardButton("2-В", callback_data='2v')
        # третие классы
        c3_a = types.InlineKeyboardButton("3-А", callback_data='3a')
        c3_b = types.InlineKeyboardButton("3-Б", callback_data='3b')
        c3_v = types.InlineKeyboardButton("3-В", callback_data='3v')
        # четвертые классы
        c4_a = types.InlineKeyboardButton("4-А", callback_data='4a')
        c4_b = types.InlineKeyboardButton("4-Б", callback_data='4b')
        c4_v = types.InlineKeyboardButton("4-В", callback_data='4v')
        # пятые классы
        c5_a = types.InlineKeyboardButton("5-А", callback_data='5a')
        c5_b = types.InlineKeyboardButton("5-Б", callback_data='5b')
        c5_v = types.InlineKeyboardButton("5-В", callback_data='5v')
        # шестые классы
        c6_a = types.InlineKeyboardButton("6-А", callback_data='6a')
        c6_b = types.InlineKeyboardButton("6-Б", callback_data='6b')
        c6_v = types.InlineKeyboardButton("6-В", callback_data='6v')
        # седьмые классы
        c7_a = types.InlineKeyboardButton("7-А", callback_data='7a')
        c7_b = types.InlineKeyboardButton("7-Б", callback_data='7b')
        c7_v = types.InlineKeyboardButton("7-В", callback_data='7v')
        # восьмые классы
        c8_a = types.InlineKeyboardButton("8-А", callback_data='8a')
        c8_b = types.InlineKeyboardButton("8-Б", callback_data='8b')
        c8_v = types.InlineKeyboardButton("8-В", callback_data='8v')
        # девятые классы
        c9_a = types.InlineKeyboardButton("9-А", callback_data='9a')
        c9_b = types.InlineKeyboardButton("9-Б", callback_data='9b')
        c9_v = types.InlineKeyboardButton("9-В", callback_data='9v')
        # десятые классы
        c10_a = types.InlineKeyboardButton("10-А", callback_data='10a')
        c10_b = types.InlineKeyboardButton("10-Б", callback_data='10b')
        c10_v = types.InlineKeyboardButton("10-В", callback_data='10v')
        # одиннадцатые классы
        c11_a = types.InlineKeyboardButton("11-А", callback_data='11a')
        c11_b = types.InlineKeyboardButton("11-Б", callback_data='11b')
        c11_v = types.InlineKeyboardButton("11-В", callback_data='11v')

        lost_pupils.add(c1_a, c1_b, c1_v, c2_a, c2_b, c2_v, c3_a, c3_b, c3_v, c4_a, c4_b,
                        c4_v, c5_a, c5_b, c5_v, c6_a, c6_b, c6_v, c7_a, c7_b, c7_v, c8_a,
                        c8_b, c8_b, c9_a, c9_b, c9_v, c10_a, c10_b, c10_v, c11_a, c11_b, c11_v)

        bot.send_message(message.chat.id, 'Виберіть клас:', reply_markup=lost_pupils)
    else:
        bot.send_message(message.from_user.id, 'Я не знаю, що відповісти :(')


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    try:
        if call.message:
            if call.data == '1a':
                bot.send_message(call.message.chat.id, '1а')
            elif call.data == '1b':
                bot.send_message(call.message.chat.id, '1б')

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text="Введіть імена та прізвища без помилок через кому", reply_markup=None)

    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)
