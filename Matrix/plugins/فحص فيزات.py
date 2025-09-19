# dev-Thon - ZelZal
# Copyright (C) 2022 BiLaL . All Rights Reserved
#
# This file is a part of < https://github.com/dev-Thon/ZelZal/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/dev-Thon/ZelZal/blob/main/LICENSE/>.
# الملــف محمــي بحقــوق النشـــر والملـكيـه
# تخمــط بــدون ذكــر المصــدر ابلــع حســابـك بانـــد
""" 
CC Checker & Generator for BDB0B™ t.me/BiLaL
Write file by Zelzal t.me/zzzzl1l
hhh o ya beby

"""

import asyncio
import os
import sys
import urllib.request
from datetime import timedelta
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest as unblock
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from Matrix import blal

from ..core.managers import edit_or_reply

plugin_category = "البوت"


# code by t.me/zzzzl1l
@blal.dev_cmd(pattern="فحص فيزات 2(?:\s|$)([\s\S]*)")
async def song2(event):
    song = event.pattern_match.group(1)
    chat = "@SakuraRendibot" # code by t.me/zzzzl1l
    reply_id_ = await reply_id(event)
    dev = await edit_or_reply(event, "**⎉╎جـارِ فحص البطـاقـةُ ...**")
    async with event.client.conversation(chat) as conv:
        try:
            gool = "/chk {}".format(song)
            await conv.send_message(gool)
        except YouBlockedUserError:
            await blal(unblock("SakuraRendibot"))
            gool = "/chk {}".format(song)
            await conv.send_message(gool)
        await asyncio.sleep(22)
        response = await conv.get_response()
        if response.text.startswith("ANTI_SPAM:"):
        	return await dev.edit("**- حاول مجـدداً ولا تستخـدم سبـام ...**")
        if response.text.startswith("RISK:"):
        	return await dev.edit("**- خطـأ :**\n**أعد محاولة فحص هذه البطاقه ...لاحقًا**")
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_message(event.chat_id, response.message)
        await dev.delete()


# code by t.me/zzzzl1l
@blal.dev_cmd(pattern="فحص فيزات(?:\s|$)([\s\S]*)")
async def song2(event):
    song = event.pattern_match.group(1)
    chat = "@SDBB_Bot" # code by t.me/zzzzl1l
    reply_id_ = await reply_id(event)
    dev = await edit_or_reply(event, "**⎉╎جـارِ فحص البطـاقـةُ ...**")
    async with event.client.conversation(chat) as conv:
        try:
            gool = "/chk {}".format(song)
            await conv.send_message(gool)
        except YouBlockedUserError:
            await blal(unblock("SDBB_Bot"))
            gool = "/chk {}".format(song)
            await conv.send_message(gool)
        await asyncio.sleep(22)
        response = await conv.get_response()
        if response.text.startswith("ANTI_SPAM:"):
        	return await dev.edit("**- حاول مجـدداً ولا تستخـدم سبـام ...**")
        if response.text.startswith("RISK:"):
        	return await dev.edit("**- خطـأ :**\n**أعد محاولة فحص هذه البطاقه ...لاحقًا**")
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_message(event.chat_id, response.message)
        await dev.delete()
        
 
# code by t.me/zzzzl1l
@blal.dev_cmd(pattern="تاريخ انشاء الحساب(?:\s|$)([\s\S]*)")
async def song2(event):
    song = event.pattern_match.group(1)
    chat = "@PPAQBot" # code by t.me/zzzzl1l
    reply_id_ = await reply_id(event)
    dev = await edit_or_reply(event, "**⎉╎جـارِ معرفـة تاريـخ إنشاء حسابـك**")
    async with event.client.conversation(chat) as conv:
        try:
            gool = "{}".format(song)
            await conv.send_message(gool)
        except YouBlockedUserError:
            await blal(unblock("PPAQBot"))
            gool = "{}".format(song)
            await conv.send_message(gool)
        await asyncio.sleep(22)
        response = await conv.get_response()
        if response.text.startswith("ANTI_SPAM:"):
        	return await dev.edit("**- حاول مجـدداً ولا تستخـدم سبـام ...**")
        if response.text.startswith("RISK:"):
        	return await dev.edit("**- خطـأ :**\n**أعد المحـــــاولـة...لاحقًا**")
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_message(event.chat_id, response.message)
        await dev.delete()


