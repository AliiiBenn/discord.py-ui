from typing import Optional
import discord
from discord.ext import commands
from discord import ui


class ExampleSelect(ui.Select):
    def __init__(self) -> None:
        options = [
            discord.SelectOption(
                label="Option 1",
                description="This is the first option!",
                emoji="🍎",
                default=True
            ),
            discord.SelectOption(
                label="Option 2",
                description="This is the second option!",
                emoji="🍊",
            ),
            discord.SelectOption(
                label="Option 3",
                description="This is the third option!",
                emoji="🍇",
            ),
            discord.SelectOption(
                label="Option 4",
                description="This is the fourth option!",
                emoji="🍉",
            ),
            discord.SelectOption(
                label="Option 5",
                description="This is the fifth option!",
                emoji="🍌",
            ),
        ]
        
        super().__init__(
            placeholder="This is a placeholder!",
            min_values=1,
            max_values=2,
            options=options
        )
        
    async def callback(self, interaction: discord.Interaction):
        return await interaction.response.send_message(f"You selected {self.values}!")
    
    
class RoleSelect(ui.RoleSelect):
    def __init__(self) -> None:
        super().__init__()


        
class ProgrammingLanguageSelect(ui.Select):
    def __init__(self) -> None:
        options = [
            discord.SelectOption(
                label="Python",
                value="The best programming language!",
            ),
            discord.SelectOption(
                label="JavaScript",
                value="The worst programming language!",
            ),
            discord.SelectOption(
                label="C++",
                value="The most confusing programming language!",
            )
        ]
        
        super().__init__(
            placeholder="Select your favorite programming language!",
            min_values=1,
            max_values=1,
            options=options
        )
        
        
    async def callback(self, interaction: discord.Interaction):
        return await interaction.response.send_message(f"You selected {''.join(self.values)}!")




class ExampleView(ui.View):
    def __init__(self, *, timeout: float | None = 180):
        super().__init__(timeout=timeout)
        
        # self.add_item(ExampleSelect())
        # self.add_item(RoleSelect())
        # self.add_item(ui.ChannelSelect())
        # self.add_item(ui.MentionableSelect())
        # self.add_item(ui.UserSelect())
        
        self.add_item(ProgrammingLanguageSelect())
        
        


class SelectCog(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot
        
    
    @commands.hybrid_command()
    async def example_select(self, ctx : commands.Context) -> discord.Message:
        return await ctx.send(view=ExampleView())
    
    
async def setup(bot : commands.Bot):
    await bot.add_cog(SelectCog(bot))