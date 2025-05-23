# This is an `<h1>` header, which is the largest

## This is an `<h2>` header

###### This is an `<h6>` header, which is the smallest

![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)

pip install disnake python-dotenv

DISCORD_TOKEN=OMMITTED FOR THIS COMMIT
DISCORD_CLIENT_ID=1374628149840711761
DISCORD_PERMISSIONS=1755381623276608

python bot.py

import os
import random

import disnake
from disnake.ext import commands
from dotenv import load_dotenv

# Load from a local .env file (optional). 
# You can also set these in your CI/CD or hosting platform directly.
load_dotenv()

# ——— Configuration ———
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
CLIENT_ID     = os.getenv("DISCORD_CLIENT_ID")
PERMISSIONS   = os.getenv("DISCORD_PERMISSIONS")  # e.g. "1755381623276608"
INVITE_SCOPES = "bot applications.commands"

# Validate
if not DISCORD_TOKEN:
    raise RuntimeError("❌ Missing DISCORD_TOKEN environment variable.")
if not CLIENT_ID:
    raise RuntimeError("❌ Missing DISCORD_CLIENT_ID environment variable.")
if not PERMISSIONS:
    raise RuntimeError("❌ Missing DISCORD_PERMISSIONS environment variable.")



# Build invite link
INVITE_URL = (
    f"https://discord.com/oauth2/authorize"
    f"?client_id={CLIENT_ID}"
    f"&scope={INVITE_SCOPES.replace(' ', '%20')}"
    f"&permissions={PERMISSIONS}"
)
CLIENT_ID = 1374628149840711761

# ——— Bot Setup ———
intents = disnake.Intents.default()
intents.messages = True
intents.guilds   = True

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    # Print out useful info on startup
    print(f"✅ Logged in as {bot.user}")
    print(f"🔗 Invite your bot with:\n{INVITE_URL}")

@bot.slash_command(description="Roll a dice in NdM format (e.g. 2d6).")
async def roll(inter, dice: str):
    try:
        if 'd' not in dice.lower():
            raise ValueError("Format must be 'NdM', e.g. '2d6'.")
        number, sides = map(int, dice.lower().split('d'))
        MAX_ROLLS = 100
        if not (1 <= number <= MAX_ROLLS):
            raise ValueError(f"Allowed rolls: 1 to {MAX_ROLLS}.")
        rolls = [random.randint(1, sides) for _ in range(number)]
        await inter.response.send_message(f"🎲 Rolls: {rolls}  →  Total: {sum(rolls)}")
    except ValueError as e:
        await inter.response.send_message(f"❗ Error: {e}")

@bot.slash_command(description="Start recording (placeholder).")
async def record(inter):
    await inter.response.send_message("🛑 Recording started! (Feature implementation pending.)")

if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)
