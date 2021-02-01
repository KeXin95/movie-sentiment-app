import pickle
from lime.lime_text import LimeTextExplainer


class Explainer():
    def __init__(self):
        self.model = pickle.load(open("models/rf.pkl", 'rb'))
        self.class_names = ['negative', 'somewhat negative', 'neutral',
                            'somewhat positive', 'positive']
        self.explainer = LimeTextExplainer(class_names=self.class_names)

    def explain(self, sentence):
        exp = self.explainer.explain_instance(sentence,
                                              self.model.predict_proba,
                                              num_features=6,
                                              top_labels=len(self.class_names))
        f = open('/Users/kexinchong/Documents/learning/self/HPE/movie-sentiment-app/frontend/public/app/temp.html',
                 'w')
        f.write(exp.as_html())
        f.close()

        return 'success'
        # return exp.as_html()
