import math


class Poisson:
    """
    This is a discrete probability distribution that expresses the probability
    of a given number of events occurring in a fixed interval of time or space
    """

    def __init__(self, λ):
        """
        :param λ: Average number of events
        :type λ: float
        """
        self.λ = λ
        self.mean = self.λ
        self.var = self.λ

    def pmf(self, x):
        """
        Probability Mass Function \n
        :param x: value of the random variable X
        :type x: int
        :return: probability that X will take a value exactly equal to x
        """
        return (self.λ ** x) * (math.e ** (-self.λ)) / math.factorial(x)

    def cdf(self, x):
        """
        Cumulative Distribution Function \n
        :param x: value of the random variable X
        :type x: int
        :return: probability that X will take a value less than or equal to x
        """
        if x == 0:
            return self.pmf(0)
        else:
            return self.pmf(x) + self.cdf(x - 1)
