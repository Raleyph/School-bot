import telebot
import config
import sqlite3

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

mode = None           # режим
lang = 'ua'             # язык

# подключение к БД и установка курсора
conn = sqlite3.connect('database.db', check_same_thread=False)
cursor = conn.cursor()


# установка значений и настройка таблицы
def db_values(user_id: int, user_name: str, user_surname: str, username: str, language: str):
    cursor.execute('INSERT INTO user_message (user_id, user_name, user_surname, username, language) VALUES (?, ?, ?, ?, ?)', (user_id, user_name, user_surname, username, language))
    conn.commit()


# выбор языка
def language_mode(message):
    lg = types.InlineKeyboardMarkup(row_width=3)
    lg.add(config.ua, config.ru, config.en)
    bot.send_message(message.from_user.id, 'Виберіть мову користування:', reply_markup=lg)


# основная клавиатура
def main_keyboard(message):
    kbrd = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kbrd.add(config.food, config.lost, config.day, config.covi, config.lang, config.info)
    bot.reply_to(message, config.hello_message, reply_markup=kbrd)


# приветствие
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # клавиатура
    main_keyboard(message)

    # ввод данных пользователя
    us_id = message.from_user.id
    us_name = message.from_user.first_name
    us_sname = message.from_user.last_name
    username = message.from_user.username
    language = 'ua'

    # записть в таблицу
    db_values(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username, language=language)


# овтеты на сообщения
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
        lost_pupils = types.InlineKeyboardMarkup(row_width=3)

        lost_pupils.add(config.c1_a, config.c1_b, config.c1_v, config.c2_a, config.c2_b, config.c2_v, config.c3_a, config.c3_b, config.c3_v, config.c4_a, config.c4_b,
                        config.c4_v, config.c5_a, config.c5_b, config.c5_v, config.c6_a, config.c6_b, config.c6_v, config.c7_a, config.c7_b, config.c7_v, config.c8_a,
                        config.c8_b, config.c8_v, config.c9_a, config.c9_b, config.c9_v, config.c10_a, config.c10_b, config.c10_v, config.c11_a, config.c11_b, config.c11_v)
        bot.send_message(message.chat.id, 'Виберіть клас:', reply_markup=lost_pupils)
    elif message.text.lower() == 'covid-19':
        # вывод статистики коронавируса
        bot.send_message(message.from_user.id, config.covid_message, parse_mode='html')
    elif message.text.lower() == 'їдальня':
        food_sys = types.InlineKeyboardMarkup(row_width=3)

        food_sys.add(config.c1_a, config.c1_b, config.c1_v, config.c2_a, config.c2_b, config.c2_v, config.c3_a, config.c3_b, config.c3_v, config.c4_a, config.c4_b,
                     config.c4_v, config.c5_a, config.c5_b, config.c5_v, config.c6_a, config.c6_b, config.c6_v, config.c7_a, config.c7_b, config.c7_v, config.c8_a,
                     config.c8_b, config.c8_v, config.c9_a, config.c9_b, config.c9_v, config.c10_a, config.c10_b, config.c10_v, config.c11_a, config.c11_b, config.c11_v)
        bot.send_message(message.chat.id, 'Виберіть клас:', reply_markup=food_sys)
    elif message.text.lower() == 'розклад':
        day_time = types.InlineKeyboardMarkup(row_width=3)

        day_time.add(config.c1_a, config.c1_b, config.c1_v, config.c2_a, config.c2_b, config.c2_v, config.c3_a, config.c3_b, config.c3_v, config.c4_a, config.c4_b,
                     config.c4_v, config.c5_a, config.c5_b, config.c5_v, config.c6_a, config.c6_b, config.c6_v, config.c7_a, config.c7_b, config.c7_v, config.c8_a,
                     config.c8_b, config.c8_v, config.c9_a, config.c9_b, config.c9_v, config.c10_a, config.c10_b, config.c10_v, config.c11_a, config.c11_b, config.c11_v, config.alarm_timeing)
        bot.send_message(message.chat.id, 'Виберіть клас:', reply_markup=day_time)
    else:
        bot.send_message(message.from_user.id, 'Я не знаю, що відповісти :(')


