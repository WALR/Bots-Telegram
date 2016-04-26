# -*- encoding: utf-8 -*-
import telebot


TOKEN = '200471947:AAEvrDdbqrtzuEgg94z0EJtIj1UhTK4CDaw'

travis = telebot.TeleBot(TOKEN)

comandos = "/ayuda, /creador, "

# 4chan
from fchan import fchan
@travis.message_handler(commands=['4chan'])
def command_4chan(m):
	fchan(m, travis)

# fecha
from fecha import fecha
@travis.message_handler(commands=['fecha'])
def command_fecha(m):
	fecha(m, travis)

# getid
@travis.message_handler(commands=['getid'])
def command_getid(m):
    cid = m.chat.id
    travis.send_message(cid, str(m.chat.id) + " " + m.from_user.username )


# creador
@travis.message_handler(commands=['creador'])
def command_iscreador(message):
    cid = message.chat.id
    us = "WilfredLemus"
    usermsg = message.from_user.username
    if(us == usermsg):
        travis.send_message(cid, 'oh gran %s mi creador' % message.from_user.username)
    else:
        travis.send_message(cid, 'no eres mi craedor, lo siento!')

# img Google
from google_img import img
@travis.message_handler(commands=['img'])
def command_img(m):
	img(m, travis)






@travis.message_handler(commands=['ayuda'])
def send_welcome(message):
	travis.reply_to(message, "Hola %s, como estas?" % message.from_user.username )



# @travis.message_handler(commands=['start', 'help', 'travis', 'Travis'])
# def send_welcome(message):
# 	travis.reply_to(message, "Hola %s, como estas?" % message.from_user.username )


# @travis.message_handler(func=lambda m: True)
# def echo_all(message):
#     travis.reply_to(message, message.text)


# @travis.message_handler(commands=['start', 'help', 'travis', 'Travis'])
# def send_(message):
# 	travis.reply_to(message, "Hola %s, como estas?" % message.from_user.username )



def listener(message):
	pass
	# for m in message:
	# 	chat_id = m.chat.id
 #        if m.content_type == 'text':
 #        	text = m.text
 #        	markup = telebot.types.ReplyKeyboardMarkup()
 #        	markup.add('a', 'v', 'd')
 #        	travis.send_message(chat_id, "Selecciona", reply_markup=markup)
            # if text == 'saluda' || text == 'Saluda':
            # travis.send_chat_action(chat_id, "typing")
            # travis.send_message(chat_id,"Me copio de tu texto")
            # travis.send_message(chat_id, text)

travis.set_update_listener(listener)
travis.polling()


while True:
    pass



# if message.chat.type == “private”:
#     # private chat message

# if message.chat.type == “group”:
#     # group chat message

# if message.chat.type == “supergroup”:
#     # supergroup chat message

# if message.chat.type == “channel”:
#     # channel message