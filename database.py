#!/usr/bin/env python

ixClothes = ["西裝上衣", "球衣", "厚外套", "帽T", "雨衣"]
dbClothes = {
    "西裝上衣": [[5, 35], "sunny", {"formal"}, {"西裝褲"}],
    "球衣": [[23, 35], "sunny", {"sport", "easy"}, {"球褲", "短褲", "長褲"}],
    "厚外套": [[5, 18], "sunny", {"easy"}, {"長褲"}],
    "帽T": [[7, 22], "sunny", {"easy"}, {"球褲", "短褲", "長褲"}],
    "雨衣": [[5, 35], "rainy", {"easy"}, {"雨褲"}]
}

ixPants = ["西裝褲", "球褲", "短褲", "長褲", "雨褲"]
dbPants = {
    "西裝褲": [[5, 35], "sunny", {"formal"}],
    "球褲": [[23, 35], "sunny", {"sport", "easy"}],
    "短褲": [[18, 35], "sunny", {"sport", "easy"}],
    "長褲": [[5, 22], "sunny", {"easy"}],
    "雨褲": [[5, 35], "rainy", {"easy"}]
}
