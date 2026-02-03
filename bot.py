import os
import discord
from discord.ext import commands

# Token ONLY from Render Environment
TOKEN = os.environ.get("TOKEN")

if TOKEN is None:
    raise RuntimeError("TOKEN environment variable not found")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong! Bot is alive ✅")

@bot.command()
async def status(ctx):
    await ctx.send("✈️ AirBoss AM4 bot running smoothly")

bot.run(TOKEN)
