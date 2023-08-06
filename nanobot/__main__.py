# Env
from dotenv import load_dotenv
import os

# Discord
import discord
from discord.ext import commands
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


@bot.command(name='reload', hidden=True, description="Reloads the bot")
@commands.is_owner()
async def reload_cog(ctx):
    bot.reload_extension('commands.auth')
    await ctx.respond('Cogs reloaded!', ephemeral=True)


@reload_cog.error
async def reload_cog_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.respond('You are not the Yuck.', ephemeral=True)

bot.load_extension('commands.auth')

bot.run(TOKEN)
