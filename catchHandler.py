import nextcord
from nextcord.ext import commands
from ballHandler import get_ball, get_ball_by_id
from dataManager import get_player_data, update_player_data

GLOBAL_CATCH = {}

class CatchModal(nextcord.ui.Modal):
    def __init__(self, ball, button, view):
        super().__init__(
            "Catch a Kingsball!"
        )

        self.ball = ball
        self.button = button
        self.view = view

        self.mdInput = nextcord.ui.TextInput("Name")
        self.add_item(self.mdInput)

    async def callback(self, interaction : nextcord.Interaction):
        if self.mdInput.value.lower() in self.ball["aliases"]:
            ### HERE THE CATCH HAPPENS!
            self.button.disabled = True

            data = get_player_data(interaction.user.id)

            if data.get("balls") == None:
                data["balls"] = []

            isNew = not self.ball["id"] in data["balls"]

            data["balls"].append(self.ball["id"])

            update_player_data(interaction.user.id, data)

            await interaction.response.edit_message(view=self.view)
            if isNew:
                return await interaction.followup.send(f"{interaction.user.mention} you caught **{self.ball["displayName"]}** `#{self.ball["id"]}` \n(This is a **new ball** that has been added to your collection!)")
            else:
                return await interaction.followup.send(f"{interaction.user.mention} you caught **{self.ball["displayName"]}** `#{self.ball["id"]}`")

        return await interaction.response.send_message(f"Wrong name! {interaction.user.mention}")

class CatchView(nextcord.ui.View):
    def __init__(self, ball):
        super().__init__()
        self.value = 0
        self.ball = ball

    @nextcord.ui.button(label="Catch me!", style=nextcord.ButtonStyle.blurple)
    async def catchme(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        await interaction.response.send_modal(CatchModal(self.ball, button, self))

class ListenedMessage:
    async def init(self, channel, ball = None):
        if ball != None:
            self.ball = get_ball_by_id(int(ball))
        else:
            self.ball = get_ball()

        await channel.send("A wild country ball has appeared!", files=[nextcord.File(self.ball["filePath"])], view=CatchView(self.ball))