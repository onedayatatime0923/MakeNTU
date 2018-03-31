#!/usr/bin/env python

import pandas as pd
import numpy as np
from database import *
from speak import speak


class Wardrobe:
    def __init__(self):
        self.degree = [0, 0]
        self.ClothesInfo = [pd.DataFrame(dbClothes).set_index([featureTitle[0]]).transpose(),  
                            pd.DataFrame(dbPants).set_index([featureTitle[1]]).transpose()]
        self.ClothesPos = [{0: [None, 0], 60: [None, 0], 120: [None, 0], 180: [None, 0], 240: [None, 0], 300: [None, 0]},
                           {0: [None, 0], 60: [None, 0], 120: [None, 0], 180: [None, 0], 240: [None, 0], 300: [None, 0]}]
        self.id = 0
        
    def addClothes(self, clothes):
        kind = self.clothesOpants(clothes)
        degree = self.findSpace(kind)
        if degree == -1:
            print("Wardrobe of", kind, "is full. Add fail")
        else:
            self.moveto(kind, degree)
            self.ClothesPos[kind][degree][0] = clothes
            self.ClothesPos[kind][degree][1] = self.id
            self.id += 1
            print("New clothes", clothes, "is added successfully at degree", degree)
            speak("這是件"+clothes+"，適合穿於"+self.ClothesInfo[kind].get_value(clothes, "Intro"))
        
    def findSpace(self, kind):
        canditate = [degree, (degree+60)%360, (degree+300)%360, (degree+120)%360, (degree+240)%360, (degree+180)%360]
        for i in range(6):
            if self.ClothesPos[kind][canditate[i]][0] == None:
                return canditate[i]
        return degree

    def moveto(self, kind, goal):
        print("Wardrobe of", kind, "has rotated from", self.degree[kind], " degree to", goal, "degree")
        self.degree[kind] = goal

    def clothesOpants(self, clothes):
        if clothes in self.ClothesInfo[0].index.values: return 0
        else: return 1

    def chooseClothes(self, featureList):
        feature = []
        for i in range(3):
            if featureList[i][1] > 0.5:
                feature.append(featureList[i][0])
            else:
                break
                               
        clothesList = list(self.ClothesPos[0].values())
        clothesList = list(set(list(filter(lambda a: a != None, clothesList))))
        pantsList = list(self.ClothesPos[1].values())
        pantsList = list(set(list(filter(lambda a: a != None, pantsList))))

        clothesDict = {}
        pantsDict = {}
        for i in range(len(clothesList)):
            clothesDict.update({clothesList[i], self.decideSuitable(clothesList[i], 0, feature)})
        for i in range(len(pantsList)):
            pantListDict.update({pantsList[i], self.decideSuitable(pantsList[i], 1, feature)})
        if len(clothesDict) is 0:
            print("This wardrobe can not fit you, sorry")
            
        clothesData = (self.ClothesInfo[0].ix[clothesList])["Clothing"]
        for i in range(clothesData.size):
            for j in range(len(clothesData[i])):
                if not (pantsDict(clothesData[i][j])):
                    clothesData[i][j] = ""
            clothesData[i] = list(filter(lambda a: a != "", clothesData[i]))
        return clothesData

    def decideSuitable(self, clothes, kind, ft):
        cft = (self.ClothesInfo[kind].loc[clothes])[1]
        for i in range(len(ft)):
            if ft(i) not in cft:
                return False
        return True
            

'''
wd = Wardrobe()
'''
