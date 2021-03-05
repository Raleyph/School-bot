import telebot
import config
import sqlite3
import classes_list

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

mode = None             # режим
lang = 'ua'             # язык
class_set = None        # класс
sent_ms = 0             # разрешение на отправку

lost = [
    1672178639
]

lost_id = 1672178639    # id получателя отсутствующих

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


# обработка отсутствующих
def lost_set(message):
    sent = bot.send_message(message.from_user.id, 'Введіть прізвища учнів через кому:')
    bot.register_next_step_handler(sent, send_list)


# отправка данных
def send_list(message):
    global class_set
    global mode
    global sent_ms

    mess = message.text

    class_set_str = "".join(class_set)
    bot.send_message(lost_id, 'Відсутні ' + class_set_str + ': ' + mess)
    bot.send_message(message.from_user.id, 'Дані відправлені!')


# обработка вывода расписания
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
    elif message.text.lower() == 'їдальня':
        mode = 2
        bot.send_message(message.chat.id, 'Дана функція поки що не працює')
    elif message.text.lower() == 'розклад':
        mode = 3
        bot.send_message(message.chat.id, 'Виберіть клас:')
    elif mode == 1:
        data = message.text.lower()
        for key in classes_list.classes.values():
            if data in key:
                lost_set(message)
                class_set = data
    else:
        bot.send_message(message.from_user.id, 'Я не знаю, що відповісти :(')


# коллбэки для инлайн-клавиатуры
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    global lang
    global sent_ms
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
