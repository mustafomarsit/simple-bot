import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import os

bot = Bot(os.getenv("BOT_TOKEN"))
dp = Dispatcher()

# Tugmalar
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Help"), KeyboardButton(text="About")],
        [KeyboardButton(text="Info"), KeyboardButton(text="Language")]
    ],
    resize_keyboard=True
)

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer(
        f"Hello, {message.from_user.first_name}! Welcome to the bot.",
        reply_markup=keyboard
    )

@dp.message(Command("help"))
@dp.message(lambda msg: msg.text.lower() == "help")
async def help_handler(message: types.Message):
    await message.answer("Available commands:\n/start - Start the bot\n/help - Show help\n/about - Info about the bot\n/info - User info\n/language - Language settings")

@dp.message(Command("about"))
@dp.message(lambda msg: msg.text.lower() == "about")
async def about_handler(message: types.Message):
    await message.answer(
        "📌 Bot haqida:\n"
        "Bu bot Aiogram yordamida mashq qilish uchun yaratilgan.\n\n"
        "👨‍💻 Muallif: Mustafo Tolibjonov\n"
        "🎓 Mars IT School o‘quvchisi, 11-sinf\n"
        "💻 Yo‘nalish: Python (Backend), Aiogram\n"
        "📅 Boshlangan sana: 2025-yil\n"
        "🎯 Maqsad: Kuchli backend dasturchi bo‘lish\n"
        "📱 Aloqa: @tol1bjono_v"
    )


@dp.message(Command("info"))
@dp.message(lambda msg: msg.text.lower() == "info")
async def info_handler(message: types.Message):
    user = message.from_user
    await message.answer(
        f"👤 Name: {user.first_name}\n"
        f"🆔 ID: {user.id}\n"
        f"🔗 Username: @{user.username if user.username else 'yo‘q'}\n\n"
        f"📌 Bot author info:\n"
        f"👨‍💻 Name: Mustafo Tolibjonov\n"
        f"🎓 Student at Mars IT School\n"
        f"💻 Learning: Python & Aiogram\n"
        f"🎯 Goal: To become a strong backend developer"
    )


@dp.message(Command("language"))
@dp.message(lambda msg: msg.text.lower() == "language")
async def language_handler(message: types.Message):
    await message.answer("Currently only English is available.\nMore languages coming soon!")

def on_start():
    print("Bot has been started...")

async def main():
    dp.startup.register(on_start)
    await dp.start_polling(bot)

asyncio.run(main())
