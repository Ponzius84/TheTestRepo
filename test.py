# !/usr/bin/env python
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
from random import randint

def milanese(bot, update):
    testo = update.message.text.lower()
    print(update.message)
    if (testo.find("milanese")!=-1):
        update.message.reply_text('{}, Va a ciapà i ratt'.format(update.message.from_user.first_name),quote=False)

def luxuria(bot, update):
    testo = update.message.text.lower()
    print(update.message)
    if (testo.find("luxuria") != -1):
        photo_ = open('images/vlad_1.jpg', 'rb')
        print(photo_)
        update.message.reply_photo(photo_,quote=False)

def rispostaFoto(bot, update):
    print(update.message)
    n = randint(0, 9)
    print(n)
    if (n == 0):
        print("si smessaggia")
        update.message.reply_text('Ue Avete finito o no, di postare foto come checche isteriche?',quote=False)




TOKEN = "344707079:AAHSu8N5ibfJTsougIE-9-4UeTVZZ9DSWuM"
PORT = int(os.environ.get('PORT', '5000'))
updater = Updater(TOKEN)
# add handle
dp = updater.dispatcher

#Handles
dp.add_handler(MessageHandler(Filters.text,milanese))
dp.add_handler(MessageHandler(Filters.text,luxuria))
dp.add_handler(MessageHandler(Filters.photo,rispostaFoto))

updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN)
updater.bot.setWebhook("https://milanese-bot.herokuapp.com/" + TOKEN)
updater.idle()
