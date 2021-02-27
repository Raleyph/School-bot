import telebot
import config
import sqlite3

from telebot import types

bot = telebot.TeleBot(config.TOKEN)
__connection = None
__data = None
__mode = None


def get_connection():
    global __connection

    if __connection is None:
        __connection = sqlite3.connect('database.db', check_same_thread=False)
    return __connection


def init_db(force: bool = False):
    conn = get_connection()
    c = conn.cursor()

    if force:
        c.execute('DROP TABLE IF EXISTS user_message')

    c.execute("""
        CREATE TABLE IF NOT EXISTS user_message (
            id              INTEGER PRIMARY_KEY,
            user_id         INTEGER NOT NULL,
            user_name       TEXT NOT NULL,
            user_surname    TEXT NOT NULL,
            username        TEXT NOT NULL
              )
        """)

    conn.commit()


def set_args(user_id: int, user_name: str, user_surname: str, username: str):
    conn = get_connection()
    c = conn.cursor()
    c.execute('INSERT INTO user_message (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)', (user_id, user_name, user_surname, username))
    conn.commit()

    global __data
    if __data is None:
        __data = c.fetchone()
    return __data


def language_mode(message):
    lg = types.InlineKeyboardMarkup(row_width=3)
    lg.add(config.ua, config.ru, config.en)
    bot.send_message(message.from_user.id, 'Виберіть мову користування:', reply_markup=lg)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    kbrd = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kbrd.add(config.food, config.lost, config.day, config.covi, config.lang, config.info)
    bot.reply_to(message, config.hello_message, reply_markup=kbrd)
    language_mode(message)

    us_id = message.from_user.id
    us_name = message.from_user.first_name
    us_sname = message.from_user.last_name
    user_name_tg = message.from_user.username

    init_db()
    if __data is None:
        set_args(user_id=us_id, user_name=us_name, user_surname=us_sname, username=user_name_tg)
    else:
        print('Error! You already register in DB!')
        print(__data)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global __mode

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
        __mode = 1
        lost_pupils = types.InlineKeyboardMarkup(row_width=3)

        lost_pupils.add(config.c1_a, config.c1_b, config.c1_v, config.c2_a, config.c2_b, config.c2_v, config.c3_a, config.c3_b, config.c3_v, config.c4_a, config.c4_b,
                        config.c4_v, config.c5_a, config.c5_b, config.c5_v, config.c6_a, config.c6_b, config.c6_v, config.c7_a, config.c7_b, config.c7_v, config.c8_a,
                        config.c8_b, config.c8_v, config.c9_a, config.c9_b, config.c9_v, config.c10_a, config.c10_b, config.c10_v, config.c11_a, config.c11_b, config.c11_v)
        bot.send_message(message.chat.id, 'Виберіть клас:', reply_markup=lost_pupils)

        print(__mode)
    elif message.text.lower() == 'covid-19':
        # вывод статистики коронавируса
        bot.send_message(message.from_user.id, config.covid_message, parse_mode='html')
    elif message.text.lower() == 'їдальня':
        __mode = 2
        food_sys = types.InlineKeyboardMarkup(row_width=3)

        food_sys.add(config.c1_a, config.c1_b, config.c1_v, config.c2_a, config.c2_b, config.c2_v, config.c3_a, config.c3_b, config.c3_v, config.c4_a, config.c4_b,
                     config.c4_v, config.c5_a, config.c5_b, config.c5_v, config.c6_a, config.c6_b, config.c6_v, config.c7_a, config.c7_b, config.c7_v, config.c8_a,
                     config.c8_b, config.c8_v, config.c9_a, config.c9_b, config.c9_v, config.c10_a, config.c10_b, config.c10_v, config.c11_a, config.c11_b, config.c11_v)
        bot.send_message(message.chat.id, 'Виберіть клас:', reply_markup=food_sys)

        print(__mode)
    elif message.text.lower() == 'розклад':
        __mode = 3
        day_time = types.InlineKeyboardMarkup(row_width=3)

        day_time.add(config.c1_a, config.c1_b, config.c1_v, config.c2_a, config.c2_b, config.c2_v, config.c3_a, config.c3_b, config.c3_v, config.c4_a, config.c4_b,
                     config.c4_v, config.c5_a, config.c5_b, config.c5_v, config.c6_a, config.c6_b, config.c6_v, config.c7_a, config.c7_b, config.c7_v, config.c8_a,
                     config.c8_b, config.c8_v, config.c9_a, config.c9_b, config.c9_v, config.c10_a, config.c10_b, config.c10_v, config.c11_a, config.c11_b, config.c11_v, config.alarm_timeing)
        bot.send_message(message.chat.id, 'Виберіть клас:', reply_markup=day_time)

        print(__mode)
    else:
        bot.send_message(message.from_user.id, 'Я не знаю, що відповісти :(')


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    try:
        if call.message:
            if __mode == 1:
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
                else:
                    bot.send_message(call.from_user.id, 'Помилка!')
            elif __mode == 2:
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
                else:
                    bot.send_message(call.from_user.id, 'Помилка!')
            elif __mode == 3:
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
                elif call.data == 'al-tm':
                    bot.send_message(call.message.chat.id, 'Розклад дзвінків:')
                else:
                    bot.send_message(call.from_user.id, 'Помилка!')
            else:
                bot.send_message(call.from_user.id, 'Помилка!')
    except Exception as e:
        print(repr(e))


bot.polling(none_stop=True)
