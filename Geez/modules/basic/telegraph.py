"""
if you can read this, this meant you use code from Geez | Ram Project
this code is from somewhere else
please dont hestitate to steal it
because Geez and Ram doesn't care about credit
at least we are know as well
who Geez and Ram is


kopas repo dan hapus credit, ga akan jadikan lu seorang developer

YANG NYOLONG REPO INI TRUS DIJUAL JADI PREM, LU GAY...
©2023 Geez | Ram Team
"""
import os
from pyrogram import Client
from pyrogram.types import Message
from telegraph import Telegraph, exceptions, upload_file
from geezlibs.geez import geez
from Geez.modules.basic import add_command_help
from Geez import cmds

telegraph = Telegraph()
r = telegraph.create_account(short_name="telegram")
auth_url = r["auth_url"]



def get_text(message: Message) -> [None, str]:
    """Extract Text From Commands"""
    text_to_return = message.text
    if message.text is None:
        return None
    if " " not in text_to_return:
        return None
    try:
        return message.text.split(None, 1)[1]
    except IndexError:
        return None

@geez(["tg", "tm", "telegraph"], cmds)
async def uptotelegraph(client: Client, message: Message):
    tex = await message.edit_text("`Processing . . .`")
    if not message.reply_to_message:
        await tex.edit(
            "**Reply to an Image or text.**"
        )
        return
    if message.reply_to_message.media:
        if message.reply_to_message.sticker:
            m_d = await convert_to_image(message, client)
        else:
            m_d = await message.reply_to_message.download()
        try:
            media_url = upload_file(m_d)
        except exceptions.TelegraphException as exc:
            await tex.edit(f"**ERROR:** `{exc}`")
            os.remove(m_d)
            return
        U_done = (
            f"**Uploaded on ** [Telegraph](https://telegra.ph/{media_url[0]})"
        )
        await tex.edit(U_done)
        os.remove(m_d)
    elif message.reply_to_message.text:
        page_title = get_text(message) if get_text(message) else client.me.first_name
        page_text = message.reply_to_message.text
        page_text = page_text.replace("\n", "<br>")
        try:
            response = telegraph.create_page(page_title, html_content=page_text)
        except exceptions.TelegraphException as exc:
            await tex.edit(f"**ERROR:** `{exc}`")
            return
        wow_graph = f"**Uploaded as** [Telegraph](https://telegra.ph/{response['path']})"
        await tex.edit(wow_graph)


add_command_help(
    "telegraph",
    [
        [
            f"{cmds}telegraph `or` {cmds}tg",
            "To upload on telegraph.",
        ],
    ],
)
