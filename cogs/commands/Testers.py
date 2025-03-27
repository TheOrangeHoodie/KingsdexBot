import nextcord
from nextcord.ext import commands

class Testers(commands.Cog):

    def __init__(self, bot : commands.Bot):
        self.bot = bot
        super().__init__()

    @commands.command("ping")
    async def ping(self, ctx : commands.Context):
        await ctx.send(f"Pong 🏓! Latency: {str(round(self.bot.latency * 1000))}ms")
        
async def setup(bot):
    bot.add_cog(Testers(bot))