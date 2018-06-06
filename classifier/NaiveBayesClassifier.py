import re
import json
from pprint import pprint
from random import shuffle
from string import punctuation
from collections import Counter


class NaiveBayesClassifier(object):
    """NaiveBayesClassifier"""

    def __init__(self):
        with open('stopwords_id.txt', 'r') as output_file:
            self.stopwords_id = output_file.read().split()

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

    def get_cond_prob(self, data):
        result = {}
        for key, value in data.items():
            total = sum([v for v in value.values()])
            cond_prob = {k: v / total for k, v in value.items()}
            result[key] = cond_prob

        return result

    def get_prior_prob(self, data_train):
        total = sum([len(value) for value in data_train.values()])
        prior_prob = {k: len(v) / total for k, v in data_train.items()}
        return prior_prob


if __name__ == '__main__':
    data_train = {}
    data_test = {}
    classifier = NaiveBayesClassifier()
    for kategori in ['bisnis', 'sains', 'sport']:
        # for kategori in ['bisnis']:
        with open('../crawler/{}_content.json'.format(kategori),
                  'r') as output_file:
            data = json.loads(output_file.read())
            temp_data_train, temp_data_test = classifier.split_dataset(data)
            data_train[kategori] = temp_data_train
            data_test[kategori] = temp_data_test

    # text = "bandung kota kembang yang indah. saya akan mengerjakan tugas dengan rajin"
    # print(classifier.tokenize(text))
    prior_prob = classifier.get_prior_prob(data_train)
    tf = classifier.get_tf(data_train)
    cond_prob = classifier.get_cond_prob(tf)
