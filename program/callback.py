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
        f"""**Hello, My name is Log Afk Official Bot.
I'm a telegram streaming bot with some useful features. Supporting platforms like Youtube, Spotify, Resso, AppleMusic , Soundcloud etc.
Feel free to add me to your groups.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔎 How to Use? Commands Menu.",
                        callback_data="cbcmds",
                    )
                ], 
                [            
                    InlineKeyboardButton("📨 Support", url=f"https://t.me/BLAZE_SUPPORT"),
                    InlineKeyboardButton("📨 Channel", url=f"https://t.me/THE_BLAZE_NETWORK"),               
                ],
                [
                    InlineKeyboardButton(
                        "✚ Add me to your Group", url=f"https://t.me/LOG_AFK_OFFICIAL_BOT?startgroup=true"),
                ],
                [
                    InlineKeyboardButton(
                        "👤 Bot Owner", url=f"https://t.me/OFFICIAL_AFK_xD"
                    ),
                    InlineKeyboardButton(
                        "💡 About me", url=f"https://t.me/iTzz_Official"                  
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "✳️ ChatZone ", url=f"https://t.me/UNIQUE_SOCIETY")                  
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **Basic Guide for using this bot:**

1.) **First, add me to your group.**
2.) **Then, promote me as administrator and give all permissions except Anonymous Admin.**
3.) **After promoting me, type /reload in group to refresh the admin data.**
3.) **Add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.**
4.) **Turn on the video chat first before start to play video/music.**
5.) **Sometimes, reloading the bot by using /reload command can help you to fix some problem.**

📌 **If the userbot not joined to video chat, make sure if the video chat already turned on, or type /userbotleave then type /userbotjoin again.**

💡 **If you have a follow-up questions about this bot, you can tell it on my support chat here: @{GROUP_SUPPORT}**

📢 __Powered by- [TheMafiaNetwork](t.me/TheMafiaNetwork)__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""**Hello [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

📢**Press the button below to read the explanation and see The list of Available commands !**

📢 __Powered by- [TheMafiaNetwork](t.me/TheMafiaNetwork)__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Admin Cmd", callback_data="cbadmin"),
                    InlineKeyboardButton("Sudo Cmd", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("Basic Cmd", callback_data="cbbasic"),
                    InlineKeyboardButton("Basic Cmd", callback_data="cbhowtouse"),
                ],[
                    InlineKeyboardButton("🔙Go Back", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 Here is the basic commands:

» /play (song name/link) - play music on video chat
» /stream (query/link) - stream the yt live/radio live music
» /vplay (video name/link) - play video on video chat
» /vstream - play live video from yt live
» /playlist - show you the playlist
» /video (query) - download video from youtube
» /song (query) - download song from youtube
» /lyric (query) - scrap the song lyric
» /search (query) - search a youtube video link

» /ping - show the bot ping status
» /uptime - show the bot uptime status
» /alive - show the bot alive info (in group)

📢 __Powered by- [TheMafiaNetwork](t.me/TheMafiaNetwork)__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 Here is the admin commands:

» /pause - pause the stream
» /resume - resume the stream
» /skip - switch to next stream
» /stop - stop the streaming
» /vmute - mute the userbot on voice chat
» /vunmute - unmute the userbot on voice chat
» /reload - reload bot and refresh the admin data
» /userbotjoin - invite the userbot to join group
» /userbotleave - order userbot to leave from group

📢 __Powered by- [TheMafiaNetwork](t.me/TheMafiaNetwork)__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 Here is the sudo commands:

» /rmw - clean all raw files
» /rmd - clean all downloaded files
» /leaveall - order userbot to leave from all group

📢 __Powered by- [TheMafiaNetwork](t.me/TheMafiaNetwork)__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    await query.message.delete()
