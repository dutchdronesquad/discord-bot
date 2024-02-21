"""Cog for handling racing commands."""
from discord.ext import commands


class Racing(commands.Cog, name="Racing"):
    """Racing class for handling racing commands."""

    def __init__(self, bot: commands.Bot) -> None:
        """Initialize the Racing class."""
        self.bot = bot

    @commands.command(name="vliegavond")
    async def trainings(self, ctx: commands.Context) -> None:
        """Let users know where to find the upcoming flying dates.

        command: !vliegavond

        Args:
        ----
            ctx (commands.Context): The context in which the command was sent.

        """
        msg: str = "Een lijst van de aankomende vliegdata is te vinden op: https://dutchdronesquad.nl/trainingen en hier vind je ook uitleg, hoe je kan aanmelden voor een vliegavond."  # noqa: E501
        await ctx.send(msg)

    @commands.command(name="track")
    async def track(self, ctx: commands.Context) -> None:
        """Let users know where to find the current racetrack.

        command: !track

        Args:
        ----
            ctx (commands.Context): The context in which the command was sent.

        """
        msg: str = "Informatie over de huidige racetrack kan je vinden op: https://dutchdronesquad.nl/racetrack, of verken de track alvast in Velocidrone."  # noqa: E501
        await ctx.send(msg)


def setup(bot: commands.Bot) -> None:
    """Add the Racing cog to the bot."""
    bot.add_cog(Racing(bot))
