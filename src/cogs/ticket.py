import nextcord, asyncio
class ticket_buttons(nextcord.ui.View):
  def __init__(self):
    super().__init__(timeout = None)
    self.value = None

  @nextcord.ui.button(label="ticket", style = nextcord.ButtonStyle.green)
  async def confirm(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
    view = cbtn()
    await interaction.response.send_message('FR\nEs-tu sûre de vouloir faire cela?\nEN\nAre you sure to do that ?', view=view, ephemeral=True)
    await view.wait()

class cbtn(nextcord.ui.View):
  def __init__(self):
    super().__init__(timeout = None)
    self.value = None

  @nextcord.ui.button(label="Yes/Oui", style = nextcord.ButtonStyle.green)
  async def Oui(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
    for channel in interaction.guild.channels:
      if channel.name == f'ticket-{interaction.user.id}':
        await interaction.response.send_message(f'FR\nTu as déja un ticket.\nEN\nYou already have a ticket.\n{channel.mention}', ephemeral=True)
        return
    channel = await interaction.guild.create_text_channel(f'ticket-{interaction.user.id}', category=interaction.guild.get_channel(category_id[str(interaction.guild.id)]))
    await channel.set_permissions(interaction.user, send_messages=True, read_messages=True)
    await interaction.response.edit_message(content=f'{channel.mention}', view=None)
    msg = await channel.send('@everyone')
    await msg.delete()
    await channel.send(embed=nextcord.Embed(title=f'FR\nLe staff sera bientôt la {interaction.user.name} !\nEN\nThe staff will soon be here {interaction.user.name} !', color = 0x2ecc71))

  @nextcord.ui.button(label="No/Non", style = nextcord.ButtonStyle.red)
  async def Non(self, button : nextcord.ui.Button, interaction : nextcord.Interaction):
    await interaction.response.edit_message(content="FR\nDemande annulée!\nEN\nDeman cancelled !", view=None)

category_id: dict = {}

async def ticket(message_id, channel_id, category_ide, guild_id, b):
  global category_id
  category_id[str(guild_id)] = category_ide
  view = ticket_buttons()
  msg = await b.get_channel(channel_id).fetch_message(message_id)
  await msg.edit(view = view)
  await view.wait()
  
from nextcord.ext import commands
import json
class Ticket(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener('on_ready')
  async def Readye(self):
    with open('data/ticket.json', 'r') as f:
      data = json.load(f)
    tasks: list = []
    for i, j in data.items():
      e = j.split('|')
      k = i.split('|')
      tasks.append(asyncio.create_task(ticket(int(k[0]), int(k[1]), e[0], e[1], self.bot)))
    for i in tasks:
      await i

def setup(bot):
  bot.add_cog(Ticket(bot))
