#
# This file is part of Zoe Assistant
# Licensed under MIT license - see LICENSE file
#

from zoe import *
import random

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

    def getRandomInsult(self):
        ins = int(random.uniform(0, len(self.allInsults)))
        return self.allInsults[ins][0]

    #Intent contiene: frase a la que se responde y respuesta
    @Intent('insult.start')
    def start(self, intent):
        insult = self.getRandomInsult() 
        return {
            'data': 'insult',
            'from': 'insultAgent',
            'insult': insult
        }

    #Intent contiene: frase a la que se responde y respuesta
    @Intent('insult.answer')
    def answer(self, intent):
        insult = intent['insult']
        answer = intent['answer']
        for i in self.allInsults:
            if answer in i and insult in i:
                return {
                    'data': 'insult',
                    'from': 'insultAgent',
                    'text': 'D\'oh!'
                }
        return {
            'data': 'insult',
            'from': 'insultAgent',
            'text': 'No pueds conmigo!'
        }
