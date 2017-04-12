# -*- coding: utf-8 -*-
#
# This file is part of Zoe Assistant
# Licensed under MIT license - see LICENSE file
#

from zoe import *

@Agent('Insult')
class InsultAgent:

    @Intent('intent.answer')
    def answer(self, intent):
        dest = intent['recipient']['email']
        # send email...
        return {
            'data': 'notification',
            'from': 'email',
            'text': 'message sent'
        }
