"""A greeting for you in the morning"""
__author__ = "Parker Ostertag"
_date__ = "1 December 2017"

import urllib.request
import urllib.parse
import re
from gtts import gTTS
from pygame import mixer

def main():
    url = 'https://www.willyweather.com/mn/clay-county/moorhead.html'
    values = {}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    req = urllib.request.Request(url, data)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    paragraphs = re.findall(r'<p>(.*?)</p>', str(respData))
    weather = (paragraphs[0])

    greeting = (f"Good morning Parker. The weather today will be {weather}")
    tts = gTTS(text = greeting, lang = 'en')
    tts.save("D:/python/test.mp3")
#play music alarm time
    mixer.init()
    mixer.music.load('D:/python/test.mp3')
    mixer.music.play()

main()
