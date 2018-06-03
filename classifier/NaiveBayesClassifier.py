import json
from pprint import pprint
from random import shuffle


class NaiveBayesClassifier(object):
    """NaiveBayesClassifier"""

    def split_dataset(self, data, ratio=0.80):
        shuffle(data)
        temp = int(len(data) * ratio)
        data_train = data[0:temp]
        data_test = data[temp:]
        return data_train, data_test


if __name__ == '__main__':
    data_train = []
    data_test = []
    classifier = NaiveBayesClassifier()
    for kategori in ['bisnis', 'sains', 'sport']:
        with open('../crawler/{}_content.json'.format(kategori),
                  'r') as output_file:
            data = json.loads(output_file.read())
            temp_data_train, temp_data_test = classifier.split_dataset(data)
            data_train += temp_data_train
            data_test += temp_data_test

    print(len(data_train), len(data_test))
