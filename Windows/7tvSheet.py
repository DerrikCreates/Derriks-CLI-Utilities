import sys
import json
import getopt
import requests
from termcolor import colored, cprint


def main(argv):

    opts, args = getopt.getopt(
        argv, "", ["help", "id="])  # help= for input

    twitchId = ""
    accountLink = ""
    for opt, arg in opts:
        if opt in ("--help"):
            cprint("--path provide a webp path or url", "green")
            cprint("--id twitch account id", "green")
        if opt in ("--id"):
            twitchId = str(arg)
            if twitchId == "":
                cprint("No twitch id provided", "red")
                quit()
            accountLink = f"https://7tv.io/v3/users/twitch/{twitchId}"

    action(accountLink)


def action(accountLink):
    cprint(accountLink, "red")

    response = requests.get(accountLink)
    data = response.json()

    for emote in data["emote_set"]["emotes"]:
        cprint(emote["name"],"red")
    



if __name__ == "__main__":
    main(sys.argv[1:])
