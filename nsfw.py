import telegram
from telegram.ext import Updater, CommandHandler, Dispatcher, Filters, MessageHandler
import requests
import logging
import token_code
import hmtai

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

#requisicao = requests.get()

print(hmtai.useHM(version="v2", category="ass"))
#context.bot.send_photo(chat_id=update.effective_chat.id, photo=r)

# print(r)


class Hentaii(object):

    def __init__(self):
        TOKEN = token_code.token

        self.updater = Updater(token=TOKEN, use_context=True)
        self.dispatcher = self.updater.dispatcher

    def run(self):
        start_handler = CommandHandler('start', self.start)
        ass_handler = CommandHandler('ass', self.ass)
        dinamico_handler = CommandHandler('dinamico', self.dinamico)

        self.dispatcher.add_handler(start_handler)
        self.dispatcher.add_handler(ass_handler)
        self.dispatcher.add_handler(dinamico_handler)

        self.updater.start_polling()

    '''
        IMPLEMENTAÇÃO DE COMANDOS
    '''

    def start(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Bem vindo ao AniheartBot, em que posso ser útil hoje?\n")

    def ass(self, update, context):
        print('Chamada de função de ass')
        img = hmtai.useHM(version="v2", category="ass")
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img)

    def dinamico(self, update, context):
        print('Chamada de função de dinâmica')
        categoria = context.args[0]
        print('Categoria: ' + categoria)
        img = hmtai.useHM(version="v2", category="" + categoria)
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img)


bot = Hentaii()
bot.run()
