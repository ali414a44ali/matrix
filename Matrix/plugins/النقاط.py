import requests
import asyncio
import time
import re
from telethon import events
from telethon.errors import FloodWaitError
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.users import GetFullUserRequest

from Matrix import blal
from ..Config import Config
from ..core.managers import edit_delete, edit_or_reply
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from ..helpers.utils import reply_id
estithmar = False
ratp = False
thifts = False
bahsees = False

ZelzalCoins_cmd = (
    "[ᯓ 𝗦𝗼𝘂𝗿𝗰𝗲 𝗧𝗲𝗽𝘁𝗵𝗼𝗻 - أوامـر تجميـع النقـاط](t.me/Matrix) 𓆪\n\n"
    "**⎉╎قـائمـة أوامـر تجميـع نقـاط بوتـات تمـويـل الخاص بسـورس تيبثـون🦾 :** \n\n"
    "`.المليار`\n"
    "**⪼ لـ تجميـع النقـاط مـن بـوت المليـار ( @EEOBot ) .. تلقـائيًّـا ✓**\n\n"
    "`.العرب`\n"
    "**⪼ لـ تجميـع النقـاط مـن بـوت العـرب ( @TTZBoT ) .. تلقـائيًّــا ✓**\n\n"
    "`.دعمكم`\n"
    "**⪼ لـ تجميـع النقـاط مـن بـوت دعمكـم ( @DamKombot ) .. تلقـائيًّــا ✓**\n\n"
    "`.الجوكر`\n"
    "**⪼ لـ تجميـع النقـاط مـن بـوت الجوكـر ( @A_MAN9300BOT ) .. تلقائيًّـا ✓**\n\n"
    "`.الجنرال`\n"
    "**⪼ لـ تجميـع النقـاط مـن بـوت العقــاب ( @TTNBOT ) .. تلقائيًّـا ✓**\n\n"
      "`.آسياسيل`\n"
    "**⪼ لـ تجميـع النقـاط مـن بـوت آسياسيـل ( @yynnurybot ) .. تلقائيًّـا ✓**\n\n"
    "`.المليون`\n"
    "**⪼ لـ تجميـع النقـاط مـن بـوت المليــون ( @qweqwe1919bot ) .. تلقائيًّـا ✓**\n\n\n"
    "`.سمسم`\n"
    "**⪼ لـ تجميـع النقـاط مـن بـوت سمـسـم ( @SMSMWAbot ) .. تلقائيًّـا ✓**\n\n\n"
    "`.تناهيد`\n"
    "**⪼ لـ تجميـع النقـاط مـن بـوت تناهيـد ( @Ncoe_bot ) .. تلقائيًّـا ✓**\n\n"
    "`.المليار ايقاف`\n"
    "**⪼ لـ إيقاف عمليـة تجميـع النقـاط من بوت المليـار ..**\n\n"
    "`.الجوكر ايقاف`\n"
    "**⪼ لـ إيقاف عمليـة تجميـع النقـاط من بوت الجوكـر ..**\n\n"
    "`.العرب ايقاف`\n"
    "**⪼ لـ إيقاف عمليـة تجميـع النقـاط من بوت العـرب ..**\n\n"
    "`.العقاب ايقاف`\n"
    "**⪼ لـ إيقاف عمليـة تجميـع النقـاط من بوت العقـاب ..**\n\n"
    "`.المليون ايقاف`\n"
    "**⪼ لـ إيقاف عمليـة تجميـع النقـاط من بوت المليـون ..**\n\n"
    "`.سمسم ايقاف`\n"
    "**⪼ لـ إيقاف عمليـة تجميـع النقـاط من بوت سمـسـم ..**\n\n"
    "`.تناهيد ايقاف`\n"
    "**⪼ لـ إيقاف عمليـة تجميـع النقـاط من بوت تناهيـد ..**\n\n\n"
    "`.اضف بوت التجميع`\n"
    "**⪼ بالـرد على معـرف البـوت الجديـد لـ إضافته لـ السـورس ..**\n\n"
    "`.تجميع`\n"
    "**⪼ لـ تجميـع النقـاط مـن البـوت المضاف لـ الفـارات .. تلقائيًّا ✓**\n\n"
    "`.تجميع ايقاف`\n"
    "**⪼ لـ ايقـاف عمليـة تجميـع النقـاط من البوت المضاف للفـارات ..**\n\n"
    "`.بوت التجميع`\n"
    "**⪼ لـ عـرض بوت التجميـع المضـاف لـ الفـارات ..**\n\n\n"
    "**⎉╎قـائمـة أوامـر تجميـع نقـاط العـاب بـوت وعـد🦾 :** \n\n"
    "`.بخشيش وعد`\n"
    "`.راتب وعد`\n"
    "`.استثمار وعد`\n"
    "`.كلمات وعد`\n"
    "**⪼ لـ تجميـع نقـاط العـاب في بوت وعـد تلقائيًــا ✓ ..قم بـ إضافة البوت في مجموعة جديدة ثم أرسل**\n"
    "**الأمـر + عـدد الإعادة للأمـر**\n"
    "**⪼ مثــال :**\n"
    "`.راتب وعد 50`\n\n\n"
    "**- ملاحظـة :**\n"
    "**⪼ سيتم إضـافـة المزيـد من البوتـات بالتحديثـات القادمـة .. إذا تريـد إضـافة بـوت محـدد راسـل مطـور السـورس @o_p_g**"
)

