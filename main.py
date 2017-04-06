#!/usr/bin/python3
#import subprocess
from function import *
import os.path


serverInfoDict = {}


########################################
# Function to create submenu  - Host management
########################################
def func_hostManagement():
    while True:
        fun_clearScreen()
        msg = 'host management menu'
        print('')        
        print('',msg.upper())
        print('','-' * len(msg))
        print('')
        
       
        print('',)
        print(' 1.Add New Host.')
        print(' 2.Delete Exisitng Host.')
        print(' 3.Change Host settings.')
        print(' 4.List all host')
        print(' 5.Quit.')
        print('')
        hm_option = input(' Select Option : ')
        if hm_option == '1':
            fun_addNewHost()
        elif hm_option == '2':
            fun_delExistingHost()
        elif hm_option == '3' or hm_option == '3':
            fun_changeSettings()
        elif hm_option == '4':
            fun_ListAllHost()
        elif hm_option == '5':
            break
        else:
            print('')
            input(' Invalid Option,Enter To continue.')
            
##########################################
# END - HostManagement
##########################################


##########################################
# START - GROUP Management
##########################################



def func_groupManagement():

	while True:
		fun_clearScreen()
		msg = 'Group management menu'
		print('')        
		print('',msg.upper())
		print('','-' * len(msg))
		print('')        
		print('',)
		print(' 1.Add New Group.')
		print(' 2.Delete Exisitng Group.')
		print(' 3.Add servers to group')
		print(' 4.Delete servers from group')
		print(' 5.List all Groups')
		print(' 6.Quit')
		print('')
		hm_option = int(input(' Select Option : '))
		if hm_option == 1:
			fun_addNewGroup()
		elif hm_option == 2:
			fun_delExistingGroup()
		elif hm_option == 3:
			fun_addservertoGroup()
		elif hm_option == 4:
			fun_deletefomGroup()			
		elif hm_option == 5:
			fun_listGroups()
		elif hm_option == 6:
			break
		else:
			print('')
			input(' Invalid Option,Enter To continue.')
            
##########################################
# END GROUP MANAGEMENT
##########################################
    




while True:
	fun_clearScreen()
	if os.path.exists("./server.json"):
		pass
	else:
		subprocess.call('touch server.json',shell=True)
		subprocess.call("echo '{}' > server.json",shell=True)
    
	print()
	msg = 'parallel command execution'
	print('',msg.upper())
	print('','-' * len(msg))
	print('')
	print(' 1.Host Managent.')
	print(' 2.Group Management.')
	print(' 3.Quick Server Access.')
	print(' 4.Parallel Execution.')
	print(' 5.Quit ')
	print('')
	OPTION = input(' Select Option : ')
    
	if OPTION == '1':
		func_hostManagement()
	elif OPTION == '2':
		func_groupManagement()
	elif OPTION == '3' or OPTION == '3':
		func_quickServerAccess()
	elif OPTION == '4':
		func_parallelExecution()
	elif OPTION == '5':
		break
	else:
		print('')
		input(' Invalid Option,Enter To continue.')     
        

