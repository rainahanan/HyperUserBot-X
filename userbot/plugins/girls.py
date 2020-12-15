from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="dad ?(.*)"))
async def _(event):

    if not event.text[0].isalnpha() and event.text[0] not in ("/", "#", "@", "!"):

        await event.edit(
            " `hey girls my father didn't fuck ur mother then why u call me brother ? \n"
        )
