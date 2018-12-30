from utils.data_loader import DataLoader
from utils.model import NaVieBayes
from sklearn.metrics import accuracy_score, f1_score
import pickle

loader = DataLoader()
len_vocab = len(loader.vocab)
features, target = loader.get_data()
n = len(target)
indexs = [i//2 if i % 2 == 0 else i//2 + n//2 for i in range(n)]
features = [features[i] for i in indexs]
target = [target[i] for i in indexs]
k_fold = 5
batch_size = len(target)//k_fold

for i in range(k_fold):
    model = NaVieBayes(num_class=2, len_vocab=len_vocab, alpha=1)
    features_train = features[0: batch_size*i] + features[batch_size*(i+1):]
    target_train = target[0: batch_size*i] + target[batch_size*(i+1):]
    features_test = features[batch_size*i: batch_size*(i+1)]
    target_test = target[batch_size*i: batch_size*(i+1)]
    model.fit(features_train, target_train)
    y_pred = model.predict(features_test)
    print('model {}: acc: {}, f1_score: {}'.format(i, accuracy_score(target_test, y_pred), f1_score(target_test, y_pred, average=None)))
    with open('models/nb_model_' + str(i) + '.pkl', 'wb+') as f:
        pickle.dump(model, f)

print('Done')
