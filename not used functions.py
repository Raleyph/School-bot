"""
# обработка заказов в столовую
def eat(message):
    sent = bot.send_message(message.from_user.id, 'Введіть дані про заказ у форматі 2*25, 3*30')
    bot.register_next_step_handler(sent, send_list)

    elif mode == 2:
        bot.send_message(eat_id, 'Заказ від ' + class_set + ': ' + mess)
        bot.send_message(message.from_user.id, 'Заказ відправлено!')
        mode = 0
"""
