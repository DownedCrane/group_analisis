# -*- coding: utf-8 -*-
import vk_requests
#import sys
#sys.path.insert(0, "~/vk-requests")
#import __init__
import auth, requests, time
import collections
# from tkinter import*
# login = "89167812455"
# password = "?real_woman223522?"

# логинимся
api = vk_requests.create_api(app_id=5745809, login=auth.login, password=auth.password, scope=['offline', 'messages', 'users', 'groups'], interactive=True)


def getGroupSubscribers(groupid): #возвращает список!
    result = api.groups.getMembers(group_id = groupid, count = 1000, offset=0)
    #numOfSubs = result[0][0]
    subscribers = [] # подписчики группы
    numOfSubs = result['count']    #количество подписчиков
    if numOfSubs <= 1000:
        result = api.groups.getMembers(group_id = groupid, count = 1000, offset=0)
        subscribers = result['items']
        #print(subscribers)
        return subscribers
        
    else:
        ofs = 0
        i = (numOfSubs // 1000) + 1 #количество необходимых запросов по тысяче человек к ВК
        while (i != 0):
             # смещение при поиске, по умолчанию нулевое, каждую итерацию растет на 1000
            result = api.groups.getMembers(group_id = groupid, count = 1000, offset=ofs)
            
            subscribers.extend(result['items'])
            ofs = ofs + 1000
            i = i - 1
            time.sleep(0.8)
            pass
        #print(subscribers)
        return subscribers
pass

def linkify(users): #меняет цифрыXXX в списке на ссылки в вк вида vk.com/idXXX, при использовании приравняй к другому списку!
    result = []
    for user in users:
        result.append("vk.com/id" + str(user))
        pass
    pass
    print(result)
    return(result)


#ввод города
print("Введите id группы, в котором будет вестись поиск")
GROUPID = 0
GROUPID = int(input("GROUPID = "))

group_subs = getGroupSubscribers(GROUPID)
24070381

usercounter = 0 #счетчик успешно посчитанных пользователей
failcounter = 0
# у каждого пользователя получаем список подписок
totalsubs = []
for user in group_subs:
    time.sleep(0.4)
    try:
        usersubs = api.groups.get(user_id = user)
        print("vk.com/id" + str(user) + " обработан")
        totalsubs.extend(usersubs['items'])
        usercounter = usercounter + 1

    except Exception:
        print("vk.com/id" + str(user) + " закрыл подписки")
        failcounter = failcounter + 1

    #else:
       # pass

   
    pass


# дописать форматирование вывода

#запись трудов в файл

result = collections.Counter(totalsubs)
print("Выборка составила " + str(usercounter) + " человек")
print("Не удалось обработать " + str(failcounter) + " человек")


f = open('ans_analisis.txt', 'w')
f.write(str(result))
f.close()

# id  lb = 101966743
