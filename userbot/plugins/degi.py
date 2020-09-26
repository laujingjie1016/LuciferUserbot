"""Fun pligon...for @PepeB0t
\nCode by @kirito6969 , ©[Eyepatch](https://t.me/NeoMatrix90)
type `.cat` and `.milli` to see the fun.
"""
import random, re
from uniborg.util import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="cat ?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("i")
        await asyncio.sleep(0.7)
        await event.edit("love")
        await asyncio.sleep(1)
        await event.edit("you")
        await asyncio.sleep(0.8)
        await event.edit("milli")
        await asyncio.sleep(0.9)
        await event.edit("i")
        await asyncio.sleep(1)
        await event.edit("love")
        await asyncio.sleep(0.8)
        await event.edit("uso")
        await asyncio.sleep(0.7)
        await event.edit("much")
        await asyncio.sleep(1)
        await event.edit("`i love you milli i love uso much`")

@borg.on(events.NewMessage(pattern=r"\.milli", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("`i love you milli i love uso much`")
    await asyncio.sleep(999)
