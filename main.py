import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.TOKEN)
mode = 0


@bot.message_handler(commands=['start'])
def send_welcome(message):

    kbrd = types.ReplyKeyboardMarkup(resize_keyboard=True)

    kbrd.add(config.food, config.lost, config.day, config.covi, config.lang, config.info)

    bot.reply_to(message, config.hello_message, reply_markup=kbrd)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привіт':
        # приветствие
        bot.send_message(message.from_user.id, 'Привіт!👋🏻')
    elif message.text.lower() == 'інформація':
        # вывод инфо
        bot.send_message(message.from_user.id, config.info_message, parse_mode='html', disable_web_page_preview=True)
    elif message.text.lower() == 'мова':
        language = types.InlineKeyboardMarkup(row_width=3)
        language.add(config.ua, config.ru, config.en)
        bot.send_message(message.from_user.id, 'Виберіть мову користування:', reply_markup=language)
    elif message.text.lower() == 'відсутні':
        mode = 1
        lost_pupils = types.InlineKeyboardMarkup(row_width=3)

        lost_pupils.add(config.c1_a, config.c1_b, config.c1_v, config.c2_a, config.c2_b, config.c2_v, config.c3_a, config.c3_b, config.c3_v, config.c4_a, config.c4_b,
                        config.c4_v, config.c5_a, config.c5_b, config.c5_v, config.c6_a, config.c6_b, config.c6_v, config.c7_a, config.c7_b, config.c7_v, config.c8_a,
                        config.c8_b, config.c8_v, config.c9_a, config.c9_b, config.c9_v, config.c10_a, config.c10_b, config.c10_v, config.c11_a, config.c11_b, config.c11_v)

        print(mode)
        bot.send_message(message.chat.id, 'Виберіть клас:', reply_markup=lost_pupils)
    # elif message.text.lower() == 'covid-19':
        # bot.send_message(message.from_user.id, config.final_message, parse_mode='html')
    elif message.text.lower() == 'їдальня':
        mode = 2
        food_sys = types.InlineKeyboardMarkup(row_width=3)

        food_sys.add(config.c1_a, config.c1_b, config.c1_v, config.c2_a, config.c2_b, config.c2_v, config.c3_a, config.c3_b, config.c3_v, config.c4_a, config.c4_b,
                     config.c4_v, config.c5_a, config.c5_b, config.c5_v, config.c6_a, config.c6_b, config.c6_v, config.c7_a, config.c7_b, config.c7_v, config.c8_a,
                     config.c8_b, config.c8_v, config.c9_a, config.c9_b, config.c9_v, config.c10_a, config.c10_b, config.c10_v, config.c11_a, config.c11_b, config.c11_v)

        print(mode)
        bot.send_message(message.chat.id, 'Виберіть клас:', reply_markup=food_sys)
    elif message.text.lower() == 'розклад':
        mode = 3
        day_time = types.InlineKeyboardMarkup(row_width=3)

        day_time.add(config.c1_a, config.c1_b, config.c1_v, config.c2_a, config.c2_b, config.c2_v, config.c3_a, config.c3_b, config.c3_v, config.c4_a, config.c4_b,
                     config.c4_v, config.c5_a, config.c5_b, config.c5_v, config.c6_a, config.c6_b, config.c6_v, config.c7_a, config.c7_b, config.c7_v, config.c8_a,
                     config.c8_b, config.c8_v, config.c9_a, config.c9_b, config.c9_v, config.c10_a, config.c10_b, config.c10_v, config.c11_a, config.c11_b, config.c11_v, config.alarm_timeing)

        print(mode)
        bot.send_message(message.chat.id, 'Виберіть клас:', reply_markup=day_time)
    else:
        bot.send_message(message.from_user.id, 'Я не знаю, що відповісти :(')


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    try:
        if call.message:
            if mode == 1:
                if call.data == '1a':
                    bot.send_message(call.message.chat.id, '1а')
                elif call.data == '1b':
                    bot.send_message(call.message.chat.id, '1б')
                elif call.data == '1v':
                    bot.send_message(call.message.chat.id, '1v')
                elif call.data == '2a':
                    bot.send_message(call.message.chat.id, '2a')
                elif call.data == '2b':
                    bot.send_message(call.message.chat.id, '2b')
                elif call.data == '2v':
                    bot.send_message(call.message.chat.id, '2v')
                elif call.data == '3a':
                    bot.send_message(call.message.chat.id, '3a')
                elif call.data == '3b':
                    bot.send_message(call.message.chat.id, '3b')
                elif call.data == '3v':
                    bot.send_message(call.message.chat.id, '3v')
                elif call.data == '4a':
                    bot.send_message(call.message.chat.id, '4a')
                elif call.data == '4b':
                    bot.send_message(call.message.chat.id, '4б')
                elif call.data == '4v':
                    bot.send_message(call.message.chat.id, '4v')
                elif call.data == '5a':
                    bot.send_message(call.message.chat.id, '5a')
                elif call.data == '5b':
                    bot.send_message(call.message.chat.id, '5b')
                elif call.data == '5v':
                    bot.send_message(call.message.chat.id, '5v')
                elif call.data == '6a':
                    bot.send_message(call.message.chat.id, '6a')
                elif call.data == '6b':
                    bot.send_message(call.message.chat.id, '6b')
                elif call.data == '6v':
                    bot.send_message(call.message.chat.id, '7v')
                elif call.data == '7a':
                    bot.send_message(call.message.chat.id, '8a')
                elif call.data == '8b':
                    bot.send_message(call.message.chat.id, '8b')
                elif call.data == '8v':
                    bot.send_message(call.message.chat.id, '8v')
                elif call.data == '9a':
                    bot.send_message(call.message.chat.id, '9a')
                elif call.data == '9b':
                    bot.send_message(call.message.chat.id, '9b')
                elif call.data == '9v':
                    bot.send_message(call.message.chat.id, '9v')
                elif call.data == '10a':
                    bot.send_message(call.message.chat.id, '10a')
                elif call.data == '10b':
                    bot.send_message(call.message.chat.id, '10б')
                elif call.data == '10v':
                    bot.send_message(call.message.chat.id, '10v')
                elif call.data == '11a':
                    bot.send_message(call.message.chat.id, '11a')
                elif call.data == '11b':
                    bot.send_message(call.message.chat.id, '11b')
                elif call.data == '11v':
                    bot.send_message(call.message.chat.id, '11v')
                else:
                    bot.send_message(call.from_user.id, 'Помилка!')
            bot.send_message(call.from_user.id, 'Помилка!')
    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)
