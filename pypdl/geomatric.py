class Geometric:

    def __init__(self, p):
        self.p = p
        self.mean = 1 / p
        self.var = (1 - p) / (p ** 2)

    def pmf(self, x):
        return (1 - self.p) ** x * self.p

    def cdf(self, x):
        if x == 0:
            return self.pmf(0)
        else:
            return self.pmf(x) + self.cdf(x - 1)
