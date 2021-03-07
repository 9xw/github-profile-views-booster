import requests
import os
import ctypes
from colorama import Fore

user = "https://camo.githubusercontent.com/fdbe1e325404dd821deec9e7ef776ab3e0cd7bbb448c7f1d87d0b6f4647e1b8b/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d707572656c787726636f6c6f723d6c6967687467726179" # put profile here
p = ("proxies.txt")
os.system("cls")
pfile = open(p, 'r')

ctypes.windll.kernel32.SetConsoleTitleW('github view booster by purelxw')
for txt in pfile:
	prox = {'http': txt}
	r = requests.get(user, headers={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Mobile Safari/537.36 Edg/88.0.705.63'}, proxies=prox)
	print(f" [{Fore.RED}>{Fore.RESET}] {Fore.GREEN} Profile viewed {Fore.RESET}")