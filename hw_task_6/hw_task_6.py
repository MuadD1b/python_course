from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import matplotlib.pyplot as plt


np.set_printoptions(precision=2, floatmode='fixed', suppress=True)

class Neural:

    def __init__(
            self,
            path='data.txt',
            loss='binary_crossentropy',
            optimizer='adam',
            metrics=['accuracy'],
            epochs=15,
            batch_size=10,
            verbose=2,
            layer_1=12,
            act_1='relu',
            layer_2=8,
            act_2='relu',
            layer_3=1,
            act_3='sigmoid'
    ):
        self.path = path
        self.loss = loss
        self.optimizer = optimizer
        self.metrics = metrics
        self.epochs = epochs
        self.batch_size = batch_size
        self.verbose = verbose
        self.layer_1 = layer_1
        self.layer_2 = layer_2
        self.layer_3 = layer_3
        self.act_1 = act_1
        self.act_2 = act_2
        self.act_3 = act_3

    def prepare(self):
        dataset = np.genfromtxt(self.path, delimiter=',', dtype=float)
        self.Y = dataset[:, -1]
        self.X = dataset[:, :8]

    def train(self):
        self.model = Sequential()
        self.model.add(Dense(self.layer_1, input_dim=8, activation=self.act_1))
        self.model.add(Dense(self.layer_2, activation=self.act_2))
        self.model.add(Dense(self.layer_3, activation=self.act_3))
        self.model.compile(loss=self.loss, optimizer=self.optimizer, metrics=self.metrics)
        self.model.fit(self.X, self.Y, epochs=self.epochs, batch_size=self.batch_size, verbose=self.verbose)

    def predict(self, num):
        prediction = np.array(self.model(self.X[:num]))
        return prediction


# nn = Neural()
# nn.prepare()
# nn.train()
# print('Prediction:\n', nn.predict(3))


m = 1
for i in range(5, 15, 5):
    for j in range(4, 10, 2):
        for k in range(10, 50, 10):
            for l in range(10, 50, 10):
                nn = Neural(layer_1=i, layer_2=j, epochs=k, batch_size=l)
                nn.prepare()
                nn.train()
                a = []
                a = np.append(a, nn.predict(3))
                a = np.append(a, nn.predict(3))
                a = np.append(a, nn.predict(3))
                np.savetxt(f'nn-{m}_layer1-{i}_layer2-{j}_epochs-{k}_batch-{l}.txt', a, delimiter=',')
                m += 1

