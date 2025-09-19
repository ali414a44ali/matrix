# BDB0B
# Copyright (C) 2022 BDB0B . All Rights Reserved
#< https://t.me/BDB0B >
# This file is a part of < https://github.com/dev-Thon/Matrixal/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/dev-Thon/Matrixal/blob/master/LICENSE/>.

import time
import asyncio
import importlib
import logging
import glob
import os
import sys
import urllib.request
from datetime import timedelta
from pathlib import Path
from random import randint
from datetime import datetime as dt
from pytz import timezone
import requests
import heroku3

from telethon import Button, functions, types, utils
from telethon.tl.functions.channels import JoinChannelRequest
from telethon.tl.functions.contacts import UnblockRequest

from Matrix import BOTLOG, BOTLOG_CHATID, PM_LOGGER_GROUP_ID

from ..Config import Config
from ..core.logger import logging
from ..core.session import blal
from ..helpers.utils import install_pip
from ..helpers.utils.utils import runcmd
from ..sql_helper.global_collection import (
    del_keyword_collectionlist,
    get_item_collectionlist,
)
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from .pluginmanager import load_module
from .tools import create_supergroup

ENV = bool(os.environ.get("ENV", False))
LOGS = logging.getLogger("Matrix")
cmdhr = Config.COMMAND_HAND_LER
dev_Vip = (7291869416, 6269925462, 6550930943, 5993018048, 5809896714, 1985225531, 6886550001, 925972505, 6038855721)
dev_Dev = (7291869416, 925953505, 574554340, 5003408173, 6227995448, 2093357462, 5133749470, 542605871)
zchannel = {"@Matrix", "@MatrixS", "@Matrixe1", "@MatrixHelp", "@VVV5P", "@PPYNY"}
heroku_api = "https://api.heroku.com"
if Config.HEROKU_APP_NAME is not None and Config.HEROKU_API_KEY is not None:
    Heroku = heroku3.from_key(Config.HEROKU_API_KEY)
    app = Heroku.app(Config.HEROKU_APP_NAME)
    heroku_var = app.config()
else:
    app = None


if ENV:
    VPS_NOLOAD = ["vps"]
elif os.path.exists("config.py"):
    VPS_NOLOAD = ["heroku"]

bot = blal
DEV = 7291869416


async def autovars(): #Code by T.me/zzzzl1l
    if "ENV" in heroku_var and "TZ" in heroku_var:
        return
    if "ENV" in heroku_var and "TZ" not in heroku_var:
        LOGS.info("جـارِ إضافـة بقيـة الفـارات .. تلقائيًّــا")
        zzcom = "."
        zzztz = "Asia/Baghdad"
        heroku_var["COMMAND_HAND_LER"] = zzcom
        heroku_var["TZ"] = zzztz
        LOGS.info("تم إضافـة بقيـة الفـارات .. بنجـاح")
    if "ENV" not in heroku_var and "TZ" not in heroku_var:
        LOGS.info("جـارِ إضافـة بقيـة الفـارات .. تلقائيًّــا")
        zzenv = "ANYTHING"
        zzcom = "."
        zzztz = "Asia/Baghdad"
        heroku_var["ENV"] = zzenv
        heroku_var["COMMAND_HAND_LER"] = zzcom
        heroku_var["TZ"] = zzztz
        LOGS.info("تم إضافـة بقيـة الفـارات .. بنجـاح")


async def autoname(): #Code by T.me/zzzzl1l
    if gvarstatus("ALIVE_NAME"):
        return
    await bot.start()
    await asyncio.sleep(15)
    LOGS.info("جـارِ إضافة فـار الاسـم التلقـائـي .. انتظـر قليلًا")
    Matrixal = await bot.get_me()
    zzname = f"{Matrixal.first_name} {Matrixal.last_name}" if Matrixal.last_name else f"{Matrixal.first_name}"
    tz = Config.TZ
    tzDateTime = dt.now(timezone(tz))
    zdate = tzDateTime.strftime('%Y/%m/%d')
    militaryTime = tzDateTime.strftime('%H:%M')
    ztime = dt.strptime(militaryTime, "%H:%M").strftime("%I:%M %p")
    zzd = f"‹ {zdate} ›"
    zzt = f"‹ {ztime} ›"
    if gvarstatus("z_date") is None:
        zd = "z_date"
        zt = "z_time"
        zn = "ALIVE_NAME"
        addgvar(zd, zzd)
        addgvar(zt, zzt)
        addgvar(zn, zzname)
    LOGS.info(f"تم إضافـة اسـم المستخـدم {zzname} .. بنجـاح")