# code by t.me/zzzzl1l
@blal.dev_cmd(pattern="عدسة الصورة(?:\s|$)([\s\S]*)")
async def song2(event):
    song = event.pattern_match.group(1)
    chat = "@linksalibot" # code by t.me/zzzzl1l
    reply_id_ = await reply_id(event)
    dev = await edit_or_reply(event, "**⎉ جـــارِِ استخـراج النـص من الصـورة...**")
    async with event.client.conversation(chat) as conv:
        try:
            gool = "{}".format(song)
            await conv.send_message(gool)
        except YouBlockedUserError:
            await blal(unblock("linksalibot"))
            gool = "{}".format(song)
            await conv.send_message(gool)
        await asyncio.sleep(22)
        response = await conv.get_response()
        if response.text.startswith("ANTI_SPAM:"):
        	return await dev.edit("**- حاول مجـــددًا ولا تستخـدم سبـام ...**")
        if response.text.startswith("RISK:"):
        	return await dev.edit("**- خطـأ :**\n**أعد المحاولـة...لاحقًا**")
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_message(event.chat_id, response.message)
        await dev.delete()
 
 
# code by t.me/zzzzl1l
@blal.dev_cmd(pattern="كومبو(?:\s|$)([\s\S]*)")
async def song2(event): # code by t.me/zzzzl1l
    been = event.pattern_match.group(1)
    chat = "@SDBB_Bot"
    reply_id_ = await reply_id(event)
    dev = await edit_or_reply(event, f"**⎉╎جـارِ جلب كومبـو لـ البين {been}  ...**\n**⎉╎عـدد 10 بطاقـات 💳**")
    async with event.client.conversation(chat) as conv:
        try:
            gool = "/gen {}".format(been)
            await conv.send_message(gool)
        except YouBlockedUserError:
            await blal(unblock("SDBB_Bot"))
            gool = "/gen {}".format(been)
            await conv.send_message(gool)
        await asyncio.sleep(5)
        response = await conv.get_response()
        if response.text.startswith("ANTI_SPAM:"):
        	return await dev.edit("**- حاول مجـدداً ولا تستخـدم سبـام ...**")
        if response.text.startswith("RISK:"):
        	return await dev.edit("**- خطـأ :**\n**أعد محاولة فحص هذه البطاقه ...لاحقًا**")
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_message(event.chat_id, response.message)
        await dev.delete()


# code by t.me/zzzzl1l
@blal.dev_cmd(pattern="معلومات فيزا وهمية(?:\s|$)([\s\S]*)")
async def song2(event):
    song = event.pattern_match.group(1)
    chat = "@SDBB_Bot" # code by t.me/zzzzl1l
    reply_id_ = await reply_id(event)
    dev = await edit_or_reply(event, "**⎉╎جـار جلب معلومـات الفيـزا ...**")
    async with event.client.conversation(chat) as conv:
        try:
            gool = "/fake {}".format(song)
            await conv.send_message(gool)
        except YouBlockedUserError:
            await blal(unblock("SDBB_Bot"))
            gool = "/fake {}".format(song)
            await conv.send_message(gool)
        await asyncio.sleep(22)
        response = await conv.get_response()
        if response.text.startswith("ANTI_SPAM:"):
        	return await dev.edit("**- حاول مجـدداً ولا تستخـدم سبـام ...**")
        if response.text.startswith("RISK:"):
        	return await dev.edit("**- خطـأ :**\n**أعد محاولة فحص هذه البطاقه ...لاحقًا**")
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_message(event.chat_id, response.message)
        await dev.delete()
        
        
# code by t.me/zzzzl1l
@blal.dev_cmd(pattern="توليد(?:\s|$)([\s\S]*)")
async def song2(event):
    been = event.pattern_match.group(1)
    chat = "@SDBB_Bot" # code by t.me/zzzzl1l
    reply_id_ = await reply_id(event)
    dev = await edit_or_reply(event, f"**⎉╎جـارِ جلب كومبـو لـ البين {been}  ...**\n**⎉╎عـدد 10 بطاقـات 💳**")
    async with event.client.conversation(chat) as conv:
        try:
            gool = "/gen {}".format(been)
            await conv.send_message(gool)
        except YouBlockedUserError:
            await blal(unblock("SDBB_Bot"))
            gool = "/gen {}".format(been)
            await conv.send_message(gool)
        await asyncio.sleep(5)
        response = await conv.get_response()
        if response.text.startswith("ANTI_SPAM:"):
        	return await dev.edit("**- حاول مجـدداً ولا تستخـدم سبـام ...**")
        if response.text.startswith("RISK:"):
        	return await dev.edit("**- خطـأ :**\n**أعد محاولة فحص هذه البطاقه ...لاحقًا**")
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_message(event.chat_id, response.message)
        await dev.delete()


