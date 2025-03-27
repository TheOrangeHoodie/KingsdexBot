import ballHandler
import nextcord
from nextcord.ext import commands
from uis import CatchView
import os

class Message(commands.Cog):

    def __init__(self, bot : commands.Bot):
        self.bot = bot
        super().__init__()

    @commands.Cog.listener("on_message")
    async def on_message(self, message : nextcord.Message):
        if message.author.bot: return
        print(os.listdir("../"))
        if ballHandler.check_stamp():
            ballInfo = ballHandler.get_ball()
            if type(ballInfo["name"]) == str:
                path = nextcord.File(f"./balls/{ballInfo["name"]}.png")
            else:
                path = nextcord.File(f"./balls/{ballInfo["display"]}.png")

            await message.reply(content="A wild Kingsball appeared!", files=[path], view=CatchView(ballInfo))
        
async def setup(bot):
    bot.add_cog(Message(bot))