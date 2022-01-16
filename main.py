import discord
import asyncio
import re
import os
from discord.ext import commands
from webserver import keep_alive

import os

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))

@bot.event
async def on_message(message):
  await bot.process_commands(message)


@bot.command()
async def archive(ctx):
  chan = discord.utils.get(ctx.guild.categories, name="Archived Channels")
  await ctx.channel.edit(category=chan)
  chan_name = ctx.channel.name
  await ctx.channel.edit(name=f"archived-{chan_name}")
  await ctx.send("Archived :white_check_mark:")


keep_alive()

TOKEN = os.environ.get("DISCORD_BOT_SECRET")

bot.run(TOKEN)
