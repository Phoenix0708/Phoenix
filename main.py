import discord
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle
import os
import pymongo


owners=['814353938429771776','918410542203412480']
client=commands.Bot(command_prefix='.',set_owners=owners)
status=cycle(['.help','Phoenix'])

cluster = pymongo.MongoClient('mongodb+srv://Phoenix:phoenixu@demonrpg.at2am.mongodb.net/test')
db = cluster['DemonRPG']



@tasks.loop(seconds=7)
async def change_status():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name='Phoenix Chacha'))


client.remove_command('help')

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')


client.run('OTIyODQzNTQ3MjQ4NTE3MTcw.YcHXBw.QeXfaLJ22FuWi9WofhJ6B9dGiNE')    