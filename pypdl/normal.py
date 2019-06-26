import math


class Normal:

    def __init__(self, μ, σ2):
        self.μ = μ
        self.σ2 = σ2
        self.mean = μ
        self.var = σ2

    def pdf(self, x):
        return (1 / math.sqrt(2 * math.pi * self.σ2)) * math.e ** (-((x - self.μ) ** 2 / 2 * self.σ2))

    def cdf(self, x):
        return (1 + math.erf((x - self.μ) / (self.σ2 * math.sqrt(2)))) / 2
