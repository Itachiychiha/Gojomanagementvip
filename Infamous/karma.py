# https://github.com/Infamous-Hydra/YaeMiko
# https://github.com/Team-ProjectCodeX
# https://t.me/O_okarma

# <============================================== IMPORTS =========================================================>
from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from Mikobot import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT

# <============================================== CONSTANTS =========================================================>
START_IMG = [
    "https://telegra.ph/file/132744bfebc084cf9c310.jpg",
    "https://telegra.ph/file/132744bfebc084cf9c310.jpg",
    "https://telegra.ph/file/132744bfebc084cf9c310.jpg",
    "https://telegra.ph/file/f3da1ad7c8e806c8d9455.jpg",
    "https://telegra.ph/file/376f495328db607fbf95d.png",
    "https://telegra.ph/file/fdb7a743855967379ba9f.jpg",
    "https://telegra.ph/file/132744bfebc084cf9c310.jpg",
]

HEY_IMG = "https://telegra.ph/file/376f495328db607fbf95d.png"

ALIVE_ANIMATION = [
    "https://telegra.ph//file/f9e2b9cdd9324fc39970a.mp4",
    "https://telegra.ph//file/8d4d7d06efebe2f8becd0.mp4",
    "https://telegra.ph//file/c4c2759c5fc04cefd207a.mp4",
    "https://telegra.ph//file/b1fa6609b1c4807255927.mp4",
    "https://telegra.ph//file/f3c7147da6511fbe27c25.mp4",
    "https://telegra.ph//file/39071b73c02e3ff5945ca.mp4",
    "https://telegra.ph//file/8d4d7d06efebe2f8becd0.mp4",
    "https://telegra.ph//file/6efdd8e28756bc2f6e53e.mp4",
]

FIRST_PART_TEXT = "✨ *ʜᴇʟʟᴏ* `{}` . . ."

PM_START_TEXT = "✨ *ɪ ᴀᴍ ɢᴏᴊᴏ, ᴀ ᴊᴜᴊᴜᴛsᴜ ᴋᴀɪsᴇɴ ᴛʜᴇᴍᴇᴅ ʀᴏʙᴏᴛ ᴡʜɪᴄʜ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ ᴛᴏ ᴍᴀɴᴀɢᴇ ᴀɴᴅ ꜱᴇᴄᴜʀᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ʜᴜɢᴇ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ*"

START_BTN = [
    [
        InlineKeyboardButton(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="HELP", callback_data="help_back"),
    ],
    [
        InlineKeyboardButton(text="DETAILS", callback_data="Miko_"),
        InlineKeyboardButton(text="AI", callback_data="ai_handler"),
        InlineKeyboardButton(text="SOURCE", callback_data="git_source"),
    ],
    [
        InlineKeyboardButton(text="CREATOR", url=f"tg://user?id={OWNER_ID}"),
    ],
]

GROUP_START_BTN = [
    [
        InlineKeyboardButton(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text="SUPPORT", url=f"https://t.me/{SUPPORT_CHAT}"),
        InlineKeyboardButton(text="CREATOR", url=f"tg://user?id={OWNER_ID}"),
    ],
]

ALIVE_BTN = [
    [
        ib(text="UPDATES", url="https://t.me/Devine_Network"),
        ib(text="SUPPORT", url="https://t.me/Devine_Support"),
    ],
    [
        ib(
            text="⇦ ADD ME ⇨",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
]

HELP_STRINGS = """
🫧 *ɢᴏᴊᴏ* 🫧

☉ *Here, you will find a list of all the available commands.*

ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /
"""
