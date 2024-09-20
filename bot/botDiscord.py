import discord
from discord.ext import commands
from cogs.scheduleCog import HyperplaningCog
from cogs.alarmCog import AlarmHyperplaningCog
import envVar

class BotHyperPlaning(commands.Bot):
    def __init__(self) -> None:
        super().__init__(command_prefix='!', intents=discord.Intents.all())

    async def setup_hook(self) -> None:
        await self.add_cog(AlarmHyperplaningCog(self, envVar.CHANNEL_ID))
        await self.add_cog(HyperplaningCog(self))
        await self.tree.sync()

    async def on_ready(self) -> None:
        print("Ready")
