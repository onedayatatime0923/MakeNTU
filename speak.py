#!/usr/bin/env python

import time
from gtts import gTTS
from pygame import mixer
import tempfile

def speak(sentence, lang='zh', wait = True, loops=1):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts=gTTS(text=sentence, lang=lang)
        tts.save('{}.mp3'.format(fp.name))
        mixer.init()
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.play(loops)
        if wait: time.sleep(7)

'''
speak('ありがとう', 'ja', False)
time.sleep(3)
speak('全國的軍民同胞們, 川普是笨蛋', 'zh', False)
time.sleep(10)
speak('Hello World!', 'en', False)
time.sleep(3)
'''
