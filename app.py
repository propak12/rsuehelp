from flask import Flask, request, json
from settings import *
from command_system import command_list
from vk_api.keyboard import VkKeyboard, VkKeyboardButton,VkKeyboardColor
import vk
import os
import importlib
import random
import threading
import datetime
import time

up = True


def check():
    if datetime.datetime.today().isoweekday() == 7:
        global up
        up = not up
    t = threading.Timer(24*60*60, check)
    t.start()


t = threading.Timer(24*60*60, check)
t.start()
app = Flask(__name__)
session = vk.Session()
api = vk.API(session, v='5.124')
user_id=''

@app.route('/', methods=['POST'])
def processing():

    data = json.loads(request.data)
    print(data['type'])
    if 'type' not in data.keys():
        return 'not vk'
    if data['type'] == 'confirmation':
        return confirmation_token
    if data['type'] == 'message_event':
        create_answer_callback(data['object'])
        return 'ok'
    elif data['type'] == 'message_new':
        create_answer(data['object']['message'])
        return 'ok'
    else:
    	return 'ok'

def create_answer_callback(data):
    print(data)
    load_modules()
    user_id = data['user_id']
    send_message_answer(data['event_id'],data['user_id'],data['peer_id'],data['payload'])
    get_answer(data,user_id)
def create_answer(data):
    if data['text'] == 'Меню':
        settings = dict(one_time=False, inline=False)

        keyboard = VkKeyboard(**settings)
        # pop-up кнопка
        keyboard.add_button(label='Общаги', color=VkKeyboardColor.POSITIVE,
                                       payload='\"общаги\"')
        keyboard.add_button(label='Общая информация об ун.', color=VkKeyboardColor.POSITIVE,
                                       payload='\"вузинфа\"')
        keyboard.add_button(label='Библиотеки', color=VkKeyboardColor.POSITIVE,
                                       payload='\"библиотеки\"')
        keyboard.add_line()
        keyboard.add_button(label='Раздача', color=VkKeyboardColor.POSITIVE,
                                       payload='\"Раздача\"')
        keyboard.add_button(label='Ссылки', color=VkKeyboardColor.POSITIVE,
                                       payload='\"Ссылки\"')
        keyboard.add_button(label='Новости', color=VkKeyboardColor.POSITIVE,
                                       payload='\"новости\"')
        keyboard.add_line()
        keyboard.add_button(label='Стипендия', color=VkKeyboardColor.POSITIVE,
                                       payload='\"Стипендия\"')
        keyboard.add_button(label='Расписание', color=VkKeyboardColor.POSITIVE,
                            payload='\"расписание\"')
        keyboard.add_button(label='Справочник', color=VkKeyboardColor.POSITIVE,
                            payload='\"справочник\"')
        send_message(data['from_id'], message="Меню:", keyboard=keyboard.get_keyboard())
        return
    print(data)
    load_modules()
    user_id = data['from_id']
    get_answer(data,user_id)


def get_answer(body, user_id):
    for c in command_list:
        if body['payload'].lower() in c.keys:
            c.process(user_id, body)


def load_modules():
    files = os.listdir("commands")
    modules = filter(lambda x: x.endswith('.py'), files)
    for m in modules:
        importlib.import_module("commands." + m[0:-3])

def send_message(user_id, message, attachment=None, keyboard=None, longi=None, lat=None):
    api.messages.send(access_token=access_token, user_id=str(user_id),
                      message=message, attachment=attachment,
                      random_id=random.getrandbits(64), keyboard=keyboard, long=longi, lat=lat)

def send_message_answer(event_id,user_id,peer_id,payload):
	api.messages.sendMessageEventAnswer(event_id=event_id,
		          access_token=access_token,
                  user_id=user_id,
                  peer_id=peer_id,                                                   
                  event_data=json.dumps(payload))

def message_edit(peer_id,message,conv_mes_id,keyboard = None):
	api.messages.edit(access_token=access_token, peer_id=peer_id,message=message,conversation_message_id=conv_mes_id,keyboard=keyboard)
