import discord
import os
import youtube_dl
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio


bot = commands.Bot(command_prefix='>>', description = 'Bot for youtube music')

@bot.command()
async def description(ctx):
    await ctx.send('Este bot es creado por CarlosReyesM')
@bot.command(pass_context = True)
async def join(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    

@bot.command(pass_context = True)
async def DameAmorPls(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    vc = get(bot.voice_clients, guild=ctx.guild)
    if vc and vc.is_connected():
        await vc.move_to(channel)
    else:
        vc = await channel.connect()
        vc.play(discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe", source="Este.mp3"))
        vc.is_playing()
        vc.pause()
        vc.resume()
        

@bot.event
async def on_ready():
    print('Funcionando')

bot.run('NzQ4Njg5NDkyMDY3NDgzNzMx.X0hFbA.lvCYa9lcFHFcolB0lPtDVM-FyZM')
