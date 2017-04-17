# -*- coding: utf-8 -*-
#
# This file is part of Zoe Assistant
# Licensed under MIT license - see LICENSE file
#

from zoe import *

@Agent('Insult')
class InsultAgent:

    allInsults = [["Espero que tengas un barco para una rápida huida.",
                    "¿Por qué? ¿Acaso querías pedir uno prestado?"],
                    ["Ya no hay técnicas que te puedan salvar.",
                    "Sí que las hay, sólo que nunca las has aprendido."],
                    ["Ahora entiendo lo que significan basura y estupidez.",
                    "Me alegra que asistieras a tu reunión familiar diaria."],
                    ["Mi lengua es más hábil que cualquier espada.",
                    "Primero deberías dejar de usarla como un plumero."],
                    ["¡Ordeñaré hasta la última gota de sangre de tu cuerpo!",
                    "Qué apropiado, tú peleas como una vaca."],
                    ["¡Eres como un dolor en la parte baja de la espalda!",""],
                    ["¡Mi pañuelo limpiará tu sangre!",
                    "Ah, ¿Ya has obtenido ese trabajo de barrendero?"],
                    ["Cada palabra que sale de tu boca es una estupidez.",
                    "Quería asegurarme de que estuvieras a gusto conmigo."],
                    ["Mi ultima pelea acabo con mis manos llenas de sangre.",
                    "Espero que ya hayas aprendido a no tocarte la nariz."]]

    #Intent contiene: frase a la que se responde y respuesta
    @Intent('insult.start')
    def start(self, intent):
        answer = input("¿Quieres enfrentarte a Zoe en duelo de insultos?\n Y/N\n")
        if answer == "Y":
            print(allInsults[0][0]+"\n"+"-"*10)
            generateAnswers()
        else:
            print("Gallina")

    def generateAnswer():
        #while True:
        #    cosas
        pass

    #Intent contiene: frase a la que se responde y respuesta
    @Intent('insult.answer')
    def answer(self, intent):
        dest = intent['recipient']['email']
        # send email...
        return {
            'data': 'notification',
            'from': 'email',
            'text': 'message sent'
        }
