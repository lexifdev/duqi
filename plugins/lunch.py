import random
from machine.plugins.base import MachineBasePlugin
from machine.plugins.decorators import listen_to, schedule


class LunchPlugin(MachineBasePlugin):
    @schedule(hour='12', minute='30')
    def ask(self):
        candidates = [
            '쿠차라?',
            '뱁 드실분?',
            '다담?',
            'ㄷㅏ담?',
        ]

        response = random.choice(candidates)
        self.say('hungry-밥먹을사람', response, as_user=True)
