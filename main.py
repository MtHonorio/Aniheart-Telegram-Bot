import telegram
from telegram.ext import Updater, CommandHandler, Dispatcher, Filters, MessageHandler
import logging
import token_code
import nsfw

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# adicione seu token em um .env
TOKEN = token_code.token

updater = Updater(token=TOKEN, use_context=True)

dispatcher = updater.dispatcher

help_message = '/start - Mensagem de boas vindas\n'
help_message += '/neko - Envia uma neko girl\n'
help_message += '/wallpaper - Envia um papel de parede para Desktop\n'
help_message += '/mobileWallpaper - Envia um papel de parede para Celular\n'
help_message += '/nsfw - Envia uma lista de comandos bem diferentes\n'
help_message += '/collaborate - Envia o github do projeto\n'
help_message += 'Mais funcionalidades em breve...'

collaborate_message = 'Github do projeto: https://github.com/MtHonorio/Aniheart-Telegram-Bot\n'

nsfw_message = '/ass - Eu sei que você gosta de bundas de animes!!\n'
nsfw_message += '/bdsm - Bondage e disciplina, dominação e submissão, sadomasoquismo, etc...\n'
nsfw_message += '/cum - Literalmente porra, pf não peça para eu explicar, só bate tua punheta queto ai!! \n'
nsfw_message += '/manga - Uma página de mangá aleatória\n'
nsfw_message += '/femdom - Dominação feminina\n'
nsfw_message += '/hentai - Envia uma imagem hentai aleatória\n'
nsfw_message += '/masturbation - Exatamente o que você está procurando fazer agora...\n'
nsfw_message += '/ero - Coisas eróticas, uniformes eróticos, etc...\n'
nsfw_message += '/orgy - Momento bom...\n'
nsfw_message += '/yuri - Mulheres se pegando e não é na porrada...\n'
nsfw_message += '/glasses - Mulheres gatas de óculos...\n'
nsfw_message += '/cuckold - Comedor de casadas, não vou nem questionar seus fetiches.\n'
nsfw_message += '/blowjob - Garota cantando no microfone.\n'
nsfw_message += '/foot - Pack do pézinho você encontra aqui, literalmente...\n'
nsfw_message += '/thighs - Coxas carnudas, melhor dos melhores, tipo uma religião...\n'
nsfw_message += '/ahegao - Garotas fazendo caras e bocas\n'
nsfw_message += '/uniform - Uniformes escolares entre outros\n'
nsfw_message += '/gangbang - 5 contra 1, injusto demais na gameplay\n'
nsfw_message += '/tentacles - Me desculpe, mas por que você gosta disso?\n'
nsfw_message += '/nsfwNeko - Mulheres gato, o batman chora.\n'
nsfw_message += '/nsfwMobileWallpaper - Uma coisa bem diferenciada para seu papel de parede!\n'


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Bem vindo ao AniheartBot, em que posso ser útil hoje?\n")


def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=help_message)


def nsfw(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=nsfw_message)


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

# nsfw.HentaiImg.run()
