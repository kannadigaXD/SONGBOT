from config import LOG, LOG_GROUP_ID, MUSIC_BOT_NAME
from ShizukaXMusic.utils.database import is_on_off
from ShizukaXMusic import app


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "𝙋 𝙍 𝙄 𝙑 𝘼 𝙏 𝙀 👀 𝘾 𝙃 𝘼 𝙏"
        logger_text = f"""
**━━━━━━━━━━━━━━━**
**👄 {MUSIC_BOT_NAME} ᴍᴜsɪᴄ ʟᴏɢs **
**━━━━━━━━━━━━━━━**
**👅 𝘾 𝙃 𝘼 𝙏 𝙉 𝘼 𝙈 𝙀 : >** {message.chat.title} [`{message.chat.id}`]
**━━━━━━━━━━━━━━━**
**👀 𝙉 𝘼 𝙈 𝙀 : ›** {message.from_user.mention}
**━━━━━━━━━━━━━━━**
**🎀 𝙐 𝙎 𝙀 𝙍 𝙉 𝘼 𝙈 𝙀 : ›** @{message.from_user.username}
**━━━━━━━━━━━━━━━**
**💜 𝙄 𝘿 𝙉 𝙊  : ›** `{message.from_user.id}`
**━━━━━━━━━━━━━━━**
**🦋 𝘾 𝙃 𝘼 𝙏 𝙇 𝙄 𝙉 𝙆: >** {chatusername}
**━━━━━━━━━━━━━━━**
**🥵 𝙎 𝙀 𝘼 𝙍 𝘾 𝙃 𝙀 𝘿:** {message.text}
**━━━━━━━━━━━━━━━**
**👉👈 𝙎 𝙏 𝙍 𝙀 𝘼 𝙈 𝙏 𝙔 𝙋 𝙀:** {streamtype}
**━━━━━━━━━━━━━━━**"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
