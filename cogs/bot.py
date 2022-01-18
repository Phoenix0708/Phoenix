import discord
from discord.ext import commands
import os

class Bot(commands.Cog):
   def __init__(self,client):
    self.client = client

   @commands.command()
   async def noob(self, ctx):
    await ctx.reply('Noob hoga tera baap saale')

def setup(client):
  client.add_cog(Bot(client))    