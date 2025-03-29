import nextcord
from nextcord.ext import commands

class Inventory(commands.Cog):

    def __init__(self, bot : commands.Bot):
        self.bot = bot
        super().__init__()

    @nextcord.slash_command(name="collection", description="Check your collection", guild_ids=[1349739992926130248])
    async def collection(self, interaction : nextcord.Interaction):
        embed = nextcord.Embed(
            description=f"""
            __**Owned Kingsballs**__
            Kingsdex Progression: 69.9%
            <:orangehoodie:1350831412655423598><:vol:1350831295936204831>

            __**Missing Kingsballs**__
            <:bored:1350831356812201984><:childannihilator:1350831460881530972><:betty:1351226202089721928><:admiral:1351227206717935706>
            """
        )

        embed.set_author(name=interaction.user.name, icon_url=interaction.user.display_avatar.url)

        await interaction.response.send_message(embed=embed)

        
async def setup(bot):
    bot.add_cog(Inventory(bot))