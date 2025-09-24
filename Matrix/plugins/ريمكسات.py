

import asyncio
import os

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from . import blal
from ..core.logger import logging

from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply

plugin_category = "البحث"

@blal.dev_cmd(
    pattern="ريماكس ([\\s\\S]*)",
    command=("ريماكس", plugin_category),
    info={
        "header": "ريمكسـات اغـانـي قصيـره",
        "الاستـخـدام": "{tr}ريماكس + كلمـة",
    },
)
async def remaxdevthon(devrm):
    ok = devrm.pattern_match.group(1)
    if not ok:
        if devrm.is_reply:
            what = (await devrm.get_reply_message()).message
        else:
            await devrm.edit("`Sir please give some query to search and download it for you..!`")
            return
    sticcers = await bot.inline_query(
        "spotifybot", f"{(deEmojify(ok))}")
    await sticcers[0].click(devrm.chat_id,
                            reply_to=devrm.reply_to_msg_id,
                            silent=True if devrm.is_reply else False,
                            hide_via=True)
    await devrm.delete()
    

@blal.dev_cmd(
    pattern="ريمكس ([\\s\\S]*)",
    command=("ريمكس", plugin_category),
    info={
        "header": "ريمكسـات اغـانـي قصيـره",
        "الاستـخـدام": "{tr}ريمكس + كلمـة",
    },
)
async def dev(event):
    if event.fwd_from:
        return
    devr = event.pattern_match.group(1)
    Matrixal = "@spotifybot"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(Matrixal, devr)
    await tap[0].click(event.chat_id)
    await event.delete()

