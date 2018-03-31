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

    def chooseClothes(self, feature = []):
        #1 collect all clothes in the wardrobe (in the clothesData series)
        clothesList = list(self.ClothesPos[0].values())
        clothesList = list(filter(lambda a: a != None, clothesList))
        pantsList = list(self.ClothesPos[1].values())
        pantsList = list(filter(lambda a: a != None, pantsList))
        clothesData = (self.ClothesInfo[0].ix[clothesList])["Clothing"]
        #2 kick out the clothes which are not suitable according to feature
        keep = []
        for i in range(clothesData.size):
            clothes = clothesData.index.values[i]
            if self.decideSuitable(clothes, 0, feature):
                keep.append(i)
        clothesData = clothesData.iloc[keep]
        if clothesData.size == 0:
            print("This wardrobe can not fit you, sorry")
            return
        
        #3 kick out the corresponding pants which are not suitable according to feature
        #PS should also check whether the pants are in the wardrobe or not
        for i in range(clothesData.size):
            for j in range(len(clothesData[i])):
                clothes = clothesData[i][j]
                if (clothes not in pantsList) or (not self.decideSuitable(clothes, 1, feature)):
                    clothesData[i][j] = ""
            clothesData[i] = list(filter(lambda a: a != "", clothesData[i]))
        return clothesData

    def decideSuitable(self, clothes, kind, ft):
        cft = self.ClothesInfo[kind].loc[clothes]
        if ft[1] != "" and ft[1] is not cft[1]: return False
        if ft[0] != "" and ft[0] not in range(cft[0][0], cft[0][1]+1): return False
        if ft[2] != "" and ft[2] not in cft[2]: return False
        return True     

'''
wd = Wardrobe()
'''
