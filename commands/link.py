import command_system
import app

def links(user_id,data = None):
    res = """Сайты:
Портфолио: https://portfolio.rsue.ru/login/index.php
Учебный портал: https://do.rsue.ru

Инстаграм:
Официальный Инстаграм: https://www.instagram.com/rsue.rinh/

ВК группы факультетов:
Факультет торгового дела: https://vk.com/club47417589
Учетно-Экономический Факультет: https://vk.com/public67629981
Факультета Экономики и Финансов: https://vk.com/public146692864
Юридический факультет: https://vk.com/urfakrinh
КТиИБ: https://vk.com/club55703898
Менеджмент и предпринимательства: https://vk.com/mip_rsue

Иные ВК группы:
РИНХбург:  https://vk.com/rinhburg
Подслушано в РГЭУ: https://vk.com/uyutnenkyrinh
Профсоюзная организация обучающихся: https://vk.com/profkom_rsue
Штаб студенческих отрядов: https://vk.com/rso_rsue
Студенческий совет: https://vk.com/studsovetrsue
Официальная группа ВК: https://vk.com/rsue_rinh_officia_lgroup
Студенческий культурный центр: https://vk.com/skc_rsue
Отдела международной мобильности: https://vk.com/otdel_mobilnosti"""
    app.send_message(user_id, res)


link_command = command_system.Command()

link_command.keys = ['"Ссылки"']
link_command.description = 'Полезные ссылки связанные с РИНХом'
link_command.process = links
