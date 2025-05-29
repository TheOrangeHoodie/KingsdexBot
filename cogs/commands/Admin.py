import nextcord
from nextcord.ext import commands
import json
import ballHandler
from catchHandler import ListenedMessage

class Admin(commands.Cog):

    def __init__(self, bot : commands.Bot):
        self.bot = bot
        super().__init__()
        with open("./owners.json") as file:
            self.owners = json.load(file)

    @commands.command("ball")
    async def ball(self, ctx : commands.Context, name = None):
        if not ctx.author.id in self.owners: return
        if ctx.author.bot: return

        listenedMessage = ListenedMessage()

        if name != None:
            if name.isnumeric():
                await listenedMessage.init(ctx.channel, name)
                return

        await listenedMessage.init(ctx.channel)
        
        
async def setup(bot):
    bot.add_cog(Admin(bot))