import telegram
from telegram.ext import Updater, CommandHandler, Dispatcher, Filters, MessageHandler
import requests
import logging
import token_code
import hmtai
from jikanpy import Jikan

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

#requisicao = requests.get()
#context.bot.send_photo(chat_id=update.effective_chat.id, photo=r)

#jikan = Jikan()
# print(jikan.anime(9874))


class HentaiImage(object):

    def __init__(self):
        TOKEN = token_code.token

        self.updater = Updater(token=TOKEN, use_context=True)
        self.dispatcher = self.updater.dispatcher

    def run(self):
        start_handler = CommandHandler('start', self.start)
        #####SFW#####
        neko_handler = CommandHandler('neko', self.neko)
        wallpaper_handler = CommandHandler('wallpaper', self.wallpaper)
        mobileWallpaper_handler = CommandHandler(
            'mobileWallpaper', self.mobileWallpaper)
        #####NSFW#####
        ass_handler = CommandHandler('ass', self.ass)
        bdsm_handler = CommandHandler('bdsm', self.bdsm)
        cum_handler = CommandHandler('cum', self.cum)
        manga_handler = CommandHandler('manga', self.manga)
        femdom_handler = CommandHandler('femdom', self.femdom)
        hentai_handler = CommandHandler('hentai', self.hentai)
        masturbation_handler = CommandHandler(
            'masturbation', self.masturbation)
        ero_handler = CommandHandler('ero', self.ero)
        orgy_handler = CommandHandler('orgy', self.orgy)
        yuri_handler = CommandHandler('yuri', self.yuri)
        glasses_handler = CommandHandler('glasses', self.glasses)
        cuckold_handler = CommandHandler('cuckold', self.cuckold)
        blowjob_handler = CommandHandler('blowjob', self.blowjob)
        foot_handler = CommandHandler('foot', self.foot)
        thighs_handler = CommandHandler('thighs', self.thighs)
        ahegao_handler = CommandHandler('ahegao', self.ahegao)
        uniform_handler = CommandHandler('uniform', self.uniform)
        gangbang_handler = CommandHandler('gangbang', self.gangbang)
        tentacles_handler = CommandHandler('tentacles', self.tentacles)
        nsfwNeko_handler = CommandHandler('nsfwNeko', self.nsfwNeko)
        nsfwMobileWallpaper_handler = CommandHandler(
            'nsfwMobileWallpaper', self.nsfwMobileWallpaper)

        ##dinamico_handler = CommandHandler('dinamico', self.dinamico)

        self.dispatcher.add_handler(start_handler)
        self.dispatcher.add_handler(neko_handler)
        self.dispatcher.add_handler(wallpaper_handler)
        self.dispatcher.add_handler(mobileWallpaper_handler)
        self.dispatcher.add_handler(ass_handler)
        self.dispatcher.add_handler(bdsm_handler)
        self.dispatcher.add_handler(cum_handler)
        self.dispatcher.add_handler(manga_handler)
        self.dispatcher.add_handler(femdom_handler)
        self.dispatcher.add_handler(hentai_handler)
        self.dispatcher.add_handler(masturbation_handler)
        self.dispatcher.add_handler(ero_handler)
        self.dispatcher.add_handler(orgy_handler)
        self.dispatcher.add_handler(yuri_handler)
        self.dispatcher.add_handler(glasses_handler)
        self.dispatcher.add_handler(cuckold_handler)
        self.dispatcher.add_handler(blowjob_handler)
        self.dispatcher.add_handler(foot_handler)
        self.dispatcher.add_handler(thighs_handler)
        self.dispatcher.add_handler(ahegao_handler)
        self.dispatcher.add_handler(uniform_handler)
        self.dispatcher.add_handler(gangbang_handler)
        self.dispatcher.add_handler(tentacles_handler)
        self.dispatcher.add_handler(nsfwNeko_handler)
        self.dispatcher.add_handler(nsfwMobileWallpaper_handler)

        # self.dispatcher.add_handler(dinamico_handler)

        self.updater.start_polling()

    '''
        IMPLEMENTAÇÃO DE COMANDOS
    '''

    def start(self, update, context):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Bem vindo ao AniheartBot, em que posso ser útil hoje?\n")

    def neko(self, update, context):
        img = hmtai.useHM(version="v2", category="neko")
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img)

    def wallpaper(self, update, context):
        img = hmtai.useHM(version="v2", category="wallpaper")
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img)

    def mobileWallpaper(self, update, context):
        img = hmtai.useHM(version="v2", category="mobileWallpaper")
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img)

    def ass(self, update, context):
        img = hmtai.useHM(version="v2", category="ass")
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img)

    def bdsm(self, update, context):
        img = hmtai.useHM(version="v2", category="bdsm")
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img)

    def cum(self, update, context):
        img = hmtai.useHM(version="v2", category="cum")
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img)

    def manga(self, update, context):
        img = hmtai.useHM(version="v2", category="manga")
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img)

    def femdom(self, update, context):
        img = hmtai.useHM(version="v2", category="femdom")
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img)

    def hentai(self, update, context):
        img = hmtai.useHM(version="v2", category="hentai")
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img)

    def masturbation(self, update, context):
        img = hmtai.useHM(version="v2", category="masturbation")
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img)

    def ero(self, update, context):
        img = hmtai.useHM(version="v2", category="ero")
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img)

    def orgy(self, update, context):
        img = hmtai.useHM(version="v2", category="orgy")
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img)

    def yuri(self, update, context):
        img = hmtai.useHM(version="v2", category="yuri")
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img)

    def glasses(self, update, context):
        img = hmtai.useHM(version="v2", category="glasses")
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img)

    def cuckold(self, update, context):
        img = hmtai.useHM(version="v2", category="cuckold")
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img)

    def blowjob(self, update, context):
        img = hmtai.useHM(version="v2", category="blowjob")
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img)

    def foot(self, update, context):
        img = hmtai.useHM(version="v2", category="foot")
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img)

    def thighs(self, update, context):
        img = hmtai.useHM(version="v2", category="thighs")
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img)

    def ahegao(self, update, context):
        img = hmtai.useHM(version="v2", category="ahegao")
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img)

    def uniform(self, update, context):
        img = hmtai.useHM(version="v2", category="uniform")
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img)

    def gangbang(self, update, context):
        img = hmtai.useHM(version="v2", category="gangbang")
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img)

    def tentacles(self, update, context):
        img = hmtai.useHM(version="v2", category="tentacles")
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img)

    def nsfwNeko(self, update, context):
        img = hmtai.useHM(version="v2", category="nsfwNeko")
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img)

    def nsfwMobileWallpaper(self, update, context):
        img = hmtai.useHM(version="v2", category="nsfwMobileWallpaper")
        context.bot.send_photo(chat_id=update.effective_chat.id, photo=img)


    # def dinamico(self, update, context):
    ##    print('Chamada de função de dinâmica')
    # pega somente a primeira palavra apos o comando
    ##    categoria = context.args[0]
    ##    print('Categoria: ' + categoria)
    ##    img = hmtai.useHM(version="v2", category="" + categoria)
    ##    context.bot.send_photo(chat_id=update.effective_chat.id, photo=img)
bot = HentaiImage()
bot.run()
