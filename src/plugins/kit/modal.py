from math import e
import discord
from discord.ext import commands
from discord import ui


class Modal(discord.ui.Modal):
    name = ui.TextInput(label='Name', placeholder='Enter your name here...', min_length=3, max_length=20)
    
    
    async def on_submit(self, interaction: discord.Interaction, /):
        ...


class Questionnaire(ui.Modal, title='Questionnaire Response'):
    name = ui.TextInput(label='Name')
    answer = ui.TextInput(label='Answer', style=discord.TextStyle.paragraph)
    
    example = ui.TextInput(
        label="Example",
        style=discord.TextStyle.paragraph,
        placeholder="This is a placeholder!",
        default="This is a default value!",
        min_length=5,
        max_length=100,
    )

    async def on_submit(self, interaction: discord.Interaction, /):
        await interaction.response.send_message(
            f'Thanks for your response, {self.name}!',
            ephemeral=True
        )
        
        embed_to_send = discord.Embed(
            title=":white_check_mark: Response Received!",
            description=f"**{interaction.user.name}** has responded to the questionnaire with the following answer:\n\n{self.answer}",
            color=discord.Color.green()
        )
        
        
        
        
        await interaction.guild.owner.send(
            embed=embed_to_send
        )
        
    async def on_timeout(self, interaction: discord.Interaction, /):
        timeout_embed = discord.Embed(
            title=":x: You took too long to respond!",
            color=discord.Color.red()
        )
        
        return await interaction.response.send_message(
            embed=timeout_embed,
            ephemeral=True
        )
        
    async def on_timeout(self, interaction: discord.Interaction, /):
        timeout_embed = discord.Embed(
            title=":x: You took too long to respond!",
            color=discord.Color.red()
        )
        
        return await interaction.response.send_message(
            embed=timeout_embed,
            ephemeral=True
        )
        
    async def on_timeout(self, interaction: discord.Interaction, /):
        timeout_embed = discord.Embed(
            title=":x: You took too long to respond!",
            color=discord.Color.red()
        )
        
        return await interaction.response.send_message(
            embed=timeout_embed,
            ephemeral=True
        )
        




class ExampleModalCog(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot


    @discord.app_commands.command()
    async def example_modal(self, interaction : discord.Interaction):
        return await interaction.response.send_modal(Questionnaire())

async def setup(bot : commands.Bot):
    await bot.add_cog(ExampleModalCog(bot))
