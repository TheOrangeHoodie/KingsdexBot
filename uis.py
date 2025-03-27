import nextcord
from nextcord.ext import commands

class CatchModal(nextcord.ui.Modal):
    def __init__(self, ball):
        super().__init__(
            "Catch a Kingsball!"
        )

        self.ball = ball

        self.mdInput = nextcord.ui.TextInput("Name")
        self.add_item(self.mdInput)

    async def callback(self, interaction):
        if type(self.ball["name"]) == str:
            if self.ball["name"].lower() == self.mdInput.value.lower(): 
                return await interaction.response.send_message(f"You catched a ball! {self.ball["name"]}")
        else:
            if self.mdInput.value.lower() in self.ball["name"]: 
                return await interaction.response.send_message(f"You catched a ball! {self.ball["display"]}")
            
        return await interaction.response.send_message("Wrong name!")

class CatchView(nextcord.ui.View):
    def __init__(self, ball):
        super().__init__()
        self.value = 0
        self.ball = ball

    @nextcord.ui.button(label="Catch me!", style=nextcord.ButtonStyle.blurple)
    async def catchme(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
        await interaction.response.send_modal(CatchModal(self.ball))
        button.disabled = True