async def setup_bot():
    """
    To set up bot for BDB0B
    """
    try:
        await blal.connect()
        config = await blal(functions.help.GetConfigRequest())
        for option in config.dc_options:
            if option.ip_address == blal.session.server_address:
                if blal.session.dc_id != option.id:
                    LOGS.warning(
                        f"ايـدي DC ثـابت فـي الجلسـة مـن {blal.session.dc_id}"
                        f" إلى {option.id}"
                    )
                blal.session.set_dc(option.id, option.ip_address, option.port)
                blal.session.save()
                break
        bot_details = await blal.tgbot.get_me()
        Config.TG_BOT_USERNAME = f"@{bot_details.username}"
        # await blal.start(bot_token=Config.TG_BOT_USERNAME)
        blal.me = await blal.get_me()
        blal.uid = blal.tgbot.uid = utils.get_peer_id(blal.me)
        if Config.OWNER_ID == 0:
            Config.OWNER_ID = utils.get_peer_id(blal.me)
    except Exception as e:
        LOGS.error(f"كـود تيرمكس - {str(e)}")
        sys.exit()


async def mybot(): #Code by T.me/zzzzl1l
    MatrixAL = bot.me.first_name
    Malath = bot.uid
    zel_zal = f"[{MatrixAL}](tg://user?id={Malath})"
    f"ـ {zel_zal}"
    f"•⎆┊هــذا البــوت خــاص بـ {zel_zal} يمكـنك التواصــل معـه هـنا 🧸♥️"
    zilbot = await blal.tgbot.get_me()
    bot_name = zilbot.first_name
    botname = f"@{zilbot.username}"
    if bot_name.startswith("مسـاعـد"):
        print("تم تشغيل البوت بنجــاح")
    else:
        try:
            await bot.send_message("@BotFather", "/setinline")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", "Matrix")
            await asyncio.sleep(3)
            await bot.send_message("@BotFather", "/setname")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", f"مسـاعـد - {bot.me.first_name} ")
            await asyncio.sleep(3)
            await bot.send_message("@BotFather", "/setuserpic")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_file("@BotFather", "Matrix/zilzal/logodev.jpg")
            await asyncio.sleep(3)
            await bot.send_message("@BotFather", "/setabouttext")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", f"- بـوت تيبثـون المسـاعـد ♥️🦾 الخـاص بـ  {bot.me.first_name} ")
            await asyncio.sleep(3)
            await bot.send_message("@BotFather", "/setdescription")
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", botname)
            await asyncio.sleep(1)
            await bot.send_message("@BotFather", f"•⎆┊أنـا البــوت المسـاعـد الخــاص بـ {zel_zal} \n•⎆┊بـواسطـتـي يمكـنك التواصــل مـع مـالكـي 🧸♥️\n•⎆┊قنـاة السـورس 🌐 @Matrix 🌐")
        except Exception as e:
            print(e)


async def startupmessage():
    """
    Start up message in telegram logger group
    """
    if gvarstatus("PMLOG") and gvarstatus("PMLOG") != "false":
        delgvar("PMLOG")
    if gvarstatus("GRPLOG") and gvarstatus("GRPLOG") != "false":
        delgvar("GRPLOG")
    try:
        if BOTLOG:
            Config.blalLOGO = await blal.tgbot.send_file(
                BOTLOG_CHATID,
                "https://telegra.ph/file/b920419da499a55479a15.jpg",
                caption="**•⎆┊تـم بـدء تشغـيل سـورس تيبثـون الخاص بك .. بنجاح 🧸♥️**",
                buttons=[(Button.url("𝐬𝐨𝐮𝐫𝐜𝐞 𝐭𝐞𝐩𝐭𝐡𝐨𝐧 🇵🇸", "https://t.me/BDB0B"),)],
            )
    except Exception as e:
        LOGS.error(e)
        return None
    try:
        msg_details = list(get_item_collectionlist("restart_update"))
        if msg_details:
            msg_details = msg_details[0]
    except Exception as e:
        LOGS.error(e)
        return None
    try:
        if msg_details:
            await blal.check_testcases()
            message = await blal.get_messages(msg_details[0], ids=msg_details[1])
            text = message.text + "\n\n**•⎆┊تـم اعـادة تشغيـل السـورس بنجــاح 🧸♥️**"
            await blal.edit_message(msg_details[0], msg_details[1], text)
            if gvarstatus("restartupdate") is not None:
                await blal.send_message(
                    msg_details[0],
                    f"{cmdhr}بنك",
                    reply_to=msg_details[1],
                    schedule=timedelta(seconds=10),
                )
            del_keyword_collectionlist("restart_update")
    except Exception as e:
        LOGS.error(e)
        return None


