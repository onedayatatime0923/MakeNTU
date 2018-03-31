
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
from sklearn.metrics.pairwise import cosine_similarity
import jieba
import numpy as np
assert Word2Vec and KeyedVectors and jieba and cosine_similarity and np


class Volcabulary:
    def __init__(self,path):
        #self.w2v = KeyedVectors.load_word2vec_format(path, binary=False) 
        self.w2v = Word2Vec.load(path)
        self.tag=[]
    def add_tag(self,text):
        self.tag.append(text)
    def query(self,text):
        score={}
        for i in self.tag:
            score[i]=self.max_simularity(i,text)
        return sorted(score.items(), key=lambda x: x[1],reverse=True)
    def max_simularity(self,tag,text):
        text=list(jieba.cut(text))#+list(text)
        scores=[]
        for i in text:
            for j in tag.feature:
                if i in self.w2v.wv.vocab and j in self.w2v.wv.vocab:
                    score=(cosine_similarity(self.w2v[j].reshape((1,-1)),self.w2v[i].reshape((1,-1)))[0,0])
                    #score=np.linalg.norm(self.w2v[j]-self.w2v[i])
                else :
                    score=(1 if j==i else 0)
                scores.append(score)
        #print('text {}, tag {}, score {}'.format(text,tag,scores))
        return max(scores)
class Tag:
    def __init__(self,name,feature):
        self.feature=feature
        self.name=name
    def __str__(self):
        return "{}".format(self.feature)
    def __repr__(self):
        return "{}".format(self.name)


if __name__ == '__main__':
    vol= Volcabulary('./data/word2vec/zh.bin')
    vol.add_tag(Tag(['婚禮','喪禮','典禮','正式','嚴肅']))
    vol.add_tag(Tag(['打球','運動','流汗','減肥','健身','球場','球隊']))
    vol.add_tag(Tag(['休閒','一般','普通','舒適','舒服','散步','約會','好看','悶','','熱','悶熱','炎熱']))
    vol.add_tag(Tag(['寒流','寒冷','寒','凍','保暖','保溫','韓系','韓流','約會','好看','正式','流行']))
    vol.add_tag(Tag(['悶','熱','炎熱','休閒','健身','肌肉','曬黑','曬太陽']))
    vol.add_tag(Tag(['寒流','寒冷','寒','凍','約會','好看','正式','流行','防風']))

    print(vol.query('我想去打球'))
    print(vol.query('我今天要去找女友'))
    print(vol.query('今天我爸結婚'))
