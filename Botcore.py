import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='>>', description = 'Bot for youtube music')

@bot.command()
async def description(ctx):
    await ctx.send('Este bot es creado por CarlosReyesM')

bot.run('NzQ4Njg5NDkyMDY3NDgzNzMx.X0hFbA.cpcwR9JW-iJ0pFxb8Q3sQbqV2uw')
