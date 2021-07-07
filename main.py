import discord
from discord.ext import commands

import os

#import all of the packages
from discord_musicbot import discord_musicbot

bot = commands.Bot(command_prefix='p')

#register the class with the bot
bot.add_cog(discord_musicbot(bot))

#start the bot with our token
bot.run("ODYxNDg0NTczMjA0NTQ1NTY2.YOKeBw.r_WzGH9VFKZM7t6uzjo6mQQuw-E")
