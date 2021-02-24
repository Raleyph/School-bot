from telebot import types
import COVID19Py

TOKEN = '1506257040:AAH5DunpqOf38JPrsIv2MFwpfjVlSafhwnI'

covid = COVID19Py.COVID19()
location = covid.getLocationByCountryCode("UA")

date = location[0]['last_updated'].split("T")
time = date[1].split(".")

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
# расписание звонков
alarm_timeing = types.InlineKeyboardButton("Розклад дзвінків", callback_data='al-tm')

# информация
info_message = ('ℹ️<b>Телеграм бот КЗЗСО №22 з профільним навчанням ім. М.М.Крупченка.</b> \n' +
                '\n' +
                '📥Увесь вихідний код на GitHub: \n' +
                'https://github.com/Raleyph/school_bot \n' +
                '\n' +
                'ℹ️Версія: 0.0.1 Pre-Alpha \n' +
                '\n' +
                '❗️Просимо вибачення за відсутність можливості вибору ім\'я учня під час сдачі відсутніх, адже ми піклуємося про персональні дані та конфіденціальність! \n' +
                '\n' +
                '❗️Система заказів до їдальні має на увазі те, що класний керівник віддасть гроші у кінці тижня (п\'ятниця) \n')

# памятка о коронавирусе
final_message = f"<b>Не забувайте одягати захисну маску, мити руки та оброблювати їх антисептиками!</b>\n"\
                f"\n"\
                f"<u>Дані по країні:</u>\nНаселення: {location[0]['country_population']:,}\n" \
                f"Останнє оновлення: {date[0]} {time[0]}\nОстанні дані:\n<b>" \
                f"Захворівших: </b>{location[0]['latest']['confirmed']:,}\n<b>Смертей: </b>" \
                f"{location[0]['latest']['deaths']:,}"

# главное меню
lang = types.KeyboardButton("Мова")
info = types.KeyboardButton("Інформація")
food = types.KeyboardButton("Їдальня")
lost = types.KeyboardButton("Відсутні")
covi = types.KeyboardButton("COVID-19")
day = types.KeyboardButton("Розклад")

# конпки выбора языка
ua = types.InlineKeyboardButton('🇺🇦', callback_data='ua_l')
ru = types.InlineKeyboardButton('🇷🇺', callback_data='ru_l')
en = types.InlineKeyboardButton('🇬🇧', callback_data='en_l')
