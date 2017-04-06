import subprocess 
import os.path
import json

#if os.path.exists("./server.json"):
#	with open('server.json','r') as json_data:
#		serverDict = json.load(json_data)
#else:
#serverDict = {}
groupDict = {}
serverlist = []

def fun_clearScreen():
	subprocess.call('clear',shell=True)

####################################
####################################

def fun_addNewHost():
	fun_makeMenu('adding new host')
	rmt_ip = input('{:<25}{:^3}'.format(' - Remote Host ip ',':'))
	rmt_name = input('{:<25}{:^3}'.format(' - Remote Host name ',':'))
	rmt_port = input('{:<25}{:^3}'.format(' - Remote Host ssh Port ',':'))
	rmt_user = input('{:<25}{:^3}'.format(' - Remote Host User ',':'))
	rmt_pkey = input('{:25}{:^3}'.format(' - User ssh key file', ':'))
	if  rmt_ip and rmt_pkey and rmt_port and rmt_user and rmt_name:
		print('ok')
		fun_addToDictionary(ip=rmt_ip,port=rmt_port,user=rmt_user,key=rmt_pkey,name=rmt_name)
	else:
		fun_addNewHost()
    	
#####################################
#####################################

def fun_makeMenu(msg):
	fun_clearScreen()
	print('')        
	print('',msg.upper())
	print('','-' * len(msg))
	print('')

######################################
######################################
def fun_ListAllHost():
	with open('server.json','r') as json_data:
		serverDict = json.load(json_data)
	fun_makeMenu('List of all host')
	for key in sorted(serverDict.keys()):
		print('  {:<4}{:<15} {}'.format(key,serverDict[key]['ip'],serverDict[key]['name']))
	input('')
######################################
######################################
def fun_delExistingHost():
	
	fun_makeMenu('Removing host ')
	with open('server.json','r') as json_data:
		serverDict = json.load(json_data)
	for key in sorted(serverDict.keys()):
		print('  {:<4}{:<15} {}'.format(key,serverDict[key]['ip'],serverDict[key]['name']))
	print('')
	print('')
	choice = input(" Select Server Id ['q' quit ] :")
	if choice == 'q':
		pass
	elif choice in serverDict:
		del serverDict[choice]
	else:
		pass
	with open('server.json','w') as json_data:
		json.dump(serverDict,json_data,indent = 4)		

######################################
######################################


def fun_changeSettings():
	fun_makeMenu('Changing host settings')
	with open('server.json','r') as json_data:
		serverDict = json.load(json_data)
	fun_ListAllHost()
	choice = input(" Select Server Id ['q' quit] : ")
	if choice == 'q':
		pass
	elif choice in serverDict:
		rmt_ip = input('{:<25}{:^3}'.format(' - Remote Host ip ',':'))
		rmt_name = input('{:<25}{:^3}'.format(' - Remote Host name ',':'))
		rmt_port = input('{:<25}{:^3}'.format(' - Remote Host Port ',':'))
		rmt_user = input('{:<25}{:^3}'.format(' - Remote Host User ',':'))
		rmt_pkey = input('{:25}{:^3}'.format(' - Private key File Name', ':'))
		if  rmt_ip and rmt_pkey and rmt_port and rmt_user and rmt_name:
			del serverDict[int(choice)]
			print('ok')
			fun_addToDictionary(ip=rmt_ip,port=rmt_port,user=rmt_user,key=rmt_pkey,name=rmt_name)
		else:
			fun_changeSettings()
		with open('server.json','w') as json_data:
			json.dump(serverDict,json_data,indent = 4)	
		input('press enter to go back ...')
	
	
	
	
############################
############################
def fun_addToDictionary(**kwars):
	with open('server.json','r') as json_data:
		serverDict = json.load(json_data)
	ip = kwars['ip']
	port = kwars['port']
	user = kwars['user']
	key = kwars['key'] 
	name = kwars['name']
	if len(serverDict) == 0:
		serverDict[1] = {'ip':ip, 'port':port , 'user':user , 'key':key, 'name':name}
	else:
		
		serverDict[len(serverDict) + 1] = {'ip':ip, 'port':port , 'user':user , 'key':key, 'name':name}
#		print(serverDict)
	with open('server.json','w') as json_data:
		json.dump(serverDict,json_data,indent = 4)	
	print('server added..'.upper())
	input('press enter to go back ...')



########################
########################

def fun_addNewGroup():
	fun_makeMenu('adding new Group')
	group_name = input('{:<25}{:^3}'.format(' - New Group Name ',':'))
	if  group_name:
		fun_addToGroup(group_name)		
	else:
		fun_addNewGroup()

########################
########################
def fun_addToGroup(name):
	if name not in groupDict:
			groupDict[name] = {}
			print('  Added group: '+name)
			input()
	else:
		print (groupDict)
		print('ERROR! Group' +name +' Already Exist.')
		input()
########################
########################
def fun_delExistingGroup():
	fun_makeMenu('delete Existing Group')
	
	servers = groupDict.keys()
	msg = 'LIST OF Groups'
	print (' '+ msg)
	print (' '+'-' *len(msg))
	for i in servers:
		print (' '+ i)
	print ('')
	del_grp = input(' ' +'Enter the group name that should be deleted: ')
	if del_grp in groupDict:
		del groupDict[del_grp]
		print ('deleted group  :'+ del_grp)
		input()
	else:
	  print ('group does not exist')
	  input ()
	
