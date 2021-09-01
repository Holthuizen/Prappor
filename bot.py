#commands
#pipenv install discord.py
#pipenv install 
#pipenv run bot.py
import os
import discord
from discord.ext import commands
import random

PREFIX = ">"
DESCRIPTION = "A Tarkov Assistant"
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=PREFIX, intents=intents, description=DESCRIPTION)

def is_me(m):
    return m.author == client.user


@client.event
async def on_ready():
    print('Logged on as', client.user)


@client.event
async def on_member_join(member):
    await member.send("Hello, soldier. What are you interested in? Cash? Goods? Ah, you want a Bot... Sure, I'll give you one. Use ? followed by a help to see all commands")


@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send("Missing a required Argument. command is incomplete")

    if isinstance(error,commands.CommandNotFound):
        #await ctx.send(f"Command not found, use {PREFIX}help, for more information")
        print(error)
    print(error) #make a logging function in the future. 

@client.command()
async def ping(ctx):
    """Check responce time"""
    await ctx.send(f'Pong {round(client.latency * 1000)}ms!')


@client.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined in {member.joined_at}')


@client.command()
async def clear(ctx,amount=10):
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
    """Use gunsmith / part followed by a nr Get info per Gunsmith task"""
    await ctx.send(f"Gunsmith part {str(number)}")
    try:
        _file = discord.File(f"./Media/Gunsmith/Part{str(number)}.png")
        await ctx.send(file=_file)
    except:
        await ctx.send("File not found")




@client.command(aliases=["Ammo","cal"])
async def ammo(ctx,bullet="default"):
    """Use ammo/cal followed by a calibar, to get a table of this calibar"""
    if not bullet == "default": 
        destdir = "./Media/Bullets"
        files = [ f for f in os.listdir(destdir) if os.path.isfile(os.path.join(destdir,f)) ]
        for file in files: 
            if bullet in file: 
                await ctx.send(file=discord.File(f'./Media/Bullets/{file}'))
                return 
    await ctx.send(file=discord.File('./Media/Ammo/ammo.png'))    
    await ctx.send("command: Ammo <caliber>")    


@client.command(aliases=['coin-flip', 'coin', 'flip'])
async def head_or_tails(ctx):
    options = ["heads","tails"]
    await ctx.send(random.choice(options))




#token must be in a separate file that doesn't get pushed to git
token = ""

with open('key.txt', 'r') as reader:
    #Read & print the token
    token += reader.read()
    print(token)
client.run(token)











