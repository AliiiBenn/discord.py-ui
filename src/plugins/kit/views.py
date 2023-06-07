import discord
from discord.ext import commands


class ExampleView(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)

        # print(self.children)

        # self.add_item(discord.ui.Button(label="Example button", style=discord.ButtonStyle.blurple, emoji="👍"))
        # self.add_item(discord.ui.Button(label="Second Example button", style=discord.ButtonStyle.blurple, emoji="👍"))
        # self.remove_item(self.children[0])
        
        
    @discord.ui.button(label="Example button 0", style=discord.ButtonStyle.blurple, emoji="👍")
    async def example_button(self, interaction : discord.Interaction, button : discord.ui.Button) -> None:
        await interaction.response.send_message("Example button clicked", 
                                                ephemeral=True)
        
        button.label = f"Example button {int(button.label[-1]) + 1}"
        
        if int(button.label[-1]) == 5:
            self.stop()
            
        await interaction.message.edit(view=self)
        
        
    async def on_error(self, 
                       interaction : discord.Interaction,
                       error : Exception,
                       item : discord.ui.Item) -> None:
        print("Error in view")
        raise error
        



class ExampleViewCog(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot


    @commands.hybrid_command(name="example_view", description="Example view command")
    async def example_view(self, ctx : commands.Context):
        message = await ctx.send("Example view command")
        view = ExampleView.from_message(message)

        print(view)

        await message.edit(view=view)


    @commands.hybrid_command(name="second_example_view", description="Second example view command")
    async def second_example_view(self, ctx : commands.Context):
        message = await ctx.send("Second example view command", view=ExampleView())
        



async def setup(bot : commands.Bot):
    await bot.add_cog(ExampleViewCog(bot))