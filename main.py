import os
from typing import Final
from dotenv import load_dotenv
from discord.ext import commands
from discord import Intents
import discord
import random

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# Intents configuration and bot creation
intents = Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='r!', intents=intents, help_command=None)

## ============ Commands ============

@client.command(name='randomize')
async def randomize(ctx):
    messages = []
    async for message in ctx.channel.history(limit=100):
        messages.append(message)
    if messages:
        random_msg = random.choice(messages)
        await ctx.send(f'Juego elegido / Chosen game: {random_msg.content}')
    else:
        await ctx.send('No hay mensajes recientes para elegir / No recent messages to choose from')

## ============ Events ==============

# Event triggered when the bot is ready
@client.event
async def on_ready():
    print(f'{client.user.name} está listo! / {client.user.name} is ready!')
    await client.change_presence(activity=discord.Game(name=" r!randomize || https://github.com/Lostdou"))

# Run the bot
client.run(TOKEN)
