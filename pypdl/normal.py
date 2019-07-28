import math


class Normal:

    def __init__(self, μ, σ2):
        """
        This is the continuous probability distribution of the random variable X
        that is assumed to be additively produced by many small effects
        :param μ:
        :param σ2:
        """
        self.μ = μ
        self.σ2 = σ2
        self.mean = μ
        self.var = σ2

    def pdf(self, x):
        """
        Probability density function \n
        :param x: Value of the random variable X
        :return: Relative likelihood that the value of the random variable would lie in the sample space
        """
        return (1 / math.sqrt(2 * math.pi * self.σ2)) * math.e ** (-((x - self.μ) ** 2 / 2 * self.σ2))

    def cdf(self, x):
        """
        Cumulative distribution function \n
        :param x: Value of the random variable X
        :return: Probability that X will take a value less than or equal to x
        """
        return (1 + math.erf((x - self.μ) / (self.σ2 * math.sqrt(2)))) / 2
