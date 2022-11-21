import requests
from requests.sessions import session
import os
import time
from colorama import Fore, Back, Style

session = requests.session()
count = 0
a = "TIKTOK REPORT LINK FROM DEVELOPER TOOLS"

while True:
    os.system('cls')
    count = count+1
    req = session.post(a)
    print(Fore.RED + req.text)
    print('\n')
    print(Fore.GREEN + 'Reported |' + str(count))
    time.sleep(10)

input()
