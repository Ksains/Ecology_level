import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
bot.remove_command('help')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!, пиши $help если хочешь узнать список комманд')

@bot.command()
async def help(ctx):
    await ctx.send(f'Список комманд: help,hello,london,city,ecology(все с префиксом $)')

@bot.command()
async def london(ctx):
    await ctx.send(f'Великий Смог - серьёзное загрязнение воздуха, произошедшее в Лондоне в декабре 1952 года.Великий смог считается худшим событием, связанным сзагрязнением воздуха, произошедшим в Великобритании, и наиболее важным с точки зрения влияния на экологические исследования. Подробнее - https://ru.wikipedia.org/wiki/%D0%92%D0%B5%D0%BB%D0%B8%D0%BA%D0%B8%D0%B9_%D1%81%D0%BC%D0%BE%D0%B3')

@bot.command()
async def city(ctx):
    await ctx.send(f'Сейчас я расскажу тебе о лучших городах в России по уровню Экологии. 1 - Сургут, 2 - Тюмень, 3 - Краснодар, 4 - Нижневартовск, 5 - Санкт-Петербург. Источник - https://visualhistory.livejournal.com/284543.html')

@bot.command()
async def ecology(ctx):
    await ctx.send(f'Уже сейчас именно ты можешь начать улучшать свою среду обитания( то есть город, деревню, микро-район), для этого надо просто выбрасывать мусор в правильном месте, начать сортировать мусор, стать волонтером.')

bot.run("token")
