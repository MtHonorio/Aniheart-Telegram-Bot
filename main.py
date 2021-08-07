import telegram
from telegram.ext import Updater, CommandHandler, Dispatcher, Filters, MessageHandler
import logging
import token_code

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# adicione seu token em um .env
TOKEN = token_code.token

updater = Updater(token=TOKEN, use_context=True)

dispatcher = updater.dispatcher

help_message = '/start - Mensagem de boas vindas\n'
help_message += '/image - Envia a logo do bot\n'
help_message += '/collaborate - Envia o github do projeto\n'
help_message += 'Mais funcionalidades em breve...'

collaborate_message = 'Github do projeto: https://github.com/MtHonorio/Aniheart-Telegram-Bot\n'


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Bem vindo ao AniheartBot, em que posso ser útil hoje?\n")


def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=help_message)


def image(update, context):
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo=open('img/jsks_pixabay.png', 'rb'))


def collaborate(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=collaborate_message)


def unknown(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Desculpe, não entendo esse comando.")


start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', help)
image_handler = CommandHandler('image', image)
collaborate_handler = CommandHandler('collaborate', collaborate)
unknown_handler = MessageHandler(Filters.command, unknown)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(image_handler)
dispatcher.add_handler(collaborate_handler)
# Esse handler tem que ser add por ultimo
dispatcher.add_handler(unknown_handler)

updater.start_polling()
