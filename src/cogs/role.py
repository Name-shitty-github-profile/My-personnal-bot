from nextcord.ext import commands
import asyncio, json
class Role(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener('on_ready')
  async def roles(self):
    with open("data/role.json", 'r') as f:
      data = json.load(f)
    tasks: list = []
    for guild in self.bot.guilds:
      try:
        role = guild.get_role(int(data[str(guild.id)]))
      except:
        pass
      for member in guild.members:
        if not role in member.roles: tasks.append(asyncio.create_task(member.add_roles(role)))
    for i in tasks: await i

  @commands.Cog.listener('on_member_join')
  async def role(self, member):
    with open("data/role.json", 'r') as f:
      data = json.load(f)
    task = asyncio.create_task(member.add_roles(member.guild.get_role(int(data[str(member.guild.id)]))))
    await member.send(f"FR\nBienvenue dans {member.guild.name}\nEN\nWelcome in {member.guild.name} !")
    await task

def setup(bot):
  bot.add_cog(Role(bot))