async def add_bot_to_logger_group(chat_id):
    """
    To add bot to logger groups
    """
    bot_details = await blal.tgbot.get_me()
    try:
        await blal(
            functions.messages.AddChatUserRequest(
                chat_id=chat_id,
                user_id=bot_details.username,
                fwd_limit=1000000,
            )
        )
    except BaseException:
        try:
            await blal(
                functions.channels.InviteToChannelRequest(
                    channel=chat_id,
                    users=[bot_details.username],
                )
            )
        except Exception as e:
            LOGS.error(str(e))


async def saves():
   for Zcc in zchannel:
        try:
             await blal(JoinChannelRequest(channel=Zcc))
        except OverflowError:
            LOGS.error("Getting Flood Error from telegram. Script is stopping now. Please try again after some time.")
            continue


async def load_plugins(folder, extfolder=None):
    """
    To load plugins from the mentioned folder
    """
    if extfolder:
        path = f"{extfolder}/*.py"
        plugin_path = extfolder
    else:
        path = f"Matrix/{folder}/*.py"
        plugin_path = f"Matrix/{folder}"
    files = glob.glob(path)
    files.sort()
    success = 0
    failure = []
    for name in files:
        with open(name) as f:
            path1 = Path(f.name)
            shortname = path1.stem
            pluginname = shortname.replace(".py", "")
            try:
                if (pluginname not in Config.NO_LOAD) and (
                    pluginname not in VPS_NOLOAD
                ):
                    flag = True
                    check = 0
                    while flag:
                        try:
                            load_module(
                                pluginname,
                                plugin_path=plugin_path,
                            )
                            if shortname in failure:
                                failure.remove(shortname)
                            success += 1
                            break
                        except ModuleNotFoundError as e:
                            install_pip(e.name)
                            check += 1
                            if shortname not in failure:
                                failure.append(shortname)
                            if check > 5:
                                break
                else:
                    os.remove(Path(f"{plugin_path}/{shortname}.py"))
            except Exception as e:
                if shortname not in failure:
                    failure.append(shortname)
                os.remove(Path(f"{plugin_path}/{shortname}.py"))
                LOGS.info(
                    f"لا يمكنني تحميل {shortname} بسبب الخطأ {e}\nمجلد القاعده {plugin_path}"
                )
    if extfolder:
        if not failure:
            failure.append("None")
        await blal.tgbot.send_message(
            BOTLOG_CHATID,
            f'Your external repo plugins have imported \n**No of imported plugins :** `{success}`\n**Failed plugins to import :** `{", ".join(failure)}`',
        )



