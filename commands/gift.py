import command_system
import app

def gift(user_id,data = None):
    attachment = 'doc-196165322_560058549'
    app.send_message(user_id, "Лови!", attachment)


gift_command = command_system.Command()

gift_command.keys = ['"Раздача"']
gift_command.description = 'Стикеры'
gift_command.process = gift
