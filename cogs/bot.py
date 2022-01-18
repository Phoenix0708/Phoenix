import discord
from discord.ext import commands
import os

class Bot(commands.Cog):
   def __init__(self,client):
    self.client = client

   @commands.command()
   @commands.is_owner()
   async def noob(self, ctx):
    await ctx.reply('Raman,Ankit PRO :)')

def setup(client):
  client.add_cog(Bot(client))    