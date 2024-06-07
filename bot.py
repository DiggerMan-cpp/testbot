import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

API_TOKEN = 'YOUR_TELEGRAM_BOT_API_TOKEN'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Welcome to Coin Clicker Bot! Click the button below to open the clicker.", 
                        reply_markup=types.InlineKeyboardMarkup().add(
                            types.InlineKeyboardButton("Open Coin Clicker", web_app=types.WebAppInfo(url="YOUR_APP_URL"))
                        ))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
