#!/usr/bin/env python
from translate  import Tag , Volcabulary

formal=Tag('formal',['婚禮','典禮','正式','嚴肅'])
casual=Tag('casual',['休閒','一般','普通','舒適','舒服'])
sport=Tag('sport',['打球','運動','流汗','減肥','健身','球場','球隊','散步'])
goodlooking=Tag('goodlooking',['好看','流行'])
korean=Tag('korean',['韓系','韓流','歐爸','大衣'])
warm=Tag('warm',['悶','熱','炎熱','太陽','不冷'])
cool=Tag('cool',['風','涼爽','清新','不熱'])
cold=Tag('cold',['寒流','寒','冷','凍'])


featureTitle = [["TempRange", "Sun_Rain", "Occasion", "Clothing", "Intro"],
                ["TempRange", "Sun_Rain", "Occasion", "Intro"]]

ixClothes = ["西裝上衣", "球衣", "厚外套", "帽梯", "雨衣"]
dbClothes = {
    "西裝上衣": [[5, 35], "sunny", [formal], ["西裝褲"], "正式場合"],
    "球衣": [[23, 35], "sunny", [sport, casual], ["球褲", "短褲", "長褲"], "球場"],
    "短襯衫": [[23, 35], "sunny", [ casual,goodlooking], ["球褲", "短褲", "長褲"], "球場"],
    "大衣圍巾": [[7, 22], "sunny", [korean, warm], ["球褲", "短褲", "長褲"], "輕鬆卻不失打扮的場合"],
    "吊嘎": [[5, 35], "rainy", [warm], ["雨褲"], "雨天"],
    "外套": [[5, 18], "sunny", [goodlooking, casual], ["長褲"], "偏冷的天氣"],
}

ixPants = ["西裝褲", "球褲", "短褲", "長褲", "雨褲"]
dbPants = {
    "西裝褲": [[5, 35], "sunny", ["formal"], "正式場合"],
    "球褲": [[23, 35], "sunny", ["sport", "easy"], "球場"],
    "短褲": [[18, 35], "sunny", ["goodlooking", "easy"], "輕鬆卻不失打扮的場合"],
    "長褲": [[5, 22], "sunny", ["easy"], "偏冷的天氣"],
    "雨褲": [[5, 35], "rainy", ["goodlooking", "easy"], "雨天"]
}


###################################################
#            query                                #
###################################################
vol= Volcabulary('./data/word2vec/zh.bin')
vol.add_tag(formal)
vol.add_tag(casual)
vol.add_tag(sport)
vol.add_tag(goodlooking)
vol.add_tag(korean)
vol.add_tag(warm)
vol.add_tag(cool)
vol.add_tag(cold)

statement='今天不熱'
print(statement,vol.query(statement))
statement='我今天要去找女友'
print(statement,vol.query(statement))
statement='今天我爸結婚'
print(statement,vol.query(statement))
statement='今天好悶，可是我想去約會'
print(statement,vol.query(statement))
statement='我今天他媽想出去玩，可是他媽好熱'
print(statement,vol.query(statement))
statement='幹，給我一套衣服'
print(statement,vol.query(statement))
statement='今天我想去打球，可是怎麼這麼冷'
print(statement,vol.query(statement))
