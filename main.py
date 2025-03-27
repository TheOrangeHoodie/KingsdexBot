import ballHandler
import nextcord
import dotenv
from nextcord.ext import commands
from os import walk

env = dotenv.dotenv_values("./.env")

intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix="$", intents=intents)

def loadCogs():
    for root, dirs, files in walk("./cogs"):
        for file in files:
            if file.endswith(".py"):
                print("Cog found!: " + file)
                extensionPath = root.replace("/", ".").replace("\\", ".")[2:] + "." + file[:-3]
                bot.load_extension(extensionPath)

@bot.event
async def on_ready():
    loadCogs()
    print("Logged in as: " + bot.user.name)



bot.run(env["TOKEN"])