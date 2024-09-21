import discord
from discord.ext import commands
from DriverService.driverService import DriverObj
import envVar
from utils.service import generate_and_send_image
from error.exceptionsCustom import ImageNotFoundError
from datetime import datetime, timedelta


class HyperplaningCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self._bot: commands.Bot = bot
        self._driver: DriverObj[str] = DriverObj(
            envVar.EXECUTABLE_PATH, envVar.URL_HYPERPLANNING, envVar.ELEMENT_TO_FOCUS, envVar.INPUT
        )

    @commands.command(name="test")
    async def test_command(self, ctx: commands.Context) -> None:
        return await ctx.send("test")

    @commands.command(name="getSchedule")
    async def slashCommand(self, ctx: commands.Context):
        try:
            channel = ctx.channel
            today = datetime.now()
            days_since_monday = today.weekday()
            date_debut = today - timedelta(days=days_since_monday)
            date_fin = date_debut + timedelta(days=4)
            dates: list = [date_debut.strftime(
                "%d %B %Y"), date_fin.strftime("%d %B %Y")]
            await generate_and_send_image(self._driver, channel, dates)
        except ImageNotFoundError as e:
            embed = discord.Embed(
                title="Erreur",
                description=f"L'image de l'emploi du temps n'a pas pu être trouvée : {
                    e}",
                color=discord.Color.red()
            )
            await channel.send(embed=embed)

        except Exception as e:
            embed = discord.Embed(
                title="Erreur inconnue",
                description=f"Une erreur inattendue est survenue : {e}",
                color=discord.Color.red()
            )
            await channel.send(embed=embed)
