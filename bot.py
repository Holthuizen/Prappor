#commands
#pipenv install discord.py
#pipenv install 
#pipenv run bot.py

import discord
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

        if message.content == 'send_img':
            await message.channel.send(file=discord.File('./Media/9x19mm.png'))

client = MyClient()
client.run('ODgxOTE2MDI4ODc0MDIyOTQz.YSzyTg.XVbikqQpaNk5SlG7iB5FuRKwYno')

