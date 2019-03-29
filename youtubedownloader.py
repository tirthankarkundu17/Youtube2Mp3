from __future__ import unicode_literals
import youtube_dl
import os

def download(location,downloadList):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': location+'/%(title)s-%(id)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '128',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(downloadList)

def setup():
    #Create a folder called downloads if it doesn't exist
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    #Create empty List of songs
    songList = []

    #Add youtube link of all the songs you wish to download
    songList.append('https://www.youtube.com/watch?v=JePnQ1gSagc')
    songList.append('https://www.youtube.com/watch?v=yU0tnrEk8H4')

    #You can also add like
    #songList =['link1','link2']

    #Start Downloading
    download("downloads",songList)

if __name__ == "__main__":
    setup()