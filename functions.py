from random import randint, choice

def milanese(testo, update):
    if "milanese" in testo:
        update.message.reply_text('{}, Va a ciapà i ratt'.format(update.message.from_user.first_name), quote=False)

def luxuria(testo, update):
    if 'luxuria' in testo:
        update.message.reply_photo(photo=open('images/vlad_{}.jpg'.format(randint(1, 6)), 'rb'), quote=False)
        # update.message.reply_photo(photo="AgADAgAD-6cxG_ULMEo-AsCQeTsfrgk5Sw0ABKN_M80VTkK4Zx8GAAEC",quote=False)

def domanda(testo, update):
    risposte = ['ce la puoi fare',
                'figa se asciughi',
                'figa mollami']

    if testo.find("?") != -1:
        update.message.reply_text('{}, {}'.format(update.message.from_user.first_name, choice(risposte)), quote=False)

def melina(testo, update):
    risposte = ['Si lavora e si fatica per la panza e per la fica',
		'lampu!',
		'lampu cu li furmina!']
    if testo.find("melina") != -1:
        update.message.reply_text('{}'.format(choice(risposte)), quote=False)

def invidia(testo, update):
    triggers = ['invidia',
              	'invidios']

    risposte = ["A cinca sta malanga, l' anni cu se chianga",
		'Pisaturi in culo, suttu nu fucalire chino de ragnatile']
    if any(s in testo for s in saluti):
        update.message.reply_text('{}'.format(choice(risposte)), quote=False)

def saluto(testo, update):
    saluti = ['ciao',
              'buongiorno',
              'buon giorno',
              'salve']

    risposte = ['we figa','we alura?']
    if any(s in testo for s in saluti):
        update.message.reply_text('{}'.format(choice(risposte)), quote=False)

#-----------------------------------------------------------------------------------------------------------------------

def rispostaTesto(bot, update):
    testo = update.message.text.lower()
    print(update.message)
    [f(testo, update) for f in [milanese,
                                luxuria,
                                domanda,
                                melina,
                                saluto,
				invidia]]



def rispostaFoto(bot, update):
    print(update.message)
    n = randint(0, 9)
    print(n)
    if (n == 0):
        update.message.reply_text('Ue Avete finito o no, di postare foto come checche isteriche?', quote=False)
