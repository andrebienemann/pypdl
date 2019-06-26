class Uniform:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.mean = (a + b) / 2
        self.var = (b - a) ** 2 / 12

    def pdf(self, x):
        return 1 / (self.b - self.a)

    def cdf(self):
        pass
