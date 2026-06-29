# Telegram AI Bot 🤖

Telegram-бот с искусственным интеллектом на базе **Llama 3.1** (через Groq API).  
Помнит контекст диалога, отвечает на любые вопросы.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![aiogram](https://img.shields.io/badge/aiogram-3.x-blue)
![Groq](https://img.shields.io/badge/AI-Llama%203.1-green)

## Возможности

- 💬 Отвечает на вопросы через Llama 3.1 (Groq)
- 🧠 Помнит историю диалога (последние 10 сообщений)
- 🗑️ `/clear` — очистить историю
- 🐳 Деплой одной командой через Docker

## Быстрый старт

### 1. Получи API ключи

- **Telegram токен** — [@BotFather](https://t.me/BotFather)
- **Groq API Key** — [console.groq.com](https://console.groq.com)

### 2. Настрой окружение

```bash
cp .env.example .env
```

Заполни `.env`:

```
TELEGRAM_TOKEN=your_telegram_bot_token
GROQ_API_KEY=your_groq_api_key
```

### 3. Запусти через Docker

```bash
docker compose up -d
```

### 3. Или локально

```bash
pip install -r requirements.txt
python -m bot.main
```

## Команды бота

| Команда | Описание |
|---------|----------|
| `/start` | Начать диалог |
| `/clear` | Очистить историю |
| `/help` | Справка |

## Стек

- **Python 3.12**
- **aiogram 3.x** — Telegram Bot API
- **Groq** — быстрый inference Llama 3.1
- **SQLite** — хранение истории диалогов
- **Docker** — деплой
