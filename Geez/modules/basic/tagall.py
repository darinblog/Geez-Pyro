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
from asyncio import sleep
from pyrogram import Client
from pyrogram.types import Message
from geezlibs.geez import geez
from Geez.modules.basic import add_command_help
from Geez import cmds

spam_chats = []

def get_arg(message: Message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    return "" if not " ".join(split[1:]).strip() else " ".join(split[1:])

@geez("tagall", cmds)
async def mentionall(client: Client, message: Message):
    chat_id = message.chat.id
    direp = message.reply_to_message
    args = get_arg(message)
    if not direp and not args:
        return await message.edit("**Send me a message or reply to a message!**")
    await message.delete()
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if chat_id not in spam_chats:
            break
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}), "
        if usrnum == 5:
            if args:
                txt = f"{args}\n\n{usrtxt}"
                await client.send_message(chat_id, txt)
            elif direp:
                await direp.reply(usrtxt)
            await sleep(2)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@geez("cancel", cmds)
async def cancel_spam(client: Client, message: Message):
    if message.chat.id not in spam_chats:
        return await message.edit("**It seems there is no tagall here.**")
    try:
        spam_chats.remove(message.chat.id)
    except:
        pass
    return await message.edit("**Cancelled.**")


add_command_help(
    "tagall",
    [
        [
            f"{cmds}tagall [text/reply ke chat]",
            f"{cmds}Tag all the members one by one",
        ],
        [f"{cmds}cancel", "to stop tagall"],
    ],
)
