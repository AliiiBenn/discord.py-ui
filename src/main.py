import discord
from discord.ext import commands

import pkgutil, dotenv, os


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.all())

    async def setup_hook(self) -> None:
        await self.load_extension("plugins.kit.buttons")
        await self.load_extension("plugins.kit.views")
        await self.load_extension("plugins.kit.modal")
        await self.load_extension("plugins.kit.select")

        await self.tree.sync()

    async def on_ready(self):
        print(f"Logged in as {self.user.name} - {self.user.id}") 


bot = Bot()

if __name__ == "__main__":
    dotenv.load_dotenv()

    bot.run(os.getenv("TOKEN"))
