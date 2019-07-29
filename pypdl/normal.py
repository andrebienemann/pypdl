import math


class Normal:
    """
    This is the continuous probability distribution of the random variable X
    that is assumed to be additively produced by many small effects
    """

    def __init__(self, μ, σ2):
        """
        :param μ: expectation of the distribution
        :type μ: float
        :param σ2: variance of the distribution
        :type σ2: float
        """
        self.μ = μ
        self.σ2 = σ2
        self.mean = μ
        self.var = σ2

    def pdf(self, x):
        """
        Probability Density Function \n
        :param x: value of the random variable X
        :type x: int
        :return: relative likelihood that the value of the random variable would lie in the sample space
        """
        return (1 / math.sqrt(2 * math.pi * self.σ2)) * math.e ** (-((x - self.μ) ** 2 / 2 * self.σ2))

    def cdf(self, x):
        """
        Cumulative Distribution Function \n
        :param x: value of the random variable X
        :type x: int
        :return: probability that X will take a value less than or equal to x
        """
        return (1 + math.erf((x - self.μ) / (math.sqrt(self.σ2 * 2)))) / 2
