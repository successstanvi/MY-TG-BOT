from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from plugins.func.users_sql import *

@Client.on_message(filters.command ('start'))
async def cmd_start(Client, message):
  try:
    user_id = str(message.from_user.id)
    chat_type = str(message.chat.type)
    chat_id = str(message.chat.id)
    pm = fetchinfo(user_id)
    status = pm[2]
    if chat_type=="ChatType.PRIVATE" and status=="FREE" :
        resp = "𝗢𝗡𝗟𝗬 𝗣𝗥𝗘𝗠𝗜𝗨𝗠 𝗠𝗘𝗠𝗕𝗘𝗥𝗦 𝗔𝗥𝗘 𝗔𝗟𝗟𝗢𝗪𝗘𝗗 𝗧𝗢 𝗨𝗦𝗘 𝗕𝗢𝗧 𝗜𝗡 𝗣𝗘𝗥𝗦𝗢𝗡𝗔𝗟 ⚠️."
        await message.reply_text(resp,message.id)

      
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("𝗝𝗢𝗜𝗡 𝗛𝗘𝗥𝗘", url="https://t.me/ff_server_freeze")]
        ])
        await Client.send_message(
            chat_id=chat_id,
            text="""
𝗪𝗘𝗟𝗖𝗢𝗠𝗘 𝗧𝗢 𝗙𝗥𝗘𝗘 𝗙𝗜𝗥𝗘 𝗦𝗘𝗥𝗩𝗘𝗥 𝗙𝗥𝗘𝗘𝗭𝗘 ⚡️ 𝗕𝗢𝗧.

𝗝𝗢𝗜𝗡 𝗚𝗥𝗢𝗨𝗣 𝗧𝗢 𝗨𝗦𝗘 𝗧𝗛𝗜𝗦 𝗕𝗢𝗧 𝗙𝗢𝗥 𝗙𝗥𝗘𝗘""",
            reply_markup=keyboard
        )
        return
    # PLAN CHECK 
    texta = """
    𝗦𝘁𝗮𝗿𝘁𝗶𝗻𝗴 𝗙𝗥𝗘𝗘 𝗙𝗜𝗥𝗘 𝗦𝗘𝗥𝗩𝗘𝗥 𝗙𝗥𝗘𝗘𝗭𝗘 ⚡ ■□□
    """
    edit = await message.reply_text(texta, message.id)
    
    textb = """
    𝗦𝘁𝗮𝗿𝘁𝗶𝗻𝗴 𝗙𝗥𝗘𝗘 𝗙𝗜𝗥𝗘 𝗦𝗘𝗥𝗩𝗘𝗥 𝗙𝗥𝗘𝗘𝗭𝗘 ⚡ ■■□
    """
    edit = await Client.edit_message_text(message.chat.id, edit.id, textb)

    textc = """
    𝗦𝘁𝗮𝗿𝘁𝗶𝗻𝗴 𝗙𝗥𝗘𝗘 𝗙𝗜𝗥𝗘 𝗦𝗘𝗥𝗩𝗘𝗥 𝗙𝗥𝗘𝗘𝗭𝗘 ⚡ ■■■
    """
    edit = await Client.edit_message_text(message.chat.id, edit.id, textc)

    textd = f"""
𝗛𝗲𝘆 <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> 

𝗪𝗘𝗟𝗖𝗢𝗠𝗘 𝗧𝗢 𝗙𝗥𝗘𝗘 𝗙𝗜𝗥𝗘 𝗦𝗘𝗥𝗩𝗘𝗥 𝗙𝗥𝗘𝗘𝗭𝗘 ⚡ 𝗕𝗢𝗧. 𝗜 𝗔𝗠 𝗔 𝗦𝗘𝗥𝗩𝗘𝗥 𝗙𝗥𝗘𝗘𝗭𝗘 𝗕𝗢𝗧 .
𝗜 𝗖𝗔𝗡 𝗗𝗢 𝗠𝗔𝗡𝗬 𝗪𝗢𝗥𝗞𝗦.

𝗧𝗬𝗣𝗘 /register 𝗧𝗢 𝗖𝗢𝗡𝗧𝗜𝗡𝗨𝗘 𝗨𝗦𝗜𝗡𝗚 𝗠𝗘🥰🥰
    """
    edit = await Client.edit_message_text(message.chat.id, edit.id, textd)

    # Add "must join to use" button


    await plan_expirychk(user_id)
  except Exception as e:
    resp = "𝗨𝗦𝗘𝗥 𝗜𝗦 𝗡𝗢𝗧 𝗥𝗘𝗚𝗜𝗦𝗧𝗘𝗥𝗘𝗗 𝗧𝗢 𝗧𝗛𝗘 𝗕𝗢𝗧 ❌ \n𝗧𝗬𝗣𝗘 /register 𝗧𝗢 𝗖𝗢𝗡𝗧𝗜𝗡𝗨𝗘 𝗨𝗦𝗜𝗡𝗚"
    await message.reply_text(resp,message.id)
    print(e)
