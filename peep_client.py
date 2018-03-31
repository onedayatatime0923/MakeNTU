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
    if rm.listen("Recorded")==True:
        time.sleep(11)
        print('downloading')
        score=[]
        with open('score.txt','rb') as f:
            for s in f.readlines():
                print(s)
                s=str(s)[2:-3].strip('\n').split(',')
                score.append((s[0],float(s[1])))
        print(score)
                
                
                
        #calculating feature
                
        feature=0
        for i in range(1,len(feature)+1)
            rm.put(feature[i][0],'s{}.JPG'.format(i))
            rm.put(feature[i][1],'p{}.JPG'.format(i))
        while  True:
            index=rm.listen("Index")
            if index>0:
                #meaning choose the index
                break



