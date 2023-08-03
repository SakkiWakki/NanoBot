from dotenv import load_dotenv
import os

# bot.py
import discord
import logging


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
logging.basicConfig(level=logging.INFO)


intents = discord.Intents.default()
intents.message_content = True
bot = discord.Bot(intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('727'):
        await message.channel.send('WYSI!')

bot.load_extension('commands.auth')

bot.run(TOKEN)
