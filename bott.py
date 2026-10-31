import asyncio
import os
import random

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton
)
from dotenv import load_dotenv


# Загружаем токен
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("Не найден токен! Проверь файл .env")


# Создаём бота
bot = Bot(token=TOKEN)
dp = Dispatcher()


# Создаём кнопки меню
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🏋️ Тренировка"),
            KeyboardButton(text="🔥 Разминка")
        ],
        [
            KeyboardButton(text="💪 Мотивация"),
            KeyboardButton(text="📅 Мой план")
        ],
        [
            KeyboardButton(text="ℹ️ Помощь")
        ]
    ],
    resize_keyboard=True
)


# Приветствие
async def show_welcome(message: Message):
    await message.answer(
        f"Привет, {message.from_user.first_name}! 👋\n\n"
        "Я SportBuddy — твой спортивный помощник! 🏆\n"
        "Помогу тебе поддерживать активность и мотивацию.\n\n"
        "Выбери действие в меню ниже!",
        reply_markup=main_keyboard
    )


# Команда /start
@dp.message(Command("start"))
async def start_command(message: Message):
    await show_welcome(message)


# Команда /help
@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer(
        "📌 Команды SportBuddy:\n\n"
        "/start — открыть меню\n"
        "/help — помощь\n"
        "/workout — тренировка\n"
        "/warmup — разминка\n"
        "/motivation — мотивация\n"
        "/plan — план активности",
        reply_markup=main_keyboard
    )


# Тренировка
async def send_workout(message: Message):
    await message.answer(
        "🏋️ ТВОЯ ТРЕНИРОВКА\n\n"
        "1. Приседания — 10 раз\n"
        "2. Отжимания от стены — 10 раз\n"
        "3. Ходьба на месте — 1 минута\n"
        "4. Подъём коленей — 20 секунд\n\n"
        "Начинай спокойно и в комфортном темпе!\n"
        "При боли или головокружении остановись."
    )


@dp.message(Command("workout"))
async def workout_command(message: Message):
    await send_workout(message)


@dp.message(F.text == "🏋️ Тренировка")
async def workout_button(message: Message):
    await send_workout(message)


# Разминка
async def send_warmup(message: Message):
    await message.answer(
        "🔥 РАЗМИНКА\n\n"
        "1. Круговые движения плечами — 20 секунд.\n"
        "2. Повороты корпуса — 20 секунд.\n"
        "3. Ходьба на месте — 1 минута.\n"
        "4. Лёгкие движения руками и ногами.\n\n"
        "Не делай резких движений!"
    )


@dp.message(Command("warmup"))
async def warmup_command(message: Message):
    await send_warmup(message)


@dp.message(F.text == "🔥 Разминка")
async def warmup_button(message: Message):
    await send_warmup(message)


# Мотивация
async def send_motivation(message: Message):
    phrases = [
        "💪 Ты сильнее, чем думаешь!",
        "🏆 Каждый маленький шаг имеет значение!",
        "🔥 Главное — не останавливаться!",
        "🌟 Твой результат начинается с первого шага!",
        "❤️ Заботься о себе и двигайся в своём темпе!"
    ]

    await message.answer(random.choice(phrases))


@dp.message(Command("motivation"))
async def motivation_command(message: Message):
    await send_motivation(message)


@dp.message(F.text == "💪 Мотивация")
async def motivation_button(message: Message):
    await send_motivation(message)


# План активности
async def send_plan(message: Message):
    await message.answer(
        "📅 ТВОЙ ПЛАН НА ДЕНЬ\n\n"
        "🌅 Утро — лёгкая разминка.\n"
        "☀️ День — прогулка.\n"
        "🏃 Вечер — активность по самочувствию.\n"
        "🌙 Ночь — отдых и восстановление.\n\n"
        "Помни: отдых тоже важен!"
    )


@dp.message(Command("plan"))
async def plan_command(message: Message):
    await send_plan(message)


@dp.message(F.text == "📅 Мой план")
async def plan_button(message: Message):
    await send_plan(message)


# Кнопка помощи
@dp.message(F.text == "ℹ️ Помощь")
async def help_button(message: Message):
    await help_command(message)


# Ответы на обычные сообщения
@dp.message()
async def text_handler(message: Message):
    if not message.text:
        await message.answer("Я пока понимаю только текстовые сообщения 😊")
        return

    text = message.text.lower()

    if "привет" in text:
        await message.answer("Привет, спортсмен! 👋")

    elif "спасибо" in text:
        await message.answer("Всегда пожалуйста! ❤️")

    elif "устал" in text or "устала" in text:
        await message.answer(
            "Не забывай отдыхать. Восстановление тоже часть спорта! ❤️"
        )

    else:
        await message.answer(
            "Я твой SportBuddy! 🏆\n"
            "Выбери кнопку меню или напиши /help."
        )


# Запуск бота
async def main():
    print("SportBuddy успешно запущен! 🏆")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
