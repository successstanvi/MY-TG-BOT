from pyrogram import Client, filters
from plugins.func.users_sql import *
import os 
@Client.on_message(filters.command ('admincmd'))
async def cmd_adm(Client,message):
  user_id = str(message.from_user.id)
  CEO = "7879803379"
  if user_id != CEO :
    resp = "𝗥𝗲𝗾𝘂𝗶𝗿𝗲 𝗢𝘄𝗻𝗲𝗿 𝗣𝗿𝗶𝘃𝗶𝗹𝗮𝗴𝗲𝘀 ⚠️"
    msg1 = await message.reply_text(resp,message.id)
  else:
    resp = f"""
𝗦𝗘𝗥𝗩𝗘𝗥 𝗙𝗥𝗘𝗘𝗭𝗘 ⚡ 𝗔𝗗𝗠𝗜𝗡 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 -

● 𝗔𝗨𝗧𝗛 𝗔 𝗚𝗥𝗢𝗨𝗣 𝗖𝗠𝗗
➔ <code>/add -10098796668</code>
● 𝗣𝗥𝗢𝗠𝗢𝗧𝗘 𝗔 𝗨𝗦𝗘𝗥 𝗖𝗠𝗗
➔ <code>/pm 1386450737</code>
● 𝗗𝗘𝗠𝗢𝗧𝗘 𝗔 𝗨𝗦𝗘𝗥 𝗖𝗠𝗗
➔ <code>/demote 1386450737</code>
● 𝗦𝗧𝗔𝗥𝗧𝗘𝗥 𝗣𝗟𝗔𝗡 𝗖𝗠𝗗
➔ <code>/plan1 1386450737</code>
● 𝗦𝗜𝗟𝗩𝗘𝗥 𝗣𝗟𝗔𝗡 𝗖𝗠𝗗
➔ <code>/plan2 1386450737</code>
● 𝗚𝗢𝗟𝗗 𝗣𝗟𝗔𝗡 𝗖𝗠𝗗
➔ <code>/plan3 1386450737</code>
● 𝗚𝗘𝗡𝗔𝗥𝗔𝗧𝗘 𝗦𝗧𝗔𝗥𝗧𝗘𝗥 𝗚𝗖 𝗖𝗠𝗗
➔ /getplan1
● 𝗚𝗘𝗡𝗔𝗥𝗔𝗧𝗘 𝗦𝗜𝗟𝗩𝗘𝗥 𝗚𝗖 𝗖𝗠𝗗
➔ /getplan2 
● 𝗚𝗘𝗡𝗔𝗥𝗔𝗧𝗘 𝗚𝗢𝗟𝗗 𝗚𝗖 𝗖𝗠𝗗
➔ /getplan3
● 𝗚𝗜𝗩𝗘 𝗖𝗥𝗘𝗗𝗜𝗧 𝗧𝗢 𝗔 𝗨𝗦𝗘𝗥 𝗖𝗠𝗗
➔ <code>/ac 100 1386450737</code>
● 𝗕𝗥𝗢𝗔𝗗𝗖𝗔𝗦𝗧 𝗠𝗘𝗦𝗦𝗔𝗚𝗘 𝗧𝗢 𝗔𝗟𝗟 𝗨𝗦𝗘𝗥𝗦 𝗖𝗠𝗗
➔ <code>/brod message</code>
    """
    await message.reply_text(resp,message.id)
  
    

@Client.on_message(filters.command ('getusers'))
async def cmd_adm_2(Client,message):
  user_id = str(message.from_user.id)
  CEO = "7879803379"
  if user_id != CEO :
    resp = "𝗥𝗲𝗾𝘂𝗶𝗿𝗲 𝗢𝘄𝗻𝗲𝗿 𝗣𝗿𝗶𝘃𝗶𝗹𝗮𝗴𝗲𝘀 ⚠️"
    msg1 = await message.reply_text(resp,message.id)
  else:
    filter_user = "users"
    get_all_user = getalldata(filter_user)

    for item in get_all_user:
        chat_id = item[1]
        with open("user_temp.txt","a",encoding="utf-8") as f:
          f.write(chat_id+"\n")
          f.close()

    file_path = "user_temp.txt"
    await message.reply_text("Data Sent To Inbox ✅ ",message.id)
    await Client.send_document(message.from_user.id,file_path)

    os.remove(file_path)