@blal.dev_cmd(pattern="بوت المليار$")
async def _(event):
    await event.edit('@EEOBot')

# Copyright (C) 2022 dev-Thon . All Rights Reserved
@blal.dev_cmd(pattern="(المليار|تجميع المليار)(?: |$)(.*)")

async def _(event):
    con = event.pattern_match.group(1).lower()
    await event.edit("**⎉╎حسنًـا .. تأكـد من أنـك مشتـرك بـ قنـوات الاشتـراك الإجبـاري لتجنب الأخطـاء @EEOBot**")
    channel_entity = await blal.get_entity('@EEOBot')
    await blal.send_message('@EEOBot', '/start')
    await asyncio.sleep(4)
    msg0 = await blal.get_messages('@EEOBot', limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await blal.get_messages('@EEOBot', limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(10)
        list = await blal(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('**⎉╎لا يوجد قنوات في الوقت الحالي .. قم يتجميع النقاط بطريقة مختلفة**') != -1:
            await blal.send_message(event.chat_id, "**⎉╎مـافي قنـوات بالبـوت حاليًـا ...**")
            break
        if con == "ايقاف": #Code by T.me/zzzzl1l
            await blal.send_message(event.chat_id, "**⎉╎تم إيقـاف تجميـع النقـاط .. بنجـاح☑️**")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await blal(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await blal(ImportChatInviteRequest(bott))
            msg2 = await blal.get_messages('@EEOBot', limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**⎉╎تم الاشتـراك في القنـاة  {chs} ...✓**")
        except: #Code by T.me/zzzzl1l
            msg2 = await blal.get_messages('@EEOBot', limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**⎉╎القنـاة رقـم {chs} .. يمكـن تبنـدت**")
    await blal.send_message(event.chat_id, "**⎉╎تم الانتهـاء مـن تجميـع النقـاط .. حاول من جديد في وقت آخر ✓**")


@blal.dev_cmd(pattern="بوت العرب$")
async def _(event):
    await event.edit('@TTZBoT')

@blal.dev_cmd(pattern="(العرب|تجميع العرب)(?: |$)(.*)")
async def _(event):
    con = event.pattern_match.group(1).lower()
    await event.edit("**⎉╎حسنًـا .. تأكـد من أنـك مشتـرك بـ قنـوات الاشتـراك الإجبـاري لتجنب الأخطـاء @TTZBoT**")
    channel_entity = await blal.get_entity('@TTZBoT')
    await blal.send_message('@TTZBoT', '/start')
    await asyncio.sleep(4)
    msg0 = await blal.get_messages('@TTZBoT', limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await blal.get_messages('@TTZBoT', limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(10)
        list = await blal(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('**⎉╎لا يوجد قنوات في الوقت الحالي .. قم يتجميع النقاط بطريقة مختلفة**') != -1:
            await blal.send_message(event.chat_id, "**⎉╎مـافي قنـوات بالبـوت حاليًـا ...**")
            break
        if con == "ايقاف": #Code by T.me/zzzzl1l
            await blal.send_message(event.chat_id, "**⎉╎تم إيقـاف تجميـع النقـاط .. بنجـاح☑️**")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await blal(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await blal(ImportChatInviteRequest(bott))
            msg2 = await blal.get_messages('@TTZBoT', limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**⎉╎تم الاشتـراك في القنـاة  {chs} ...✓**")
        except: #Code by T.me/zzzzl1l
            msg2 = await blal.get_messages('@TTZBoT', limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**⎉╎القنـاة رقـم {chs} .. يمكـن تبنـدت**")
    await blal.send_message(event.chat_id, "**⎉╎تم الانتهـاء مـن تجميـع النقـاط .. حاول من جديد في وقت آخر ✓**")


@blal.dev_cmd(pattern="بوت التجميع$")
async def _(event):
    zpoint = gvarstatus("Z_Point")
    if gvarstatus("Z_Point") is None:
        await event.edit("**⎉╎لايوجـد بوت تجميع مضاف بعـد ؟!**\n\n**⎉╎لـ إضافة بوت تجميع جديد**\n**⎉╎ارسـل**  `.اضف بوت التجميع`  **بالـرد ع معـرف البـوت**")
    else:
        await event.edit(f"**⎉╎بوت التجميـع المضـاف حاليًـا**\n**⎉╎هـو** {zpoint}")

# Copyright (C) 2022 dev-Thon . All Rights Reserved
@blal.dev_cmd(pattern="تجميع(?: |$)(.*)")
async def _(event):
    con = event.pattern_match.group(1).lower()
    zpoint = gvarstatus("Z_Point")
    if con in ("المليار", "الجوكر", "الجنرال", "العقاب", "المليون", "سمسم", "تناهيد", "العرب"):
        return await event.edit("**⎉╎عـذرًا .. عـزيـزي امـر خاطـئ .\n⎉╎لـ رؤيـة أوامـر التجميـع ارسـل**\n\n`.اوامر التجميع`")
    if gvarstatus("Z_Point") is None:
        return await event.edit("**⎉╎لايوجـد بـوت تجميـع مضـاف للفـارات ؟!\n⎉╎لـ إضافة بـوت تجميـع\n⎉╎ارسـل** `.اضف بوت التجميع` **بالـرد ع معـرف البـوت\n\n⎉╎او استخـدم امر تجميع** `.المليار`")
    await event.edit(f"**⎉╎حسنًـا .. تأكـد من أنـك مشتـرك بـ قنـوات الاشتـراك الإجبـاري لتجنب الأخطـاء {zpoint} .**")
    channel_entity = await blal.get_entity(zpoint)
    await blal.send_message(zpoint, '/start')
    await asyncio.sleep(4)
    msg0 = await blal.get_messages(zpoint, limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await blal.get_messages(zpoint, limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(10)
        list = await blal(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('**⎉╎لا يوجد قنوات في الوقت الحالي .. قم يتجميع النقاط بطريقة مختلفة**') != -1:
            await blal.send_message(event.chat_id, "**⎉╎مـافي قنـوات بالبـوت حاليًـا ...**")
            break
        if con == "ايقاف": #Code by T.me/zzzzl1l
            await blal.send_message(event.chat_id, "**⎉╎تم إيقـاف تجميـع النقـاط .. بنجـاح☑️**")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await blal(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await blal(ImportChatInviteRequest(bott))
            msg2 = await blal.get_messages(zpoint, limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**⎉╎تم الاشتـراك في القنـاة  {chs} ...✓**")
        except: #Code by T.me/zzzzl1l
            msg2 = await blal.get_messages(zpoint, limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**⎉╎القنـاة رقـم {chs} .. يمكـن تبنـدت**")
    await blal.send_message(event.chat_id, "**⎉╎تم الانتهـاء مـن تجميـع النقـاط .. حاول من جديد في وقت آخر ✓**")


@blal.dev_cmd(pattern="بوت الجوكر$")
async def _(event):
    await event.edit('@A_MAN9300BOT')

# Copyright (C) 2022 dev-Thon . All Rights Reserved
@blal.dev_cmd(pattern="(الجوكر|تجميع الجوكر)(?: |$)(.*)")
async def _(event):
    con = event.pattern_match.group(1).lower()
    await event.edit("**⎉╎حسنًـا .. تأكـد من أنـك مشتـرك بـ قنـوات الاشتـراك الإجبـاري لتجنب الأخطـاء @A_MAN9300BOT**")
    channel_entity = await blal.get_entity('@A_MAN9300BOT')
    await blal.send_message('@A_MAN9300BOT', '/start')
    await asyncio.sleep(4)
    msg0 = await blal.get_messages('@A_MAN9300BOT', limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await blal.get_messages('@A_MAN9300BOT', limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(10)
        list = await blal(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('**⎉╎لا يوجد قنوات في الوقت الحالي .. قم يتجميع النقاط بطريقة مختلفة**') != -1:
            await blal.send_message(event.chat_id, "**⎉╎مـافي قنـوات بالبـوت حاليًـا ...**")
            break
        if con == "ايقاف": #Code by T.me/zzzzl1l
            await blal.send_message(event.chat_id, "**⎉╎تم إيقـاف تجميـع النقـاط .. بنجـاح☑️**")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await blal(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await blal(ImportChatInviteRequest(bott))
            msg2 = await blal.get_messages('@A_MAN9300BOT', limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**⎉╎تم الاشتـراك في القنـاة  {chs} ...✓**")
        except: #Code by T.me/zzzzl1l
            msg2 = await blal.get_messages('@A_MAN9300BOT', limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**⎉╎القنـاة رقـم {chs} .. يمكـن تبنـدت**")
    await blal.send_message(event.chat_id, "**⎉╎تم الانتهـاء مـن تجميـع النقـاط .. حاول من جديد في وقت آخر ✓**")


@blal.dev_cmd(pattern="بوت الجنرال$")
async def _(event):
    await event.edit('@TTNBOT')

# Copyright (C) 2022 dev-Thon . All Rights Reserved
@blal.dev_cmd(pattern="(الجنرال|تجميع الجنرال)(?: |$)(.*)")
async def _(event):
    con = event.pattern_match.group(1).lower()
    await event.edit("**⎉╎حسنًـا .. تأكـد من أنـك مشتـرك بـ قنـوات الاشتـراك الإجبـاري لتجنب الأخطـاء @TTNBOT**")
    channel_entity = await blal.get_entity('@TTNBOT')
    await blal.send_message('@TTNBOT', '/start')
    await asyncio.sleep(4)
    msg0 = await blal.get_messages('@TTNBOT', limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await blal.get_messages('@TTNBOT', limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(10)
        list = await blal(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('**⎉╎لا يوجد قنوات في الوقت الحالي .. قم يتجميع النقاط بطريقة مختلفة**') != -1:
            await blal.send_message(event.chat_id, "**⎉╎مـافي قنـوات بالبـوت حاليًـا ...**")
            break
        if con == "ايقاف": #Code by T.me/zzzzl1l
            await blal.send_message(event.chat_id, "**⎉╎تم إيقـاف تجميـع النقـاط .. بنجـاح☑️**")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await blal(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await blal(ImportChatInviteRequest(bott))
            msg2 = await blal.get_messages('@TTNBOT', limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**⎉╎تم الاشتـراك في القنـاة  {chs} ...✓**")
        except: #Code by T.me/zzzzl1l
            msg2 = await blal.get_messages('@TTNBOT', limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**⎉╎القنـاة رقـم {chs} .. يمكـن تبنـدت**")
    await blal.send_message(event.chat_id, "**⎉╎تم الانتهـاء مـن تجميـع النقـاط .. حاول من جديد في وقت آخر ✓**")


@blal.dev_cmd(pattern="بوت آسياسيل$")
async def _(event):
    await event.edit('@yynnurybot')

# Copyright (C) 2022 dev-Thon . All Rights Reserved
@blal.dev_cmd(pattern="(آسياسيل|تجميع آسياسيل)(?: |$)(.*)")
async def _(event):
    con = event.pattern_match.group(1).lower()
    await event.edit("**⎉╎حسنًـا .. تأكـد من أنـك مشتـرك بـ قنـوات الاشتـراك الإجبـاري لتجنب الأخطـاء @yynnurybot**")
    channel_entity = await blal.get_entity('@yynnurybot')
    await blal.send_message('@yynnurybot', '/start')
    await asyncio.sleep(4)
    msg0 = await blal.get_messages('@yynnurybot', limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await blal.get_messages('@yynnurybot', limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(10)
        list = await blal(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('**⎉╎لا يوجد قنوات في الوقت الحالي .. قم يتجميع النقاط بطريقة مختلفة**') != -1:
            await blal.send_message(event.chat_id, "**⎉╎مـافي قنـوات بالبـوت حاليًّـا ...**")
            break
        if con == "ايقاف": #Code by T.me/zzzzl1l
            await blal.send_message(event.chat_id, "**⎉╎تم إيقـاف تجميـع النقـاط .. بنجـاح☑️**")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await blal(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await blal(ImportChatInviteRequest(bott))
            msg2 = await blal.get_messages('@yynnurybot', limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**⎉╎تم الاشتـراك في القنـاة  {chs} ...✓**")
        except: #Code by T.me/zzzzl1l
            msg2 = await blal.get_messages('@yynnurybot', limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**⎉╎القنـاة رقـم {chs} .. يمكـن تبنـدت**")
    await blal.send_message(event.chat_id, "**⎉╎تم الانتهـاء مـن تجميـع النقـاط .. حاول من جديد في وقت آخر ✓**")
    
    
@blal.dev_cmd(pattern="بوت العقاب$")
async def _(event):
    await event.edit('@TTNBOT')

# Copyright (C) 2022 dev-Thon . All Rights Reserved
@blal.dev_cmd(pattern="(العقاب|تجميع العقاب)(?: |$)(.*)")
async def _(event):
    con = event.pattern_match.group(1).lower()
    await event.edit("**⎉╎حسنًـا .. تأكـد من أنـك مشتـرك بـ قنـوات الاشتـراك الإجبـاري لتجنب الأخطـاء @TTNBOT**")
    channel_entity = await blal.get_entity('@TTNBOT')
    await blal.send_message('@TTNBOT', '/start')
    await asyncio.sleep(4)
    msg0 = await blal.get_messages('@TTNBOT', limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await blal.get_messages('@TTNBOT', limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(10)
        list = await blal(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('**⎉╎لا يوجد قنوات في الوقت الحالي .. قم يتجميع النقاط بطريقة مختلفة**') != -1:
            await blal.send_message(event.chat_id, "**⎉╎مـافي قنـوات بالبـوت حاليًـا ...**")
            break
        if con == "ايقاف": #Code by T.me/zzzzl1l
            await blal.send_message(event.chat_id, "**⎉╎تم إيقـاف تجميـع النقـاط .. بنجـاح☑️**")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await blal(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await blal(ImportChatInviteRequest(bott))
            msg2 = await blal.get_messages('@TTNBOT', limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**⎉╎تم الاشتـراك في القنـاة  {chs} ...✓**")
        except: #Code by T.me/zzzzl1l
            msg2 = await blal.get_messages('@TTNBOT', limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**⎉╎القنـاة رقـم {chs} .. يمكـن تبنـدت**")
    await blal.send_message(event.chat_id, "**⎉╎تم الانتهـاء مـن تجميـع النقـاط .. حاول من جديد في وقت آخر ✓**")


@blal.dev_cmd(pattern="بوت المليون$")
async def _(event):
    await event.edit('@qweqwe1919bot')

# Copyright (C) 2022 dev-Thon . All Rights Reserved
@blal.dev_cmd(pattern="(المليون|تجميع المليون)(?: |$)(.*)")
async def _(event):
    con = event.pattern_match.group(1).lower()
    await event.edit("**⎉╎حسنًـا .. تأكـد من أنـك مشتـرك بـ قنـوات الاشتـراك الإجبـاري لتجنب الأخطـاء @qweqwe1919bot**")
    channel_entity = await blal.get_entity('@qweqwe1919bot')
    await blal.send_message('@qweqwe1919bot', '/start')
    await asyncio.sleep(4)
    msg0 = await blal.get_messages('@qweqwe1919bot', limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await blal.get_messages('@qweqwe1919bot', limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(10)
        list = await blal(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('**⎉╎لا يوجد قنوات في الوقت الحالي .. قم يتجميع النقاط بطريقة مختلفة**') != -1:
            await blal.send_message(event.chat_id, "**⎉╎مـافي قنـوات بالبـوت حاليًـا ...**")
            break
        if con == "ايقاف": #Code by T.me/zzzzl1l
            await blal.send_message(event.chat_id, "**⎉╎تم إيقـاف تجميـع النقـاط .. بنجـاح☑️**")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await blal(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await blal(ImportChatInviteRequest(bott))
            msg2 = await blal.get_messages('@qweqwe1919bot', limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**⎉╎تم الاشتـراك في القنـاة  {chs} ...✓**")
        except: #Code by T.me/zzzzl1l
            msg2 = await blal.get_messages('@qweqwe1919bot', limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**⎉╎القنـاة رقـم {chs} .. يمكـن تبنـدت**")
    await blal.send_message(event.chat_id, "**⎉╎تم الانتهـاء مـن تجميـع النقـاط .. حاول من جديد في وقت آخر ✓**")


@blal.dev_cmd(pattern="بوت سمسم$")
async def _(event):
    await event.edit('@SMSMWAbot')

# Copyright (C) 2023 dev-Thon . All Rights Reserved
@blal.dev_cmd(pattern="(سمسم|تجميع سمسم)(?: |$)(.*)")
async def _(event):
    con = event.pattern_match.group(1).lower()
    await event.edit("**⎉╎حسنًـا .. تأكـد من أنـك مشتـرك بـ قنـوات الاشتـراك الإجبـاري لتجنب الأخطـاء @SMSMWAbot**")
    channel_entity = await blal.get_entity('@SMSMWAbot')
    await blal.send_message('@SMSMWAbot', '/start')
    await asyncio.sleep(4)
    msgz = await blal.get_messages('@SMSMWAbot', limit=1)
    await msgz[0].click(0)
    await asyncio.sleep(4)
    msg0 = await blal.get_messages('@SMSMWAbot', limit=1)
    await msg0[0].click(3)
    await asyncio.sleep(4)
    msg1 = await blal.get_messages('@SMSMWAbot', limit=1)
    await msg1[0].click(1)
    chs = 1
    for i in range(100):
        await asyncio.sleep(10)
        list = await blal(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('**⎉╎لا يوجد قنوات في الوقت الحالي .. قم يتجميع النقاط بطريقة مختلفة**') != -1:
            await blal.send_message(event.chat_id, "**⎉╎مـافي قنـوات بالبـوت حاليًـا ...**")
            break
        if con == "ايقاف": #Code by T.me/zzzzl1l
            await blal.send_message(event.chat_id, "**⎉╎تم إيقـاف تجميـع النقـاط .. بنجـاح☑️**")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await blal(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await blal(ImportChatInviteRequest(bott))
            msg2 = await blal.get_messages('@SMSMWAbot', limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**⎉╎تم الاشتـراك في القنـاة  {chs} ...✓**")
        except: #Code by T.me/zzzzl1l
            msg2 = await blal.get_messages('@SMSMWAbot', limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**⎉╎القنـاة رقـم {chs} .. يمكـن تبنـدت**")
    await blal.send_message(event.chat_id, "**⎉╎تم الانتهـاء مـن تجميـع النقـاط .. حاول من جديد في وقت آخر ✓**")


@blal.dev_cmd(pattern="بوت تناهيد$")
async def _(event):
    await event.edit('@Ncoe_bot')

# Copyright (C) 2023 dev-Thon . All Rights Reserved
@blal.dev_cmd(pattern="(تناهيد|تجميع تناهيد)(?: |$)(.*)")
async def _(event):
    con = event.pattern_match.group(1).lower()
    await event.edit("**⎉╎حسنًـا .. تأكـد من أنـك مشتـرك بـ قنـوات الاشتـراك الإجبـاري لتجنب الأخطـاء @Ncoe_bot**")
    channel_entity = await blal.get_entity('@Ncoe_bot')
    await blal.send_message('@Ncoe_bot', '/start')
    await asyncio.sleep(4)
    msg0 = await blal.get_messages('@Ncoe_bot', limit=1)
    await msg0[0].click(2)
    await asyncio.sleep(4)
    msg1 = await blal.get_messages('@Ncoe_bot', limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(10)
        list = await blal(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('**⎉╎لا يوجد قنوات في الوقت الحالي .. قم يتجميع النقاط بطريقة مختلفة**') != -1:
            await blal.send_message(event.chat_id, "**⎉╎مـافي قنـوات بالبـوت حاليًـا ...**")
            break
        if con == "ايقاف": #Code by T.me/zzzzl1l
            await blal.send_message(event.chat_id, "**⎉╎تم إيقـاف تجميـع النقـاط .. بنجـاح☑️**")
            break
        url = msgs.reply_markup.rows[0].buttons[0].url
        try:
            try:
                await blal(JoinChannelRequest(url))
            except:
                bott = url.split('/')[-1]
                await blal(ImportChatInviteRequest(bott))
            msg2 = await blal.get_messages('@Ncoe_bot', limit=1)
            await msg2[0].click(text='تحقق')
            chs += 1
            await event.edit(f"**⎉╎تم الاشتـراك في القنـاة  {chs} ...✓**")
        except: #Code by T.me/zzzzl1l
            msg2 = await blal.get_messages('@Ncoe_bot', limit=1)
            await msg2[0].click(text='التالي')
            chs += 1
            await event.edit(f"**⎉╎القنـاة رقـم {chs} .. يمكـن تبنـدت**")
    await blal.send_message(event.chat_id, "**⎉╎تم الانتهـاء مـن تجميـع النقـاط .. حاول من جديد في وقت آخر ✓**")


@blal.dev_cmd(pattern="بوت دعمكم$")
async def _(event):
    await event.edit('@DamKombot')

# Copyright (C) 20223 dev-Thon . All Rights Reserved
@blal.dev_cmd(pattern="(دعمكم|تجميع دعمكم)(?: |$)(.*)")
async def _(event):
    con = event.pattern_match.group(1).lower()
    await event.edit("**⎉╎حسنًـا .. تأكـد من أنـك مشتـرك بـ قنـوات الاشتـراك الإجبـاري لتجنب الأخطـاء @DamKombot**")
    channel_entity = await blal.get_entity('@DamKombot')
    await blal.send_message('@DamKombot', '/start')
    await asyncio.sleep(4)
    msg0 = await blal.get_messages('@DamKombot', limit=1)
    await msg0[0].click(1)
    await asyncio.sleep(4)
    msg1 = await blal.get_messages('@DamKombot', limit=1)
    await msg1[0].click(0)
    chs = 1
    for i in range(100):
        await asyncio.sleep(10)
        list = await blal(GetHistoryRequest(peer=channel_entity, limit=1, offset_date=None, offset_id=0, max_id=0, min_id=0, add_offset=0, hash=0))
        msgs = list.messages[0]
        if msgs.message.find('**⎉╎لا يوجد قنوات في الوقت الحالي .. قم يتجميع النقاط بطريقة مختلفة**') != -1:
            await blal.send_message(event.chat_id, "**⎉╎مـافي قنـوات بالبـوت حاليًـا ...**")
            break
        if con == "ايقاف": #Code by T.me/zzzzl1l
            await blal.send_message(event.chat_id, "**⎉╎تم إيقـاف تجميـع النقـاط .. بنجـاح☑️**")
            break
        msg_text = msgs.message
        if "اشترك فالقناة @" in msg_text:
            the_channel = msg_text.split('@')[1].split()[0]
            try:
                entity = await blal.get_entity(the_channel)
                if entity:
                    await blal(JoinChannelRequest(entity.id))
                    await asyncio.sleep(4)
                    msg2 = await blal.get_messages('@DamKombot', limit=1)
                    await msg2[0].click(text='اشتركت ✅')
                    chs += 1
                    await event.edit(f"**⎉╎تم الاشتـراك في القنـاة  {chs} ...✓**")
            except:
                await blal.send_message(event.chat_id, f"**⎉╎خطـأ , يمكـن تبنـدت ؟!**")
                break
    await blal.send_message(event.chat_id, "**⎉╎تم الانتهـاء مـن تجميـع النقـاط .. حاول من جديد في وقت آخر ✓**")



# Code by @r0r77 & @Dar4k
@blal.dev_cmd(pattern="بخشيش وعد(?:\s|$)([\s\S]*)")
async def baqshis(event):
    global bahsees
    await event.delete()
    if not bahsees:
        bahsees = True
        if event.is_group:
            await the_bahsees(event)
        else:
            await event.edit("**⎉╎ الامـر خاص بـ المجموعات فقـط ؟!**")
async def the_bahsees(event):
    await event.respond('بخشيش')
    await asyncio.sleep(660)
    global bahsees
    if bahsees:
        await the_bahsees(event)  
@blal.dev_cmd(pattern="ايقاف بخشيش وعد(?:\s|$)([\s\S]*)")
async def baqshis(event):
    global bahsees
    bahsees = False
    await event.edit("**⎉╎تم إيقـاف تجميـع البخشيش  .. بنجـاح ✓** ")

@blal.dev_cmd(pattern="معطل(?:\s|$)([\s\S]*)")
async def thift(event):
    global thifts
    await event.delete()
    if not thifts:
        thifts = True
        if event.is_group:
            message = event.pattern_match.group(1).strip()
            if message:
                await send_message(event, message)
            else:
                await event.edit("**⎉╎قم بكتابة ايدي الشخص مع الامـر ؟!**")

async def send_message(event, message):
    await event.respond(f"زرف {message}")
    await asyncio.sleep(660)
    global thifts
    if thifts:
        await send_message(event, message)

@blal.dev_cmd(pattern="ايقاف سرقة وعد(?:\s|$)([\s\S]*)")
async def Reda(event):
    global thifts
    thifts = False
    await event.edit("**⎉╎تم إيقـاف السرقة  .. بنجـاح ✓**")
client = blal


@blal.dev_cmd(pattern="راتب وعد(?:\s|$)([\s\S]*)")
async def thift(event):
    global ratp
    await event.delete()
    if not ratp:
        ratp = True
        if event.is_group:
            await the_ratp(event)
        else:
            await event.edit("**⎉╎ الامـر خاص بـ المجموعات فقـط ؟!**")

async def the_ratp(event):
    await event.respond('راتب')
    await asyncio.sleep(660)
    global ratp
    if ratp:
        await the_ratp(event)  
@blal.dev_cmd(pattern="ايقاف راتب وعد(?:\s|$)([\s\S]*)")
async def thift(event):
    global ratp
    ratp = False
    await event.edit("**تم تعطيل راتب وعد بنجاح ✅**")


@blal.dev_cmd(pattern="كلمات وعد (.*)")
async def waorwaad(event):
    for i in range(int("".join(event.text.split(maxsplit=2)[2:]).split(" ", 2)[0])):
        chat = event.chat_id
        await blal.send_message(chat, "كلمات")
        await asyncio.sleep(0.5)
        masg = await blal.get_messages(chat, limit=1)
        masg = masg[0].message
        masg = ("".join(masg.split(maxsplit=3)[3:])).split(" ", 2)
        if len(masg) == 2:
            msg = masg[0]
            await blal.send_message(chat, msg)
        else:
            msg = masg[0] + " " + masg[1]
            await blal.send_message(chat, msg)


@blal.dev_cmd(pattern="استثمار وعد")
async def _(event):
    await event.delete()
    global estithmar
    estithmar = True
    while estithmar:
        if event.is_group:
            await event.client.send_message(event.chat_id, "فلوسي")
            await asyncio.sleep(4)
            zzBDB0B = await event.client.get_messages(event.chat_id, limit=1)
            zzBDB0B = zzBDB0B[0].message
            zzBDB0B = ("".join(zzBDB0B.split(maxsplit=2)[2:])).split(" ", 2)
            blal = zzBDB0B[0]
            if blal.isdigit() and int(blal) > 500000000:
                await event.client.send_message(event.chat_id,f"استثمار {blal}")
                await asyncio.sleep(5)
                zBDB0B = await event.client.get_messages(event.chat_id, limit=1)
                await zBDB0B[0].click(text="اي ✅")
            else:
                await event.client.send_message(event.chat_id, f"استثمار {blal}")
            await asyncio.sleep(1210)
        
        else:
            await event.edit("**⎉╎امر الاستثمار يمكنك استعماله في المجموعات فقط 🖤**")
@blal.dev_cmd(pattern="ايقاف استثمار وعد")
async def stop_wad(event):
    global estithmar
    estithmar = False
    await event.edit("**⎉╎تم إيقـاف استثمار وعـد  .. بنجـاح ✓**")


@blal.dev_cmd(pattern="اوامر النقاط")
async def cmd(zelzallll):
    await edit_or_reply(zelzallll, ZelzalCoins_cmd)

@blal.dev_cmd(pattern="اوامر التجميع")
async def cmd(zelzallll):
    await edit_or_reply(zelzallll, ZelzalCoins_cmd)
    
