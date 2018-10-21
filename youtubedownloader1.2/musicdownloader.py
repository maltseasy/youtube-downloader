from __future__ import unicode_literals
from bs4 import BeautifulSoup
import urllib2
import os
import youtube_dl


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')


ydl_opts = {
    
}

search = raw_input("What do you want to search?: ")
search2 = search.replace(" ", "+")
url = "https://www.youtube.com/results?search_query=" + search2 + "&page=&utm_source=opensearch"

content = urllib2.urlopen(url).read()

soup = BeautifulSoup(content)

for link in soup.find_all('a'):
    a = link.get('href')
    b = a[:6]
    if (b == "/watch"):
        print " "
        print "First link: " + a
        page = "youtube.com/" + a
        command = "youtube-dl " + str(page)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([page])
        print "Done!"

        break

    print a
