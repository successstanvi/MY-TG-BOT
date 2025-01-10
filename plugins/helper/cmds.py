from pyrogram import Client, filters
from plugins.func.users_sql import *
@Client.on_message(filters.command ('cmds'))
async def cmd_cmds(Client,message):
  try:
    user_id = str(message.from_user.id)
    regdata = fetchinfo(user_id)
    results = str(regdata)
    if results=='None':
      resp = "𝗬𝗢𝗨 𝗔𝗥𝗘 𝗡𝗢𝗧 𝗥𝗘𝗚𝗜𝗦𝗧𝗘𝗥𝗘𝗗 𝗬𝗘𝗧 ⚠️. 𝗥𝗘𝗚𝗜𝗦𝗧𝗘𝗥 𝗙𝗜𝗥𝗦𝗧 𝗕𝗬 𝗨𝗦𝗜𝗡𝗚 /register 𝗧𝗢 𝗨𝗦𝗘 𝗠𝗘."
      await message.reply_text(resp,message.id)
    else:
      user_id = str(message.from_user.id)
      chat_type = str(message.chat.type)
      chat_id = str(message.chat.id)
      #PLAN CHECK 
      await plan_expirychk(user_id)
      texta = f"""
  𝗛𝗲𝘆 <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
  𝗟𝗼𝗮𝗱𝗶𝗻𝗴 𝗮𝗹𝗹 𝗼𝗳 𝗦𝗘𝗥𝗩𝗘𝗥 𝗙𝗥𝗘𝗘𝗭𝗘 𝗖𝗼𝗺𝗺𝗮𝗻𝗱𝘀..
      """
      msg1 = await message.reply_text(texta,message.id)
      textb = """
 𝗦𝗘𝗥𝗩𝗘𝗥 𝗙𝗥𝗘𝗘𝗭𝗘 ⚡ 𝗔𝗟𝗟 𝗖𝗢𝗠𝗠𝗔𝗡𝗗𝗦 -

● 𝗦𝗘𝗥𝗩𝗘𝗥 𝗙𝗥𝗘𝗘𝗭𝗘 𝗖𝗢𝗠𝗠𝗔𝗡𝗗
➔ /attack <code>{Target Ip} {Port} {Time}</code>

● 𝗞𝗡𝗢𝗪 𝗨𝗦𝗘𝗥 𝗜𝗗 𝗖𝗠𝗗
➔ <code>/id</code>
● 𝗞𝗡𝗢𝗪 𝗨𝗦𝗘𝗥 𝗣𝗥𝗢𝗙𝗜𝗟𝗘 𝗖𝗠𝗗
➔ <code>/info</code>
● 𝗞𝗡𝗢𝗪 𝗨𝗦𝗘𝗥 𝗖𝗥𝗘𝗗𝗜𝗧 𝗖𝗠𝗗
➔ <code>/credits</code>
● 𝗡𝗘𝗪 𝗨𝗦𝗘𝗥 𝗥𝗘𝗚 𝗖𝗠𝗗

➔ <code>/crdsystem</code>
● 𝗔𝗗𝗗 𝗕𝗢𝗧 𝗧𝗢 𝗬𝗢𝗨𝗥 𝗚𝗥𝗢𝗨𝗣 𝗖𝗠𝗗

➔ <code>/howgp</code>
● 𝗣𝗨𝗥𝗖𝗛𝗔𝗦𝗘 𝗕𝗢𝗧 𝗣𝗔𝗜𝗗 𝗣𝗟𝗔𝗡 𝗖𝗠𝗗
➔ <code>/buy</code>
      """
      msg2 = await     Client.edit_message_text(message.chat.id,msg1.id,textb)
  except Exception as e:
      msg1 = await message.reply_text(e,message.id)
      print(e)