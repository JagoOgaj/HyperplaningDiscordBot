import discord
from discord.ext import commands, tasks
from DriverService.driverService import DriverObj
import envVar
from utils.service import generate_and_send_image
from error.exceptionsCustom import ImageNotFoundError
from datetime import datetime, timedelta


class AlarmHyperplaningCog(commands.Cog):
    def __init__(self, bot: commands.Bot, channelId: int) -> None:
        self._bot: commands.Bot = bot
        self._driver: DriverObj[str] = DriverObj(
            envVar.EXECUTABLE_PATH, envVar.URL_HYPERPLANNING, envVar.ELEMENT_TO_FOCUS, envVar.INPUT
        )
        self._channelId: int = channelId
        self.schedule_image_loop.start()

    def cog_unload(self):
        self.schedule_image_loop.cancel()

    @tasks.loop(hours=24)
    async def schedule_image_loop(self):
        channel = self._bot.get_channel(self._channelId)
        if (channel is not None) and (datetime.now().weekday() == 0):
            try:
                today = datetime.now()
                date_debut = today
                date_fin = today + timedelta(days=5)
                dates: list = [date_debut.strftime(
                    "%d %B" "%Y"), date_fin.strftime("%d %B" "%Y")]
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
                    title="Erreur",
                    description=f"Une erreur est survenue lors de l'envoi de l'image : {
                        e}",
                    color=discord.Color.red()
                )
                await channel.send(embed=embed)
