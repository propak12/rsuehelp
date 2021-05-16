import command_system
import json
import app
from vk_api.keyboard import VkKeyboard, VkKeyboardButton,VkKeyboardColor

def info(user_id, data = None):
    print(data['payload'])
    if data['payload'] == '"вузинфа"':
        settings = dict(one_time=False, inline=True)
        settings = dict(one_time=False, inline=True)
        keyboard = VkKeyboard(**settings)
        # pop-up кнопка
        keyboard.add_callback_button(label='Информация о вузе', color=VkKeyboardColor.POSITIVE,
									payload='\"Информация о вузе\"')
        keyboard.add_line()
        keyboard.add_callback_button(label='РГЭУ РИНХ Большая Садовая', color=VkKeyboardColor.POSITIVE,
									payload='\"РГЭУ РИНХ Большая Садовая\"')
        keyboard.add_line()
        keyboard.add_callback_button(label='РГЭУ РИНХ Буденовский', color=VkKeyboardColor.POSITIVE,
									payload='\"РГЭУ РИНХ Буденовский\"')
        keyboard.add_line()
        keyboard.add_callback_button(label='РГЭУ РИНХ Максима-Горького', color=VkKeyboardColor.POSITIVE,
									payload='\"РГЭУ РИНХ Максима-Горького\"')
        app.send_message(user_id, message="&#127979;", keyboard=keyboard.get_keyboard())
    if data['payload'] == 'Информация о вузе':
        message ="""В 1930—1931 годах в СССР были созданы финансово-экономические институты в Москве, Ленинграде, Харькове, Ташкенте, Иркутске, Казани, Киеве и в Ростове-на-Дону (1931).
Ростовский финансово-экономический институт (РФЭИ) возник на базе экономического факультета Северо-Кавказского государственного университета (прежнее название РГУ). Именно на его кадровой, научно-исследовательской и учебно-методической базе развивался институт в предвоенное десятилетие.
Постановлением Совета Народных Комиссаров СССР от 28 февраля 1933 года за № 330 РФЭИ был включен в список высших учебных заведений страны, 11 марта 1939 года приказом Всесоюзного комитета высшей школы был утвержден устав института.
13 октября 1964 года приказом Министерства высшего и среднего специального образования РСФСР № 718 РФЭИ был переименован в Ростовский институт народного хозяйства (РИНХ). В 1994 году институт стал академией, а 2000 году — университетом."""
        app.send_message(user_id, message)
        #app.message_edit(data['peer_id'], message, data['conversation_message_id'])
    if data['payload'] == 'РГЭУ РИНХ Большая Садовая':
        message ="""Факультеты:
Факультет Торгового Дела
Факультет Компьютерных технологий и информационной безопасности
Учетно-экономический факультет
Факультет Экономики и финансов
Факультет Лингвистики и журналистики"""
        app.send_message(user_id, message, longi=39.739537, lat=47.223185)
        #app.message_edit(data['peer_id'], message, data['conversation_message_id'])
    if data['payload'] == 'РГЭУ РИНХ Буденовский':
        message ="""Факультеты:
Факультет Менеджмента и предпринимательства"""
        app.send_message(user_id, message, longi=39.705702, lat=47.221863)
        #app.message_edit(data['peer_id'], message, data['conversation_message_id'])
    if data['payload'] == 'РГЭУ РИНХ Максима-Горького':
        message ="""Факультеты:
Юридический факультет"""
        app.send_message(user_id, message, longi=39.724418, lat=47.228614)
        #app.message_edit(data['peer_id'], message, data['conversation_message_id'])
    #app.send_message(user_id, res)

info_command = command_system.Command()

info_command.keys = ['"вузинфа"','Информация о вузе','РГЭУ РИНХ Большая Садовая','РГЭУ РИНХ Буденовский','РГЭУ РИНХ Максима-Горького']
info_command.description = 'Иноформация о вузе'
info_command.process = info
