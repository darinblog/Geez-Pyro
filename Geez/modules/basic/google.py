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
import requests
from bs4 import BeautifulSoup
from googlesearch import search
from pyrogram import Client
from pyrogram.types import Message
from geezlibs.geez import geez
from geezlibs.geez.helper.basic import edit_or_reply

from Geez.modules.basic import add_command_help
from Geez import cmds

def googlesearch(query):
    co = 1
    returnquery = {}
    for j in search(query, num_results=10):
        url = str(j)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        metas = soup.find_all("meta")
        site_title = None
        for title in soup.find_all("title"):
            site_title = title.get_text()
        metadeta = [
            meta.attrs["content"]
            for meta in metas
            if "name" in meta.attrs and meta.attrs["name"] == "description"
        ]
        returnquery[co] = {"title": site_title, "metadata": metadeta, "url": j}
        co = co + 1
    return returnquery


@geez("google", cmds)
async def gs(client: Client, message: Message):
    Man = await edit_or_reply(message, "`Processing...`")
    msg_txt = message.text
    query = None
    if " " in msg_txt:
        query = msg_txt[msg_txt.index(" ") + 1:]
    else:
        await Man.edit("berikan sesuatu untuk mencari")
        return
    results = googlesearch(query)
    returnmsg = ""
    for i in range(1, 10, 1):
        presentquery = results[i]
        presenttitle = presentquery["title"]
        presentmeta = presentquery["metadata"]
        presenturl = presentquery["url"]
        presentmeta = "" if not presentmeta else presentmeta[0]
        returnmsg = f"{returnmsg}[{str(presenttitle)}]({str(presenturl)})\n{str(presentmeta)}\n\n"
    await Man.edit(returnmsg)


add_command_help(
    "google",
    [
        [ f"{cmds}google","Mencari melalui google."],
    ],
)
