import os 
import sys
from translate  import Tag , Volcabulary
from database import formal,casual,sport,goodlooking,korean,warm,cool,cold
from drive import RemoteManager
import time
import numpy as np
assert Tag and sys and np and time




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
        time.sleep(1)
        print('downloading')
        rm.get('recording1.3gp','./data/record/record.3gp')
        os.system('cd ./data/record/ && ffmpeg -loglevel panic -y -i record.3gp -crf 18 record.wav' )
        with os.popen('python2 speech_to_text.py ./data/record/record.wav') as pse:
            for s in pse:
                statement=s
        print(statement)
        score=vol.query(statement)
        print(score)
        with open('score.txt','w') as f:
            for i in score:
                f.write('{},{}\n'.format(i[0].name,i[1]))
                print('{},{}'.format(i[0].name,i[1]))
        os.system('sshpass -p raspberry scp score.txt pi@10.1.30.178:MakeNTU')
