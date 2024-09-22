import discord
import asyncio
import envVar
from DriverService.driverService import DriverObj
from error.exceptionsCustom import ImageNotFoundError, DriverExecutionError


async def generate_and_send_image(driver: DriverObj, channel: discord.TextChannel, dates: list):
    try:
        await asyncio.to_thread(driver.runDriver)
        await channel.send(f"Le planning du {dates[0]} au {dates[1]}")
        with open(envVar.OUTPUT, 'rb') as f:
            picture = discord.File(f)
            await channel.send(file=picture)

    except FileNotFoundError:
        raise ImageNotFoundError(
            "L'image de l'emploi du temps n'a pas pu être trouvée.")

    except Exception as e:
        raise DriverExecutionError(
            f"Une erreur s'est produite lors de l'exécution du driver : {e}")
