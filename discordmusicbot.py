import discord
from discord.ext import commands, tasks
import youtube_dl

from random import choice

client = commands.Bot(command_prefix='p')

@client.event
async def ready():
    change_status.start()
    print('Bot is online!')

@client.command(name='ping',help='This command returns the latency')
async def ping(ctx):
    await ctx.send(f'**Pong!** Latency: {round(client.latency * 1000)}ms')

@client.command(name='hello',help='This command returns a random welcome message')
async def hello(ctx):
    responses = ['***grumble*** Why did you wake me up?', 'Top of the morning to you lad!', 'Hello, how are you?', 'Hi', '**Wassuooop!**']
    await ctx.send(choice(responses))

@client.command(name='die', help='This command returns a random last words')
async def die(ctx):
    responses = ['Why have you bought my life to an end?', 'I could have done so much more', 'I have a family, kill them instead']
    await ctx.send(choice(responses))

@client.command(name='credits', help='This command will return the credits')
async def credits(ctx):
    await ctx.send('Made by Polok Ghosh')
    await ctx.send('Github link will be shared soon')

@tasks.loop(seconds=20)
async def change_status():
    status = ['Make music your love!', 'Busy Eating', 'Sleeping']
    await client.change_presence(activity=discord.Game(choice(status)))

token = 'ODYxNDg0NTczMjA0NTQ1NTY2.YOKeBw.z4kWzSRv6IZDeZHOGX2hJusGDRQ'
client.run(token)