from __future__ import unicode_literals
from bs4 import BeautifulSoup
import urllib2
import youtube_dl

count = 0
link1 = 0
link2 = 0
link3 = 0
run = 0

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

soup = BeautifulSoup(content, "html.parser")

for link in soup.find_all('a'):
    a = link.get('href')
    b = a[:6]
    
    if (b == "/watch") & (count == 0):
        print count
        count += 1
        print count
        link1 = link.get('href')
        print " "
        #print "First link: http://youtube.com" + link1
        page1 = "http://youtube.com/" + link1

        if (link1 == link2):
            print "you"
            count == 0
        

    if (b == "/watch") & (count == 1):
        print count
        count += 1
        print count
        link2 = link.get('href')
        
        print "First link: http://youtube.com" + link2
        page2 = "http://youtube.com/" + link2

        if (link1 == link2):
            print "you"
            count == 0

    if (b == "/watch") & (count == 2):
        print count
        count += 1
        link3 = link.get('href')
        print "Second link: http://youtube.com" + link3
        page3 = "http://youtube.com/" + link3
        if (link2 == link3):
            count = 1

        if (link1 == link3):
            count = 0

    if (b == "/watch") & (count == 3):
        print count
        link4 = link.get('href')
        print "Third link: http://youtube.com" + link4
        page4 = "http://youtube.com/" + link4
        if (link3 == link4):
            count = 2

        if (link2 == link4):
            count = 1

        print " "
        while (run == 0):
            ask = raw_input("Which link would you like to download(1/2/3)?: ")
            if (ask == "1"):
                run = 1
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([page2])
                    print "Done!"
                    break


            elif (ask == "2"):
                run = 1
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([page3])
                    print "Done!"
                    break

            elif (ask == "3"):
                run = 1
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([page4])
                    print "Done!"
                    break

            else:
                run = 0
                print "Please enter either 1, 2 or 3!"


