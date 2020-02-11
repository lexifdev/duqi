import random
from machine.plugins.base import MachineBasePlugin
from machine.plugins.decorators import listen_to


class CryPlugin(MachineBasePlugin):
    @listen_to(regex=r'(?P<tears>(ㅠ|ㅜ|ㅡ){2,99})')
    def cry(self, msg, tears):
        if len(tears) > 2:
            candidates = [
                'ㅡㅠㅠㅡㅡ으ㅜㅠㅠ',
                'ㅡㅠㅠㅡㅜㅠ',
            ]
        else:
            candidates = [
                'ㅠㅜ',
                'ㅠㅠ',
            ]

        response = random.choice(candidates)
        msg.say(response, as_user=True)
