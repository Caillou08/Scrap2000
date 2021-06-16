import discord
import os
from art import text2art
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix = "s!")
bot.remove_command("help")

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_ready():
    print(text2art("Scrap2000")+"Bot connecté à l'API de discord ! ")
    game = discord.Game("préfix = zebi!")
    await bot.change_presence(status=discord.Status.idle, activity=game)

bot.run(TOKEN)