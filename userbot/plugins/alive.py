import asyncio
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "My Boss"
PM_IMG = "https://telegra.ph/file/d7cbffcb6bae55874b1c2.jpg"
pm_caption = "**Lucifer ɪꜱ ᴏɴʟɪɴᴇ**\n"

pm_caption += f"**M̴y̴ ̴B̴o̴s̴s̴**            : {DEFAULTUSER}\n"

pm_caption += "ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ        :  15.0.0 \n"

pm_caption += "ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ          : [ᴊᴏɪɴ](https://t.me/lucifer_userbot)\n"

pm_caption += "ꜱᴜᴘᴘᴏʀᴛ ɢʀᴏᴜᴘ        : [ᴊᴏɪɴ](https://t.me/lucifer_support)\n"

pm_caption += "ʟɪᴄᴇɴꜱᴇ                 : [ᴍɪᴛ ʟɪᴄᴇɴꜱᴇ](https://github.com/silverhalobit/luciferuserbot/blob/master/LICENSE)\n"

pm_caption += "ᴄᴏᴘʏʀɪɢʜᴛ ʙʏ            : [SilVerHalobit](https://github.com/silverhalobit)\n"
pm_caption += " [┏┓━┏┓━━━━┏┓━┏┓\n ┃┃━┃┃━━━━┃┃━┃┃\n ┃┗━┛┃┏━━┓┃┃━┃┃\n ┃┏━┓┃┃┏┓┃┃┃━┃┃━\n ┃┃━┃┃┃┃━┫┃┗┓┃┗┓\n ┗┛━┗┛┗━━┛┗━┛┗━┛](https://t.me/LUCIFER_USERBOT)"
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is alive.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delet
