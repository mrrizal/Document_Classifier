import re
import json
import pickle
from math import exp
from pprint import pprint
from random import shuffle
from collections import Counter


class NaiveBayesClassifier(object):
    """NaiveBayesClassifier"""

    def __init__(self):
        with open('stopwords_id.txt', 'r') as output_file:
            self.stopwords_id = output_file.read().split()

        try:
            self.prior_prob = pickle.load(open('prior_prob.pickle', 'rb'))
        except Exception:
            self.prior_prob = None

        try:
            self.word_prob = pickle.load(open('word_prob.pickle', 'rb'))
        except Exception:
            self.word_prob = None

        try:
            self.total_word = pickle.load(open('total_word.pickle', 'rb'))
        except Exception:
            self.total_word = None

        if self.prior_prob is not None:
            self.kategories = list(self.prior_prob.keys())

    def split_dataset(self, data, ratio=0.80):
        shuffle(data)
        temp = int(len(data) * ratio)
        data_train = data[0:temp]
        data_test = data[temp:]
        return data_train, data_test

    def tokenize(self, text):
        text = re.sub(r'[^A-Za-z ]', r'', text).strip()
        text = re.sub(r'\s+', ' ', text)
        words = text.split()
        return words

    def cleaning_words(self, words):
        words = list(
            filter(lambda x: x.lower() not in self.stopwords_id and len(x) > 1,
                   words))
        words = list(map(lambda x: x.lower(), words))
        return words

    def get_tf(self, data):
        result = {}
        for key, value in data.items():
            temp = []
            for content in value:
                words = self.tokenize(content['content'])
                words = self.cleaning_words(words)
                temp += words

            result[key] = dict(Counter(temp))
        return result

    def get_word_prob(self, data):
        result = {}
        total_word = {}
        for key, value in data.items():
            total = sum([v for v in value.values()])
            total_word[key] = total
            cond_prob = {k: v / total for k, v in value.items()}
            result[key] = cond_prob

        return result, total_word

    def get_prior_prob(self, data_train):
        total = sum([len(value) for value in data_train.values()])
        prior_prob = {k: len(v) / total for k, v in data_train.items()}
        return prior_prob

    def get_dataset(self, kategories=['bisnis', 'sains', 'sport']):
        self.data_train = {}
        self.data_test = {}
        for kategori in kategories:
            with open('../crawler/{}_content.json'.format(kategori),
                      'r') as output_file:
                data = json.loads(output_file.read())
                temp_data_train, temp_data_test = self.split_dataset(data)
                self.data_train[kategori] = temp_data_train
                self.data_test[kategori] = temp_data_test

        return self.data_train, self.data_test

    def train(self, data_train):
        prior_prob = classifier.get_prior_prob(data_train)
        tf = classifier.get_tf(data_train)
        word_prob, total_word = classifier.get_word_prob(tf)

        pickle.dump(total_word, open('total_word.pickle', 'wb'))
        pickle.dump(prior_prob, open('prior_prob.pickle', 'wb'))
        pickle.dump(word_prob, open('word_prob.pickle', 'wb'))

    def classifier(self, text):
        words = self.tokenize(text)
        words = self.cleaning_words(words)
        result = {}
        evidence = 0
        for i in self.kategories:
            result[i] = {'prior_prob': self.prior_prob[i]}
            cond_prob = 0
            for word in words:
                if word in self.word_prob[i]:
                    cond_prob += exp(self.word_prob[i][word])
                else:
                    cond_prob += exp(1 / self.total_word[i])

            result[i]['cond_prob'] = cond_prob
            result[i]['posterior_prob'] = exp(
                result[i]['prior_prob']) + result[i]['cond_prob']
            evidence += result[i]['posterior_prob']

        temp = 0
        label = None
        for i in self.kategories:
            result[i]['result'] = result[i]['posterior_prob'] / evidence
            if result[i]['result'] > temp:
                temp = result[i]['result']
                label = i

        return {'text': text, 'label': label}

    def evaluate(self, data_test):
        result = {}
        for i in self.kategories:
            result[i] = {'total_artikel': len(datatest[i])}
            result[i]['predict_artikel'] = {'benar': 0, 'salah': 0}
            for j in datatest[i]:
                temp = self.classifier(j['content'])['label']
                if temp == i:
                    result[i]['predict_artikel']['benar'] += 1
                else:
                    result[i]['predict_artikel']['salah'] += 1

            result[i]['percent'] = result[i]['predict_artikel'][
                'benar'] / result[i]['total_artikel']

        return result


if __name__ == '__main__':
    classifier = NaiveBayesClassifier()
    datatrain, datatest = classifier.get_dataset()
    classifier.train(datatrain)
    pprint(classifier.evaluate(datatest))
