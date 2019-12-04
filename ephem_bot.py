from telegram.ext import Updater, CommandHandler, MessageHandler, Filters 

PROXY = {'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}}

import logging
logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
import ephem

from datetime import datetime
dt_now = datetime.now()

def main():
    mybot = Updater("998165570:AAHwOKmYmf-86VvkMr-MQL4PfHl29N0RP80", request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler('planet', planet_text))
     
    mybot.start_polling()
    mybot.idle()

def greet_user(bot, update):
    print(update)
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def planet_text(bot, update):
    user_planet = update.message.text.split()
    planet = getattr(ephem, user_planet(dt_now))
    constellation = ephem.constellation(planet)
    print(constellation)
    update.message.reply_text(constellation)

def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)
       
main()  
