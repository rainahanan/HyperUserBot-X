import asyncio

from ..utils import admin_cmd
from . import ALIVE_NAME

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "HyperUserBot-X"

aryan = bot.uid


@borg.on(admin_cmd(pattern="dp ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("😎Jaha matter bada hota hai😎")
    await asyncio.sleep(2)
    await event.edit("{}😈wahi khada hota hai 💪".format(DEFAULTUSER, aryan))
    await asyncio.sleep(2)
    await event.edit("😡Tera baap hu madharchod😒")
    await asyncio.sleep(2)
    await event.edit("😏Naam yad rakhna😏")
    await asyncio.sleep(2)
    await event.edit("😎Tera baap {}🤓".format(DEFAULTUSER, aryan))
    await asyncio.sleep(2)
    await event.edit("🔥{}🔥".format(DEFAULTUSER, a))
    await asyncio.sleep(2)
    await event.edit(
        "😎Jaha matter bada hota hai😎. {} wahi khada hota hai😏".format(
            DEFAULTUSER, aryan
        )
    )
    await asyncio.sleep(2)
    await event.edit(
        "Tera baap hu madharchod😈. Naam yad rakhna😡. Tera baap {}. 🔥🔥🔥🔥🔥".format(
            DEFAULTUSER, aryan
        )
    )
