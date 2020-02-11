import random
from machine.plugins.base import MachineBasePlugin
from machine.plugins.decorators import listen_to


class LolPlugin(MachineBasePlugin):
    @listen_to(regex=r'(?P<ks>ㅋ{3})')
    def laugh(self, msg, ks):
        candidates = [
            'ㅋㅋㅋㅋ',
            '와 씨 ㅋㅋㅋ',
            '와 씨 졸라 웃겨 ㅋㅋㅋㅋ',
        ]

        response = random.choice(candidates)
        msg.say(response, as_user=True)
