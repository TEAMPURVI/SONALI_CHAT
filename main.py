from pyrogram import Client, filters
from pyrogram.types import *
from pymongo import MongoClient
from pyrogram.enums import ChatAction
from flask import Flask
import requests
import random
import threading
from random import choice
import os
import dns.resolver
import re
import asyncio
import time
from datetime import datetime
from pyrogram import enums
API_ID = os.environ.get("API_ID","27838385") 
API_HASH = os.environ.get("API_HASH","0710bd2a89a41c3506f98f7e6fd7294a") 
BOT_TOKEN = os.environ.get("BOT_TOKEN", None) 
# Set custom DNS resolver
dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers = ['8.8.8.8']  # Google DNS
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://teamdaxx123:teamdaxx123@cluster0.ysbpgcp.mongodb.net/?retryWrites=true&w=majority")
client = MongoClient(MONGO_URL, connectTimeoutMS=30000, serverSelectionTimeoutMS=30000)
db = client["Word"]
chatai = db["WordDb"]
BOT_USERNAME = os.environ.get("BOT_USERNAME","PURVI_CHAT_BOT") 
UPDATE_CHNL = os.environ.get("UPDATE_CHNL","PURVI_SUPPORT")
OWNER_USERNAME = os.environ.get("OWNER_USERNAME","ll_ALPHA_BABY_lll")
SUPPORT_GRP = os.environ.get("SUPPORT_GRP","PURVI_UPDATES")
BOT_NAME = os.environ.get("BOT_NAME", None)
START_IMG = os.environ.get("START_IMG","https://graph.org/file/6ccfbda0b79239188c14c.jpg")

STKR = os.environ.get("STKR","CAACAgEAAx0Cd5L74gAClqVmhNlbqSgKMe5TIswcgft9l6uSpgACEQMAAlEpDTnGkK-OP8PZpzUE")


StartTime = time.time()
Sonali = Client(
    "chat-gpt" ,
    api_id = API_ID ,
    api_hash = API_HASH ,
    bot_token = BOT_TOKEN
)
START =f"""
**๏ ʜᴇʏ, ɪ ᴀᴍ {BOT_NAME}**
**➻ᴀɴ ᴀɪ-ʙᴀsᴇᴅ ᴄʜᴀᴛʙᴏᴛ.**
**──────────────────**
**➻ ᴜsᴀɢᴇ /chatbot [on/off]**
**๏ ᴛᴏ ɢᴇᴛ ʜᴇʟᴘ ᴜsᴇ /help**
"""
SOURCE_TEXT = f"""
**๏ ʜᴇʏ, ɪ ᴀᴍ [{BOT_NAME}]
➻ ᴀɴ ᴀɪ-ʙᴀsᴇᴅ ᴄʜᴀᴛʙᴏᴛ.
──────────────────
ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ᴛʜᴇ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ**
"""
SOURCE_BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton('sᴏᴜʀᴄᴇ', callback_data='hurr')], [InlineKeyboardButton(" ꜱᴜᴘᴘᴏʀᴛ ", url=f"https://t.me/{SUPPORT_GRP}"), InlineKeyboardButton(text="ʙᴀᴄᴋ ", callback_data="HELP_BACK")]])
SOURCE = 'https://te.legra.ph/file/ebc3fc421b8776e29ad98.mp4'
x=["❤️","🎉","✨","🪸","🎉","🎈","🎯"]
g=choice(x)
async def is_admins(chat_id: int):
    return [
        member.user.id
        async for member in Mukesh.get_chat_members(
            chat_id, filter=enums.ChatMembersFilter.ADMINISTRATORS
        )
    ]

MAIN = [
    [
        InlineKeyboardButton(text="ᴅᴇᴠᴇʟᴏᴘᴇʀ", url=f"https://t.me/{OWNER_USERNAME}"),
        InlineKeyboardButton(text=" ꜱᴜᴘᴘᴏʀᴛ ", url=f"https://t.me/{SUPPORT_GRP}"),
    ],
    [
        InlineKeyboardButton(
            text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="ʜᴇʟᴘ & ᴄᴍᴅs ", callback_data="HELP"),
    ],
    [
        InlineKeyboardButton(text="sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", callback_data='source'),
        InlineKeyboardButton(text=" ᴜᴘᴅᴀᴛᴇs ", url=f"https://t.me/{UPDATE_CHNL}"),
    ],
]
PNG_BTN = [
    [
         InlineKeyboardButton(
             text="ᴀᴅᴅ ᴍᴇ ʙᴀʙʏ",
             url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
         ),
     ],
     [
         InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", 
                              url=f"https://t.me/{SUPPORT_GRP}",
         ),
     ],
]

