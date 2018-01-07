import vk_api
from time import sleep
import notify2
import httplib2
import os

preview = 50
count = 2
login = 'login'
password = 'password'

def exists(path):
    try:
        os.stat(path)
    except OSError:
        return False
    return True

vk_session = vk_api.VkApi(login, password)
try:
        vk_session.auth()
except vk_api.AuthError as error_msg:
        print(error_msg)

vk = vk_session.get_api()
#############Engine starter###############
messages_vk = vk.messages.getDialogs(count=count, unread=0).get('items')
queue = messages_vk

users = vk.users.get(user_ids=','.join([str(queue[x].get('message').get('user_id')) for x in range(0, len(queue))]), fields='photo_max')

readed = []
try:
    os.mkdir('photos')
except:
    print('exist')

for x in range(0, len(users)):
    if exists('photos/' + str(users[x].get('id')) + '.jpg'):
        print('exist')
    else:
        h = httplib2.Http('.cache')
        response, content = h.request(users[x].get('photo_max'))
        out = open('photos/'+str(users[x].get('id'))+'.jpg', 'wb')
        out.write(content)
        out.close()
chat =''

#############Engine starter###############

while True:
    if queue != []:
        for i in range(0, len(queue)):
            current = queue[i].get('message')
            try:
                users_current = users[i]
            except:
                users_current = users_current

            notify2.init('vk',mainloop='glib' )
            if current.get('title') != '':
                chat = str('@' + current.get('title'))
            if current.get('attachments') != None:
                body = '<b>Вложение</b> '
            elif current.get('fwd_messages') != None:
                body = '<b>Пересланное сообщение</b>'
            else:
                body = current.get('body')[0:preview]

            n = notify2.Notification(users_current.get('first_name')+ ' ' + users_current.get('last_name') + ' ' + chat,
        message=body, icon = os.path.abspath('photos/' + str(users_current.get('id')) + '.jpg'))
            n.set_urgency(notify2.URGENCY_NORMAL)
            n.set_timeout(5000)
            n.show()
            chat = ''
    messages_vk = vk.messages.getDialogs(count=count, unread=0).get('items')
    try:
        readed.append(queue[0])
    except:
        readed = readed
    # print(readed)
    # print('='*100)

    try:
        queue = [x for x in messages_vk if x not in readed]

        users = vk.users.get(user_ids=','.join([str(queue[x].get('message').get('user_id')) for x in range(0, len(queue))]), fields='photo_max')

        for x in range(0, len(users)):
            if exists('photos/' + str(users[x].get('id')) + '.jpg'):
                print('exist')
            else:
                h = httplib2.Http('.cache')
                response, content = h.request(users[x].get('photo_max'))
                out = open('photos/'+str(users[x].get('id'))+'.jpg', 'wb')
                out.write(content)
                out.close()
    except:
        queue = []
    # print(queue)
    sleep(5)
