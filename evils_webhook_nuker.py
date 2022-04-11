import requests
from discord import Webhook, RequestsWebhookAdapter
import colorama
from colorama import init, Fore
import threading
import os

clear = lambda: os.system('cls') if os.name == 'nt' else os.system('clear')
colorama.init()
input("PUSH ENTER TO CONTINUE")
print(f"""

                       {Fore.MAGENTA} ╦ ╦╔═╗╔╗ ╦ ╦╔═╗╔═╗╦╔═  {Fore.WHITE}╔═╗╔═╗╔═╗╔╦╗╔╦╗╔═╗╦═╗
                       {Fore.MAGENTA} ║║║║╣ ╠╩╗╠═╣║ ║║ ║╠╩╗  {Fore.WHITE}╚═╗╠═╝╠═╣║║║║║║║╣ ╠╦╝
                       {Fore.MAGENTA} ╚╩╝╚═╝╚═╝╩ ╩╚═╝╚═╝╩ ╩  {Fore.WHITE}╚═╝╩  ╩ ╩╩ ╩╩ ╩╚═╝╩╚═

                                            {Fore.MAGENTA}[ 1 ] {Fore.WHITE}Start{Fore.RESET}
                                                                """)
bruh = input(f"[ SELECT ] ")
if bruh == '1': 
  os.system('cls')
  url = input(f"{Fore.RED}[{Fore.LIGHTBLACK_EX} Webhook Url {Fore.RED}]{Fore.RESET} ")
  os.system('cls')
  message = input(f"{Fore.RED}[{Fore.LIGHTBLACK_EX} Message {Fore.RED}]{Fore.RESET} ")
  os.system('cls')
  while True: 
   webhook = Webhook.from_url(f"{url}", adapter=RequestsWebhookAdapter())
   webhook.send(f"{message}")
   print(f"{Fore.RED}[{Fore.GREEN} Sent {message} {Fore.RED}]{Fore.RESET}")