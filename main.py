###################################################
# Please add new dependencies to requirements.txt #
###################################################
import os
from dotenv import load_dotenv
import discord
import logging
from datetime import date

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='T'+str(date.today())+'discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

load_dotenv()
__token__ = os.getenv('TOKEN', '')

intents = discord.Intents.default()
intents.members = True
intents.__setattr__('message_content', True)

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user.mentioned_in(message):
        await message.channel.send('Summ, summ, summ,\neine Erwänung von {0.mention}, ach wie dumm!'.format(message.author))

    if message.content.startswith('ping'):
         await message.channel.send('pong')

@client.event
async def on_raw_reaction_add(payload):
    channel = client.get_channel(payload.channel_id)

    if channel.name != 'regeln':
        return

    current_guild = next(x for x in client.guilds if x.id == payload.guild_id)
    csciencedude_role = next(x for x in current_guild.roles if x.name == 'cScience Dude')
    member_already_has_role = next((x for x in payload.member.roles if x.id == csciencedude_role.id), None) is not None

    if not member_already_has_role:
        await payload.member.add_roles(csciencedude_role)

    return

@client.event
async def on_raw_reaction_remove(payload):
    channel = client.get_channel(payload.channel_id)

    if channel.name != 'regeln':
        return

    current_guild = next(x for x in client.guilds if x.id == payload.guild_id)
    member = current_guild.get_member(payload.user_id)
    csciencedude_role = next(x for x in current_guild.roles if x.name == 'csciencedude')
    member_already_has_role = next((x for x in member.roles if x.id == csciencedude_role.id), None) is not None

    if member_already_has_role:
        await member.remove_roles(csciencedude_role)

    return

client.run(__token__)
