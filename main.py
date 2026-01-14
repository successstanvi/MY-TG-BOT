import asyncio
from pyrogram import Client, compose, filters, enums
import re
from keep_alive import keep_alive
keep_alive()
from plugins.func.users_sql import *

plugins = dict(root="plugins")


async def main():

  bot = Client("my_bot",
               api_id="14011503",
               api_hash="10f47cfbbcc7326db4365c54ca89e3df",
               bot_token="7330308276:AAFcf8DY6NMeZMeniMyQc46qXsUoYhanuYk",
               plugins=plugins)
  clients = [bot]
  bot.set_parse_mode(enums.ParseMode.HTML)

  @bot.on_message(filters.command('adm_test'))
  async def cmd_help(client, message):
    await message.reply_text("i am working", message.id)



  print("Done Bot Active ✅")

  await compose(clients)


asyncio.run(main())
