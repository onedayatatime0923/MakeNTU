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
        time.sleep(20)
        print('downloading')
        with open('score.txt','rb') as f:
            for i in f:
                print(f.read())
