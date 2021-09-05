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

"""Custom help command"""
class CustomHelpCommand(commands.MinimalHelpCommand):
    def __init__(self) -> None:
        super().__init__()

    async def send_bot_help(self,mapping):
        #only show relevant commands
        commands = await self.filter_commands([ping,ammo,gunsmith,head_or_tails])
        #create an embed obj
        help_embed = discord.Embed(color=discord.Colour.green(), title="Help")
        help_embed.set_thumbnail(url='https://static.wikia.nocookie.net/escape-from-tarkov/images/1/17/Prapor_portrait.jpg/revision/latest?cb=20190905181528')
        for command in commands: 
            if command.description:
                help_embed.add_field(name=f"{command.name} {command.description}",value= f"Aliases: {command.aliases} \n {command.help}\n", inline=False)
            else: 
                help_embed.add_field(name=f"{command.name}",value= f"Aliases: {command.aliases} \n {command.help}\n", inline=False)


        await self.get_destination().send(embed=help_embed)


    async def send_command_help(self, command):
        help_embed = discord.Embed(color=discord.Colour.green(), title=f"{command.name} help")
        help_embed.set_thumbnail(url='https://static.wikia.nocookie.net/escape-from-tarkov/images/1/17/Prapor_portrait.jpg/revision/latest?cb=20190905181528')

        command.aliases.append(command.name)
        _names = ", ".join(command.aliases)
        help_embed.add_field(name=f"{_names}\n",value=f"{command.help}\n attributes: {command.description} ", inline=False)

        await self.get_destination().send(embed=help_embed)

client = commands.Bot(command_prefix=PREFIX, help_command=CustomHelpCommand(), intents=intents, description=DESCRIPTION)



def is_me(m):
    return m.author == client.user

"""Events"""
 
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
        await ctx.send(f"Command not found, use {PREFIX}help, for more information")
        print(error)
    print(error) #make a logging function in the future. 


"""Test Commands"""

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




"""Official Commands"""

@client.command(brief="Pong", help="A command to test the responce time between client and bot")
async def ping(ctx):
    await ctx.send(f'Pong {round(client.latency * 1000)}ms!')


@client.command(aliases=["part","gun"], help="Returns a images with all importend information per Gunsmith task", description="<number>")
async def gunsmith(ctx , number: int):
    await ctx.send(f"Gunsmith part {str(number)}")
    try:
        _file = discord.File(f"./Media/Gunsmith/Part{str(number)}.png")
        await ctx.send(file=_file)
    except:
        await ctx.send("File not found")



@client.command(aliases=["a","cal"], help="Returns a table of all rounds in the given caliber", description="<caliber name>" )
async def ammo(ctx,bullet="default"):
    if not bullet == "default": 
        destdir = "./Media/Bullets"
        files = [ f for f in os.listdir(destdir) if os.path.isfile(os.path.join(destdir,f)) ]
        for file in files: 
            if bullet in file: 
                await ctx.send(file=discord.File(f'./Media/Bullets/{file}'))
                return 
    await ctx.send(file=discord.File('./Media/Ammo/ammo.png'))    
    await ctx.send("command: ammo <caliber>")    


@client.command(aliases=['coin-flip', 'coin', 'flip'], help="Flips a coin, returns --> head or tails")
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











