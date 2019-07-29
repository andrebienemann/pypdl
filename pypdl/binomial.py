import math


def _binomial(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))


class Binomial:
    """
    This is the discrete probability distribution of the number of successes
    in a sequence of size n independent experiments with probability of success p
    """

    def __init__(self, n, p):
        """
        :param n: size of sequence
        :type n: int
        :param p: probability of success
        :type p: float
        """
        self.n = n
        self.p = p
        self.mean = n * p
        self.var = n * p * (1 - p)

    def pmf(self, x):
        """
        Probability Mass Function \n
        :param x: value of the random variable X
        :type x: int
        :return: probability that X will take a value exactly equal to x
        """
        return _binomial(self.n, x) * self.p ** x * (1 - self.p) ** (self.n - x)

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
