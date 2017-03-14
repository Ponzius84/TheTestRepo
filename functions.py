from random import randint, choice
from richieste_imbruttite import generate_request
from  chat_information import ChatInfo

class Parser(object):

    chats = {}


    def rispostaTesto(self, bot, update):

        if update.message.chat_id not in self.chats:
            self.chats[update.message.chat_id] = ChatInfo()
            print(update.message.chat_id)

        testo = update.message.text.lower()
        print(update.message)
        [f(testo, update) for f in [self.milanese,
                                    self.luxuria,
                                    self.domanda,
                                    self.melina,
                                    self.saluto,
                                    self.invidia,
                                    self.richiesta_imbruttita]]


    def rispostaFoto(self, bot, update):

        if update.message.chat_id not in self.chats:
            self.chats[update.message.chat_id] = ChatInfo()
            print(update.message.chat_id)

        print(update.message)
        n = randint(0, 9)
        print(n)
        if (n == 0):
            update.message.reply_text('Ue Avete finito o no, di postare foto come checche isteriche?', quote=False)

    # -----------------------------------------------------------------------------------------------------------------------

    def milanese(self, testo, update):
        if "milanese" in testo:
            update.message.reply_text('{}, Va a ciapà i ratt'.format(update.message.from_user.first_name),
                                      quote=False)

    def luxuria(self, testo, update):
        if 'luxuria' in testo:
            update.message.reply_photo(photo=open('images/vlad_{}.jpg'.format(randint(1, 6)), 'rb'),
                                       quote=False)

            # update.message.reply_photo(photo="AgADAgAD-6cxG_ULMEo-AsCQeTsfrgk5Sw0ABKN_M80VTkK4Zx8GAAEC",quote=False)

    def domanda(self, testo, update):
        risposte = ['ce la puoi fare',
                    'figa se asciughi',
                    'figa mollami']

        if "?" in testo:
            update.message.reply_text('{}, {}'.format(update.message.from_user.first_name, choice(risposte)),
                                      quote=False)

    def melina(self, testo, update):
        usare_personalizzate = (randint(1, 2) == 1)

        risposte_personalizzate = {'yle': ['Yle, ti bastano un kg di pucce di Rodolfo?'],
                                   'misia': ['Misia, anche se donna basta che me la porti'],
                                   'alessia': ['Alessia, vieni che ti tiro quel pelo lungo sul braccio',
                                               'Allessia mia!']}

        risposte_generiche = ['Si lavora e si fatica per la panza e per la fica',
                              'lampu!',
                              'lampu cu li furmina!',
                              "Quest' inverno mi sono morte due galline di freddo. Sono andata per prendere le uova e le ho trovate stecchite"]

        if "melina" in testo:
            if (usare_personalizzate and any(nome in update.message.from_user.first_name.lower() for nome in
                                             ['yle', 'alessia', 'misia'])):
                update.message.reply_text(
                    '{}'.format(choice(risposte_personalizzate[update.message.from_user.first_name.lower()])),
                    quote=False)
            else:
                update.message.reply_text('{}'.format(choice(risposte_generiche)), quote=False)

    def invidia(self, testo, update):
        triggers = ['invidia',
                    'invidios']

        risposte = ["A cinca sta malanga, l' anni cu se chianga",
                    'Pisaturi in culo, suttu nu fucalire chino de ragnatile']
        if any(s in testo for s in triggers):
            update.message.reply_text('{}'.format(choice(risposte)), quote=False)

    def saluto(self, testo, update):
        saluti = ['ciao',
                  'buongiorno',
                  'buon giorno',
                  'salve']

        risposte = ['we figa', 'we alura?']
        if any(s in testo for s in saluti):
            update.message.reply_text('{}'.format(choice(risposte)), quote=False)

    def richiesta_imbruttita(self, testo, update):
        chat = self.chats[update.message.chat_id]
        if (chat.richiesta_imbruttita_in_atto):
            if (update.message.from_user.first_name in chat.richiesta_imbruttita.malcapitato):
                chat.richiesta_imbruttita.process_next_step(chat, testo, update)

        elif (randint(1, 30) == 1) and (chat.richiesta_imbruttita_in_atto == False):
            print("generazione nuova richiesta imbruttita")
            chat.richiesta_imbruttita = generate_request(update.message.from_user.first_name)
            chat.richiesta_imbruttita_in_atto = True
            chat.richiesta_imbruttita.process_next_step(chat, testo, update)