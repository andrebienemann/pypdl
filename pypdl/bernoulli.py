class Bernoulli:

    def __init__(self, p):
        self.p = p
        self.mean = p
        self.var = p * (1 - p)

    def pmf(self, x):
        if x == 0:
            return 1 - self.p
        else:
            return self.p

    def cdf(self, x):
        if x == 0:
            return 1 - self.p
        else:
            return 1
