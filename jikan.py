import telegram
from telegram.ext import Updater, CommandHandler, Dispatcher, Filters, MessageHandler
import requests
import logging
import token_code
import json
from jikanpy import Jikan

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

#requisicao = requests.get()
#context.bot.send_photo(chat_id=update.effective_chat.id, photo=r)

jikan = Jikan()
# print(jikan.anime(9874))
#print(jikan.search('anime', 'Slime'))


class JikanMAL(object):

    def __init__(self):
        TOKEN = token_code.token

        self.updater = Updater(token=TOKEN, use_context=True)
        self.dispatcher = self.updater.dispatcher

    def run(self):
        start_handler = CommandHandler('start', self.start)
        anime_handler = CommandHandler('anime', self.anime)

        self.dispatcher.add_handler(start_handler)
        self.dispatcher.add_handler(anime_handler)

        # self.dispatcher.add_handler(dinamico_handler)

        self.updater.start_polling()

    '''
        IMPLEMENTAÇÃO DE COMANDOS
    '''

    def start(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Bem vindo ao AniheartBot, em que posso ser útil hoje?\n")

    def anime(self, update, context):
        argumento = ' '.join(context.args)
        print(argumento)
        requisicao = jikan.search('anime', argumento)
        # print(requisicao['results'][0]['image_url'])
        i = 0
        while (i < len(requisicao['results'])):
            i += 1
            img = requisicao['results'][i]['image_url']
            title = requisicao['results'][i]['title']
            sinopse = requisicao['results'][i]['synopsis']
            ep = requisicao['results'][i]['episodes']
            context.bot.send_photo(chat_id=update.effective_chat.id, photo=img)
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='título: ' + title + '\n' + 'sinopse: ' + sinopse + '\n' + 'episódios: ' + str(ep))
            if (i == 5):
                break

        #img = requisicao['results'][i]['image_url']
        #context.bot.send_photo(chat_id=update.effective_chat.id, photo=img)


    # def dinamico(self, update, context):
    ##    print('Chamada de função de dinâmica')
    # pega somente a primeira palavra apos o comando
    ##    categoria = context.args[0]
    ##    print('Categoria: ' + categoria)
    ##    img = hmtai.useHM(version="v2", category="" + categoria)
    ##    context.bot.send_photo(chat_id=update.effective_chat.id, photo=img)
bot = JikanMAL()
bot.run()
