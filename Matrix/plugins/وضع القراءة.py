#حقوق_سورس_الجوكر
import asyncio
from telethon import events
from Matrix import blal

tep_enabled = False
Matrix_enabled = False
OWNER_ID = {}

@blal.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def mark_as_read(event):
    global Matrix_enabled, OWNER_ID
    sender_id = event.sender_id
    if Matrix_enabled and sender_id in OWNER_ID:
        joker_time = OWNER_ID[sender_id]
        if joker_time > 0:
            await asyncio.sleep(joker_time)
        await event.mark_read()

@blal.on(events.NewMessage(outgoing=True, pattern=r'^\.ايقاف القراءة تلقائيا$'))
async def disable_Matrix(event):
    global Matrix_enabled
    Matrix_enabled = False
    await event.edit('**⎉╎ تـم تعطيـل أمر القراءة تلقائيًّــا بنجــاح .. ✅**')

@blal.on(events.NewMessage(outgoing=True, pattern=r'^\.القراءة تلقائيا (\d+) (\d+)$'))
async def enable_Matrix(event):
    global Matrix_enabled, OWNER_ID
    joker_time = int(event.pattern_match.group(1))
    user_id = int(event.pattern_match.group(2)) 
    OWNER_ID[user_id] = joker_time
    Matrix_enabled = True
    await event.edit(f'**⎉╎ تم تفعيل أمر قـراءة الرسائـل تلقائـيًّــا مع {joker_time} ثانيـة للمستخـدم {user_id}.**')

@blal.on(events.NewMessage(outgoing=True, pattern=r'^\.ايقاف قراءة الرسائل للجميع$'))
async def disable_tep(event):
    global tep_enabled
    tep_enabled = False
    await event.edit('**⎉╎ لقـد تم تعطيل أمر قراءة الرسائل تلقائيًّـا على الجميـع بنجـاح .. ✅**')

@blal.on(events.NewMessage(outgoing=True, pattern=r'^\.قراءة رسائل الجميع (\d+)$'))
async def enable_tep(event):
    global tep_enabled, tep_time
    tep_time = int(event.pattern_match.group(1))
    tep_enabled = True
    await event.edit(f'**⎉╎ ✅ تم تفعيل قراءة الرسائل تلقائـيًّا الجميع مع {tep_time} ثانيـة.**')

@blal.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def tep_read(event):
    global tep_enabled, tep_time
    if tep_enabled:
        await asyncio.sleep(tep_time)
        await event.mark_read()
