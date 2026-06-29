import json
import aiosqlite

DB_PATH = "data/conversations.db"
MAX_HISTORY = 10


async def init_db() -> None:
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS conversations (
                user_id INTEGER PRIMARY KEY,
                messages TEXT NOT NULL DEFAULT '[]',
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
        await db.commit()


async def get_history(user_id: int) -> list[dict]:
    async with aiosqlite.connect(DB_PATH) as db:
        async with db.execute(
            "SELECT messages FROM conversations WHERE user_id = ?", (user_id,)
        ) as cursor:
            row = await cursor.fetchone()
            return json.loads(row[0]) if row else []


async def save_history(user_id: int, messages: list[dict]) -> None:
    messages = messages[-MAX_HISTORY:]
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            INSERT INTO conversations (user_id, messages, updated_at)
            VALUES (?, ?, CURRENT_TIMESTAMP)
            ON CONFLICT(user_id) DO UPDATE SET
                messages = excluded.messages,
                updated_at = excluded.updated_at
        """, (user_id, json.dumps(messages, ensure_ascii=False)))
        await db.commit()


async def clear_history(user_id: int) -> None:
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("DELETE FROM conversations WHERE user_id = ?", (user_id,))
        await db.commit()
