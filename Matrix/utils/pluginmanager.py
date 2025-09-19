import contextlib
import importlib
import sys
from pathlib import Path

from Matrix import CMD_HELP, LOAD_PLUG

from ..Config import Config
from ..core import LOADED_CMDS, PLG_INFO
from ..core.logger import logging
from ..core.managers import edit_delete, edit_or_reply
from ..core.session import blal
from ..helpers.tools import media_type
from ..helpers.utils import _devtools, _devutils, _format, install_pip, reply_id
from .decorators import admin_cmd, sudo_cmd

LOGS = logging.getLogger("BDB0B")
inst_done = "✅ تـم تنصيب سـورس تيبثـون .. بنجـاح ⌔\n♥️ قم بالذهاب الى تيليجـرام الان ⌔\n💡 ثم أرسـل الأمـر ( .الاوامر ) ⌔" 

def load_module(shortname, plugin_path=None):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        path = Path(f"Matrix/plugins/{shortname}.py")
        checkplugins(path)
        name = "Matrix.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        LOGS.info(f"Successfully imported {shortname}")
    else:
        if plugin_path is None:
            path = Path(f"Matrix/plugins/{shortname}.py")
            name = f"Matrix.plugins.{shortname}"
        else:
            path = Path((f"{plugin_path}/{shortname}.py"))
            name = f"{plugin_path}/{shortname}".replace("/", ".")
        checkplugins(path)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = blal
        mod.LOGS = LOGS
        mod.Config = Config
        mod._format = _format
        mod.tgbot = blal.tgbot
        mod.sudo_cmd = sudo_cmd
        mod.CMD_HELP = CMD_HELP
        mod.reply_id = reply_id
        mod.admin_cmd = admin_cmd
        mod._devutils = _devutils
        mod._devtools = _devtools
        mod.media_type = media_type
        mod.edit_delete = edit_delete
        mod.install_pip = install_pip
        mod.parse_pre = _format.parse_pre
        mod.edit_or_reply = edit_or_reply
        mod.logger = logging.getLogger(shortname)
        mod.borg = blal
        spec.loader.exec_module(mod)
        # for imports
        sys.modules[f"Matrix.plugins.{shortname}"] = mod
        LOGS.info(f"Successfully imported {shortname}")


def lload_module(shortname, plugin_path=None):
    if shortname.startswith("__"):
        pass
    elif shortname.endswith("_"):
        path = Path(f"Matrix/plugins/{shortname}.py")
        checkplugins(path)
        name = "Matrix.plugins.{}".format(shortname)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        print("Successfully imported library")
    else:
        if plugin_path is None:
            path = Path(f"Matrix/plugins/{shortname}.py")
            name = f"Matrix.plugins.{shortname}"
        else:
            path = Path((f"{plugin_path}/{shortname}.py"))
            name = f"{plugin_path}/{shortname}".replace("/", ".")
        checkplugins(path)
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        mod.bot = blal
        mod.LOGS = LOGS
        mod.Config = Config
        mod._format = _format
        mod.tgbot = blal.tgbot
        mod.sudo_cmd = sudo_cmd
        mod.CMD_HELP = CMD_HELP
        mod.reply_id = reply_id
        mod.admin_cmd = admin_cmd
        mod._devutils = _devutils
        mod._devtools = _devtools
        mod.media_type = media_type
        mod.edit_delete = edit_delete
        mod.install_pip = install_pip
        mod.parse_pre = _format.parse_pre
        mod.edit_or_reply = edit_or_reply
        mod.logger = logging.getLogger(shortname)
        mod.borg = blal
        spec.loader.exec_module(mod)
        # for imports
        sys.modules[f"Matrix.plugins.{shortname}"] = mod
        print("Successfully imported library")


def remove_plugin(shortname):
    try:
        cmd = []
        if shortname in PLG_INFO:
            cmd += PLG_INFO[shortname]
        else:
            cmd = [shortname]
        for cmdname in cmd:
            if cmdname in LOADED_CMDS:
                for i in LOADED_CMDS[cmdname]:
                    blal.remove_event_handler(i)
                del LOADED_CMDS[cmdname]
        return True
    except Exception as e:
        LOGS.error(e)
    with contextlib.suppress(BaseException):
        for i in LOAD_PLUG[shortname]:
            blal.remove_event_handler(i)
        del LOAD_PLUG[shortname]
    try:
        name = f"Matrix.plugins.{shortname}"
        for i in reversed(range(len(blal._event_builders))):
            ev, cb = blal._event_builders[i]
            if cb.__module__ == name:
                del blal._event_builders[i]
    except BaseException as exc:
        raise ValueError from exc


def checkplugins(filename):
    with open(filename, "r") as f:
        filedata = f.read()
    filedata = filedata.replace("sendmessage", "send_message")
    filedata = filedata.replace("sendfile", "send_file")
    filedata = filedata.replace("editmessage", "edit_message")
    with open(filename, "w") as f:
        f.write(filedata)
