#commands
#pipenv install discord.py
#pipenv install 
#pipenv run bot.py

import discord
from discord.ext import commands

PREFIX = "?"
DESCRIPTION = "A Tarkov Assistant"
client = commands.Bot(command_prefix=PREFIX, description=DESCRIPTION)

def is_me(m):
    return m.author == client.user


@client.event
async def on_ready():
    print('Logged on as', client.user)


@client.event
async def on_member_join(member):
    await member.send(f"Hello, soldier. What are you interested in? Cash? Goods? Ah, you want a Bot... Sure, I'll give you a Bot. If you need me, use {PREFIX} followed by help")


@client.command()
async def ping(ctx):
    """Check responce time"""
    await ctx.send(f'Pong {round(client.latency * 1000)}ms!')


@client.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined in {member.joined_at}')


@client.command(category="Util")
async def clear_bot(ctx,amount=10):
    """Remove last 10 messages of this bot"""
    deleted = await ctx.channel.purge(limit=amount, check=is_me)
    await ctx.channel.send('Deleted {} message(s)'.format(len(deleted)))


@client.command()
async def clear_all(ctx):
    """Remove ALL messages"""
    deleted = await ctx.channel.purge()
    await ctx.channel.send('Deleted {} message(s)'.format(len(deleted)))   


@client.command(aliases=["Gunsmith", "part", "Part"])
async def gunsmith(ctx , number: int):
    """Get info per Gunsmith task"""

    await ctx.send(f"Gunsmith part {str(number)}")
    try:
        _file = discord.File(f"./Media/Gunsmith/Part{str(number)}.png")
        await ctx.send(file=_file)
    except:
        await ctx.send("File not found")

token = ""

with open('key.txt', 'r') as reader:
    # Read & print the entire file
    token += reader.read()
    print(token)
client.run(token)











