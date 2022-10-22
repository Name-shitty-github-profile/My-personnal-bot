from nextcord.ext import commands
import nextcord
from utils import checkperm
class Say(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @nextcord.slash_command(name = "say", description = "FR Me fait dire un message EN make me say something")
  async def sayslash(self, interaction: nextcord.Interaction, content: str = nextcord.SlashOption(name="content", description="FR Ce que tu me fais dire EN What you make me say")):
    if checkperm(interaction.user, ['admin']) is False:
      await interaction.response.send_message(content=content + f'- **{interaction.user.name}**')
      return None
    await interaction.response.send_message(content=content)

def setup(bot):
  bot.add_cog(Say(bot))
