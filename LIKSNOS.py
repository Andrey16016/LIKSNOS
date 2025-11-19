#RESHETKA

import os
import requests
import colorama
from colorama import Fore, Style
import platform
import time

colorama.init()


logo = f"""
  ╭╮╱╱╭━━┳╮╭━┳━━━┳━╮╱╭┳━━━┳━━━╮
  ┃┃╱╱╰┫┣┫┃┃╭┫╭━╮┃┃╰╮┃┃╭━╮┃╭━╮┃
  ┃┃╱╱╱┃┃┃╰╯╯┃╰━━┫╭╮╰╯┃┃╱┃┃╰━━╮
  ┃┃╱╭╮┃┃┃╭╮┃╰━━╮┃┃╰╮┃┃┃╱┃┣━━╮┃
  ┃╰━╯┣┫┣┫┃┃╰┫╰━╯┃┃╱┃┃┃╰━╯┃╰━╯┃
  ╰━━━┻━━┻╯╰━┻━━━┻╯╱╰━┻━━━┻━━━╯
"""


if platform.system() == "Windows": 
    os.system("title [+] LIKROOT")
    st = "python LIKSNOS.py"
    dl = "cls"
    os.system("cls")
else:
    dl = "clear"
    st = "python3 LIKSNOS.py"
    os.system("clear")



menu = """

  ----------------
  = [1] Snosers  =
  = [2] Выход    =
  = [3] Обновить =
  ----------------

"""

update = f"""

КОМАНДЫ ДЛЯ ОБНОВЛЕНИЯ LIKROOT

Для Linux:
Скопируйте и вставьте эту команду:

{Fore.BLUE}cd && rm -rf LIKSNOS && git clone https://github.com/Andrey16016/LIKSNOS && cd LIKSNOS && python3 LIKSNOS.py

{Fore.YELLOW}Для Windows:
Просто переустановите софт.

https://github.com/Andrey16016/LIKSNOS

"""
for i in logo:
    time.sleep(0.01)
    print(Style.BRIGHT + i, end='', flush=True)

    
    
    
os.system(dl)
print(Fore.BLUE + logo)
print("")
print (Fore.CYAN + "[=] Developer: RESHETKA")
print (Fore.GREEN + "[=] Admins: Зимний_SBX❄")
print (Fore.YELLOW + "[=] Admins: ZIMKA_SBX")
print(Fore.YELLOW + menu)

us = input("[=] Выбирай>")

if us == "1":
    from scripts import snosv2


if us == "3":
    print (update)
    input("Нажмите Enter")
    os.system(dl)
    os.system(st)
    
else:
    exit()

exit()
