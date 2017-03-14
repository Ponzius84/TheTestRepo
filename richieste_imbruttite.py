from random import choice
class Richiesta(object):
    domanda = ""
    risposta_affermativa = ""
    risposta_negativa = ""
    poke = ""
    reset = ''
    iteration = 0
    malcapitato = ""


    def __init__(self, malcapitato, dmd, si, no, poke, reset):
        self.domanda = dmd
        self.risposta_affermativa = si
        self.risposta_negativa = no
        self.poke = poke
        self.reset = reset
        self.malcapitato = malcapitato

    def process_next_step(self, chat_info, testo, update):
        print(testo)
        if self.iteration == 0:
            update.message.reply_text(self.domanda, quote=False)

        elif (self.iteration<=2) and (any(scelta in testo for scelta in ['si','no'])):
            if testo == "no":
                update.message.reply_text(self.risposta_negativa, quote=False)
                chat_info.richiesta_imbruttita_in_atto = False
            elif testo == "si":
                update.message.reply_text(self.risposta_affermativa, quote=False)
                chat_info.richiesta_imbruttita_in_atto = False
        elif self.iteration == 1:
            update.message.reply_text(self.poke, quote=False)
        elif self.iteration == 2:
            update.message.reply_text(self.reset, quote=False)
            chat_info.richiesta_imbruttita_in_atto = False

        self.iteration += 1


def generate_request(name):
    return choice([Richiesta(   name,
                                "{}. me lo fai un bel chinotto?".format(name),
                                "Non riesco a capire se sentirmi onorato o schifato",
                                "Oh! OHHHH!! Ma cosa no!?",
                                "So che per un pirla come te sia difficile da capire, ma voglio solamente un 'si' od un 'no'. Allora questo chinotto?",
                                "Va bhè {}, fatti una bella nuotata nel naviglio e vedi di non riemergere".format(name))
                    ])