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
    "https://telegra.ph/file/3a6e0bdb234f7f4fccdb6.mp4",
    "https://telegra.ph/file/1ed9379b42df13c0019ad.mp4",
    "https://telegra.ph/file/a5c7b3b3e1a51d2f84656.mp4",
    "https://telegra.ph/file/846d5d21d9351bed457ec.mp4",
    "https://telegra.ph/file/4dc9965b66caf621b06d4.mp4",
    "https://telegra.ph/file/f5a85dc3a19006905153e.mp4",
    "https://telegra.ph/file/df89957eeb15ecc58f54d.mp4",
    "https://telegra.ph/file/b707bf38341dfd9481fbe.mp4",
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
