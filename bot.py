import discord
from discord.ext import commands, tasks
from logic import createreply
from config import TOKEN

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    content = message.content
    await message.channel.send(createreply(content))
    await bot.process_commands(message)

bot.run(TOKEN)