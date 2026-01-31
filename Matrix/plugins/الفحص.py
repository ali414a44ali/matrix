# =====================[ Imports ]=====================
import random
import re
import time
import psutil
from datetime import datetime
from platform import python_version

from telethon import version, types
from telethon.extensions import html
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery

from . import StartTime, blal, tepversion
from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import devalive, check_data_base_heal_th, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import mention

# =====================[ Constants ]=====================
plugin_category = "العروض"
STATS = gvarstatus("Z_STATS") or "فحص"

MATRIX_EMOJI = 5834880210268329130   # 💎 Emoji مميز
PREMIUM_EMOJI = 5832422209074762334 # 🌟 Premium

# =====================[ Custom ParseMode ]=====================
class CustomParseMode:
    def __init__(self, parse_mode: str):
        self.parse_mode = parse_mode

    def parse(self, text):
        text, entities = html.parse(text)
        for i, e in enumerate(entities):
            if isinstance(e, types.MessageEntityTextUrl):
                if e.url.startswith("emoji/"):
                    entities[i] = types.MessageEntityCustomEmoji(
                        e.offset, e.length, int(e.url.split("/")[1])
                    )
        return text, entities

    @staticmethod
    def unparse(text, entities):
        for i, e in enumerate(entities or []):
            if isinstance(e, types.MessageEntityCustomEmoji):
                entities[i] = types.MessageEntityTextUrl(
                    e.offset, e.length, f"emoji/{e.document_id}"
                )
        return html.unparse(text, entities)

# =====================[ Alive Template ]=====================
dev_temp = """
<b>{ALIVE_TEXT}</b>
<a href="emoji/5834880210268329130">💎</a>

<b>{Z_EMOJI} قاعـدة البيانـات :</b> سريعـة جدًا 🚀
<b>{Z_EMOJI} إصدار Telethon :</b> <code>{telever}</code>
<b>{Z_EMOJI} إصدار MaTrix :</b> <code>{devver}</code>
<b>{Z_EMOJI} إصدار Python :</b> <code>{pyver}</code>

<b>{Z_EMOJI} وقت التشغيل :</b> <code>{uptime}</code>
<b>{Z_EMOJI} تاريخ التنصيب :</b> <code>{devda}</code>

<b>{Z_EMOJI} المالك :</b> {mention}
<b>{Z_EMOJI} قناتنا :</b>
<a href="https://t.me/BDB0B">اضغـط هنـا</a>
<a href="emoji/5834880210268329130">✨</a>
"""

# =====================[ Alive Command ]=====================
@blal.dev_cmd(pattern=f"{STATS}$")
async def amireallyalive(event):
    reply_to_id = await reply_id(event)
    devevent = await edit_or_reply(event, "**⎆┊ جـاري فحـص البـوت ...**")

    start = datetime.now()
    uptime = await get_readable_time((time.time() - StartTime))
    _, db_health = check_data_base_heal_th()
    end = datetime.now()
    ping = (end - start).microseconds / 1000

    boot_time = datetime.fromtimestamp(psutil.boot_time())
    devda = f"{boot_time.year}/{boot_time.month}/{boot_time.day}"

    Z_EMOJI = gvarstatus("ALIVE_EMOJI") or "✾╿"
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "بـوت ماتركـس MaTrix يعمـل بنجـاح"
    DEV_IMG = gvarstatus("ALIVE_PIC")
    dev_caption = gvarstatus("ALIVE_TEMPLATE") or dev_temp

    me = await event.client.get_me()
    if me.premium:
        ALIVE_TEXT += f' <a href="emoji/{PREMIUM_EMOJI}">🌟</a>'

    caption = dev_caption.format(
        ALIVE_TEXT=ALIVE_TEXT,
        Z_EMOJI=Z_EMOJI,
        mention=mention,
        uptime=uptime,
        devda=devda,
        telever=version.__version__,
        devver=tepversion,
        pyver=python_version(),
        dbhealth=db_health,
        ping=ping,
    )

    if DEV_IMG:
        pic = random.choice(DEV_IMG.split())
        try:
            await event.client.send_file(
                event.chat_id,
                pic,
                caption=caption,
                reply_to=reply_to_id,
                parse_mode=CustomParseMode("html"),
            )
            await devevent.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            await devevent.edit(caption, parse_mode=CustomParseMode("html"))
    else:
        await devevent.edit(
            caption,
            parse_mode=CustomParseMode("html"),
            link_preview=False,
        )

# =====================[ Inline Alive ]=====================
@blal.dev_cmd(
    pattern="الفحص$",
    command=("الفحص", plugin_category),
)
async def amireallyialive(event):
    reply_to_id = await reply_id(event)
    Z_EMOJI = gvarstatus("ALIVE_EMOJI") or "✾╿"

    caption = (
        f"<b>بوت ماتركـس MaTrix يعمل بنجاح</b> "
        f'<a href="emoji/{MATRIX_EMOJI}">💎</a>\n\n'
        f"<b>{Z_EMOJI} Telethon :</b> <code>{version.__version__}</code>\n"
        f"<b>{Z_EMOJI} MaTrix :</b> <code>{tepversion}</code>\n"
        f"<b>{Z_EMOJI} Python :</b> <code>{python_version()}</code>\n"
        f"<b>{Z_EMOJI} المالك :</b> {mention}"
    )

    results = await event.client.inline_query(
        Config.TG_BOT_USERNAME, caption
    )
    await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
    await event.delete()

# =====================[ Callback Stats ]=====================
@blal.tgbot.on(CallbackQuery(data=re.compile(b"stats")))
async def on_stats_callback(event):
    text = await devalive(StartTime)
    await event.answer(text, cache_time=0, alert=True)
