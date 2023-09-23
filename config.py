from decouple import config
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage




storage = MemoryStorage()
TOKEN = config("TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot, storage=storage)
ADMIN_ID = 5939724769
GROUP_ID = -4027099704
BOT_PIC = '/Users/adiletsaparbek/PycharmProjects/geek_33_1_bot/media/bot_pic.jpeg'
ANIMATION_PIC = 'C:/Users/Welcome/PycharmProjects/geek_33_1_telegram_bot/media/bot.gif'
DESTINATION_DIR = "C:/Users/Welcome/PycharmProjects/geek_33_1_telegram_bot/media"