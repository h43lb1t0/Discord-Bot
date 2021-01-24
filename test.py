import discord
from discord.ext import commands, tasks
from secret import token3

import random
from itertools import  cycle

client = commands.Bot(command_prefix='.')
status = cycle(['Hiiiii','zweiiii'])

@client.event
async def on_ready():
    change_status.start()
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('I"m a Bot'))
    print('ready')


@client.event
async def on_member_join(member):
    print(f'{member} has joint')


@client.event
async def on_member_remove(member):
    print(f'{member} has left')

@client.command()
async def ping(ctx):
    await ctx.send(f'pong!!! {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    response = ['yes!', 'no!', 'idk', 'maybe']
    await ctx.send(f'Question: {question}\nAnsswer: {random.choice(response)}')

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)


@tasks.loop(seconds=10)
async def change_status():
    await  client.change_presence(activity=discord.Game(next(status)))

client.run(token3)