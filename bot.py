#commands
#pipenv install discord.py
#pipenv install 
#pipenv run bot.py

import discord

prefix = "`"
commands = {}


class Ping:
    def __init__(self,base_command,arguments):
        self.command = base_command
        self.arguments = arguments
    def run(self,args): 
        return "Pong"






def input_handeler(msg):
    if len(msg) > 1: 
        msg = msg[1:] #remove prefix
        _input_list = msg.split()
        command = _input_list[0]
        arguments = _input_list[1:]

        if command in commands:
            responce = commands[command].run(arguments)
            return responce


ping = Ping("ping",[])
commands[ping.command] = ping 


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return


    
        if message.content == 'send_img':
            await message.channel.send(file=discord.File('./Media/9x19mm.png'))


        if message.content.startswith(prefix):
            await message.channel.send(input_handeler(message.content))



client = MyClient()
client.run('ODgxOTE2MDI4ODc0MDIyOTQz.YSzyTg.tSsW_C3Is1DHytj752msnI74P3A')











