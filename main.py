import os
from dotenv import load_dotenv
import discord
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

load_dotenv()
__token__ = os.getenv('TOKEN', '')

intents = discord.Intents.default()
intents.__setattr__('message_content', True)

client = discord.Client(intents=intents)

client.run(__token__)
