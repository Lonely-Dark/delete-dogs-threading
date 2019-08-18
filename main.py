#Python3.7.3
#Make by Lonely-Dark

#Modules:
import threading
import requests
import time

#Set conversation_id
conversation_id=int(input('Set conversation_id: '))
#Token:
token='Token here'

def delete_dogs_friends(token):
	#Get all friends
	friends=requests.get('https://api.vk.com/method/friends.get',params={'access_token': token, 'v': 5.101, 'fields': 'deactivated'}).json()
	for i in friends['response']['items']:
		if 'deactivated' in i:
			#Delete friend
			f=requests.get('https://api.vk.com/method/friends.delete',params={'access_token': token, 'v': '5.101', 'user_id': i['id']}).json()
			print(time.strftime('%H')+':'+time.strftime('%M')+'|[delete]: delete '+ str(i['first_name']) + ' ' + str(i['last_name'])) + ' in friends'
	else:
		print('Nothing to do, exit')

def delete_dogs_conversation(token,conversation_id):
	#Get all peoples in conversation
	get_conversation_peoples=requests.get('https://api.vk.com/method/messages.getConversationMembers',params={'access_token': token, 'peer_id': 2000000000+conversation_id, 'fields': 'deactivated', 'v': '5.101'}).json()
	for i in get_conversation_peoples['response']['profiles']:
		if 'deactivated' in i:
			#Delete human in conversation
			f_re=requests.get('https://api.vk.com/method/messages.removeChatUser',params={'access_token': token, 'chat_id': conversation_id, 'user_id': i['id'], 'v': '5.101'}).json()
			print(time.strftime('%H')+':'+time.strftime('%M')+'|[delete]: delete '+ str(i['first_name']) + ' ' + str(i['last_name']) + ' in conversation')
	else:
		print('Nothing to do, exit')

#Initialization threads
one=threading.Thread(target=delete_dogs_friends, args=(token,))
two=threading.Thread(target=delete_dogs_conversation, args=(token,conversation_id))

#Start threads
one.start()
two.start()

#Join threads to the main thread
one.join()
two.join()