# code by t.me/zzzzl1l
@blal.dev_cmd(pattern="فيزا(?:\s|$)([\s\S]*)")
async def song2(event):
    been = "415464xxxxxxxxxx|xx|xxxx|xxx" # code by t.me/zzzzl1l
    chat = "@SDBB_Bot" # code by t.me/zzzzl1l
    reply_id_ = await reply_id(event)
    dev = await edit_or_reply(event, f"**⎉╎جـارِ تولـيد 𝚅𝙸𝚂𝙴💲...**\n**⎉╎لـ البين {been}  ...**\n**⎉╎عـدد 10 بطاقـات 💳**")
    async with event.client.conversation(chat) as conv:
        try:
            gool = "/gen {}".format(been)
            await conv.send_message(gool)
        except YouBlockedUserError:
            await blal(unblock("SDBB_Bot"))
            gool = "/gen {}".format(been)
            await conv.send_message(gool)
        await asyncio.sleep(5)
        response = await conv.get_response()
        if response.text.startswith("ANTI_SPAM:"):
        	return await dev.edit("**- حاول مجـدداً ولا تستخـدم سبـام ...**")
        if response.text.startswith("RISK:"):
        	return await dev.edit("**- خطـأ :**\n**أعد محاولة فحص هذه البطاقه ...لاحقًا**")
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_message(event.chat_id, response.message)
        await dev.delete()


# code by t.me/zzzzl1l
@blal.dev_cmd(pattern="ماستر(?:\s|$)([\s\S]*)")
async def song2(event):
    been = "524447000053xxxx|xx|xxxx|xxx" # code by t.me/zzzzl1l
    chat = "@SDBB_Bot" # code by t.me/zzzzl1l
    reply_id_ = await reply_id(event)
    dev = await edit_or_reply(event, f"**⎉╎جـارِ تولـيد بن 𝙼𝙰𝚂𝚃𝙴𝚁𝙲𝙰𝚁𝙳 💳...**\n**⎉╎لـ البين {been}  ...**\n**⎉╎عـدد 10 بطاقـات 💳**")
    async with event.client.conversation(chat) as conv:
        try:
            gool = "/gen {}".format(been)
            await conv.send_message(gool)
        except YouBlockedUserError:
            await blal(unblock("SDBB_Bot"))
            gool = "/gen {}".format(been)
            await conv.send_message(gool)
        await asyncio.sleep(5)
        response = await conv.get_response()
        if response.text.startswith("ANTI_SPAM:"):
        	return await dev.edit("**- حاول مجـدداً ولا تستخـدم سبـام ...**")
        if response.text.startswith("RISK:"):
        	return await dev.edit("**- خطـأ :**\n**أعد محاولة فحص هذه البطاقه ...لاحقًا**")
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_message(event.chat_id, response.message)
        await dev.delete()


# code by t.me/zzzzl1l
@blal.dev_cmd(pattern="اماكس(?:\s|$)([\s\S]*)")
async def song2(event):
    been = "373352589xxxxxx|xx|xxxx|xxxx" # code by t.me/zzzzl1l
    chat = "@SDBB_Bot" # code by t.me/zzzzl1l
    reply_id_ = await reply_id(event)
    dev = await edit_or_reply(event, f"**⎉╎جـارِ تولـيد بن 🇧🇷 𝙰𝙼𝙴𝚇...**\n**⎉╎لـ البين {been}  ...**\n**⎉╎عـدد 10 بطاقـات 💳**")
    async with event.client.conversation(chat) as conv:
        try:
            gool = "/gen {}".format(been)
            await conv.send_message(gool)
        except YouBlockedUserError:
            await blal(unblock("SDBB_Bot"))
            gool = "/gen {}".format(been)
            await conv.send_message(gool)
        await asyncio.sleep(5)
        response = await conv.get_response()
        if response.text.startswith("ANTI_SPAM:"):
        	return await dev.edit("**- حاول مجـدداً ولا تستخـدم سبـام ...**")
        if response.text.startswith("RISK:"):
        	return await dev.edit("**- خطـأ :**\n**أعد محاولة فحص هذه البطاقه ...لاحقًا**")
        await event.client.send_read_acknowledge(conv.chat_id)
        await event.client.send_message(event.chat_id, response.message)
        await dev.delete()

