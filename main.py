from pickle import TRUE
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
from config import TOKEN
from func import*

global candies  
global game_on 
candies = 200
game_on = False

bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)#/start 
game_handler = CommandHandler('Poehali', game)#/info
computer_handler =CommandHandler('Computer', game)
#human_handler = CommandHandler('Human', game)
message_handler = MessageHandler(Filters.text, message)
unknown_handler = MessageHandler(Filters.command, unknown) #/game




dispatcher.add_handler(start_handler)
dispatcher.add_handler(game_handler)
dispatcher.add_handler(computer_handler)
#dispatcher.add_handler(human_handler)
dispatcher.add_handler(unknown_handler)
dispatcher.add_handler(message_handler)

print('server started')
updater.start_polling()
updater.idle()