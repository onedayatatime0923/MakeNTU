import os 
import sys
from translate  import Tag , Volcabulary
from database import formal,casual,sport,goodlooking,korean,warm,cool,cold
from drive import RemoteManager
import time
import numpy as np
assert Tag and sys




###################################################
#            query                                #
###################################################
vol= Volcabulary('./data/word2vec/zh.bin')
vol.add_tag(formal)
vol.add_tag(casual)
vol.add_tag(sport)
vol.add_tag(goodlooking)
vol.add_tag(korean)
vol.add_tag(warm)
vol.add_tag(cool)
vol.add_tag(cold)
rm=RemoteManager()

while True:
    if rm.listen()==True:
        time.sleep(2.5)
        print('downloading')
        rm.get('recording1.3gp','./data/record/record.3gp')
        os.system('cd ./data/record/ && ffmpeg -loglevel panic -y -i record.3gp -crf 18 record.wav' )
        with os.popen('python2 speech_to_text.py ./data/record/record.wav') as pse:
            for s in pse:
                statement=s
        np.save('score.npy',np.array(vol.query(statement)))
        rm.put('./score.npy','/')
        rm.ls()
