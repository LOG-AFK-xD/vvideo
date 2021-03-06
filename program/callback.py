# Copyright (C) 2021 By XmartyMusicProject

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Hello, My name is Happy MusÃ­c Bot.\n\nI'm a telegram streaming bot with some useful features. Supporting platforms like Youtube, Spotify, Resso, AppleMusic , Soundcloud etc.\n\nFeel free to add me to your groups.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ð How to Use? Commands Menu.",
                        callback_data="cbcmds",
                    )
                ], 
                [            
                    InlineKeyboardButton("ð¨ Support", url=f"https://t.me/TheMafiaSupport"),
                    InlineKeyboardButton("ð¨ Channel", url=f"https://t.me/TheMafiaNetwork"),               
                ],
                [
                    InlineKeyboardButton(
                        "â Add me to your Group", url=f"https://t.me/happy_ro_bot?startgroup=true"),
                ],
                [
                    InlineKeyboardButton(
                        "ð¤ Bot Owner", url=f"https://t.me/OFFICIAL_AFK_xD"
                    ),
                    InlineKeyboardButton(
                        "ð¡ About Me", url=f"https://t.me/iTzz_Official"                  
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "â³ï¸ chitchat ", url=f"https://t.me/UNIQUE_SOCIETY")                  
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""â **Basic Guide for using this bot:**

1.) **First, add me to your group.**
2.) **Then, promote me as administrator and give all permissions except Anonymous Admin.**
3.) **After promoting me, type /reload in group to refresh the admin data.**
3.) **Add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.**
4.) **Turn on the video chat first before start to play video/music.**
5.) **Sometimes, reloading the bot by using /reload command can help you to fix some problem.**

ð **If the userbot not joined to video chat, make sure if the video chat already turned on, or type /userbotleave then type /userbotjoin again.**

ð¡ **If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}**

ð¢ __Powered by- [TheMafiaNetwork](t.me/TheMafiaNetwork)__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ð Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

**Press the button below to read the explanation and see The list of Available commands !**

ð¢ __Powered by- [TheMafiaNetwork](t.me/TheMafiaNetwork)__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Admin Cmd", callback_data="cbadmin"),
                    InlineKeyboardButton("Sudo Cmd", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("Basic Cmd", callback_data="cbbasic"),
                    InlineKeyboardButton("Basic Cmd", callback_data="cbhowtouse"),
                ],[
                    InlineKeyboardButton("ðGo Back", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ð® Here is the basic commands:

Â» /play (song name/link) - play music on video chat
Â» /stream (query/link) - stream the yt live/radio live music
Â» /vplay (video name/link) - play video on video chat
Â» /vstream - play live video from yt live
Â» /playlist - show you the playlist
Â» /video (query) - download video from youtube
Â» /song (query) - download song from youtube
Â» /lyric (query) - scrap the song lyric
Â» /search (query) - search a youtube video link

Â» /ping - show the bot ping status
Â» /uptime - show the bot uptime status
Â» /alive - show the bot alive info (in group)

ð¢ __Powered by- [TheMafiaNetwork](t.me/TheMafiaNetwork)__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ð Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ð® Here is the admin commands:

Â» /pause - pause the stream
Â» /resume - resume the stream
Â» /skip - switch to next stream
Â» /stop - stop the streaming
Â» /vmute - mute the userbot on voice chat
Â» /vunmute - unmute the userbot on voice chat
Â» /reload - reload bot and refresh the admin data
Â» /userbotjoin - invite the userbot to join group
Â» /userbotleave - order userbot to leave from group

ð¢ __Powered by- [TheMafiaNetwork](t.me/TheMafiaNetwork)__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ð Go Back", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""ð® Here is the sudo commands:

Â» /rmw - clean all raw files
Â» /rmd - clean all downloaded files
Â» /leaveall - order userbot to leave from all group

ð¢ __Powered by- [TheMafiaNetwork](t.me/TheMafiaNetwork)__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("ð Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
