# !/usr/bin/env python
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
def start(bot, update):
    update.message.reply_text('Hi!')

def risposta(bot, update):
    if (update.message.text.find("cazzone")!=-1):
        update.message.reply_text('stronzo!',quote=False)

def rispostaFoto(bot, update):
        update.message.reply_text('hai rotto la minchia')


TOKEN = "344707079:AAHSu8N5ibfJTsougIE-9-4UeTVZZ9DSWuM"
PORT = int(os.environ.get('PORT', '5000'))
updater = Updater(TOKEN)
# add handle
dp = updater.dispatcher
dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text,risposta))
dp.add_handler(MessageHandler(Filters.photo,rispostaFoto))

updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.setWebhook("https://milanese-bot.herokuapp.com/" + TOKEN)
updater.idle()
