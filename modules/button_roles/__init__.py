"""Cog for giving and removing roles based on button presses."""
from discord.ext import commands
from .role_view import RoleView


class ButtonRoles(commands.Cog, name="Button Roles"):
    """ButtonRoles class for handling button roles."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """When the bot is ready, load the role view."""
        self.bot.add_view(RoleView())

    @commands.command()
    @commands.is_owner()
    async def roles(self, ctx: commands.Context):
        """Creates a new role view."""
        await ctx.send("Click a button to add or remove a role.", view=RoleView())

def setup(bot: commands.Bot):
    bot.add_cog(ButtonRoles(bot))