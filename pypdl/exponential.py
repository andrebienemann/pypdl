import math


class Exponential:
    """
    This is the continuous probability distribution of the time between events in a Poisson process
    """

    def __init__(self, λ):
        """
        :param λ: Average number of events
        :type λ: float
        """
        self.λ = λ
        self.mean = λ ** -1
        self.var = λ ** -2

    def pdf(self, x):
        """
        Probability Density Function \n
        :param x: Value of the random variable X
        :return: Relative likelihood that the value of the random variable would lie in the sample space
        """
        return self.λ * math.e ** (-self.λ * x)

    def cdf(self, x):
        """
        Cumulative Distribution Function \n
        :param x: value of the random variable X
        :return: probability that X will take a value less than or equal to x
        """
        return 1 - math.e ** (-self.λ * x)
