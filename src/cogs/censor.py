from nextcord.ext import commands
import asyncio
from utils import checkperm
data: dict = {}
class Censor(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener('on_message')
  async def censor(self, message):
    global data
    if message.guild is None: return
    if checkperm(message.author, ['admin']): return
    if any(word in message.content.lower() for word in ['discord.gg/', 'https://', 'http://', 'nig', 'fag', 'trann', 'neg', 'pd', 'ftg']):
      task = asyncio.create_task(message.delete())
      await message.author.send(f"FR\nTu avais un mot interdit dans ton message donc je l'ai supprimer.\nEN\nYou had a bad word in your message so I deleted it.\n```\n{message.content}\n```")
      await task
      

def setup(bot):
  bot.add_cog(Censor(bot))