# коллбэки для инлайн-клавиатуры
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    global lang
    try:
        if call.message:
            if call.data == '1a':
                bot.send_message(call.message.chat.id, 'Ви вибрали 1-А')
            elif call.data == '1b':
                bot.send_message(call.message.chat.id, 'Ви вибрали 1-Б')
            elif call.data == '1v':
                bot.send_message(call.message.chat.id, 'Ви вибрали 1-В')
            elif call.data == '2a':
                bot.send_message(call.message.chat.id, 'Ви вибрали 2-А')
            elif call.data == '2b':
                bot.send_message(call.message.chat.id, 'Ви вибрали 2-Б')
            elif call.data == '2v':
                bot.send_message(call.message.chat.id, 'Ви вибрали 2-В')
            elif call.data == '3a':
                bot.send_message(call.message.chat.id, 'Ви вибрали 3-А')
            elif call.data == '3b':
                bot.send_message(call.message.chat.id, 'Ви вибрали 3-Б')
            elif call.data == '3v':
                bot.send_message(call.message.chat.id, 'Ви вибрали 3-В')
            elif call.data == '4a':
                bot.send_message(call.message.chat.id, 'Ви вибрали 4-А')
            elif call.data == '4b':
                bot.send_message(call.message.chat.id, 'Ви вибрали 4-Б')
            elif call.data == '4v':
                bot.send_message(call.message.chat.id, 'Ви вибрали 4-В')
            elif call.data == '5a':
                bot.send_message(call.message.chat.id, 'Ви вибрали 5-А')
            elif call.data == '5b':
                bot.send_message(call.message.chat.id, 'Ви вибрали 5-Б')
            elif call.data == '5v':
                bot.send_message(call.message.chat.id, 'Ви вибрали 5-В')
            elif call.data == '6a':
                bot.send_message(call.message.chat.id, 'Ви вибрали 6-А')
            elif call.data == '6b':
                bot.send_message(call.message.chat.id, 'Ви вибрали 6-Б')
            elif call.data == '6v':
                bot.send_message(call.message.chat.id, 'Ви вибрали 7-В')
            elif call.data == '7a':
                bot.send_message(call.message.chat.id, 'Ви вибрали 8-А')
            elif call.data == '8b':
                bot.send_message(call.message.chat.id, 'Ви вибрали 8-Б')
            elif call.data == '8v':
                bot.send_message(call.message.chat.id, 'Ви вибрали 8-В')
            elif call.data == '9a':
                bot.send_message(call.message.chat.id, 'Ви вибрали 9-А')
            elif call.data == '9b':
                bot.send_message(call.message.chat.id, 'Ви вибрали 9-Б')
            elif call.data == '9v':
                bot.send_message(call.message.chat.id, 'Ви вибрали 9-В')
            elif call.data == '10a':
                bot.send_message(call.message.chat.id, 'Ви вибрали 10-А')
            elif call.data == '10b':
                bot.send_message(call.message.chat.id, 'Ви вибрали 10-Б')
            elif call.data == '10v':
                bot.send_message(call.message.chat.id, 'Ви вибрали 10-В')
            elif call.data == '11a':
                bot.send_message(call.message.chat.id, 'Ви вибрали 11-А')
            elif call.data == '11b':
                bot.send_message(call.message.chat.id, 'Ви вибрали 11-Б')
            elif call.data == '11v':
                bot.send_message(call.message.chat.id, 'Ви вибрали 11-В')
            elif call.data == 'ua_l':
                lang = 'ua'
                print(lang)
            elif call.data == 'ru_l':
                lang = 'ru'
                print(lang)
            elif call.data == 'en_l':
                lang = 'en'
                print(lang)
            else:
                bot.send_message(call.message.chat.id, 'Помилка!')

            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Виберіть клас:')
    except Exception as e:
        print(repr(e))


# постоянная работа бота
bot.polling(none_stop=True)
