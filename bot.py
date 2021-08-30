#pip install -U discord.py

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

client = MyClient()
client.run('ODgxOTE2MDI4ODc0MDIyOTQz.YSzyTg.DSIGDWT4lgJP2z3rdv_g9GpKLs0')