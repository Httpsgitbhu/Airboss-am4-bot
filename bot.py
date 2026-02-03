import discord
from discord.ext import commands
from PIL import Image
import pytesseract
import re
from datetime import datetime

TOKEN = "MTQ2ODI1OTgxMzE3MDYxNDQyNA.Gbpr52.N7nWdaeFuAOTGSvm3kt3N8eUy8Wet146QYkdA8"

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

history = []

def parse_text(text):
    cash = re.search(r'(\d+[.,]?\d*)\s*M', text)
    fuel = re.search(r'Fuel\s*[:\-]?\s*(\d+)', text)
    rep = re.search(r'(\d{2}\.\d)%', text)

    return {
        "cash": cash.group(1) if cash else "N/A",
        "fuel": fuel.group(1) if fuel else "N/A",
        "rep": rep.group(1) if rep else "N/A"
    }

@bot.event
async def on_ready():
    print("✈️ AirBoss AM4 is ONLINE")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.attachments:
        for file in message.attachments:
            if file.filename.lower().endswith((".png", ".jpg", ".jpeg")):
                img = Image.open(await file.read())
                text = pytesseract.image_to_string(img)

                data = parse_text(text)
                history.append((datetime.now(), data))

                await message.channel.send(
                    f"✅ **Airline Data Detected**\n"
                    f"💰 Cash: {data['cash']}M\n"
                    f"⛽ Fuel: {data['fuel']}\n"
                    f"⭐ Reputation: {data['rep']}%"
                )

    await bot.process_commands(message)

@bot.command()
async def status(ctx):
    if not history:
        await ctx.send("❌ No data yet. Upload screenshot 📸")
        return

    t, d = history[-1]
    await ctx.send(
        f"📊 **Latest Status**\n"
        f"🕒 {t}\n"
        f"💰 Cash: {d['cash']}M\n"
        f"⛽ Fuel: {d['fuel']}\n"
        f"⭐ Rep: {d['rep']}%"
    )

bot.run(TOKEN)

TOKEN = "MTQ2ODI1OTgxMzE3MDYxNDQyNA.Gbpr52.N7nWdaeFuAOTGSvm3kt3N8eUy8Wet146QYkdA8"