HELP_READ = "**ᴜsᴀɢᴇ ☟︎︎︎**\n**➻ ᴜsᴇ** `/chatbot on` **ᴛᴏ ᴇɴᴀʙʟᴇ ᴄʜᴀᴛʙᴏᴛ.**\n**➻ ᴜsᴇ** `/chatbot off` **ᴛᴏ ᴅɪsᴀʙʟᴇ ᴛʜᴇ ᴄʜᴀᴛʙᴏᴛ.**\n**๏ ɴᴏᴛᴇ ➻ ʙᴏᴛʜ ᴛʜᴇ ᴀʙᴏᴠᴇ ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ ᴄʜᴀᴛ-ʙᴏᴛ ᴏɴ/ᴏғғ ᴡᴏʀᴋ ɪɴ ɢʀᴏᴜᴘ ᴏɴʟʏ!!**\n\n**➻ ᴜsᴇ** `/ping` **ᴛᴏ ᴄʜᴇᴄᴋ ᴛʜᴇ ᴘɪɴɢ ᴏғ ᴛʜᴇ ʙᴏᴛ.**\n||©️ @SHIVANSHDEVS||"
HELP_BACK = [
     
    [
           InlineKeyboardButton(text="ʙᴀᴄᴋ ", callback_data="HELP_BACK"),
    ]
]
@Sonali.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not UPDATE_CHNL:
        return
    try:
        try:
            await bot.get_chat_member(UPDATE_CHNL, msg.from_user.id)
        except UserNotParticipant:
            if UPDATE_CHNL.isalpha():
                link = "https://t.me/" + UPDATE_CHNL
            else:
                chat_info = await bot.get_chat(UPDATE_CHNL)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo=START_IMG, caption=f"» ᴀᴄᴄᴏʀᴅɪɴɢ ᴛᴏ ᴍʏ ᴅᴀᴛᴀʙᴀsᴇ ʏᴏᴜ'ᴠᴇ ɴᴏᴛ ᴊᴏɪɴᴇᴅ [ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ]({link}) ʏᴇᴛ, ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴜsᴇ ᴍᴇ ᴛʜᴇɴ ᴊᴏɪɴ [ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ]({link}) ᴀɴᴅ sᴛᴀʀᴛ ᴍᴇ ᴀɢᴀɪɴ !",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ", url=link),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"Promote me as an admin in the UPDATE CHANNEL  : {UPDATE_CHNL} !")
@Sonali.on_message(filters.command(["start",f"start@{BOT_USERNAME}"]))
async def restart(client, m: Message):
        accha = await m.reply_text(
                        text = f"{g}")
        await asyncio.sleep(1)
        await accha.edit("ᴘɪɴɢ ᴘᴏɴɢ ꜱᴛᴀʀᴛɪɴɢ..")
        await asyncio.sleep(0.5)
        await accha.edit("ᴜᴍ ꜱᴛᴀʀᴛɪɴɢ..")
        await asyncio.sleep(0.5)
        await accha.delete()
        umm = await m.reply_sticker(
                  sticker = STKR,
        )
        await asyncio.sleep(1)
        await umm.delete()
        await m.reply_photo(
            photo = START_IMG,
            caption=START,
            reply_markup=InlineKeyboardMarkup(MAIN),
        )
@Sonali.on_callback_query()
async def cb_handler(Client, query: CallbackQuery):
    if query.data == "HELP":
     await query.message.edit_text(
                      text = HELP_READ,
                      reply_markup = InlineKeyboardMarkup(HELP_BACK),
     )
    elif query.data == "HELP_BACK":
            await query.message.edit(
                  text = START,
                  reply_markup=InlineKeyboardMarkup(MAIN),
        )
    elif query.data == 'source':
        await query.message.edit_text(SOURCE_TEXT, reply_markup=SOURCE_BUTTONS)
    elif query.data == 'hurr':
        await query.answer()
        await query.message.reply(SOURCE)
@Sonali.on_message(filters.command(["help", f"help@{BOT_USERNAME}"], prefixes=["/"]))
async def restart(client, message):
    hmm = await message.reply_photo(START_IMG,
                             caption= HELP_READ,
                        reply_markup= InlineKeyboardMarkup(HELP_BACK),
       )
@Sonali.on_message(filters.command(['source', 'repo']))
async def source(bot, m):
    await m.reply_photo(START_IMG, caption=SOURCE_TEXT, reply_markup=SOURCE_BUTTONS, reply_to_message_id=m.id)