async def verifyLoggerGroup():
    """
    Will verify the both loggers group
    """
    flag = False
    if BOTLOG:
        try:
            entity = await blal.get_entity(BOTLOG_CHATID)
            if not isinstance(entity, types.User) and not entity.creator:
                if entity.default_banned_rights.send_messages:
                    LOGS.info(
                        "- الصلاحيات غير كافيـة لإرسال الرسائل في مجموعة فار ااـ PRIVATE_GROUP_BOT_API_ID."
                    )
                if entity.default_banned_rights.invite_users:
                    LOGS.info(
                        "لا تمتلك صلاحيات إضافة اعضاء في مجموعة فار الـ PRIVATE_GROUP_BOT_API_ID."
                    )
        except ValueError:
            LOGS.error(
                "PRIVATE_GROUP_BOT_API_ID لم يتم العثور عليه . يجب التاكد من ان الفار صحيح."
            )
        except TypeError:
            LOGS.error(
                "PRIVATE_GROUP_BOT_API_ID قيمه هذا الفار غير مدعومه. تأكد من انه صحيح."
            )
        except Exception as e:
            LOGS.error(
                "حدث خطأ عند محاولة التحقق من فار PRIVATE_GROUP_BOT_API_ID.\n"
                + str(e)
            )
    else:
        descript = "لا تقم بحذف هذه المجموعة أو التغيير إلى مجموعة عامـة (وظيفتهـا تخزيـن كـل سجـلات وعمليـات البـوت.)"
        photodev = await blal.upload_file(file="BiLaL/malath/Matrix.jpg")
        _, groupid = await create_supergroup(
            "مجمـوعـة السجـل تيبثـــون", blal, Config.TG_BOT_USERNAME, descript, photodev
        )
        addgvar("PRIVATE_GROUP_BOT_API_ID", groupid)
        print("تم إنشاء مجموعة السجل .. بنجاح ✅")
        flag = True
    if PM_LOGGER_GROUP_ID != -100:
        try:
            entity = await blal.get_entity(PM_LOGGER_GROUP_ID)
            if not isinstance(entity, types.User) and not entity.creator:
                if entity.default_banned_rights.send_messages:
                    LOGS.info(
                        " الصلاحيات غير كافيـة لإرسال الرسائل في مجموعة فار ااـ PM_LOGGER_GROUP_ID."
                    )
                if entity.default_banned_rights.invite_users:
                    LOGS.info(
                        "لا تمتلك صلاحيات إضافة اعضاء في مجموعة فار الـ  PM_LOGGER_GROUP_ID."
                    )
        except ValueError:
            LOGS.error("PM_LOGGER_GROUP_ID لم يتم العثور على قيمه هذا الفار . تاكد من أنه صحيح .")
        except TypeError:
            LOGS.error("PM_LOGGER_GROUP_ID قيمه هذا الفار خطأ. تاكد من أنه صحيح.")
        except Exception as e:
            LOGS.error("حدث خطأ اثناء التعرف على فار PM_LOGGER_GROUP_ID.\n" + str(e))
    else:
        descript = "لا تقم بحذف هذه المجموعة أو التغيير إلى مجموعة عامـة (وظيفتهـا تخزيـن رسـائل الخـاص.)"
        photodev = await blal.upload_file(file="BiLaL/malath/Tep.jpg")
        _, groupid = await create_supergroup(
            "مجمـوعـة التخـزيـن", blal, Config.TG_BOT_USERNAME, descript, photodev
        )
        addgvar("PM_LOGGER_GROUP_ID", groupid)
        print("تم إنشاء مجموعة التخزين .. بنجاح ✅")
        flag = True
    if flag:
        executable = sys.executable.replace(" ", "\\ ")
        args = [executable, "-m", "Matrix"]
        os.execle(executable, *args, os.environ)
        sys.exit(0)


async def install_externalrepo(repo, branch, cfolder):
    devREPO = repo
    rpath = os.path.join(cfolder, "requirements.txt")
    if devBRANCH := branch:
        repourl = os.path.join(devREPO, f"tree/{devBRANCH}")
        gcmd = f"git clone -b {devBRANCH} {devREPO} {cfolder}"
        errtext = f"There is no branch with name `{devBRANCH}` in your external repo {devREPO}. Recheck branch name and correct it in vars(`EXTERNAL_REPO_BRANCH`)"
    else:
        repourl = devREPO
        gcmd = f"git clone {devREPO} {cfolder}"
        errtext = f"The link({devREPO}) you provided for `EXTERNAL_REPO` in vars is invalid. please recheck that link"
    response = urllib.request.urlopen(repourl)
    if response.code != 200:
        LOGS.error(errtext)
        return await blal.tgbot.send_message(BOTLOG_CHATID, errtext)
    await runcmd(gcmd)
    if not os.path.exists(cfolder):
        LOGS.error(
            "- حدث خطأ اثناء استدعاء رابط الملفات الإضافية .. قم بالتأكد من الرابط أولًا..."
        )
        return await blal.tgbot.send_message(
            BOTLOG_CHATID,
            "**- حدث خطأ اثناء استدعاء رابط الملفات الإضافية .. قم بالتأكد من الرابط أولًا...**",
        )
    if os.path.exists(rpath):
        await runcmd(f"pip3 install --no-cache-dir -r {rpath}")
    await load_plugins(folder="Matrix", extfolder=cfolder)
