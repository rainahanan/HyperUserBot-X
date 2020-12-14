import asyncio
import os
import urllib

import requests

from ..utils import admin_cmd

from . import TMP_DOWNLOAD_DIRECTORY

@borg.on(admin_cmd(pattern=r"boobs"))
async def boobs(event):
    pic_loc = os.path.join(TMP_DOWNLOAD_DIRECTORY, "bobs.jpg")
    a = await event.edit("`Finding some big bobs 🧐...`")
    await asyncio.sleep(0.5)
    await a.edit("`Sending some big bobs 🌚...`")
    nsfw = requests.get("http://api.oboobs.ru/noise/1").json()[0]["preview"]
    urllib.request.urlretrieve("http://media.oboobs.ru/{}".format(nsfw), pic_loc)
    await event.client.send_file(event.chat_id, pic_loc, force_document=False)
    os.remove(pic_loc)
    await event.delete()
    await a.delete()


@borg.on(admin_cmd(pattern=r"butts"))
async def butts(event):
    pic_loc = os.path.join(TMP_DOWNLOAD_DIRECTORY, "butts.jpg")
    a = await event.edit("`Finding some beautiful butts 🧐...`")
    await asyncio.sleep(0.5)
    await a.edit("`Sending some beautiful butts 🌚...`")
    nsfw = requests.get("http://api.obutts.ru/noise/1").json()[0]["preview"]
    urllib.request.urlretrieve("http://media.obutts.ru/{}".format(nsfw), pic_loc)
    await event.client.send_file(event.chat_id, pic_loc, force_document=False)
    os.remove(pic_loc)
    await event.delete()
    await a.delete()
