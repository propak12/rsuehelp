import command_system
import json
import app
from vk_api.keyboard import VkKeyboard, VkKeyboardButton,VkKeyboardColor


def money(user_id, data = None):
    print(data['payload'])
    if data['payload'] == '"Стипендия"':
        settings = dict(one_time=False, inline=True)
        keyboard = VkKeyboard(**settings)
        # pop-up кнопка
        keyboard.add_callback_button(label='Академическая', color=VkKeyboardColor.POSITIVE,
                                       payload='\"Академическая\"')
        keyboard.add_callback_button(label='Социальная', color=VkKeyboardColor.POSITIVE,
                                       payload='\"Социальная\"')
        
        app.send_message(user_id, message="Виды стипендии", keyboard=keyboard.get_keyboard())
    if data['payload'] == 'Академическая':
        message="""Академическая стипендия зависит от успеваемости обучаегося.
При получении образования степендия составляет 2200 рублей.
Если по итогам сессии обучающийся имеет оценки «ХОРОШО» и «ОТЛИЧНО» или только «ХОРОШО», стипендия составляет 2200 рублей.
Если обучающийся по итогам сессии имеет только оценки «ОТЛИЧНО», он может рассчитывать на повышенную стипендию в размере 3000 рублей."""
        app.message_edit(data['peer_id'], message, data['conversation_message_id'])
    if data['payload'] == 'Социальная':
        message="""Социальная стипендия назначается студенту с даты предоставления документа, подтверждающего соответствие одной из категорий студентов, указанных в ФЗ № 273 «Об образовании в РФ» статья 36 пункт 5 по месяц прекращения действия основания её назначения.
Государственная социальная стипендия назначается студентам:
1.распорядительным актом руководителя организации на основании документа, подтверждающего соответствие одной из категорий граждан, с даты его представления
2.В случае, если документ бессрочный назначается до конца обучения
В РГЭУ РИНХ социальную стипендию могут получить:
-студенты, из числа детей - сирот и детей, оставшихся без попечения родителей - 3800 руб
-студенты - инвалиды 1 и 2 группы, дети - инвалиды и инвалидам с детства -3000 руб
-студенты, подвергшиеся радиации вследствие катастрофы на Чернобыльской АЭС и иных радикальных катастроф - 3000 руб
-студенты, инвалиды и ветераны боевых действий - 3000 руб
-студенты, получающих государственную помощь - 3000 руб"""
        app.message_edit(data['peer_id'], message, data['conversation_message_id'])

    


money_command = command_system.Command()

money_command.keys = ['"Стипендия"','Академическая','Социальная']
money_command.description = 'Стипендия'
money_command.process = money
