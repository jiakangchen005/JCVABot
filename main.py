import os
import sys
from asyncio import sleep

import discord
from discord.ext import commands, tasks

from live import live

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = '>', help_command = None, intents = intents)

token = os.environ['token']

# Start of Bot

@client.event
async def on_ready():
	status = discord.Game("/home/jc/work")
	await client.change_presence(activity = status)
		
	count.start()

	print("yey")

@client.event
async def on_member_join(member):
	channel = client.get_channel(840211266869919784)
	await channel.send(f"Welcome to JC's League, <@{member.id}>. Enjoy!")

@client.event
async def on_member_remove(member):
	channel = client.get_channel(840211266869919784)
	await channel.send(f"{member} has left the server.")

@tasks.loop(seconds = 300)
async def count():
	temp = client.get_channel(839976544692731985)

	channel = client.get_channel(840442030785691678)

	await channel.edit(name = "Server Users: " + str(temp.guild.member_count))

@client.command()
async def clear(ctx, amount = sys.maxsize - 1):
  if (amount != sys.maxsize - 1):
    await ctx.channel.purge(limit = amount + 1)
  else:
	  await ctx.channel.purge(limit = amount)

@client.command()
async def test(ctx):
 	await ctx.send(ctx.guild.member_count)

# End of Bot

live()
client.run(token)
