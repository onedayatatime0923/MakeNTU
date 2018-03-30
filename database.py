#!/usr/bin/env python

featureTitle = [["TempRange", "Sun_Rain", "Occasion", "Clothing", "Intro"],
                ["TempRange", "Sun_Rain", "Occasion", "Intro"]]

ixClothes = ["西裝上衣", "球衣", "厚外套", "帽梯", "雨衣"]
dbClothes = {
    "西裝上衣": [[5, 35], "sunny", ["formal"], ["西裝褲"], "正式場合"],
    "球衣": [[23, 35], "sunny", ["sport", "easy"], ["球褲", "短褲", "長褲"], "球場"],
    "厚外套": [[5, 18], "sunny", ["goodlooking", "easy"], ["長褲"], "偏冷的天氣"],
    "帽梯": [[7, 22], "sunny", ["goodlooking", "easy"], ["球褲", "短褲", "長褲"], "輕鬆卻不失打扮的場合"],
    "雨衣": [[5, 35], "rainy", ["goodlooking", "easy"], ["雨褲"], "雨天"]
}

ixPants = ["西裝褲", "球褲", "短褲", "長褲", "雨褲"]
dbPants = {
    "西裝褲": [[5, 35], "sunny", ["formal"], "正式場合"],
    "球褲": [[23, 35], "sunny", ["sport", "easy"], "球場"],
    "短褲": [[18, 35], "sunny", ["goodlooking", "easy"], "輕鬆卻不失打扮的場合"],
    "長褲": [[5, 22], "sunny", ["easy"], "偏冷的天氣"],
    "雨褲": [[5, 35], "rainy", ["goodlooking", "easy"], "雨天"]
}
