#!/usr/bin/env python

import pandas as pd
import numpy as np
from database import *


class Wardrobe:
    def __init__(self):
        self.degree = [0, 0]
        self.ClothesInfo = [pd.DataFrame(dbClothes, columns = ixClothes), 
                            pd.DataFrame(dbPants, columns = ixPants)]
        self.ClothesPos = [{0: None, 72: None, 144: None, 216: None, 288: None},
                        {0: None, 72: None, 144: None, 216: None, 288: None}]

    def setClothes(self, clothes, degree):
        kind = self.clothesOpants(clothes)
        if self.ClothesPos[kind][degree] == None:
            self.ClothesPos[kind][degree] = clothes
            print("New clothes", clothes, "is successfully added at degree", degree)
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
        if clothes in self.ClothesInfo[0]: return 0
        else: return 1

    def chooseClothes(self, feature = []):
        if (feature == []): feature = self.featureCollect()
        clothesList = np.asarray(self.ClothesPos[0].values())
        np.delete(clothesList, np.where(clothesList == None))
        if feature[1] is "sunny":
            pass
        elif feature[1] is "rainy":
            pass
        else:
            pass
            

    def choosePants(self):
        pass
        
    def featureCollect(self):
        temperature = input("Temperture (number): ")
        sunnyOrainy = input("sunny or rainy").lower
        occasion = input("Formal, Sport or Easy (string): ").lower
        return [temperature, sunny, occasion]
        
