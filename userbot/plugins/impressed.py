from ..utils import admin_cmd


@borg.on(admin_cmd(pattern="impressgf ?(.*)"))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(
            " `meri gf bnjao tumhari har icha poori karuga .... Jo tum kahogi wo kruga plzz.. ban jao ..... I love you baby ....... Tumhare saare nakhre seh luga babes ..... I love you.... Maan jao 🥺🥺!\n"
        )
