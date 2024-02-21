"""Cog for handling racing commands."""
import discord
from discord.ext import commands


class Racing(commands.Cog, name="Racing"):
    """Specific commands about racing."""

    def __init__(self, bot: commands.Bot) -> None:
        """Initialize the Racing class."""
        self.bot = bot

    @commands.command(name="training")
    async def trainings(self, ctx: discord.ApplicationContext) -> None:
        """Know where to find the upcoming flying dates.

        command: !training

        Args:
        ----
            ctx: The context in which the command was sent.

        """
        msg: str = "Een lijst met aankomende vliegdata is te vinden op: https://dutchdronesquad.nl/trainingen. Daar vind je ook instructies over hoe je je kunt aanmelden voor een vliegavond."  # noqa: E501
        await ctx.send(msg)

    @commands.command(name="track")
    async def track(self, ctx: discord.ApplicationContext) -> None:
        """Know where to find the current racetrack.

        command: !track

        Args:
        ----
            ctx: The context in which the command was sent.

        """
        msg: str = "Informatie over de huidige racetrack is te vinden op: https://dutchdronesquad.nl/racetrack. Je kunt ook de track alvast verkennen in Velocidrone."  # noqa: E501
        await ctx.send(msg)


def setup(bot: commands.Bot) -> None:
    """Add the Racing cog to the bot."""
    bot.add_cog(Racing(bot))
