import discord
import os
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio


bot = commands.Bot(command_prefix='>>', description = 'Bot for youtube music')

@bot.command()
async def description(ctx):
    await ctx.send('Este bot es creado por CarlosReyesM')
@bot.command()
async def bb(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
 

@bot.event
async def on_ready():
    print('Funcionando')
bot.run('NzQ4Njg5NDkyMDY3NDgzNzMx.X0hFbA.cpcwR9JW-iJ0pFxb8Q3sQbqV2uw')