######################
######################
def fun_addservertoGroup():
	fun_makeMenu('''Adding Server's to group''')
	print ('')
	print ('')
	msg = 'list of groups'
	print (' ' + msg.upper())
	print (' ' + '-'*len(msg))
	print ('')
	groups = groupDict.keys()
	n = 1
	for i in groups:
		print (str(n) +' :  '+ i)
		n += 1
		print ('')
	group = input('Select the group by name : ')
	if group in groupDict:
		heading = ' Group : ' + group.upper()
		fun_makeMenu(heading)
		with open('server.json','r') as json_data:
			serverDict = json.load(json_data)
			for key in sorted(serverDict.keys()):
				print('  {:<4}{:<15} {}'.format(key,serverDict[key]['ip'],serverDict[key]['name']))
				print ('')
			server = input('Select the server by id [q :QUIT] : ')
			if server == 'q':
				pass
			elif server  in serverDict:
				groupDict[group][server] = serverDict[server]['name']
				print ('Added server ' + groupDict[group][server] + ' to group' + group )
				input()		
			else:
				input('Error! server not listed ...')
					
						
		
	else:
		opt = input('group not listed..[q:go back]')
		if opt == 'q':
			pass
		else:
			fun_addservertoGroup()
		
	

######################
######################
def fun_deletefomGroup():
	fun_makeMenu('''Deleting Server's from group''')
	print ('')
	print ('')
	msg = 'list of groups'
	print (' ' + msg.upper())
	print (' ' + '-'*len(msg))
	print ('')
	groups = groupDict.keys()
	n = 1
	for i in groups:
		print (str(n) +' :  '+ i)
		n += 1
		print ('')
	group = input('Select the group by name : ')
	if group in groupDict:
		heading = ' Group : ' + group.upper()
		fun_makeMenu(heading)
		if len(groupDict[group]) == 0:
			input(' There is no server listed in this group..')
		else:
			for key in sorted(groupDict[group].keys()):
				print('  {:<4}{:<15}'.format(key,groupDict[group][key]))
				print('')
			serverkey = input('Enter id of the server that is to be deleted  [q:QUIT] : ')
			if serverkey == 'q':
				pass
			elif serverkey in groupDict[group]:
				mesg = print(' Server ' + groupDict[group][serverkey] +' removed from group :' + group)
				del groupDict[group][serverkey]
				input()
		
	else:
		opt = input('group not listed..[q:go back]')
		if opt == 'q':
			pass
		else:
			fun_deletefromGroup()
	
	

######################
######################
def fun_listGroups():
	fun_makeMenu('LIST OF groups')
	n =1
	servers = groupDict.keys()

	for i in servers:
		print (str(n) +': '' '+ i)
		n += 1
	print ('')
	input('press enter to go back')

######################
######################
def func_quickServerAccess():
	fun_makeMenu('QUICK server access')
	with open('server.json','r') as json_data:
		serverDict = json.load(json_data)
	for key in sorted(serverDict.keys()):
		print('  {:<4}{:<15} {}'.format(key,serverDict[key]['ip'],serverDict[key]['name']))
	choice = input(" Select Server Id ['q' quit] : ")
	if choice == 'q':
		pass
	elif choice in serverDict:
#3		choice = int(choice)
		connect_server = 'ssh '+serverDict[choice]['user']+'@'+serverDict[choice]['ip']+' -p '+serverDict[choice]['port']
		subprocess.call(connect_server,shell=True)
#		print (serverDict[choice])
	else:
		func_quickServerAccess()

#######################
#######################

def func_parallelExecution():
	with open('server.json','r') as json_data:
		serverDict = json.load(json_data)
	fun_makeMenu('Parallel Shell')
	print('')
	msg = ('Select the group on which command should be executed')
	print (' ' +msg)
	print (' ' + '-'*len(msg))
	servers = groupDict.keys()
	n = 1
	for i in servers:
		print (str(n) +' : ''Group: '+ i)
		n += 1
	print (str(n) + ' : All servers')
	option = input('Select group by name [A:All servers] ')
	if option == 'a' or option == 'A':
		func_parallelshellAll(option)
	elif option in groupDict:
		func_parallelshellgroup(option)
	else:
		func_parallelExecution()
#######################
#######################

def func_parallelshellAll(key):
	with open('server.json','r') as json_data:
		serverDict = json.load(json_data)
	fun_makeMenu('Parallel Shell - All servers')
	command = input('Enter the command to run on all servers : ')
	for key in sorted(serverDict.keys()):
		connect_server = 'ssh '+serverDict[key]['user']+'@'+serverDict[key]['ip']+' -p '+serverDict[key]['port']
		ssh_command = connect_server + " '"+ command +" ' "
		print('')
		print('Output from server : '+serverDict[key]['name'])
		subprocess.call(ssh_command,shell=True)
		print('')
	test = input("Press  'r' to run again..['q' quit] :")
	if test == 'q':
		pass
	elif test == 'r':
		func_parallelshellAll()
	
		
#######################
#######################
		
def func_parallelshellgroup(option):
	with open('server.json','r') as json_data:
		serverDict = json.load(json_data)
	group = groupDict[option]
	fun_makeMenu('Parallel Shell on group ' + option.upper())
	command = input('Enter the command to run on all servers : ')
	for key in group.keys():				
		connect_server = 'ssh '+serverDict[key]['user']+'@'+serverDict[key]['ip']+' -p '+serverDict[key]['port']
		ssh_command = connect_server + " '"+ command +" ' "
		print('')				
		print('Output from server : '+serverDict[key]['name'])
		subprocess.call(ssh_command,shell=True)
		print('')
	test = input("Press  'r' to run again..['q' quit] :")
	if test == 'q':		
		pass
	else:
		func_parallelshellgroup(option)
#	elif test == 'r':
#		func_parallelshellgroup(option)
					
########################
########################

