
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
from sklearn.metrics.pairwise import cosine_similarity
import jieba
assert Word2Vec and KeyedVectors and jieba


class Volcabulary:
    def __init__(self,path):
        #self.w2v = KeyedVectors.load_word2vec_format(path, binary=False) 
        self.w2v = Word2Vec.load(path)
        self.tag=[]
    def add_tag(self,text):
        if text in self.w2v.wv.vocab:
            self.tag.append(text)
        else :
            raise ValueError("tag is not availible.")
    def query(self,text):
        score={}
        for i in self.tag:
            score[i]=self.max_simularity(i,text)
        return score
    def max_simularity(self,tag,text):
        #text=list(jieba.cut(text))
        score=[]
        for i in text:
            if i in self.w2v.wv.vocab:
                score.append(cosine_similarity(self.w2v[tag].reshape((1,-1)),self.w2v[i].reshape((1,-1)))[0,0])
            else :
                score.append(0)
        print('text {}, tag {}, score {}'.format(text,tag,score))
        return max(score)

if __name__ == '__main__':
    vol= Volcabulary('./data/word2vec/zh.bin')
    vol.add_tag('韓')
    vol.add_tag('暖')
    vol.add_tag('冷')
    vol.add_tag('涼')
    print(vol.query('今天風好大'))
