"""Cog for giving and removing roles based on button presses."""

import discord
from discord.ext import commands

from .role_view import RoleView


class ButtonRoles(commands.Cog, name="Button Roles"):
    """ButtonRoles class for handling button roles."""

    def __init__(self, bot: commands.Bot) -> None:
        """Initialize the ButtonRoles class."""
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self) -> None:
        """When the bot is ready, load the role view."""
        self.bot.add_view(RoleView())

    @commands.command()
    @commands.is_owner()
    async def roles(self, ctx: discord.ApplicationContext) -> None:
        """Display the role buttons.

        command: !roles

        Args:
        ----
            ctx: The context in which the command was sent.

        """
        await ctx.send("Click a button to add or remove a role.", view=RoleView())


def setup(bot: commands.Bot) -> None:
    """Add the ButtonRoles cog to the bot."""
    bot.add_cog(ButtonRoles(bot))
