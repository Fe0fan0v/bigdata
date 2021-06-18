# pip install numpy
import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def der(x):
    fx = sigmoid(x)
    return fx * (1 - fx)


def loss(y_true, y_pred):
    return ((y_true - y_pred) ** 2).mean()


class Neuron:
    def __init__(self, weight, bias):
        self.wieght = weight
        self.bias = bias

    def feed(self, inputs):
        total = np.dot(self.wieght, inputs) + self.bias
        return sigmoid(total)


class NeuralNetwork:
    def __init__(self):
        self.w1 = np.random.normal()
        self.w2 = np.random.normal()
        self.w3 = np.random.normal()
        self.w4 = np.random.normal()
        self.w5 = np.random.normal()
        self.w6 = np.random.normal()

        self.b1 = np.random.normal()
        self.b2 = np.random.normal()
        self.b3 = np.random.normal()

    def feed(self, x):
        out_n1 = sigmoid(self.w1 * x[0] + self.w2 * x[1] + self.b1)
        out_n2 = sigmoid(self.w3 * x[0] + self.w4 * x[1] + self.b2)
        out_r1 = sigmoid(self.w5 * out_n1 + self.w6 * out_n2 + self.b3)
        return out_r1

    def train(self, data, y_trues):
        learn_rate = 0.1

        for epoch in range(1000):
            for x, y_true in zip(data, y_trues):
                sum_n1 = self.w1 * x[0] + self.w2 * x[1] + self.b1
                n1 = sigmoid(self.w1 * x[0] + self.w2 * x[1] + self.b1)
                sum_n2 = self.w3 * x[0] + self.w4 * x[1] + self.b2
                n2 = sigmoid(self.w3 * x[0] + self.w4 * x[1] + self.b2)
                sum_r1 = self.w5 * n1 + self.w6 * n2 + self.b3
                r1 = sigmoid(self.w5 * n1 + self.w6 * n2 + self.b3)
                pr1 = -2 * (y_true - r1)
                pw5 = n1 * der(sum_r1)
                pw6 = n2 * der(sum_r1)
                pb3 = der(sum_r1)
                pn1 = self.w5 * der(sum_r1)
                pn2 = self.w6 * der(sum_r1)
                pw1 = x[0] * der(sum_n1)
                pw2 = x[1] * der(sum_n1)
                pb1 = der(sum_n1)
                pw3 = x[0] * der(sum_n2)
                pw4 = x[1] * der(sum_n2)
                pb2 = der(sum_n2)
                self.w1 -= learn_rate * pr1 * pn1 * pw1
                self.w2 -= learn_rate * pr1 * pn1 * pw2
                self.b1 -= learn_rate * pr1 * pn1 * pb1

                self.w3 -= learn_rate * pr1 * pn2 * pw3
                self.w4 -= learn_rate * pr1 * pn2 * pw4
                self.b2 -= learn_rate * pr1 * pn2 * pb2

                self.w5 -= learn_rate * pr1 * pw5
                self.w6 -= learn_rate * pr1 * pw6
                self.b3 -= learn_rate * pr1 * pb3

            if epoch % 10 == 0:
                preds = np.apply_along_axis(self.feed, 1, data)
                losses = loss(y_trues, preds)
                print(f'Потери эпохи {epoch}: {losses}')

data = np.array([
    [54, 165],
    [65, 180],
    [62, 178],
    [49, 152]
])

y_trues = np.array([
    1,
    0,
    0,
    1
])
network = NeuralNetwork()
network.train(data,y_trues)

petya = np.array([70, 173])
masha = np.array([52, 160])
print(f'Маша - {network.feed(masha)}')
print(f'Петя - {network.feed(petya)}')
