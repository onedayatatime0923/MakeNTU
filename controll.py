#!/usr/bin/env python

from wardrobe import Wardrobe
import os 
import sys
from drive import RemoteManager
import time
assert sys and os


wd = Wardrobe()
rm = RemoteManager()

wd.addClothes("球褲")
wd.addClothes("短褲")
wd.addClothes("長褲")
wd.addClothes("球褲")
wd.addClothes("短褲")
wd.addClothes("長褲")
wd.addClothes("球褲")

wd.addClothes("西裝外套")
wd.addClothes("球衣")
wd.addClothes("短襯衫")
wd.addClothes("大衣圍巾")
wd.addClothes("吊嘎")
wd.addClothes("外套")

print(wd.ClothesPos[0])
print(wd.ClothesPos[1])

while True:
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
            rm.put('image_train/data/train/'+feature[i][0],'s{}.JPG'.format(i))
            rm.put('image_train/data/train/'+feature[i][1],'p{}.JPG'.format(i))
        while len(feature)>0:
            index = rm.listen("index")
            if index > 0:
                wd.takeClothes(feature[index-1])
                break
