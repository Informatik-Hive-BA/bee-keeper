import os
from dotenv import load_dotenv
import discord

load_dotenv()
__token__ = os.getenv('TOKEN', '')

intents = discord.Intents.default()
intents.__setattr__('message_content', True)

client = discord.Client(intents=intents)

client.run(__token__)