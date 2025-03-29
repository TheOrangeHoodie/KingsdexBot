import ballHandler
import nextcord
from nextcord.ext import commands
from catchHandler import ListenedMessage
import os

class Message(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot
        super().__init__()

    @commands.Cog.listener("on_message")
    async def on_message(self, message : nextcord.Message):
        if message.author.bot: return
        if not ballHandler.check_stamp(): return

        listenedMessage = ListenedMessage()
        await listenedMessage.init(message.channel)
        
async def setup(bot):
    bot.add_cog(Message(bot))