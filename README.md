[English](#english) | [Русский](#русский)

---

<a name="english"></a>
# telegram-ai-bot

A Telegram bot powered by Groq API (Llama 3.1) with persistent per-user conversation history. Deployed via Docker.

## Features

- Answers messages using **Llama 3.1** via Groq API
- Maintains **conversation history** per user across messages
- Commands:
  - `/start` — welcome message and instructions
  - `/help` — show available commands
  - `/clear` — clear conversation history

## Quick Start

```bash
git clone https://github.com/GetDark/telegram-ai-bot.git
cd telegram-ai-bot

cp .env.example .env
nano .env  # set TELEGRAM_TOKEN and GROQ_API_KEY

docker compose up -d
```

## Environment Variables

| Variable | Description |
|----------|-------------|
| `TELEGRAM_TOKEN` | Bot token from [@BotFather](https://t.me/BotFather) |
| `GROQ_API_KEY` | API key from [console.groq.com](https://console.groq.com) |

## Project Structure

```
bot/
├── main.py          # Entry point, bot startup
├── handlers.py      # Message and command handlers
├── groq_client.py   # Groq API client
└── storage.py       # Conversation history (SQLite)
```

## Tech Stack

- Python 3 / aiogram 3
- Groq API (Llama 3.1)
- SQLite (conversation history)
- Docker + Docker Compose

---

<a name="русский"></a>
# telegram-ai-bot

Telegram-бот на базе Groq API (Llama 3.1) с постоянной историей диалога для каждого пользователя. Деплой через Docker.

## Возможности

- Отвечает на сообщения с помощью **Llama 3.1** через Groq API
- Сохраняет **историю диалога** для каждого пользователя
- Команды:
  - `/start` — приветствие и инструкции
  - `/help` — список доступных команд
  - `/clear` — очистить историю диалога

## Быстрый старт

```bash
git clone https://github.com/GetDark/telegram-ai-bot.git
cd telegram-ai-bot

cp .env.example .env
nano .env  # задать TELEGRAM_TOKEN и GROQ_API_KEY

docker compose up -d
```

## Переменные окружения

| Переменная | Описание |
|------------|----------|
| `TELEGRAM_TOKEN` | Токен бота от [@BotFather](https://t.me/BotFather) |
| `GROQ_API_KEY` | API-ключ с [console.groq.com](https://console.groq.com) |

## Структура проекта

```
bot/
├── main.py          # Точка входа, запуск бота
├── handlers.py      # Обработчики сообщений и команд
├── groq_client.py   # Клиент Groq API
└── storage.py       # История диалога (SQLite)
```

## Технологический стек

- Python 3 / aiogram 3
- Groq API (Llama 3.1)
- SQLite (история диалога)
- Docker + Docker Compose
