import pickle
import json
from utils.pre_process import PreProcess
from tkinter import Tk, Text, TOP, BOTH, X, N, LEFT, RIGHT, CENTER, Label, Frame, Button


class Application(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.parent.title('Naive Bayes')
        self.pack(fill=BOTH, expand=True)
        self.frm_title = Frame(self)
        self.frm_title.pack(fill=X)
        self.lpl_title = Label(self.frm_title, text='Title', width=6)
        self.lpl_title.pack(side=LEFT, padx=10, pady=10)
        self.txt_title = Text(self.frm_title, height=40)
        self.txt_title.pack(padx=10, expand=True)
        self.frm_calculator = Frame(self)
        self.frm_calculator.pack(fill=X)
        self.btn_calculator = Button(self.frm_calculator, text='Guess', command=self.run,  width=10)
        self.btn_calculator.pack(side=LEFT, padx=10, pady=10)
        self.txt_result = Label(self.frm_calculator, text='', state='disabled', anchor=CENTER, bg="white")
        self.txt_result.pack(fill=X, side=RIGHT, padx=10, pady=10, expand=True)
        with open('models/nb_model_0.pkl', 'rb') as f:
            self.model = pickle.load(f)
        self.preprocess = PreProcess()
        with open('/home/chiendb/data/aclImdb/vocab.txt', 'r') as f:
            self.vocab = json.load(f)

    def run(self):
        title = [self.txt_title.get('1.0', 'end-1c')]
        title = self.preprocess.transform(title)
        title = [self.word2vec(line) for line in title]
        y_pred = self.model.predict(title)
        tag = 'pos' if y_pred[0] == 0 else 'neg'
        self.txt_result.config(text=tag)

    def word2vec(self, text):
        result = []
        for word in text:
            if word not in self.vocab:
                result.append(self.vocab['<unk>'])
            else:
                result.append(self.vocab[word])
        return result
