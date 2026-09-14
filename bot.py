import os
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_Token")

if not BOT_TOKEN:
    raise RuntimeError("BOT_TOKEN is not configured")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


def main_menu():
    kb = InlineKeyboardBuilder()

    kb.button(text="🔗 Connect Account", callback_data="connect")
    kb.button(text="📝 Register Account", callback_data="register")
    kb.button(text="🔐 Login Account", callback_data="login")
    kb.button(text="🟢 Server Status & Price", callback_data="status")
    kb.button(text="⬇️ Download Tool", callback_data="download")
    kb.button(text="💬 Contact Us", callback_data="contact")

    kb.adjust(1, 2, 1, 1, 1)
    return kb.as_markup()


@dp.message(CommandStart())
async def start_handler(message: Message):
    text = (
        "🔥 <b>FIRE FRP TOOL</b>\n"
        "Professional Android Service Tool\n\n"
        "🔗 <b>Welcome!</b>\n"
        "Your account is not connected yet.\n\n"
        "Connect your account to access available bot features."
    )

    await message.answer(
        text,
        reply_markup=main_menu(),
        parse_mode="HTML"
    )


@dp.callback_query(F.data == "connect")
async def connect_handler(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "🔗 <b>Connect Account</b>\n\n"
        "Your account is not connected yet.\n"
        "Please register or login first.",
        parse_mode="HTML"
    )


@dp.callback_query(F.data == "register")
async def register_handler(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "📝 <b>Register Account</b>\n\n"
        "Registration system will be added here.",
        parse_mode="HTML"
    )


@dp.callback_query(F.data == "login")
async def login_handler(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "🔐 <b>Login Account</b>\n\n"
        "Login system will be added here.",
        parse_mode="HTML"
    )


@dp.callback_query(F.data == "status")
async def status_handler(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "🟢 <b>Server Status</b>\n\n"
        "🟢 Server: Online\n"
        "⚡ Response: Normal\n\n"
        "💰 <b>Price</b>\n"
        "Contact admin for current pricing.",
        parse_mode="HTML"
    )


@dp.callback_query(F.data == "download")
async def download_handler(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "⬇️ <b>Download Tool</b>\n\n"
        "Download link will be available here.",
        parse_mode="HTML"
    )


@dp.callback_query(F.data == "contact")
async def contact_handler(callback: CallbackQuery):
    await callback.answer()
    await callback.message.answer(
        "💬 <b>Contact Us</b>\n\n"
        "Please contact the administrator for support.",
        parse_mode="HTML"
    )


async def main():
    print("🔥 Fire Telegram Bot is running...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
