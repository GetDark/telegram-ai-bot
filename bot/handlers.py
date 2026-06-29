from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from bot.groq_client import ask
from bot.storage import clear_history, get_history, save_history

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message) -> None:
    await message.answer(
        "Привет! Я AI-ассистент на базе Llama 3.1 🤖\n\n"
        "Просто напиши мне что-нибудь — отвечу.\n\n"
        "/clear — очистить историю диалога\n"
        "/help — помощь"
    )


@router.message(Command("help"))
async def cmd_help(message: Message) -> None:
    await message.answer(
        "Команды:\n"
        "/start — начать диалог\n"
        "/clear — очистить историю\n"
        "/help — эта справка\n\n"
        "Пиши любой вопрос — отвечу с учётом контекста диалога."
    )


@router.message(Command("clear"))
async def cmd_clear(message: Message) -> None:
    await clear_history(message.from_user.id)
    await message.answer("История диалога очищена ✅")


@router.message()
async def handle_message(message: Message) -> None:
    if not message.text:
        return

    user_id = message.from_user.id

    await message.bot.send_chat_action(message.chat.id, "typing")

    history = await get_history(user_id)
    history.append({"role": "user", "content": message.text})

    try:
        reply = await ask(history)
        history.append({"role": "assistant", "content": reply})
        await save_history(user_id, history)
        await message.answer(reply)
    except Exception:
        await message.answer("Произошла ошибка. Попробуй ещё раз.")
