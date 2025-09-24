from numpy import *


class LinearRegression:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coeficiente_correlacao = self.__coeficiente_correlacao()
        self.inclinacao = self.__inclinacao()
        self.interceptacao = self.__correlacao()

    def __coeficiente_correlacao(self):
        covariacao = cov(self.x, self.y, bias=True)[0][1]
        variancia_x = var(self.x)
        variancia_y = var(self.y)
        return covariacao / (sqrt(variancia_x) * sqrt(variancia_y))

    def __inclinacao(self):
        stdx = std(self.x)
        stdy = std(self.y)
        return self.coeficiente_correlacao * (stdy / stdx)

    def __correlacao(self):
        meanx = mean(self.x)
        meany = mean(self.y)
        return meany - meanx * self.inclinacao

    def previsao(self, valor):
        return self.interceptacao + (self.inclinacao * valor)
