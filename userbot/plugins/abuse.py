from telethon.tl.types import ChannelParticipantsAdmins

from ..utils import admin_cmd


@borg.on(admin_cmd("abuse"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "MADARCHOODOO.••>__________BHAG BETA BHAG TERA BAAP AAYA___________<•••🔥 {DEFAULTUSER} HΣRΣ🔥RυKKKK RυKK βΣτΔΔ βHΔGGG KΔHΔ RΔHΔΔ HΔII ΔβHI τΟ τΣRI мΔΔ CHUDEGI RυKK☜☜☜мΔτLΔββ βΔβΥ MARBAKE MANEGI👅👅👅👅>>>>◑︿◐jhant bhar ki aukaat nhi teri aur baap ({DEFAULTUSER}) se ladega bhenchod◑︿◐<<<<<τΣRI βΣHΣП KI GΔПd мΣ LΟHΣ KΔ RΟδδ dΔL dυПGΔ🎋🎋🎋βILLII βΔПΔ KΣ ζHΟδυПGΔ τΣRI βΣHΣП KΟΟ▀▄▀▄▀▄τΣRI мΔΔ KI GΔПd мΣ βΣΔR KI βΟττLΣ dalL KΣ FΟdd δυПGΔ🍾🍾🍾__________________________βHΔGGG δΔRLIПG βHΔGGG_______GΔПδδ βΔζζHΔ KΣΣ βHΔGGGG_________βΔP ΔΥΔ τΣRΔ 😎{DEFAULTUSER} HΣRΣ😎>>>>>◑︿◐JHΔПτ βHΔRR KI ΔυKΔτ  ПΔHI τΣRI ΔυR βΔPPP ςΣ LΔδΣGΔΔΔ◑︿◐<<<<<τΣRI βΣHΣП KI GΔПδ мΣ LΟHΣ KΔ RΟδδ δΔL δυПGΔ🎋🎋🎋βILLII βΔПΔ KΣ ζHΟδυПGΔ τΣRI βΣHΣП KΟΟ▀▄▀▄▀{DEFAULTUSER} ΨΩUR ҒΔTHΣR HΣRΣ😎😎"
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
