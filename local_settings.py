import os

SLACK_API_TOKEN = os.environ.get('SLACK_TOKEN')

PLUGINS = [
    'plugins.lol.LolPlugin',
    'plugins.cry.CryPlugin',
    'plugins.agree.AgreePlugin',
    'plugins.lunch.LunchPlugin',
    'plugins.dinner.DinnerPlugin',
    'plugins.menu.MenuPlugin',
]
