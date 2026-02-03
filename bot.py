import discord
from discord.ext import commands
from datetime import datetime

TOKEN = None  # token Render se aayega

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

history = []

@bot.event
async def on_ready():
    print("✈️ AirBoss AM4 is ONLINE")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.attachments:
        history.append((datetime.now(), "Screenshot received"))
        await message.channel.send(
            "📸 Screenshot received!\n"
            "⚠️ OCR temporarily disabled\n"
            "Bot is online and working ✅"
        )

    await bot.process_commands(message)

@bot.command()
async def status(ctx):
    if not history:
        await ctx.send("❌ No data yet. Upload screenshot 📸")
        return
    t, _ = history[-1]
    await ctx.send(f"📊 Bot working\nLast update: {t}")

bot.run(TOKEN)
