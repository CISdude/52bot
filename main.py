import discord
from discord.ext import tasks, commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import pytz


TOKEN = 'MTI2MDg4MjgzNzkwOTc5ODkyMw.G1xS12.MKQmOS8EpO5BHAbuHShk6TlYN7WGYs_dP0tVLw'


CHANNEL_ID = 1147832935504953346


GIF_URL = 'https://tenor.com/view/hu52ar-h52-batman-huszar-gif-26591124'


TIMEZONE = 'Etc/GMT-5'

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    scheduler.start()

async def send_gif():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(GIF_URL)
    else:
        print(f"Channel with ID {CHANNEL_ID} not found.")


scheduler = AsyncIOScheduler(timezone=pytz.timezone(TIMEZONE))
scheduler.add_job(send_gif, CronTrigger(minute=52, timezone=pytz.timezone(TIMEZONE)))

bot.run(TOKEN)
