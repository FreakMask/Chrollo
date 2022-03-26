import os

import urllib

import aiohttp

import requests

from pyrogram import filters

from SiestaRobot import pbot as siesta_memer

@siesta_memer.on_message(filters.command("meme"))

async def memes(client, message):

    async with aiohttp.ClientSession() as siesta_session:

        async with siesta_session.get(

            "https://meme-api.herokuapp.com/gimme/wholesomememes/2"

        ) as resp:

            r = await resp.json()

            await message.reply_photo(r["url"], caption=r["title"])
