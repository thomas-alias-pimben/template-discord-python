import discord
import json


from slashCommands import *

#file who have bot token, guildId
with open('config.json') as f:
    d = json.load(f)



intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():

    #the guild ID
    guild = discord.Object(id=int(d['guildId']))

    #for command
    bot.tree.clear_commands(guild=guild)   
    bot.tree.copy_global_to(guild=guild)
    synced = await bot.tree.sync(guild=guild)

    print(f"Synced {len(synced)} commands")
    print(f"Logged in as {bot.user}")


setupCommand(bot)


#run the bot
bot.run(d['token'])
