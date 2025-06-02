import nextcord
from nextcord.ext import commands

class Testers(commands.Cog):

    def __init__(self, bot : commands.Bot):
        self.bot = bot
        super().__init__()

    @commands.command("ping")
    async def ping(self, ctx : commands.Context):
        await ctx.send(f"Pong 🏓! Latency: {str(round(self.bot.latency * 1000))}ms")

    @nextcord.slash_command(name="info", description="All the info about this bot", guild_ids=[1349739992926130248])
    async def collection(self, interaction : nextcord.Interaction):
        embed = nextcord.Embed(
            description=f"""
                Kingsdex Bot is based on the Ballsdex bot.
                Made for The Color Kings discord server.
            """,

            color=nextcord.Color.orange()
        )

        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar.url)
        embed.set_footer(text="© TheOrangeHoodie 2025")

        embed.add_field(name="Credits:", value="""
            Ball art: @averagevol, @admiral_podushka
            Scripter: @orange.hoodie
                        
            Special thanks to: Entire The Color Kings Server!
        """)

        await interaction.response.send_message(embed=embed)
        
async def setup(bot):
    bot.add_cog(Testers(bot))