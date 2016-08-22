# Youtube Downloader
![alt tag](http://root32.comlu.com/images/youdownload.jpg)

Version 1.2(Latest)

A easy to use python script that downloads youtube videos in whatever format they were uploaded in. Just type in what you want to search and it will download the first video link into the folder which the script is in.

This is my first project on github and I'm not thaaat experienced with python(and I'm 12) so any help or suggestions would be appreciated.

You can send suggestions to rootorg1@gmail.com

##How to use:

1. Make sure you have all the requirements
2. Download .py file(latest version)
3. Run .py file
4. Input the name of the video you want to download from youtube
5. Press enter and after a short while, your video will be downloaded into the folder with the python file.
6. The file type may be weird(mkd,webm) and W.M.P. cant play most of them so I recommend VLC media player.

##Requirements:
1. VLC media player(or any media player that can play any type of video file) ![alt tag](http://getpcsoft.wikisend.com/img_howto/0/309/vlc%20media%20player.jpg)
2. Python 2.7 + Libraries


##Python Libs(extra installation required):
1. youtube-dl
2. beautiful soup 4

#How to install beautiful soup 4:

###Windows:
Open cmd.exe
Go to C:/Python27/Scripts
run "pip install beautifulsoup4"

Debian based linux:

Available as python-beautifulsoup4 package in debian repositories
Just run "sudo apt-get install python-beautifulsoup4" in terminal

#How to install youtube-dl:

Windows:
Open cmd.exe
Go to C:/Python27/Scripts
run "pip install --upgrade youtube-dl"

Linux:

run "sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl"

run "sudo chmod a+rx /usr/local/bin/youtube-dl"

#Changes planned:

Priority 1:Options for first, second or third link.
Priority 2:Impliment simple GUI
Priority 3:Add option to download as selected formats
