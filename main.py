#!/usr/bin/python3

from twitchio.ext import commands

class Bot(commands.Bot):
    def __init__(self):
        # Initialise our Bot with our access token, prefix and list of channels to join on bot...
        # Prexif can be callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(token='', prefix='!', initial_channels=["joanvaro"])

    async def event_ready(self):
        # Notify us when everything is reasy!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')

    async def event_message(self, message):
        # Message with echo set to True are messages sent by the bot...
        # For now we just want to ignore them
        if message.echo:
            return

        # Print the contents of our message to console...
        print(message.content)

        # Since we have commands and are overriding the default 'event_message'
        # We must let the bot know we want to handle and invoke our commands...
        await self.handle_commands(message)

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Here we have a command hello, we can invoke our command with our prefix and command name 
        # e.g. ?hello
        # We can also give our commands aliases (diferent names) to invoke with.

        # Send a hello back!
        # Sending a reply back to the channel is easy... Below is an example.
        await ctx.send(f'Hello {ctx.author.name}!')

bot = Bot()
bot.run()
