import telegram
from telegram.ext import Updater, CommandHandler, Dispatcher, Filters, MessageHandler
import logging
import token_code

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

bot_token = token_code.token

updater = Updater(token=bot_token, use_context=True)

dispatcher = updater.dispatcher

help_message = '/start - Mensagem de boas vindas\n'
help_message += 'Próximas funcionalidades em breve...'


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Bem vindo ao AniheartBot, em que posso ser útil hoje?\nGithub do projeto: https://github.com/MtHonorio/Aniheart-Telegram-Bot")


def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=help_message)


def unknown(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="Desculpe, não entendo esse comando.")


start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', help)
unknown_handler = MessageHandler(Filters.command, unknown)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(help_handler)
# Esse handler tem que ser add por ultimo
dispatcher.add_handler(unknown_handler)

updater.start_polling()
