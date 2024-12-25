from aiogram import Bot, Dispatcher, types, F

def register(dp:Dispatcher, bot:Bot):
    @dp.message(F.text.lower().startswith("!модер"))
    @dp.message(F.text.lower().startswith("+модер"))
    @dp.message(F.text.lower().startswith("+модер")) # это такой убогий говнокод 😭
    async def setRank(msg:types.Message):
        # потом переделаю ибо мне лень
        pass