from aiogram import Dispatcher, types
import utils

def register(dp:Dispatcher):
    @dp.message()
    async def onMessage(msg:types.Message):
        await utils.onMessage(msg)