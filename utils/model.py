import numpy as np


class NaVieBayes:
    def __init__(self, num_class, len_vocab, alpha=1):
        self.num_class = num_class
        self.len_vocab = len_vocab
        self.alpha = alpha
        self.weight = np.zeros((num_class, len_vocab), dtype=np.float)
        self.num_word_class = np.zeros(num_class, dtype=np.int)
        self.prob_class = np.zeros(num_class, dtype=np.int)

    def fit(self, x, y):
        for i, xi in enumerate(x):
            for w in xi:
                self.weight[y[i]][w] += 1
                self.num_word_class[y[i]] += 1
            self.prob_class[y[i]] += 1
        self.prob_class = self.prob_class/len(x)
        for i in range(self.num_class):
            self.weight[i] = (self.weight[i] + self.alpha)/(self.num_word_class[i] + self.alpha*self.len_vocab)

    def predict(self, x):
        y = []
        for i, xi in enumerate(x):
            y_pred = np.log2(self.prob_class)
            for w in xi:
                for c in range(self.num_class):
                    y_pred[c] += np.log2(self.weight[c][w])
            y.append(np.argmax(y_pred))

        return y