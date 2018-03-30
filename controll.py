#!/usr/bin/env python

from wardrobe import Wardrobe

wd = Wardrobe()

wd.setClothes("西裝褲", 144)
wd.setClothes("短褲", 144)
wd.setClothes("短褲", 72)
wd.setClothes("長褲", 0)
wd.setClothes("球褲", 288)
wd.setClothes("雨褲", 216)

wd.setClothes("西裝上衣", 216)
wd.setClothes("球衣", 216)
wd.setClothes("球衣", 144)
wd.setClothes("厚外套", 0)

print("")
print("*** 1 ***")
print(wd.ClothesPos[0])
print(wd.ClothesPos[1])
print("Wardrode origin is now at degree", wd.degree)
print("")

print('what clothes do you want to set? "雨衣"')
wd.addClothes("雨衣")
print("*** 2 ***")
print(wd.ClothesPos[0])
print(wd.ClothesPos[1])
print("Wardrode origin is now at degree", wd.degree)
print("")

print('what clothes do you want to set? "雨衣"')
wd.addClothes("帽梯")
print("*** 3 ***")
print(wd.ClothesPos[0])
print(wd.ClothesPos[1])
print("Wardrode origin is now at degree", wd.degree)
print("")

print('what clothes do you want to set? "雨衣"')
wd.addClothes("雨衣")
print("*** 4 ***")
print(wd.ClothesPos[0])
print(wd.ClothesPos[1])
print("Wardrode origin is now at degree", wd.degree)
print("")

print('what features of the clothes you want to have? [18, "sunny"]')
fit = wd.chooseClothes([18, "sunny", ""])
print(fit)
print("")

print('what features of the clothes you want to have? [18, "sunny"]')
fit = wd.chooseClothes([45, "sunny", ""])
print(fit)
print("")
