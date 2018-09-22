from errbot import BotPlugin, botcmd
import random
import json, requests

class Reddit(BotPlugin):
    """Reddit plugin for errbot"""

    @botcmd
    def subme(self, msg, args):
        """Usage: !subme <subreddit>"""
        url = "https://www.reddit.com/r/"
        for arg in args:
            if arg is " ":
                arg = "+"
            url += arg

        url += "/top.json"

        response = requests.get(url, headers = {'User-agent': 'Chrome'})
        parsed = json.loads(response.text)

        i = random.randint(0, 25)
        url = parsed['data']['children'][i]['data']['url']
        title = parsed['data']['children'][i]['data']['title']


        return "Title: \"{title}\" {url}".format(title=title, url=url)
