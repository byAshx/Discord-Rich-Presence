import os
import rpc
import time
import colorama
from time import mktime
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

print(Fore.BLUE +  Style.BRIGHT + r""" 
______  _                            _  ______  _        _      ______                                        
|  _  \(_)                          | | | ___ \(_)      | |     | ___ \                                       
| | | | _  ___   ___  ___   _ __  __| | | |_/ / _   ___ | |__   | |_/ /_ __  ___  ___   ___  _ __    ___  ___ 
| | | || |/ __| / __|/ _ \ | '__|/ _` | |    / | | / __|| '_ \  |  __/| '__|/ _ \/ __| / _ \| '_ \  / __|/ _ \
| |/ / | |\__ \| (__| (_) || |  | (_| | | |\ \ | || (__ | | | | | |   | |  |  __/\__ \|  __/| | | || (__|  __/
|___/  |_||___/ \___|\___/ |_|   \__,_| \_| \_||_| \___||_| |_| \_|   |_|   \___||___/ \___||_| |_| \___|\___| v1.1
""")


time.sleep(.5)
print(Fore.BLUE +  Style.BRIGHT + "Made by byAsh#0999")
client_id = ''  # Client ID from Discord Dev portal.


        # details - first line
        # state - second line
        # small image - small round icon - MUST MATCH ASSET NAME ON DISCORD DEV PORTAL - if you dont want an icon, type in anything random
        # large image - large icon - MUST MATCH ASSET NAME ON DISCORD DEV PORTAL - if you dont want an icon, type in anything random
        ### MUST HAVE A LARGE OR SMALL ICON OTHERWISE IT WILL NOT CONNECT SUCCESSFULLY ###


time.sleep(3)
usrDetails = input(Fore.MAGENTA +  Style.BRIGHT + "What would you like the first line of Rich Presence to say? (CAN'T BE BLANK)\n" + Fore.WHITE +  Style.BRIGHT)
usrState = input(Fore.CYAN +  Style.BRIGHT + "What would you like the second line of Rich Presence to say? (CAN'T BE BLANK)\n" + Fore.WHITE +  Style.BRIGHT)
usrSmallImg = input(Fore.MAGENTA +  Style.BRIGHT + "Enter the small icon filename you uploaded to discord dev portal:\n" + Fore.WHITE +  Style.BRIGHT)
usrLargeImg = input(Fore.CYAN +  Style.BRIGHT + "Enter the large icon filename you uploaded to discord dev portal?\n" + Fore.WHITE +  Style.BRIGHT)
usrSmallTxt = input(Fore.MAGENTA +  Style.BRIGHT + "What would you like the small icon to say when hovered over? (CAN'T BE BLANK)\n" + Fore.WHITE +  Style.BRIGHT)
usrLargeTxt = input(Fore.CYAN +  Style.BRIGHT + "What would you like the large icon to say when hovered over? (CAN'T BE BLANK)\n" + Fore.WHITE +  Style.BRIGHT)


clear = lambda: os.system('cls') # Windows System
# os.system('clear') # Linux System
clear()

time.sleep(1)

print(Fore.BLUE +  Style.BRIGHT + r"""
______  _                            _  ______  _        _      ______                                        
|  _  \(_)                          | | | ___ \(_)      | |     | ___ \                                       
| | | | _  ___   ___  ___   _ __  __| | | |_/ / _   ___ | |__   | |_/ /_ __  ___  ___   ___  _ __    ___  ___ 
| | | || |/ __| / __|/ _ \ | '__|/ _` | |    / | | / __|| '_ \  |  __/| '__|/ _ \/ __| / _ \| '_ \  / __|/ _ \
| |/ / | |\__ \| (__| (_) || |  | (_| | | |\ \ | || (__ | | | | | |   | |  |  __/\__ \|  __/| | | || (__|  __/
|___/  |_||___/ \___|\___/ |_|   \__,_| \_| \_||_| \___||_| |_| \_|   |_|   \___||___/ \___||_| |_| \___|\___| v1.1
""")
print(Fore.BLUE +  Style.BRIGHT + "Made by byAsh#0999")

time.sleep(1)
start_time = mktime(time.localtime())
print(Fore.YELLOW + Style.BRIGHT + "Connecting to your local Discord...")
time.sleep(3)
while True:
    activity = {
            "state": usrState,  
            "details": usrDetails,  
            "timestamps": {
                "start": start_time
            },
            "assets": {
                "small_text": usrSmallTxt,  
                "small_image": usrSmallImg,  
                "large_text": usrLargeTxt,  
                "large_image": usrLargeImg  
            },
            "buttons": [
                {"label": "Developed by byAsh#0999", "url": "https://e-z.bio/root"}, # Button with URL
            ]
        }
    try:
        rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)
        print(Fore.GREEN + Style.BRIGHT + "Connection successful.")
        rpc_obj.set_activity(activity)
        time.sleep(900)
    except:
        print(Fore.RED + Style.BRIGHT +"Lost connection to Discord, trying again in 5 seconds.")
        time.sleep(5)