from telegram import Bot
from apscheduler.schedulers.blocking import BlockingScheduler

TOKEN = 8029974864:AAEJ0_QzysihIb-T-bmGdXDoDWgM6voxVeA
CHANNEL_ID = -1003549531541   # replace with your channel id

LINK = "https://qqwinoo.com/?dl=9unx2l"

bot = Bot(TOKEN)
scheduler = BlockingScheduler()

def msg1():
    bot.send_message(CHANNEL_ID,
    f"🔥 காலை 6AM சிக்னல்\n\n👉 Join: {LINK}")

def msg2():
    bot.send_message(CHANNEL_ID,
    f"🚀 6:15AM Update\n\n👉 Register: {LINK}")

def msg3():
    bot.send_message(CHANNEL_ID,
    f"💰 6:30AM High Chance\n\n👉 Click: {LINK}")

scheduler.add_job(msg1, 'cron', hour=6, minute=0)
scheduler.add_job(msg2, 'cron', hour=6, minute=15)
scheduler.add_job(msg3, 'cron', hour=6, minute=30)

scheduler.start()