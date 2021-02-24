import telebot
import config

from telebot import types

bot = telebot.TeleBot(config.TOKEN)
mode = 0


@bot.message_handler(commands=['start'])
def send_welcome(message):

    kbrd = types.ReplyKeyboardMarkup(resize_keyboard=True)

    kbrd.add(config.food, config.lost, config.day, config.covi, config.lang, config.info)

    bot.reply_to(message, f'Привіт, це бот Краматорського закладу середньої освіти №22 з профільним навчанням ім. М.М.Крупченка \n' +
                          f'\n' +
                          f'Виберіть мову користування:\n', reply_markup=kbrd)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привіт!👋🏻')
    elif message.text.lower() == 'інформація':
        bot.send_message(message.from_user.id, config.info_message, parse_mode='html', disable_web_page_preview=True)
    elif message.text.lower() == 'відсутні':
        mode == 1
        lost_pupils = types.InlineKeyboardMarkup(row_width=3)
        lost_pupils.add(config.c1_a, config.c1_b, config.c1_v, config.c2_a, config.c2_b, config.c2_v, config.c3_a, config.c3_b, config.c3_v, config.c4_a, config.c4_b,
                        config.c4_v, config.c5_a, config.c5_b, config.c5_v, config.c6_a, config.c6_b, config.c6_v, config.c7_a, config.c7_b, config.c7_v, config.c8_a,
                        config.c8_b, config.c8_b, config.c8_v, config.c9_a, config.c9_b, config.c9_v, config.c10_a, config.c10_b, config.c10_v, config.c11_a, config.c11_b, config.c11_v)
        bot.send_message(message.chat.id, 'Виберіть клас:', reply_markup=lost_pupils)
    elif message.text.lower() == 'covid-19':
        bot.send_message(message.from_user.id, config.final_message, parse_mode='html')
    elif message.text.lower() == 'мова':
        language = types.InlineKeyboardMarkup(row_width=3)
        language.add(config.ua, config.ru, config.en)
        bot.send_message(message.from_user.id, 'Виберіть мову користування:', reply_markup=language)
    elif message.text.lower() == 'їдальня':
        mode == 2
        food_sys = types.InlineKeyboardMarkup(row_width=3)
        food_sys.add(config.c1_a, config.c1_b, config.c1_v, config.c2_a, config.c2_b, config.c2_v, config.c3_a, config.c3_b, config.c3_v, config.c4_a, config.c4_b,
                     config.c4_v, config.c5_a, config.c5_b, config.c5_v, config.c6_a, config.c6_b, config.c6_v, config.c7_a, config.c7_b, config.c7_v, config.c8_a,
                     config.c8_b, config.c8_b, config.c8_v, config.c9_a, config.c9_b, config.c9_v, config.c10_a, config.c10_b, config.c10_v, config.c11_a, config.c11_b, config.c11_v)
        bot.send_message(message.chat.id, 'Виберіть клас:', reply_markup=food_sys)
    elif message.text.lower() == 'розклад':
        day_time = types.InlineKeyboardMarkup(row_width=3)

        day_time.add(config.c1_a, config.c1_b, config.c1_v, config.c2_a, config.c2_b, config.c2_v, config.c3_a, config.c3_b, config.c3_v, config.c4_a, config.c4_b,
                     config.c4_v, config.c5_a, config.c5_b, config.c5_v, config.c6_a, config.c6_b, config.c6_v, config.c7_a, config.c7_b, config.c7_v, config.c8_a,
                     config.c8_b, config.c8_b, config.c8_v, config.c9_a, config.c9_b, config.c9_v, config.c10_a, config.c10_b, config.c10_v, config.c11_a, config.c11_b, config.c11_v, config.alarm_timeing)

        bot.send_message(message.chat.id, 'Виберіть клас:', reply_markup=day_time)
    else:
        bot.send_message(message.from_user.id, 'Я не знаю, що відповісти :(')
        mode == 0


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
