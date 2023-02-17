from dotenv import load_dotenv
from pyHoneygain import HoneyGain
from discord_webhook import DiscordWebhook, DiscordEmbed
from os.path import join, dirname
import os

load_dotenv(verbose=True)
load_dotenv(join(dirname(__file__), ".env"))
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")
WEBHOOK = os.environ.get("WEBHOOK")

if EMAIL == "" or PASSWORD == "":
    print("Email or Password not found")
    exit(1)

user = HoneyGain()
user.login(EMAIL, PASSWORD)

if user.actions_accept_honeypot():
    result = user.open_honeypot()
    if not result["success"]:
        print("ERROR")
        exit(1)
    print(result)
    if WEBHOOK != "":
        webhook = DiscordWebhook(url=WEBHOOK)
        embed = DiscordEmbed(title="Open HoneyPot", description=f"{result['credits']} Credits", color="a8f79a")
        webhook.add_embed(embed)
        webhook.execute()
