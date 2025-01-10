from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import requests
import re
import subprocess
import time
from plugins.func.users_sql import *
from datetime import date
import random
import requests
import json


def detect_ip_format(ip):
    # Regular expression to match the pattern of IPv4 address
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    
    if re.match(pattern, ip):
        # Check if each part is between 0 and 255
        parts = ip.split('.')
        if all(0 <= int(part) <= 255 for part in parts):
            return  True
        else:
            return False
    else:
        return False





session = requests.session()
@Client.on_message(filters.command ('attack'))
async def cmd_chk(Client,message):

  try:

    msg = message.text[len('/attack '):]
    splitter = msg.split(' ')
    target = splitter[0]
    try:
      port = int(splitter[1])
      time_s = int(splitter[2])
    except:
        resp = "𝗜𝗡𝗩𝗔𝗟𝗜𝗗 Target_IP ,Port and Time."
        await message.reply_text(resp,message.id)
        return

    if detect_ip_format(target) is False:
      resp = "Error: Invalid Ip Sent Please Send me a Valid Ip To check."
      await message.reply_text(resp,message.id)
      return



    if time_s > 120:
      resp = "Error: Time interval must be less than 120 seconds."
      await message.reply_text(resp,message.id)
      return


  except Exception as e:
    print(e)
    resp = "𝗜𝗡𝗩𝗔𝗟𝗜𝗗 Target_IP ,Port and Time."
    await message.reply_text(resp,message.id)
    return





  try:
    user_id = str(message.from_user.id)
    chat_type = str(message.chat.type)
    chat_id = str(message.chat.id)
    #PLAN CHECK 
    await plan_expirychk(user_id)
    regdata = fetchinfo(user_id)
    results = str(regdata)
    if results=='None':
      resp = "𝗬𝗢𝗨 𝗔𝗥𝗘 𝗡𝗢𝗧 𝗥𝗘𝗚𝗜𝗦𝗧𝗘𝗥𝗘𝗗 𝗬𝗘𝗧 ⚠️. 𝗥𝗘𝗚𝗜𝗦𝗧𝗘𝗥 𝗙𝗜𝗥𝗦𝗧 𝗕𝗬 𝗨𝗦𝗜𝗡𝗚 /register 𝗧𝗢 𝗨𝗦𝗘 𝗠𝗘."
      await message.reply_text(resp,message.id)
    else:
      #HERE
      #PM AND AUTH CHECK
      pm = fetchinfo(user_id)
      status = pm[2]
      role = status
      GROUP = open("plugins/group.txt").read().splitlines()
      if chat_type=="ChatType.PRIVATE" and status=="FREE" :
        resp = "𝗢𝗡𝗟𝗬 𝗣𝗥𝗘𝗠𝗜𝗨𝗠 𝗠𝗘𝗠𝗕𝗘𝗥𝗦 𝗔𝗥𝗘 𝗔𝗟𝗟𝗢𝗪𝗘𝗗 𝗧𝗢 𝗨𝗦𝗘 𝗕𝗢𝗧 𝗜𝗡 𝗣𝗘𝗥𝗦𝗢𝗡𝗔𝗟 ⚠️."
        await message.reply_text(resp,message.id)
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("𝗝𝗢𝗜𝗡 𝗛𝗘𝗥𝗘", url="https://t.me/ff_server_freeze")]
        ])
        await Client.send_message(
            chat_id=chat_id,
            text="""
𝗝𝗢𝗜𝗡 𝗚𝗥𝗢𝗨𝗣 𝗧𝗢 𝗨𝗦𝗘 𝗧𝗛𝗜𝗦 𝗕𝗢𝗧 𝗙𝗢𝗥 𝗙𝗥𝗘𝗘""",
            reply_markup=keyboard
        )
        return
      
      elif chat_type=="ChatType.GROUP" or   chat_type=="ChatType.SUPERGROUP" and chat_id not in GROUP:
        resp = "𝗨𝗡𝗔𝗨𝗧𝗛𝗢𝗥𝗜𝗭𝗘𝗗 𝗖𝗛𝗔𝗧 ❌. 𝗖𝗢𝗡𝗧𝗔𝗖𝗧 @srfxdzz 𝗧𝗢 𝗔𝗨𝗧𝗛𝗢𝗥𝗜𝗭𝗘."
        await message.reply_text(resp,message.id)
      else:
        #CREDIT CHECK
        chk_credit = fetchinfo(user_id)
        credit = int(chk_credit[5])
        if credit < 3:
          resp = "𝗬𝗢𝗨 𝗛𝗔𝗩𝗘 𝗜𝗡𝗦𝗨𝗙𝗙𝗜𝗖𝗜𝗘𝗡𝗧 𝗖𝗥𝗘𝗗𝗜𝗧 𝗧𝗢 𝗨𝗦𝗘 𝗠𝗘 ⚠️ . 𝗥𝗘𝗖𝗛𝗔𝗥𝗚𝗘 𝗖𝗥𝗘𝗗𝗜𝗧 𝗨𝗦𝗜𝗡𝗚 /buy 𝗢𝗥 𝗪𝗔𝗜𝗧 𝗙𝗢𝗥 𝗙𝗥𝗘𝗘 𝗖𝗥𝗘𝗗𝗜𝗧 𝗨𝗦𝗜𝗡𝗚 𝗚𝗜𝗙𝗧𝗖𝗢𝗗𝗘 ."
          await message.reply_text(resp,message.id)
        else:
          #ANTISPAM MODULE
          user_id = str(message.from_user.id)
          results = fetchinfo(user_id)
          status = results[2]
          antispam_time = int(results[7])
          now = int(time.time())
          count_antispam = now - antispam_time
          if status=='FREE' and count_antispam < 100:
            after = 100 - count_antispam
            resp = f"""
Attack Failed  
Reason 𝗔𝗡𝗧𝗜𝗦𝗣𝗔𝗠 ⚠️ 𝗧𝗥𝗬 𝗔𝗚𝗔𝗜𝗡 𝗔𝗙𝗧𝗘𝗥 {after} 𝗦𝗘𝗖𝗢𝗡𝗗𝗦
            """
            await message.reply_text(resp,message.id)
          elif status=='PREMIUM' and count_antispam < 50:
            after = 50 - count_antispam
            resp = f"""
Attack Failed  
Reason 𝗔𝗡𝗧𝗜𝗦𝗣𝗔𝗠 ⚠️ 𝗧𝗥𝗬 𝗔𝗚𝗔𝗜𝗡 𝗔𝗙𝗧𝗘𝗥 {after} 𝗦𝗘𝗖𝗢𝗡𝗗𝗦
            """
            await message.reply_text(resp,message.id)
          
          else:
              module_name = "antispam_time"
              value = int(time.time())
              updatedata(user_id,module_name,value)
              fetch= fetchinfo(user_id)
              credit = int(fetch[5])
              module_name = "credit"
              deduct = credit - 10
              value = deduct
              updatedata(user_id,module_name,value)

                

              finalresp = f"""
<b>↯ 
✨\n𝗔𝗧𝗧𝗔𝗖𝗞 𝗦𝗧𝗔𝗥𝗧𝗘𝗗 🚀 BY {message.from_user.first_name} 
📡 𝗧𝗔𝗥𝗚𝗘𝗧: {target} 
🔌 𝗣𝗢𝗥𝗧: {port} 
⏱️ 𝗧𝗜𝗠𝗘: {time_s} 𝗦𝗘𝗖𝗢𝗡𝗗𝗦

𝐏𝐋𝐀𝐍: {results[3]}

Credit Deducted - 10
Checked by: <a href="tg://user?id={message.from_user.id}"> {message.from_user.first_name}</a> ♻️ [ {role} ]
Bot by - <a href="tg://user?id=7879803379">Sherlock Holmes </a>
－－－－－－－－－－－－－－－－</b>
            """
            
              finalchk = await message.reply_text(finalresp,message.id)
              full_command = f"./RAGNAROK {target} {port} {time_s}"
              #subprocess.run(full_command, shell=True)
              #ANTISPAM TIME SET

  except Exception as e:
      print(e)
