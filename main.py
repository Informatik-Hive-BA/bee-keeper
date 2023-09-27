import os
from dotenv import load_dotenv
import discord

load_dotenv()
__token__ = os.getenv('TOKEN', '')

intents = discord.Intents.default()
intents.message_content = True

client.run(__token__)