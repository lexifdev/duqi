import random
from machine.plugins.base import MachineBasePlugin
from machine.plugins.decorators import listen_to, schedule


class DinnerPlugin(MachineBasePlugin):
    @schedule(hour='19', day_of_week='1-6')
    def ask(self):
        candidates = [
            '뱁 드실분?',
            '다담?',
            'ㄷㅏ담?',
            'ㄷㅏ담한 저녁 드실 분?',
        ]

        response = random.choice(candidates)
        self.say('hungry-밥먹을사람', response, as_user=True)
