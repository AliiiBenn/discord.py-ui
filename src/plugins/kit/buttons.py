import discord
from discord.ext import commands

import random


class ExampleButton(discord.ui.Button):
    def __init__(self):
        super().__init__(style=discord.ButtonStyle.blurple, label="Example button", emoji="👍") # Create a button using constructor


    async def callback(self, interaction : discord.Interaction):
        self.label = "Example button (clicked)" # Change the label of the button
        self.style = random.choice(list(discord.ButtonStyle)) # Change the style of the button

        await interaction.response.edit_message(view=self.view) # Update the message with the new button



class SecondExampleView(discord.ui.View):
    def __init__(self):
        super().__init__()

        self.add_item(ExampleButton()) # Add the button to the view

        # for i in range(24): # Add 24 buttons to the view
        #     self.add_item(ExampleButton()) 



class ExampleView(discord.ui.View):
    @discord.ui.button(label="Example button", style=discord.ButtonStyle.blurple, emoji="👍") # Create a button using decorator
    async def example_button(self, interaction : discord.Interaction, button : discord.ui.Button):

        button.label = "Example button (clicked)" # Change the label of the button
        button.style = random.choice(list(discord.ButtonStyle)) # Change the style of the button

        await interaction.response.edit_message(view=self) # Update the message with the new button


class ButtonCog(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot


    @commands.hybrid_command(name="example_button", description="Example button command")
    async def example_button(self, ctx : commands.Context):
        await ctx.send("Example button command", view=ExampleView()) 

    @commands.hybrid_command(name="second_example_button", description="Second example button command")
    async def second_example_button(self, ctx : commands.Context):
        await ctx.send("Second example button command", view=SecondExampleView())




async def setup(bot : commands.Bot):
    await bot.add_cog(ButtonCog(bot))