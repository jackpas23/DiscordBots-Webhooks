# bot.py
import os
import discord
from dotenv import load_dotenv
import random

load_dotenv()
TOKEN = os.getenv('TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
intents = discord.Intents.default()
intents.members = True 
intents.message_content = True
intents.messages = True
client = discord.Client(intents=intents)


@client.event
##triggers event
async def on_ready():
    
    print(f'{client.user.name} has connected to Discord!')


    
@client.event
async def on_member_join(member):
    await member.create.dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcomet to the server'
    )
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    brooklyn_99_quotes = [
            'I\'m the human form of the 💯 emoji.',
            'Bingpot!',
            (
                'Cool. Cool cool cool cool cool cool cool, '
                'no doubt no doubt no doubt no doubt.'
            ),
    ]
    if message.content == '99!':
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException
@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log','a') as f:
        if event =='on_message':
            f.write(f'Unhandeled message: {args[0]}\n')
        else:
            raise
client.run(TOKEN)
