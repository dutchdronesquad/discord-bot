"""Cog for handling Discord events."""
import discord

from discord.ext import commands


class Events(commands.Cog, name="Events"):
    """Events class for handling Discord events."""
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("--- Bot is online and ready to interact! ---")
        print(f'{self.bot.user.name} has connected to Discord (ID: {self.bot.user.id})')

    @commands.Cog.listener()
    async def on_message(self, message):
        username = str(message.author).split('#')[0]
        user_message = str(message.content)
        if message.type == discord.MessageType.default:
            print(f'{username} in #{message.channel}: {user_message}')

        if message.author == self.bot.user:
            return

        # msg = message.content

        # if any(word in msg for word in sad_words):
        #     await message.reply(random.choice(happy_response))

        # Leave this here, otherwise commands wil stop running
        await self.bot.process_commands(message)

def setup(bot: commands.Bot):
    bot.add_cog(Events(bot))