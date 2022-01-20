from multiprocessing import Value
import discord
from discord.ext import commands
import os
import random



class NSFW(commands.Cog):
   def __init__(self,client):
    self.client = client
    
   

   @commands.command()
   async def kiss(self, ctx , member:discord.Member):
      kick = ['https://c.tenor.com/G954PGQ7OX8AAAAM/cute-urara-shiraishi-anime.gif','https://c.tenor.com/03wlqWILqpEAAAAM/highschool-dxd-asia.gif','https://c.tenor.com/Ge4DoX5aDD0AAAAM/love-kiss.gif','https://c.tenor.com/dJU8aKmPKAgAAAAM/anime-kiss.gif','https://c.tenor.com/wDYWzpOTKgQAAAAM/anime-kiss.gif','https://c.tenor.com/I8kWjuAtX-QAAAAM/anime-ano.gif','https://c.tenor.com/e6cYiAPPCq4AAAAM/anime-kissing.gif']
      embedkiss = discord.Embed(title=f'Cute!! {ctx.author.name} kisses {member.name}',color=discord.Color.green())
      embedkiss.set_image(url=random.choice(kick))
      embedkiss.set_footer(text='Awwwwww :)')  
      await ctx.send(embed=embedkiss)


def setup(client):
  client.add_cog(NSFW(client))