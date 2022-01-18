import discord
from discord.ext import commands
import os

class Mod(commands.Cog):
   def __init__(self,client):
    self.client = client
    
   @commands.command()
   @commands.has_permissions(kick_members=True)
   @commands.bot_has_permissions(kick_members=True)
   async def kick(self, ctx, member:discord.Member, *, reason=None):
     await member.send(f'You were kicked in {ctx.guild.name} for {reason}')
     await member.kick(reason=reason)
     await ctx.reply(f'Kicked {member.mention}')

   @commands.command()
   @commands.has_permissions(ban_members=True)
   @commands.bot_has_permissions(ban_members=True)
   async def ban(self, ctx, member:discord.Member,* , reason=None):
       await ctx.send(f'Banned {member.name}')
       await member.ban(reason=reason)
       await member.send(f'You were banned in {ctx.guild.name} for '+reason) 

   @commands.command()
   @commands.has_permissions(manage_messages=True)
   async def purge(self, ctx, amount):
     await ctx.channel.purge(limit=amount) 
     await ctx.send(f'Purged {amount} messages')
       

   @commands.Cog.listener()
   async def on_command_error(self, ctx, error):
     if isinstance(error, commands.MissingRequiredArgument):
       await ctx.reply(f'```{ctx.author.name}, Please pass in all the required arguements```')  
     elif isinstance(error , commands.MissingPermissions):
       await ctx.reply(f'```{ctx.author.name}, You do not have all the required permissions to run this command```')    
     elif isinstance(error, commands.NotOwner):
       await ctx.reply(f'```{ctx.author.name}, You are not the owner to use this command')
     elif isinstance(error , commands.MemberNotFound):
       await ctx.reply(f'```{ctx.author.name}, I did not seem to find this particular member in the server```')
     elif isinstance(error , commands.BotMissingPermissions):
      await ctx.reply(f'```{ctx.author.name}, Uh-Oh I guess I am missing permissions to run this command```')  

def setup(client):
  client.add_cog(Mod(client))