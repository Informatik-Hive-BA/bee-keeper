import os
from dotenv import load_dotenv
import discord
import logging
from datetime import date

today = date.today()

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='T'+str(today)+'discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

load_dotenv()
__token__ = os.getenv('TOKEN', '')

intents = discord.Intents.default()
intents.__setattr__('message_content', True)

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

client.run(__token__)
