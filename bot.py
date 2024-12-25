from aiogram.filters import ChatMemberUpdatedFilter, JOIN_TRANSITION
from aiogram.types.chat_member_updated import ChatMemberUpdated
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from aiogram import Bot, Dispatcher
import modules.moderation
import modules.other
import modules.test
import asyncio
import config
import utils

bot = Bot(token=config.TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


@dp.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=JOIN_TRANSITION))
async def greet(event:ChatMemberUpdated, bot:Bot):
    await utils.greet(event, bot)


async def main():
    modules.test.register(dp)
    modules.moderation.register(dp, bot)
    modules.other.register(dp)
    print("started")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())