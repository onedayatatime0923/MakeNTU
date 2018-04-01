#!/usr/bin/env python

from wardrobe import Wardrobe
import os 
import sys
from drive import RemoteManager
import time
assert sys and os
from autocam import *


wd = Wardrobe()
rm = RemoteManager()

Id = wd.askId()
wd.setClothes("球褲", 300, Id)
Id = wd.askId()
wd.setClothes("短褲", 60, Id)
Id = wd.askId()
wd.setClothes("長褲", 180, Id)

Id = wd.askId()
wd.setClothes("西裝外套", 240, Id)
Id = wd.askId()
wd.setClothes("短襯衫", 300, Id)
Id = wd.askId()
wd.setClothes("大衣圍巾", 120, Id)
Id = wd.askId()
wd.setClothes("外套", 60, Id)

print(wd.ClothesPos[0])
print(wd.ClothesPos[1])

while True:
    
    if checkClothes():
        Id = wd.askId()
        takePhoto(Id)
        addClothes(Id)
        
        
    if rm.listen("Recorded") == True:
        time.sleep(11)
        print('downloading')
        score = []
        with open('score.txt','rb') as f:
            for s in f.readlines():
                print(s)
                s=str(s)[2:-3].strip('\n').split(',')
                score.append((s[0],float(s[1])))
        print(score)

        feature = wd.chooseClothes(score)
        print(feature)
        for i in range(1,len(feature)+1):
            rm.put('data/test/'+str(feature[i][0])+'.jpg','s{}.JPG'.format(i))
            rm.put('data/test/'+str(feature[i][1])+'.jpg','p{}.JPG'.format(i))
        while True:
            index = rm.listen("Index")
            if index > 0:
                wd.takeClothes(feature[index-1])
                break
