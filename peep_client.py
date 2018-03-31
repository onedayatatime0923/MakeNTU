import os 
import sys
from translate  import Tag , Volcabulary
from database import formal,casual,sport,goodlooking,korean,warm,cool,cold
from drive import RemoteManager
import time
assert Tag and sys and os




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
        time.sleep(5)
        print('downloading')
        rm.get('score','score.txt')
        with open('score.txt','r') as f:
            for i in f:
                print(f.read())
