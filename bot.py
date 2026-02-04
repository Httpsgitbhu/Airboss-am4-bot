import os
import discord
from discord.ext import commands

TOKEN = os.environ.get("TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("✈️ AirBoss DEMO is online")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 AirBoss awake hai!")

@bot.command()
async def about(ctx):
    await ctx.send(
        "✈️ **AirBoss Project**\n"
        "AM4 airline tracking & route assistant\n"
        "🚧 Demo version (under development)"
    )

@bot.command()
async def airport(ctx, code):
    demo_airports = {
        "DEL": "Delhi – Market 95 – Hub Cost 500k",
        "DXB": "Dubai – Market 90 – Hub Cost 700k",
        "JFK": "New York – Market 100 – Hub Cost 1.2M"
    }
    code = code.upper()
    await ctx.send(demo_airports.get(code, "❌ Airport not in demo database"))

bot.run(TOKEN)
