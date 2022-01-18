import discord
from discord.ext import commands
from discord.ext import tasks
from itertools import cycle
import os

client=commands.Bot(command_prefix='.')

status=cycle(['.help','Phoenix'])

@client.event
async def on_ready():
  change_status.start()
  print('Running')

@tasks.loop(seconds=7)
async def change_status():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name=status))


client.remove_command('help')

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')

client.run('OTIyODQzNTQ3MjQ4NTE3MTcw.YcHXBw.QeXfaLJ22FuWi9WofhJ6B9dGiNE')    