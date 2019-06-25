import math


def _binomial(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))


class NegativeBinomial:

    def __init__(self, r, p):
        self.r = r
        self.p = p
        self.mean = r * p / (1 - p)
        self.var = r * p / (1 - p) ** 2

    def cdf(self, x):
        if x == 0:
            return self.pmf(0)
        else:
            return self.pmf(x) + self.cdf(x - 1)

    def pmf(self, x):
        return _binomial(x + self.r - 1, x) * self.p ** x * (1 - self.p) ** self.r