#  alive
@Sonali.on_message(filters.command(["ping","alive"], prefixes=["/"]))
async def ping(client, message: Message):
        start = datetime.now()
        t = "__ᴘɪɴɢ ʜᴏ ʀʜᴀ 😒...__"
        txxt = await message.reply(t)
        await asyncio.sleep(0.25)
        await txxt.edit_text("__ᴘɪɴɢ ʜᴏ ʀʜᴀ 😒.....__")
        await asyncio.sleep(0.35)
        await txxt.delete()
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await message.reply_photo(
                             photo=START_IMG,
                             caption=f"ʜᴇʏ ʙᴀʙʏ!!\n**[{BOT_NAME}](t.me/{BOT_USERNAME})** ɪꜱ ᴀʟɪᴠᴇ 🥀 ᴀɴᴅ ᴡᴏʀᴋɪɴɢ ꜰɪɴᴇ ᴡɪᴛʜ ᴘᴏɴɢ ᴏꜰ \n➥ `{ms}` ms\n\n**ᴍᴀᴅᴇ ᴡɪᴛʜ ❣️ ʙʏ || [SHIVANSH](https://t.me/SHIVANSHDEVS)||**",
                             reply_markup=InlineKeyboardMarkup(PNG_BTN),
       )

@Sonali.on_message(
    filters.command(["chatbot off", f"chatbot@{BOT_USERNAME} off"], prefixes=["/"])
    & ~filters.private)
async def chatbotofd(client, message):
    vickdb = MongoClient(MONGO_URL)    
    vick = vickdb["VickDb"]["Vick"]     
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
           await is_admins(chat_id)
        ):
           return await message.reply_text(
                "You are not admin"
            )
    is_vick = vick.find_one({"chat_id": message.chat.id})
    if not is_vick:
        vick.insert_one({"chat_id": message.chat.id})
        await message.reply_text(f"Chatbot Disabled!")
    if is_vick:
        await message.reply_text(f"ChatBot Already Disabled")
    

@Sonali.on_message(
    filters.command(["chatbot on", f"chatbot@{BOT_USERNAME} on"] ,prefixes=["/"])
    & ~filters.private)
async def chatboton(client, message):
    vickdb = MongoClient(MONGO_URL)    
    vick = vickdb["VickDb"]["Vick"]     
    if message.from_user:
        user = message.from_user.id
        chat_id = message.chat.id
        if user not in (
            await is_admins(chat_id)
        ):
            return await message.reply_text(
                "You are not admin"
            )
    is_vick = vick.find_one({"chat_id": message.chat.id})
    if not is_vick:           
        await message.reply_text(f"Chatbot Already Enabled")
    if is_vick:
        vick.delete_one({"chat_id": message.chat.id})
        await message.reply_text(f"ChatBot Enabled!")
    

@Sonali.on_message(
    filters.command(["chatbot", f"chatbot@{BOT_USERNAME}"], prefixes=["/"])
    & ~filters.private)
async def chatbot(client, message):
    await message.reply_text(f"**ᴜsᴀɢᴇ:**\n/**chatbot [on/off]**\n**ᴄʜᴀᴛ-ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅ(s) ᴡᴏʀᴋ ɪɴ ɢʀᴏᴜᴘ ᴏɴʟʏ!**")


# Non-private chats handler (both text and stickers)
Sonali.on_message((filters.text | filters.sticker) & ~filters.private & ~filters.bot)
async def vickai(client: Client, message: Message):
    if not message.reply_to_message:
        vick = db["VickDb"]["Vick"]
        is_vick = vick.find_one({"chat_id": message.chat.id})

        if not is_vick:
            await Sonali.send_chat_action(message.chat.id, ChatAction.TYPING)

            results = chatai.find({"word": message.text})
            results_list = [result for result in results]

            if results_list:
                result = random.choice(results_list)
                if result.get('check') == "sticker":
                    await message.reply_sticker(result['text'])
                else:
                    await message.reply_text(result['text'])

# Private chats handler (both text and stickers)
@Sonali.on_message((filters.text | filters.sticker) & filters.private & ~filters.bot)
async def vickprivate(client: Client, message: Message):
    if not message.reply_to_message:
        await Sonali.send_chat_action(message.chat.id, ChatAction.TYPING)

        results = chatai.find({"word": message.text})
        results_list = [result for result in results]

        if results_list:
            result = random.choice(results_list)
            if result.get('check') == "sticker":
                await message.reply_sticker(result['text'])
            else:
                await message.reply_text(result['text'])

# Flask Web Server (for keep-alive)
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

# Flask ko alag thread mein run karne ka function
def run_flask():
    app.run(host="0.0.0.0", port=8000)

# Keep-alive function jo periodic ping bhejta hai
def keep_alive():
    while True:
        try:
            # Apne Render app ya kisi bhi remote URL ko ping karein
            requests.get("https://sonali-chat.onrender.com")
        except Exception as e:
            print(f"Ping error: {e}")
        time.sleep(300)  # Har 5 minute mein ping bhejna

# Bot ko run karne ka function
def run_bot():
    print(f"{BOT_NAME} ɪs ᴀʟɪᴠᴇ!")
    Sonali.run()

if __name__ == "__main__":
    # Flask server ko alag thread mein run karna
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # Keep-alive function ko alag thread mein run karna
    keep_alive_thread = threading.Thread(target=keep_alive)
    keep_alive_thread.daemon = True
    keep_alive_thread.start()

    # Bot ko main thread mein run karna
    run_bot()
