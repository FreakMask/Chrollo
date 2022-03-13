import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from SiestaRobot.events import register
from SiestaRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/e0476d15503157bfb7795.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hello [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Chrollo Lucifer.** \n\n"
  TEXT += "🕷️ **The Spider Head is working properly** \n\n"
  TEXT += f"🕷️ **Committee: [Hunter Committee](https://t.me/Hunter_Committee)** \n\n"
  TEXT += f"🕷️ **Library Version :** `{telever}` \n\n"
  TEXT += f"🕷️ **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"🕷️ **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**Thanks For Adding Me Here 🕸️**"
  BUTTON = [[Button.url("Help ‼️", "https://t.me/Chrollo_Bot?start=help"), Button.url("Troupes 🕸️", "https://t.me/Phantom_Troupes")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
