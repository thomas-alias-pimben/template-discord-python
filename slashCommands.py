import discord
from discord.ext import commands

def setupCommand(bot):
    @bot.tree.command(name="first_slash", description="the first_slash")
    async def first_slash(interaction: discord.Interaction):
        await interaction.response.send_message("You executed the slash command!")

    @bot.tree.command(name="second_slash", description="the second_slash")
    async def second_slash(interaction: discord.Interaction):
        await interaction.response.send_message("You executed the second slash command!")
    
    

    print("command loaded")

