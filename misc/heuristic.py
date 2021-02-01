from nltk.tokenize import word_tokenize
from string import punctuation
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import re
import pickle


class AIModel():
    def __init__(self):
        self.model = pickle.load(open("models/rf.pkl", 'rb'))
        # Helper functions
        self.ps = PorterStemmer()
        self.negation_list = ["arent", "isnt", "dont", "doesnt", "not",
                              "cant", "couldnt",  "werent", "wont", "didnt",
                              "never", "nothing", "nowhere", "noone", "none",
                              "hasnt", "hadnt", "shouldnt", "wouldnt", "aint"]
        self.stops_lst = stopwords.words('english')
        self.stops_lst.extend(['film', 'movie'])
        self.label_map = {0: 'negative',
                          1: 'somewhat negative',
                          2: 'neutral',
                          3: 'somewhat positive',
                          4: 'positive'
                          }

    def preProcess(self, sentence):
        sentence = sentence.lower()
        sentence = re.sub('n[^A-Za-z ]t', 'nt', sentence)
        sentence = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', '', sentence)
        sentence = re.sub('@[^\s]+', '', sentence)
        sentence = re.sub(r'#([^\s]+)', r'\1', sentence)
        sentence = word_tokenize(sentence)
        clean_list = []
        negate = False
        for word in sentence:
            word = self.ps.stem(word)
            if word in self.negation_list:
                negate = True
            elif negate is True and word in list(punctuation):
                negate = False

            if negate and word not in self.negation_list:
                word = "not_"+word
            else:
                pass
            word = re.sub('[^A-Za-z_ ]+', '', word)
            if len(word) > 2 and word not in self.stops_lst:
                clean_list.append(word)
        clean_set = set(clean_list)
        return " ".join(clean_set)

    def predict(self, sentence):
        if type(sentence) == str:
            clean_txt = self.preProcess(sentence)
            pred_val = self.model.predict([clean_txt])[0]
            return self.label_map[pred_val]

