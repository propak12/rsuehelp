import command_system
import pymysql
import pymysql.cursors
import json
import app
from datetime import datetime
from vk_api.keyboard import VkKeyboard, VkKeyboardButton, VkKeyboardColor

fakul = {"111":"ФМиП","211":"ФТД","311":"ФКТиИБ","411":"УЭФ","511":"ФЭиФ","611":"ЮФ","711":"ФЛиЖ"}
fakulfull = {"111":"Менеджмента и предпринимательства","211":"Торгового дела","311":"Компьютерных технологий и информационной безопасности","411":"Учетно-экономический","511":"Экономики и финансов","611":"Юридический","711":"Лингвистики и журналистики"}
dictf = ["111","211","311","411","511","611","711"]
dicty = ["1","2","3","4"]
dictfy = []

res = 's'
currentW = 1
def sch(user_id,data = None):

    con = pymysql.connect(host='',user='',
                          password='', db='', charset ='utf8mb4')
    
    if datetime.today().strftime("%a") == 'Sat':
    	currentW = 0
    if data['payload'] == '"расписание"':
        

        settings = dict(one_time=False, inline=True)
        keyboard = VkKeyboard(**settings)
        print("button preesed")
        for row in range(0,7):
            keyboard.add_callback_button(label=fakul[dictf[row]], color=VkKeyboardColor.POSITIVE,
									payload='\"' + dictf[row] + '\"')
            if row==3:
                keyboard.add_line()
        app.send_message(user_id, "Факультеты", keyboard=keyboard.get_keyboard())

    faculty = []
    if data['payload'] in dictf:
        settings = dict(one_time=False, inline=True)
        keyboard = VkKeyboard(**settings)
        print("button preesed")
        for y in range(1,5):
            keyboard.add_callback_button(label=y, color=VkKeyboardColor.POSITIVE,
									payload='\"'+data['payload']+str(y)+'\"')
        #app.send_message(user_id, "Расписание", keyboard=keyboard.get_keyboard())
        print(dictfy)
        app.message_edit(data['peer_id'], "Курс", data['conversation_message_id'],keyboard=keyboard.get_keyboard())
    if data['payload'] in dictfy:
        print(data)
        fct = data['payload'][0:3]
        yaer = data['payload'][3]
        with con:
            cur = con.cursor()
            fac = cur.execute("SELECT distinct schedule.group FROM schedule where faculty = '"+fakulfull[fct]+"' AND year = "+yaer+"")
            print(fac)
            res = cur.fetchall()
            print(res)
            m=[]
            for rw in res:
                print(rw)
                print(str(rw[0]))
                m += [str(rw[0])]
                print('next')
        settings = dict(one_time=False, inline=True)
        keyboard = VkKeyboard(**settings)
        print('keyboard')
        print(m)
        for row in range(0,len(m)):
            keyboard.add_button(label=m[row], color=VkKeyboardColor.POSITIVE,
									payload='\"group\"')
            print(m[row])
            if row==3:
                keyboard.add_line()
                print(m[row])
        print(keyboard.get_keyboard())
        print('edit')
        app.message_edit(data['peer_id'], "Группа", data['conversation_message_id'], keyboard=keyboard.get_keyboard())
        print('end')
    if data['payload'] == '"group"':
        m = [[]]
        with con:
            cur = con.cursor()
            fetch = cur.execute("select schedule.day,schedule.schedule from schedule where schedule.group = '"+data['text']+"' and schedule.up_weak = '+app.up+'")
            res = cur.fetchall()
            m = res
        message = ""
        for row in m:
        	for col in row:
        	    message+=str(col)+"\n"
        app.send_message(user_id, message)



sch_command = command_system.Command()
for f in dictf:
	for y in dicty:
		dictfy += [f + y]
sch_command.keys = ['"расписание"','"group"'] + dictf + dictfy
sch_command.description = 'Иноформация о вузе'
sch_command.process = sch

