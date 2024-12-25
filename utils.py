from aiogram.filters import ChatMemberUpdatedFilter, JOIN_TRANSITION
from aiogram.types.link_preview_options import LinkPreviewOptions
from aiogram.types.chat_member_updated import ChatMemberUpdated
from aiogram.enums.parse_mode import ParseMode
from aiogram import Bot, types
from aiogram import types
import database as db

greeting = """✅ Я так рад, что меня добавили. Пока я признаю команды только админов этого чата.
⚙️ Со списком всех команд можно ознакомиться в <a href="https://teletype.in/@iris_cm/commands">нашей статье</a>

⚪️ В целях безопасности от спама в чате по умолчанию установлен лимит одновременных инвайтов в 30 человек.
— Если вы хотите изменить этот лимит, введите "инвайты {число}", где число может быть 0, это отключит лимит

Остались вопросы? Можете обратиться в <a href="https://t.me/barbaris_cm_chat">наш официальный чат</a>"""

ranks = ["Участник", "Младший модератор", "Старший модератор", "Младший админ", "Старший админ", "Создатель"]


async def greet(event:ChatMemberUpdated, bot:Bot):
    admins = await event.chat.get_administrators()
    for admin in admins:
        if admin.status == "creator":
            db.setAdminValue(event.chat.id, admin.user.id, 5)
    await bot.send_message(chat_id=event.chat.id, text=greeting, parse_mode=ParseMode.HTML, link_preview_options=LinkPreviewOptions(is_disabled=True))


async def onMessage(msg:types.Message):
    db.checkUser(msg.chat.id, msg.from_user.id)

# функции для проверки чего-либо
def checkAccess(chatID:int, userID:int, cmd:str, levelNeeded:int) -> str:
    if db.getAdminValue(chatID, userID) >= levelNeeded:
        return None
    else:
        return f"📝 Команда доступна только с ранга {ranks[levelNeeded]} ({levelNeeded})\nОграничение: Команда «{cmd}»"
    
# функции для получения чего-либо
def parseUsername(args:list[str]) -> str:
    for elem in args:
        if "@" in elem or "t.me" in elem:
            return elem.replace("@", "").replace("https://t.me/", "").replace(".t.me", "")
    return None

def parseID(args:list[str]) -> id:
    for elem in args:
        if len(elem) in (9, 10) and elem.isdigit():
            return int(elem)
    return None