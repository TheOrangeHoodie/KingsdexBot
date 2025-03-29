import nextcord
from nextcord.ext import commands
from dataManager import get_player_data
from ballHandler import get_ball_by_id, get_config

class Inventory(commands.Cog):

    def __init__(self, bot : commands.Bot):
        self.bot = bot
        super().__init__()

    @nextcord.slash_command(name="collection", description="Check your collection", guild_ids=[1349739992926130248])
    async def collection(self, interaction : nextcord.Interaction):
        ownedBalls = get_player_data(interaction.user.id)["balls"]
        allBalls = get_config()

        ownedEmojis = []
        notOwnedEmojis = []
        for ballData in allBalls:
            if ballData["id"] in ownedBalls:
                ownedEmojis.append(ballData["emoji"])
            else:
                notOwnedEmojis.append(ballData["emoji"])

        embed = nextcord.Embed(
            description=f"""
            __**Owned Kingsballs**__
            Kingsdex Progression: {round((len(ownedEmojis) / (len(ownedEmojis) + len(notOwnedEmojis))) * 100, 1)}%
            {"".join(ownedEmojis)}

            __**Missing Kingsballs**__
            {"".join(notOwnedEmojis)}
            """
        )

        embed.set_author(name=interaction.user.name, icon_url=interaction.user.display_avatar.url)

        await interaction.response.send_message(embed=embed)

        
async def setup(bot):
    bot.add_cog(Inventory(bot))