from telebot import types

TOKEN = '1506257040:AAH5DunpqOf38JPrsIv2MFwpfjVlSafhwnI'

# информация
info_message = 'ℹ️<b>Телеграм бот КЗЗСО №22 з профільним навчанням ім. М.М.Крупченка.</b> \n' \
               '\n' \
               '📥Увесь вихідний код на GitHub: \n' \
               'https://github.com/Raleyph/school_bot \n' \
               '\n' \
               'ℹ️Версія: 0.2.1 Alpha \n' \
               '\n' \
               '❗️Просимо вибачення за відсутність можливості вибору ім\'я учня під час сдачі відсутніх, адже ми піклуємося про персональні дані та конфіденціальність! \n' \
               '\n' \
               '❗️Система заказів до їдальні має на увазі те, що класний керівник віддасть гроші у кінці тижня (п\'ятниця) \n'

hello_message = f'Привіт, це бот Краматорського закладу середньої освіти №22 з профільним навчанням ім. М.М.Крупченка'

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

# кнопки подтверждения
ok = types.InlineKeyboardButton('Відправити✅', callback_data='c_ok')
no = types.InlineKeyboardButton('Відмінити❌', callback_data='c_no')
