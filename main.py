import telebot
import config
import sqlite3

from telebot import types

bot = telebot.TeleBot(config.TOKEN)
mode = 0
__connection = None
__data = None


def get_connection():
    global __connection

    if __connection is None:
        __connection = sqlite3.connect('database.db')
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
    c.execute('INSERT INTO user_message (user_id, user_name, user_surname, username) VALUES (?, ?, ?, ?)',
              (user_id, user_name, user_surname, username))
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
        print('Error!')
    else:
        set_args(user_id=us_id, user_name=us_name, user_surname=us_sname, username=user_name_tg)


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


bot.polling(none_stop=True)
