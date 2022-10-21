from nextcord.ext import commands
import asyncio
from utils import checkperm
class Annoncement(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener('on_message')
  async def annoncement(self, message):
    if message.guild is None: return
    if checkperm(message.author, ['admin']) is False or message.author.bot: return
    with open('data/annoncement.txt', 'r') as f:
      dat = f.read()
    if str(message.channel.id) in dat.split('\n'):
      task = asyncio.create_task(message.delete())
      await message.channel.send(message.content.replace("@", ''))
      await task

def setup(bot):
  bot.add_cog(Annoncement(bot))
