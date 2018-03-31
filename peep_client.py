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
        time.sleep(10)
        print('downloading')
        rm.get('score','score.txt')
        print("kdfj")
        with open('score.txt','rb') as f:
            print("kdfj")
            for i in f:
                print(f.read())
