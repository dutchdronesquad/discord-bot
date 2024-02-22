"""Cog for handling Discord listeners."""
# ruff: noqa: ERA001
import discord
from discord.ext import commands


class Listener(commands.Cog, name="Listener"):
    """Listener class for handling Discord listeners."""

    def __init__(self, bot: commands.Bot) -> None:
        """Initialize the Listener class."""
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        """When the bot is ready to interact."""
        print(f"{self.bot.user.name} has connected to Discord (ID: {self.bot.user.id})")
        print()

        print("Connected to the following servers:")
        for guild in self.bot.guilds:
            print(f" - {guild.name} (ID: {guild.id})")

        print()
        print("--- Bot is online and ready to interact! ---")

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        """When a message is sent on Discord.

        Args:
        ----
            message (discord.Message): The message that was sent.

        """
        username = str(message.author).split("#")[0]
        user_message = str(message.content)
        if message.type == discord.MessageType.default:
            print(f"{username} in #{message.channel}: {user_message}")

        if message.author == self.bot.user:
            return

        # msg = message.content

        # if any(word in msg for word in sad_words):
        #     await message.reply(random.choice(happy_response))

        # Leave this here, otherwise commands wil stop running
        # await self.bot.process_commands(message)


def setup(bot: commands.Bot) -> None:
    """Add the Listener cog to the bot."""
    bot.add_cog(Listener(bot))
