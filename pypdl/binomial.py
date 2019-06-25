import math


def _binomial(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))


class Binomial:

    def __init__(self, n, p):
        self.n = n
        self.p = p
        self.mean = n * p
        self.var = n * p * (1 - p)

    def pmf(self, x):
        bc = _binomial(self.n, x)
        return bc * self.p ** x * (1 - self.p) ** (self.n - x)

    def cdf(self, x):
        if x == 0:
            return self.pmf(0)
        else:
            return self.pmf(x) + self.cdf(x - 1)
