import asyncio
from telegram import Bot

TOKEN = "8787363520:AAHpPtsSmAFP6c6XTgUPfSH31YykLtGOLjA"
CHAT_ID = "8843719025"

async def main():
bot = Bot(token=TOKEN)
await bot.send_message(chat_id=CHAT_ID, text="Hello! Your BIGDDGOAT_BOT is now working perfectly!")
print("Success")

if __name__ == "__main__":
asyncio.run(main())
