import asyncio
from telethon import TelegramClient, events
from Matrix import blal
from telethon.tl.functions.channels import LeaveChannelRequest
from ..Config import Config

plugin_category = "البوت"

@blal.on(events.NewMessage(pattern='.مغادرة القنوات'))
async def leave_all_channels(event):
    # تأكد من أن المرسل هو الحساب المنصب فقط
    if event.sender_id != Config.OWNER_ID:  # استبدل Config.OWNER_ID بمعرف صاحب الحساب
        return

    await event.reply("جاري مغادرة جميع القنوات...")

    try:
        async for dialog in blal.iter_dialogs():
            if dialog.is_channel and not dialog.is_group:  # تحقق من أنها قناة وليست جروب
                await blal(LeaveChannelRequest(dialog.id))  # استخدم LeaveChannelRequest لمغادرة القناة
                await event.reply(f"✅ مغادرة القناة: {dialog.title}")

        await event.reply("✅ تم مغادرة جميع القنوات بنجاح.")
    except Exception as e:
        await event.reply(f"خطأ ❌: {str(e)}")
