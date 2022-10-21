from nextcord.ext import commands
import asyncio
from utils import checkperm
data: dict = {}
class Antispam(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener('on_message')
  async def antispam(self, message):
    global data
    if message.guild is None: return
    if checkperm(message.author, ['admin']): return
    msdg = str(message.author.id)
    try:
      data[msdg]['d'] += 1
      num = data[msdg]['d']
    except KeyError:
      data[msdg] = {"e": True, 'd': 1}
      num = 1
    if data[msdg]['e']:
      data[msdg]['e'] = False
      await asyncio.sleep(1)
      del data[msdg]
    elif num == 2:
      await message.author.send("FR\nJe vais te kick si tu envoie plus de messages par seconde.\nEN\nI will kick you if you send more messages per seconds.")
    elif num == 3:
      task = asyncio.create_task(message.author.send(f"FR\nTu spammais dans {message.guild.name} donc je t'ai kick.\nEN\nYou were spamming in {message.guild.name} so I kicked you."))
      await message.author.kick(reason="FR Spam |EN Spamming")
      await task

def setup(bot):
  bot.add_cog(Antispam(bot))
