from telethon.tl.types import ChannelParticipantsAdmins

from ..utils import admin_cmd


@borg.on(admin_cmd("gandu"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "Gandu bhosdhike bhenkelode macchar ki jhat matherchod maaaaa ki chut teri ..fathe condom ke natije....ma se pooch kitna dard hua tha gandu.......jhaant jitni bhi badi ho jaye lund ke niche hi rhti he .......tatto ke saudagar"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()
