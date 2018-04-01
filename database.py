import os 
import sys
assert os and sys

class Tag:
    def __init__(self,name,feature):
        self.feature=feature
        self.name=name
    def __str__(self):
        return "{}".format(self.feature)
    def __repr__(self):
        return "{}".format(self.name)

formal = Tag('formal',['婚禮','典禮','正式','嚴肅'])
casual = Tag('casual',['休閒','一般','普通','舒適','舒服'])
sport = Tag('sport',['打球','運動','流汗','減肥','健身','球場','球隊','散步'])
goodlooking = Tag('goodlooking',['約會','約','女朋友','好看','流行'])
korean = Tag('korean',['韓系','韓流','歐爸','大衣'])
warm = Tag('warm',['悶','熱','炎熱','太陽'])
cool = Tag('cool',['風','涼爽','清新'])
cold = Tag('cold',['寒流','寒','冷','凍'])

tagTitle = [formal, casual, sport, goodlooking, korean, warm, cool, cold]


featureTitle = [["TempRange", "Occasion", "Clothing", "Intro"],
                ["TempRange", "Occasion", "Intro"]]

ixClothes = ["西裝外套", "球衣", "短襯衫", "大衣圍巾", "吊嘎", "外套"]
dbClothes = {
    "西裝外套": [[5, 35], ['formal', 'warm', 'cool', 'cold'], ["長褲"], "正式場合"],
    "球衣": [[22, 35], ['sport', 'casual', 'warm', 'cool'], ["球褲", "短褲", "長褲"], "球場"],
    "短襯衫": [[20, 35], ['formal', 'casual', 'goodlooking', 'warm', 'cool'], ["球褲", "短褲", "長褲"], "輕鬆卻不失打扮的場合"],
    "大衣圍巾": [[5, 18], ['goodlooking', 'korean', 'cool', 'cold'], ["長褲"], "需要打扮自我的流行場合"],
    "吊嘎": [[25, 35], ['casual', 'sport', 'warm', 'cool'], ["球褲", "短褲"], "很熱的天氣"],
    "外套": [[5, 17], ['casual', 'goodlooking', 'cold'], ["長褲"], "偏冷的天氣"],
}

ixPants = ["球褲", "短褲", "長褲"]
dbPants = {
    "球褲": [[22, 35], ['sport', 'casual', 'warm', 'cool'], "球場"],
    "短褲": [[20, 35], ['formal', 'casual', 'goodlooking', 'warm', 'cool'], "偏熱的天氣"],
    "長褲": [[5, 22], ['formal', 'casual', 'goodlooking', 'korean', 'cool', 'cold'], "偏冷的天氣"],
}



###################################################
#            query                                #
###################################################
'''
vol= Volcabulary('./data/word2vec/zh.bin')
vol.add_tag(formal)
vol.add_tag(casual)
vol.add_tag(sport)
vol.add_tag(goodlooking)
vol.add_tag(korean)
vol.add_tag(warm)
vol.add_tag(cool)
vol.add_tag(cold)

with os.popen('python2 speech_to_text.py '+sys.argv[1]) as pse:
    for s in pse:
        statement=s
print(statement,vol.query(statement))
'''
