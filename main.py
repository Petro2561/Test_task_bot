import asyncio
import logging

from aiogram import Bot, Dispatcher

from bot.handler import router
from config import Config, load_config


async def main():
    logging.basicConfig(level=logging.INFO)
    config: Config = load_config()
    bot = Bot(token=config.tg_bot.token)
    dp: Dispatcher = Dispatcher(
        name="main_dispatcher",
        config=config,
    )
    dp.include_router(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
