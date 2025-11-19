#RESHETKA

import os
import requests
import colorama
from colorama import Fore, Style
import platform

colorama.init()


logo = f"""
{Fore.WHITE}╭╮╱╱╭━━┳╮╭━┳━━━┳━╮╱╭┳━━━┳━━━╮
{Fore.WHITE}┃┃╱╱╰┫┣┫┃┃╭┫╭━╮┃┃╰╮┃┃╭━╮┃╭━╮┃
{Fore.WHITE}┃┃╱╱╱┃┃┃╰╯╯┃╰━━┫╭╮╰╯┃┃╱┃┃╰━━╮
{Fore.CYAN}┃┃╱╭╮┃┃┃╭╮┃╰━━╮┃┃╰╮┃┃┃╱┃┣━━╮┃
{Fore.CYAN}┃╰━╯┣┫┣┫┃┃╰┫╰━╯┃┃╱┃┃┃╰━╯┃╰━╯┃
{Fore.CYAN}╰━━━┻━━┻╯╰━┻━━━┻╯╱╰━┻━━━┻━━━╯
"""


if platform.system() == "Windows": 
    os.system("title [+] LIKROOT")
    st = "python LIKROOT.py"
    dl = "cls"
    os.system("cls")
else:
    dl = "clear"
    st = "python3 LIKROOT.py"
    os.system("clear")



menu = """

----------------
= [1] Snosers  =
= [2] Выход    =
----------------

"""

print(Style.BRIGHT + logo)
print("")
print (Fore.CYAN + "[=] Developer: RESHETKA")
print (Fore.GREEN + "[=] Admin: Зимний_SBX❄")
print(Fore.YELLOW + menu)

us = input("[=] Выбирай>")

if us == "1":
    from scripts import snosv2

if us == "2":
    exit()


else:
    os.system(dl)
    os.system(st)

exit()
