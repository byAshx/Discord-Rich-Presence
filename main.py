import rpc
import time
import colorama
from time import mktime
from colorama import Fore, Back, Style

colorama.init(autoreset=True)


print(Fore.GREEN + Style.BRIGHT + "Discord Rich Presence" + Fore.MAGENTA +  Style.BRIGHT + " -"+ Fore.BLUE +  Style.BRIGHT + " Made by byAsh#0999")
client_id = ''  # Your application's client ID as a string. (This isn't a real client ID)

time.sleep(1)
start_time = mktime(time.localtime())
print(Fore.MAGENTA + Style.BRIGHT + "Connecting to Discord...")
while True:
    activity = {
            "state": "state",  # anything you like
            "details": "details",  # anything you like
            "timestamps": {
                "start": start_time
            },
            "assets": {
                "small_text": "image",  # anything you like
                "small_image": "small-image-key",  # must match the image key
                "large_text": "image",  # anything you like
                "large_image": "large-image-key"  # must match the image key
            },
            "buttons": [
                {"label": "Socials", "url": "https://e-z.bio/root"},
            ]
        }
    try:
        rpc_obj = rpc.DiscordIpcClient.for_platform(client_id)  # Send the client ID to the rpc module
        print(Fore.GREEN + Style.BRIGHT + "Connection successful.")
        rpc_obj.set_activity(activity)
        time.sleep(900)
    except:
        print(Fore.RED + Style.BRIGHT +"Failed to set activity, trying again in 5 seconds")
        time.sleep(5)