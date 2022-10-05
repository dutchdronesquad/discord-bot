from discord.ext import commands

class Racing(commands.Cog, name="Racing"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="vliegavond")
    async def trainings(self, ctx: commands.Context):
        """
        command: !vliegavond
        """
        await ctx.send('Een lijst van de aankomende vliegdata is te vinden op: https://dutchdronesquad.nl/trainingen en hier vind je ook uitleg, hoe je kan aanmelden voor een vliegavond.')
    
    @commands.command(name="track")
    async def track(self, ctx: commands.Context):
        """
        command: !track
        """
        await ctx.send('Informatie over de huidige racetrack kan je vinden op: https://dutchdronesquad.nl/racetrack, of verken de track alvast in Velocidrone.')

def setup(bot: commands.Bot):
    bot.add_cog(Racing(bot))