import config

from discord.ext import commands
from .quote import get_quote

class System(commands.Cog, name="System"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="hallo")
    async def hello(self, ctx: commands.Context):
        """
        command: !hallo
        Say hello to the users
        """
        await ctx.send('Hee hallo! Welkom op de server')

    @commands.command(name="version")
    @commands.has_permissions(administrator=True)
    async def version(self, ctx: commands.Context):
        """
        command: !version
        admin only
        """
        await ctx.send(f'Versie: {config.VERSION}')

    @commands.command(name="inspire")
    async def inspire(self, ctx: commands.Context):
        """
        command: !inspire
        Get a inspiration quote
        """
        inspire = get_quote()
        await ctx.reply(inspire)

def setup(bot: commands.Bot):
    bot.add_cog(System(bot))