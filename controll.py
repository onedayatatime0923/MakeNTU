#!/usr/bin/env python

from wardrobe import Wardrobe

wd = Wardrobe()

wd.addClothes("球褲")
wd.addClothes("短褲")
wd.addClothes("長褲")
wd.addClothes("球褲")
wd.addClothes("短褲")
wd.addClothes("長褲")
wd.addClothes("球褲")
print(wd.ClothesPos[0])
print(wd.ClothesPos[1])

wd.addClothes("西裝外套")
wd.addClothes("球衣")
wd.addClothes("短襯衫")
wd.addClothes("大一圍巾")
wd.addClothes("吊嘎")
wd.addClothes("外套")
print(wd.ClothesPos[0])
print(wd.ClothesPos[1])

print('what features of the clothes you want to have? [18, "sunny"]')
fit = wd.chooseClothes([18, "sunny", ""])
print(fit)
print("")

print('what features of the clothes you want to have? [45, "sunny"]')
fit = wd.chooseClothes([45, "sunny", ""])
print(fit)
print("")

print('what features of the clothes you want to have? [45, "sunny"]')
fit = wd.chooseClothes(["", "", "easy"])
print(fit)
print("")
