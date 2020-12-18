#    Copyright (C) Midhun KM 2020
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from userbot import catversion



PM_IMG = "https://telegra.ph/file/22535f8051a58af113586.jpg"
hubx_caption = "➥ **ASSISTANT IS:** `ONLINE`\n\n"
hubx_caption += "➥ **SYSTEMS STATS**\n"
hubx_caption += "➥ **Telethon Version:** `1.15.0` \n"
hubx_caption += "➥ **Python:** `3.7.4` \n"
hubx_caption += "➥ **Database Status:**  `Functional`\n"
hubx_caption += "➥ **Current Branch** : `main`\n"
hubx_caption += f"➥ **Version** : `{catversion}`\n"
hubx_caption += "➥ **Heroku Database** : `AWS - Working Properly`\n\n"
hubx_caption += "➥ **License** : [GNU General Public License v3.0](github.com/StarkGang/FridayUserbot/blob/master/LICENSE)\n"

# only Owner Can Use it
@assistant_cmd("alive", is_args=False)
@peru_only
async def friday(event):
    await tgbot.send_file(event.chat_id, PM_IMG, caption=hubx_caption)
