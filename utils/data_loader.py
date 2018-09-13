import os
import json
from utils.pre_process import PreProcess


class DataLoader:
    def __init__(self):
        self.vocab = {'<unk>': 0}
        self.features = []
        self.target = []
        dir_path = '/home/chiendb/data/aclImdb/pos/'
        dir = os.listdir(dir_path)
        for i, file in enumerate(dir):
            try:
                with open(dir_path + file, 'r') as f:
                    text = f.read().replace('\n', ' ')
                    self.features.append(text)
                    self.target.append(0)
            except Exception as e:
                print(e)

        dir_path = '/home/chiendb/data/aclImdb/neg/'
        dir = os.listdir(dir_path)
        for i, file in enumerate(dir):
            try:
                with open(dir_path + file, 'r') as f:
                    text = f.read().replace('\n', ' ')
                    self.features.append(text)
                    self.target.append(1)
            except Exception as e:
                print(e)

        self.features = PreProcess().transform(self.features)
        self.features = [self.word2vec(line) for line in self.features]

        with open('/home/chiendb/data/aclImdb/vocab.txt', 'w') as f:
            f.write(json.dumps(self.vocab))

    def word2vec(self, text):
        result = []
        for word in text:
            if word not in self.vocab:
                self.vocab[word] = len(self.vocab)

            result.append(self.vocab[word])
        return result

    def get_data(self):
        return self.features, self.target
