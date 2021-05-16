import command_system
import json
import app


def hostels(user_id,data = None):
    button = json.dumps({
        "one_time":False,
        "buttons": [[
            {
                "action": {
                    "type": "open_link",
                    "payload":"\"Открыть в картах\"",
                    "link": "https://yandex.ru/maps/-/CCQhvJwYLD",
                    "label": "Открыть в картах"
                }
            }]],
        "inline": True
    })
    res = """Информация по общежитиям:
1.г. Ростов-на-Дону ул. 2-я Краснодарская, 113/1"""
    app.send_message(user_id, res, keyboard=button, longi=47.205484, lat=39.649176);
    button = json.dumps({
        "one_time":False,
        "buttons": [[
            {
                "action": {
                    "type": "open_link",
                    "payload":"\"Открыть в картах\"",
                    "link": "https://yandex.ru/maps/-/CCQhvJwYLD",
                    "label": "Открыть в картах"
                }
            }]],
        "inline": True
    })
    res = """
2.г. Ростов-на-Дону пер. Гвардейский, 6"""
    app.send_message(user_id, res, keyboard=button, longi=47.225523, lat=39.692779);
    button = json.dumps({
        "one_time":False,
        "buttons": [[
            {
                "action": {
                    "type": "open_link",
                    "payload":"\"Открыть в картах\"",
                    "link": "https://yandex.ru/maps/-/CCQhvJwYLD",
                    "label": "Форма заявления"
                }
            }]],
        "inline": True
    })
    res = """
Подача завляния для заселения на E-mail: Obshezitierinh@yandex.ru"""
    app.send_message(user_id, res, keyboard=button);



hostel_command = command_system.Command()

hostel_command.keys = ['"общаги"']
hostel_command.description = 'Общежития'
hostel_command.process = hostels
