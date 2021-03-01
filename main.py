import telebot
import config
import sqlite3
import classes_list

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

mode = None           # режим
lang = 'ua'           # язык
class_set = None      # класс

eat_id = 1672178639

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


def lost(message):
    bot.send_message(message.from_user.id, 'Введіть імена учнів через кому:')


def eat(message):
    sent = bot.send_message(message.from_user.id, 'Введіть дані про заказ у форматі 2*25, 3*30')
    bot.register_next_step_handler(sent, save_link)


def save_link(message):
    global class_set

    mess = message.text
    bot.send_message(eat_id, 'Заказ від ' + class_set + ': ' + mess)
    bot.send_message(message.from_user.id, 'Заказ відправлено!')


def day_subjects(message):
    bot.send_message(message.from_user.id, 'Розклад на увесь тиждень:')


# овтеты на сообщения
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global mode
    global class_set

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
        bot.send_message(message.chat.id, 'Виберіть клас:')
    elif message.text.lower() == 'covid-19':
        # вывод статистики коронавируса
        bot.send_message(message.from_user.id, config.covid_message, parse_mode='html')
    elif message.text.lower() == 'їдальня':
        mode = 2
        bot.send_message(message.chat.id, 'Виберіть клас:')
    elif message.text.lower() == 'розклад':
        mode = 3
        bot.send_message(message.chat.id, 'Виберіть клас:')
    elif mode == 1:
        if message.text.lower() in classes_list.classes.get("a1"):
            lost(message)
            class_set = '1A'
        elif message.text.lower() in classes_list.classes.get("b1"):
            lost(message)
            class_set = '1Б'
        elif message.text.lower() in classes_list.classes.get("v1"):
            lost(message)
            class_set = '1В'
        elif message.text.lower() in classes_list.classes.get("a2"):
            lost(message)
            class_set = '2А'
        elif message.text.lower() in classes_list.classes.get("b2"):
            lost(message)
            class_set = '2Б'
        elif message.text.lower() in classes_list.classes.get("v2"):
            lost(message)
            class_set = '2В'
        elif message.text.lower() in classes_list.classes.get("a3"):
            lost(message)
            class_set = '3А'
        elif message.text.lower() in classes_list.classes.get("b3"):
            lost(message)
            class_set = '3Б'
        elif message.text.lower() in classes_list.classes.get("v3"):
            lost(message)
            class_set = '3В'
        elif message.text.lower() in classes_list.classes.get("a4"):
            lost(message)
            class_set = '4А'
        elif message.text.lower() in classes_list.classes.get("b4"):
            lost(message)
            class_set = '4Б'
        elif message.text.lower() in classes_list.classes.get("v4"):
            lost(message)
            class_set = '4В'
        elif message.text.lower() in classes_list.classes.get("a5"):
            lost(message)
            class_set = '5А'
        elif message.text.lower() in classes_list.classes.get("b5"):
            lost(message)
            class_set = '5Б'
        elif message.text.lower() in classes_list.classes.get("v5"):
            lost(message)
            class_set = '5В'
        elif message.text.lower() in classes_list.classes.get("a6"):
            lost(message)
            class_set = '6А'
        elif message.text.lower() in classes_list.classes.get("b6"):
            lost(message)
            class_set = '6Б'
        elif message.text.lower() in classes_list.classes.get("v6"):
            lost(message)
            class_set = '6В'
        elif message.text.lower() in classes_list.classes.get("a7"):
            lost(message)
            class_set = '7A'
        elif message.text.lower() in classes_list.classes.get("b7"):
            lost(message)
            class_set = '7Б'
        elif message.text.lower() in classes_list.classes.get("v7"):
            lost(message)
            class_set = '7В'
        elif message.text.lower() in classes_list.classes.get("a8"):
            lost(message)
            class_set = '8А'
        elif message.text.lower() in classes_list.classes.get("b8"):
            lost(message)
            class_set = '8Б'
        elif message.text.lower() in classes_list.classes.get("v8"):
            lost(message)
            class_set = '8В'
        elif message.text.lower() in classes_list.classes.get("a9"):
            lost(message)
            class_set = '9А'
        elif message.text.lower() in classes_list.classes.get("b9"):
            lost(message)
            class_set = '9Б'
        elif message.text.lower() in classes_list.classes.get("v9"):
            lost(message)
            class_set = '9В'
        elif message.text.lower() in classes_list.classes.get("a10"):
            lost(message)
            class_set = '10A'
        elif message.text.lower() in classes_list.classes.get("b10"):
            lost(message)
            class_set = '10Б'
        elif message.text.lower() in classes_list.classes.get("v10"):
            lost(message)
            class_set = '10В'
        elif message.text.lower() in classes_list.classes.get("a11"):
            lost(message)
            class_set = '11A'
        elif message.text.lower() in classes_list.classes.get("b11"):
            lost(message)
            class_set = '11Б'
        elif message.text.lower() in classes_list.classes.get("v11"):
            lost(message)
            class_set = '11В'
    elif mode == 2:
        if message.text.lower() in classes_list.classes.get("a1"):
            eat(message)
            class_set = '1-A'
        elif message.text.lower() in classes_list.classes.get("b1"):
            eat(message)
            class_set = '1-Б'
        elif message.text.lower() in classes_list.classes.get("v1"):
            eat(message)
            class_set = '1-В'
        elif message.text.lower() in classes_list.classes.get("a2"):
            eat(message)
            class_set = '2-А'
        elif message.text.lower() in classes_list.classes.get("b2"):
            eat(message)
            class_set = '2-Б'
        elif message.text.lower() in classes_list.classes.get("v2"):
            eat(message)
            class_set = '2-В'
        elif message.text.lower() in classes_list.classes.get("a3"):
            eat(message)
            class_set = '3-А'
        elif message.text.lower() in classes_list.classes.get("b3"):
            eat(message)
            class_set = '3-Б'
        elif message.text.lower() in classes_list.classes.get("v3"):
            eat(message)
            class_set = '3-В'
        elif message.text.lower() in classes_list.classes.get("a4"):
            eat(message)
            class_set = '4-А'
        elif message.text.lower() in classes_list.classes.get("b4"):
            eat(message)
            class_set = '4-Б'
        elif message.text.lower() in classes_list.classes.get("v4"):
            eat(message)
            class_set = '4-В'
        elif message.text.lower() in classes_list.classes.get("a5"):
            eat(message)
            class_set = '5-А'
        elif message.text.lower() in classes_list.classes.get("b5"):
            eat(message)
            class_set = '5-Б'
        elif message.text.lower() in classes_list.classes.get("v5"):
            eat(message)
            class_set = '5-В'
        elif message.text.lower() in classes_list.classes.get("a6"):
            eat(message)
            class_set = '6-А'
        elif message.text.lower() in classes_list.classes.get("b6"):
            eat(message)
            class_set = '6-Б'
        elif message.text.lower() in classes_list.classes.get("v6"):
            eat(message)
            class_set = '6-В'
        elif message.text.lower() in classes_list.classes.get("a7"):
            eat(message)
            class_set = '7-A'
        elif message.text.lower() in classes_list.classes.get("b7"):
            eat(message)
            class_set = '7-Б'
        elif message.text.lower() in classes_list.classes.get("v7"):
            eat(message)
            class_set = '7-В'
        elif message.text.lower() in classes_list.classes.get("a8"):
            eat(message)
            class_set = '8-А'
        elif message.text.lower() in classes_list.classes.get("b8"):
            eat(message)
            class_set = '8-Б'
        elif message.text.lower() in classes_list.classes.get("v8"):
            eat(message)
            class_set = '8-В'
        elif message.text.lower() in classes_list.classes.get("a9"):
            eat(message)
            class_set = '9-А'
        elif message.text.lower() in classes_list.classes.get("b9"):
            eat(message)
            class_set = '9-Б'
        elif message.text.lower() in classes_list.classes.get("v9"):
            eat(message)
            class_set = '9-В'
        elif message.text.lower() in classes_list.classes.get("a10"):
            eat(message)
            class_set = '10-A'
        elif message.text.lower() in classes_list.classes.get("b10"):
            eat(message)
            class_set = '10-Б'
        elif message.text.lower() in classes_list.classes.get("v10"):
            eat(message)
            class_set = '10-В'
        elif message.text.lower() in classes_list.classes.get("a11"):
            eat(message)
            class_set = '11-A'
        elif message.text.lower() in classes_list.classes.get("b11"):
            eat(message)
            class_set = '11-Б'
        elif message.text.lower() in classes_list.classes.get("v11"):
            eat(message)
            class_set = '11-В'
    else:
        bot.send_message(message.from_user.id, 'Я не знаю, що відповісти :(')


# коллбэки для инлайн-клавиатуры
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    global lang
    try:
        if call.message:
            if call.data == 'ua_l':
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
