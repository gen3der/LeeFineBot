import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio

bot = commands.Bot(command_prefix='!')


@bot.command(pass_context = True)
async def info(ctx,*args):
  retStr = ("""\n**Привет, LeeFine - Ванильный, Приватный Сервер, который к тому же Кроссплатформенный!Сервер строгий ,но дружелюбный! Мы всегда рады видеть всех игроков.**\n \n **Сервер РП ,создай персонажа и отыгрывай свою роль.На сервере дружные игроки и много кланов, организаций и партий. У каждого из них уникальная цель ,или уникальные игроки!!**""")
  embed = discord.Embed(title = 'Info', colour = discord.Color.orange()) #info
  embed.add_field(name="LeeFine",value=retStr)
  await ctx.send(embed=embed) #info

@bot.command(pass_context = True)
async def helps(ctx,*args):
  retStr = ("""\n**!helps - Основные команды сервера!\n!info - Показывает основное описание нашего проект!**""")
  embed = discord.Embed(title = 'Helps', colour = discord.Color.red()) #info
  embed.add_field(name="Основные команды",value=retStr)
  await ctx.send(embed=embed) #помощь

@bot.command(pass_context = True)
async def online(ctx,*args):
  retStr = ("""\n**Средний онлайн на сервере\n 7 \n Присоединяйся! **""")
  embed = discord.Embed(title = 'Средний Онлайн', colour = discord.Color.green()) #info
  embed.add_field(name="По подсчетам, которые проводятся каждые 10h \n Вы можете наблюдать нашу статистику на",value=retStr)
  await ctx.send(embed=embed) #помощ


bot.run('OTY1NTY4MTk4MDA5MzIzNTkx.GM0WMm.5ygkelhWPK_sN_iStCB83qbBnTRBQfGWu28jwQ')