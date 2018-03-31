import os 
import sys
from drive import RemoteManager
import time
assert sys and os




###################################################
#            query                                #
###################################################
rm=RemoteManager()

while True:
    if rm.listen()==True:
        time.sleep(5)
        print('downloading')
        rm.get('score','score.txt')
        with open('score.txt','r') as f:
            for i in f:
                print(f.read())
