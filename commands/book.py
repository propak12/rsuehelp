import command_system
import json
import app


def books(user_id,data = None):
    button = json.dumps({
        "one_time":False,
        "buttons": [[
            {
                "action": {
                    "type": "open_link",
                    "payload":"\"Открыть в картах\"",
                    "link": "https://yandex.ru/maps/-/CCQhqDxC~B",
                    "label": "Открыть в картах"
                }
            }]],
        "inline": True
    })
    res = """Библиотека РГЭУ(РИНХ) на Островского
Тел.: +7 (863) 267-43-83"""
    app.send_message(user_id, res, keyboard=button, longi=47.221722, lat=39.705331);

    button = json.dumps({
        "one_time":False,
        "buttons": [[
            {
                "action": {
                    "type": "open_link",
                    "payload":"\"Открыть в картах\"",
                    "link": "https://yandex.ru/maps/-/CCQhqLCVKC",
                    "label": "Открыть в картах"
                }
            }]],
        "inline": True
    })
    res = """Библиотека в главном корпусе РИНХ
Тел.: +7 (863) 261-38-21"""
    app.send_message(user_id, res, keyboard=button, longi=47.223079, lat=39.718184);

    button = json.dumps({
        "one_time":False,
        "buttons": [[
            {
                "action": {
                    "type": "open_link",
                    "payload":"\"Главный сайт\"",
                    "link": "https://library.rsue.ru/",
                    "label": "Главный сайт библиотки"
                }
            }
            ],
            [
            {
                "action": {
                    "type": "open_link",
                    "payload":"\"Электронная\"",
                    "link": "https://lib.rsue.ru/MegaPro/web",
                    "label": "Электронная библиотека"
                }
            }]],
        "inline": True
    })
    res = """&#128213;&#128215;&#128216;&#128217;"""
    app.send_message(user_id, res, keyboard=button);



books_command = command_system.Command()

books_command.keys = ['"Библиотеки"']
books_command.description = 'Библиотеки'
books_command.process = books
