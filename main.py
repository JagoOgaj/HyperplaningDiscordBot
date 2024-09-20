import discord
from discord.ext import commands
from discord import Intents
from typing import Optional
from driver.driver import Driver
import constants

# Configuration du bot
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

driver = Driver(
    constants.EXECUTABLE_PATH, constants.URL_HYPERPLANNING, constants.ELEMENT_TO_FOCUS, constants.INPUT
)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower() == "test":
        await message.channel.send(f"{message.content}")
        print("Message envoyé")

    await bot.process_commands(message)

@bot.command()
async def test(ctx):
    await ctx.send("Le bot fonctionne correctement!")

@bot.command()
async def getSchedule(ctx):
    try:
        driver.runDriver()
        with open('screenshot.png', 'rb') as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
    except Exception as e:
        print(e)
        await ctx.send(embed=discord.Embed(
            title="Error",
            description=f"Une erreur est survenue \n {e}",
            color=discord.Color.red()
        ))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(
            title="Error",
            description="Cette commande n'existe pas.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

# Lancer le bot
bot.run(constants.BOT_TOKEN)