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
        text=list(jieba.cut(text))+list(text)
        #print(text)
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
