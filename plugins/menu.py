import random
from machine.plugins.base import MachineBasePlugin
from machine.plugins.decorators import listen_to, schedule


class MenuPlugin(MachineBasePlugin):
    @listen_to(regex=r'뭐먹지?|뭐먹(.)요?')
    def suggest(self, msg):
        candidates = [
            '쿠차라?',
            '다담?',
            'ㄷㅏ담?',
        ]
        response = random.choice(candidates)
        msg.say(response, as_user=True)
