import pymysql
import pymysql.cursors
import command_system
import app

def news(user_id,data = None):
    #con = sqlite3.connect("VKBotData.db")
    con = pymysql.connect(host='',user='',
                          password='', db='', charset ='utf8mb4')
    with con:
        cur = con.cursor()
        fetch = cur.execute("select * from news limit 3")
        res = cur.fetchall()
        #res = fetch.fetchall()
        m = ['&#9654;', '&#9654;', '&#9654;']
        i = 0
        for rw in res:
            for each in range(1,3):
                m[i] += str(rw[each])
                m[i] += ' \n'
            i += 1

    for row in m:
        app.send_message(user_id, row)



new_command = command_system.Command()

new_command.keys = ['"новости"']
new_command.description = 'Новости'
new_command.process = news

