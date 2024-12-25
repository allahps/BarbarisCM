import asyncio
import logging
import re
import os
import random

from contextlib import suppress
from datetime import datetime, timedelta

from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters import Command, CommandObject
from aiogram.client.default import DefaultBotProperties
from aiogram.exceptions import TelegramBadRequest
from aiogram.enums.parse_mode import ParseMode
from aiogram.enums.chat_member_status import ChatMemberStatus
import sqlite3
import utils

def register(dp:Dispatcher):
    @dp.message(F.text.lower().startswith("юзер"))
    async def test(msg:types.Message):
        te = await utils.getUser(msg.text.split()[1])
        await msg.reply(str(te))