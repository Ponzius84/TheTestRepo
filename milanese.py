#!/usr/bin/env python
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
from functions import Parser

TOKEN = "344707079:AAHSu8N5ibfJTsougIE-9-4UeTVZZ9DSWuM"
PORT = int(os.environ.get('PORT', '5000'))
updater = Updater(TOKEN)
# add handle
dp = updater.dispatcher

p = Parser()

#Handles
dp.add_handler(MessageHandler(Filters.text,p.rispostaTesto))
dp.add_handler(MessageHandler(Filters.photo,p.rispostaFoto))

updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.setWebhook("https://milanese-bot.herokuapp.com/" + TOKEN)
updater.idle()



