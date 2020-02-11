import random
from machine.plugins.base import MachineBasePlugin
from machine.plugins.decorators import listen_to


class AgreePlugin(MachineBasePlugin):
    @listen_to(regex=r'어때요?|괜찮(.)요?')
    def agree(self, msg):
        candidates = [
            'ㅇㅇ',
            '조습니다',
            'ㅇㅇ 조습니다',
        ]

        response = random.choice(candidates)
        msg.say(response, as_user=True)
