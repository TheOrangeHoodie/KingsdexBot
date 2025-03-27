import ballHandler
import nextcord
from nextcord.ext import commands

class Message(commands.Cog):

    def __init__(self, bot : commands.Bot):
        self.bot = bot
        super().__init__()

    @commands.Cog.listener("on_message")
    async def on_message(self, message : nextcord.Message):
        if message.author.bot: return
        if ballHandler.check_stamp():
            await message.reply("Sending a ball!")
        
async def setup(bot):
    bot.add_cog(Message(bot))