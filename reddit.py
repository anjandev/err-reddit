#    <err-reddit: Message with the name of a subreddit and bot returns a link from the hot page>
#    Copyright (C) <2018>  <Anjandev Momi> anjan@momi.ca
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


from errbot import BotPlugin, botcmd
import random
import json, requests

class Reddit(BotPlugin):
    """Reddit plugin for errbot"""

    @botcmd
    def subme(self, msg, args):
        """Usage: !subme <subreddit>"""

        if " " in args or len(args) == 0:
            return "Usage: !subme <subreddit>"

        url = "https://www.reddit.com/r/"
        for arg in args:
            if arg is " ":
                arg = "+"
            url += arg

        url += "/hot.json"

        response = requests.get(url, headers = {'User-agent': 'Chrome'})
        parsed = json.loads(response.text)

        try:
            if len(parsed['data']['children']) == 0:
                return "The subreddit {args} does not exist".format(args=args)
        except KeyError:
            return "The subreddit {args} does not exist".format(args=args)

        randomItem = random.choice(parsed['data']['children'])
        url = randomItem['data']['url']
        title = randomItem['data']['title']


        return "Title: \"{title}\" {url}".format(title=title, url=url)
