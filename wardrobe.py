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
        self.ClothesPos = [{0: None, 72: None, 144: None, 216: None, 288: None},
                        {0: None, 72: None, 144: None, 216: None, 288: None}]

    def setClothes(self, clothes, degree):
        kind = self.clothesOpants(clothes)
        if self.ClothesPos[kind][degree] == None:
            self.ClothesPos[kind][degree] = clothes
            print("New clothes", clothes, "is added successfully at degree", degree)
            #speak("這是件"+clothes+"，適合穿於"+self.ClothesInfo[kind].get_value(clothes, "Intro"))
            return True
        else:
            print("This position is occupied by another clothes")
            return False

    def addClothes(self, clothes):
        kind = self.clothesOpants(clothes)
        degree = self.findSpace(kind)
        if degree == -1:
            print("Wardrobe of", kind, "is full. Add fail")
        else:
            result = self.setClothes(clothes, degree)
            if result: self.moveto(kind, degree)
        
    def findSpace(self, kind):
        degree = self.degree[kind]
        canditate = [degree, (degree+72)%360, (degree+144)%360, (degree+216)%360, (degree+288)%360]
        if   self.ClothesPos[kind][canditate[0]] == None: pass
        elif self.ClothesPos[kind][canditate[1]] == None: degree = canditate[1]
        elif self.ClothesPos[kind][canditate[2]] == None: degree = canditate[2]
        elif self.ClothesPos[kind][canditate[3]] == None: degree = canditate[3]
        elif self.ClothesPos[kind][canditate[4]] == None: degree = canditate[4]
        else: degree = -1
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
