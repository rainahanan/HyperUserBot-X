from ..utils import admin_cmd


@borg.on(admin_cmd(pattern="dad ?(.*)"))
async def _(event):


        await event.edit(
            " `hey girls my father didn't fuck ur mother then why u call me brother ? \n"
        )
