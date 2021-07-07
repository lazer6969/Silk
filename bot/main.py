import discord
import json
import os
from keep_alive import keep_alive
import random
from random import choice
import asyncio
from discord.ext import commands

client = commands.Bot(command_prefix="?", help_command=None)

print("Bot Is Ready")
print("Logged In As Silk")
print("No Errors Found")
print("Working Nicely")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"?help"))

@client.command()
async def help(ctx):
  e = discord.Embed(
  title="Silk Commands!",
  description="howgay, howcute, simprate, pp, coinflip, randomnumber, ping, invite",
    color=0xFF0000
)
  await ctx.send(embed=e)

@client.command()
async def simprate(ctx):
    x = random.randint(0,100)
    e = discord.Embed(
  title="Simp Rate",
  description=f"{x}% Simp",
    color=0xFF0000
    )
    await ctx.send(embed=e)

@client.command()
async def howgay(ctx):
    x = random.randint(0,100)
    e = discord.Embed(
  title="Gay Rate",
  description=f"{x}% Gay",
    color=0xFF0000
    )
    await ctx.send(embed=e)

@client.command()
async def pp(ctx):
    x = random.randint(1,10)
    e = discord.Embed(
  title="Calculated PP",
  description=f"8{'='*random.randint(1, 10)}D",
    color=0xFF0000
    )
    await ctx.send(embed=e)

determine_flip = [1, 0]

@client.command()
async def coinflip(ctx):
    if random.choice(determine_flip) == 1:
        embed = discord.Embed(title="Coinflip", description=f"{ctx.author.mention} Flipped coin, we got **Heads**!", color=0xFF0000)
        await ctx.send(embed=embed)

    else:
        embed = discord.Embed(title="Coinflip", description=f"{ctx.author.mention} Flipped coin, we got **Tails**!", color=0xFF0000)
        await ctx.send(embed=embed)

@client.command()
async def randomnumber(ctx):
    x = random.randint(1,100)
    e = discord.Embed(
  title="Random Number Is",
  description=f"{x}",
    color=0xFF0000
)
    await ctx.send(embed=e)

@client.command()
async def invite(ctx):
  e = discord.Embed(
  title="My Invite Link And My Support Server Link Here!",
  description="My Invite Link [here](https://discord.com/api/oauth2/authorize?client_id=853611248440180746&permissions=2148005952&scope=bot) And My Support Server [here](https://discord.gg/Ry33J6qPZE)",
    color=0xFF0000
  )
  await ctx.send(embed=e)
  
@client.command()
async def howcute(ctx):
    x = random.randint(0,100)
    e = discord.Embed(
  title="Cute Rate",
  description=f"{x}% Cute",
    color=0xFF0000
)
    await ctx.send(embed=e)
    

@client.command()
async def ping(ctx):
    x = random.randint(5,25)
    e = discord.Embed(
  title="Pong!",
  description=f"{x}ms",
    color=0xFF0000,
    )
    await ctx.send(embed=e)

keep_alive()

client.run(os.getenv('token'))