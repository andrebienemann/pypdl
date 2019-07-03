import math


def _binomial(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))


class NegativeBinomial:

    def __init__(self, r, p):
        """
        This is the discrete probability distribution of the
        number of trials needed to get r successes \n
        :param r: Number of successes
        :param p: Probability of success
        """
        self.r = r
        self.p = p
        self.mean = r / p
        self.var = r / p ** 2

    def pmf(self, x):
        """
        Probability mass function \n
        :param x: Value of the random variable X
        :return: Probability that X will take a value exactly equal to x
        """
        return _binomial(x - 1, self.r - 1) * (self.p ** self.r) * ((1 - self.p) ** (x - self.r))

    def cdf(self, x):
        """
        Cumulative distribution function \n
        :param x: Value of the random variable X
        :return: Probability that X will take a value less than or equal to x
        """
        if x == 0:
            return self.pmf(0)
        else:
            return self.pmf(x) + self.cdf(x - 1)
