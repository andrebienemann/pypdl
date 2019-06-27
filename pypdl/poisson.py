import math


class Poisson:

    def __init__(self, λ):
        self.λ = λ
        self.mean = self.λ
        self.var = self.λ

    def pmf(self, x):
        return (self.λ ** x) * (math.e ** (-self.λ)) / math.factorial(x)

    def cdf(self, x):
        if x == 0:
            return self.pmf(0)
        else:
            return self.pmf(x) + self.cdf(x - 1)
