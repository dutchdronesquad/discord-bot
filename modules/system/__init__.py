"""Cog for handling system commands."""
from discord.ext import commands

import config

from .quote import get_quote


class System(commands.Cog, name="System"):
    """System class for handling system commands."""

    def __init__(self, bot: commands.Bot) -> None:
        """Initialize the System class."""
        self.bot = bot

    @commands.command(name="hallo")
    async def hello(self, ctx: commands.Context) -> None:
        """Say hello to the users.

        command: !hallo
        """
        await ctx.send("Hee hallo! Welkom op de server")

    @commands.command(name="version")
    @commands.has_permissions(administrator=True)
    async def version(self, ctx: commands.Context) -> None:
        """Get the bot version.

        admin: True
        command: !version
        """
        await ctx.send(f"Versie: {config.VERSION}")

    @commands.command(name="inspire")
    async def inspire(self, ctx: commands.Context) -> None:
        """Get a inspiration quote.

        command: !inspire
        """
        inspire = get_quote()
        await ctx.reply(inspire)


def setup(bot: commands.Bot) -> None:
    """Add the System cog to the bot."""
    bot.add_cog(System(bot))
