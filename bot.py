import discord
from discord.ext import commands
from discord import app_commands
import json

with open('config.json') as f:
    d = json.load(f)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Logged in as {bot.user}")

@bot.tree.command(name="first_slash")
async def first_slash(interaction: discord.Interaction):
    await interaction.response.send_message("You executed the slash command!")


#cmd = bot.tree.get_command("first_slash")
#bot.tree.remove_command(cmd.name)

bot.run(d['token'])
