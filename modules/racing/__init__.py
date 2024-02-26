"""Cog for handling racing commands."""
import discord
from discord.commands import SlashCommandGroup
from discord.ext import commands


class Racing(commands.Cog, name="Racing"):
    """Specific commands about racing."""

    def __init__(self, bot: commands.Bot) -> None:
        """Initialize the Racing class."""
        self.bot = bot

    racing = SlashCommandGroup(
        name="race",
        description="Commands specific about drone racing.",
    )

    @racing.command(
        name="training",
        description="Get the URL to the upcoming flying dates.",
    )
    async def training(self, ctx: discord.ApplicationContext) -> None:
        """Know where to find the upcoming flying dates.

        command: !training

        Args:
        ----
            ctx: The context in which the command was sent.

        """
        msg: str = "Een lijst met aankomende vliegdata is te vinden op: https://dutchdronesquad.nl/trainingen. Daar vind je ook instructies over hoe je je kunt aanmelden voor een vliegavond."  # noqa: E501
        await ctx.respond(msg)

    @racing.command(
        name="track",
        description="Get URL for information about the current racetrack.",
    )
    async def track(self, ctx: discord.ApplicationContext) -> None:
        """Know where to find the current racetrack.

        command: !track

        Args:
        ----
            ctx: The context in which the command was sent.

        """
        msg: str = "Informatie over de huidige racetrack is te vinden op: https://dutchdronesquad.nl/racetrack. Je kunt ook de track alvast verkennen in Velocidrone."  # noqa: E501
        await ctx.respond(msg)

    @racing.command(
        name="results",
        description="Get URL for information where to find the timing results.",
    )
    async def results(self, ctx: discord.ApplicationContext) -> None:
        """Know where to find the timing results.

        command: !results

        Args:
        ----
            ctx: The context in which the command was sent.

        """
        msg: str = "De resultaten van de tijdwaarneming tijdens een vliegavond zijn beschikbaar op: https://fpvscores.com/organisation/dds."  # noqa: E501
        await ctx.respond(msg)


def setup(bot: commands.Bot) -> None:
    """Add the Racing cog to the bot."""
    bot.add_cog(Racing(bot))
