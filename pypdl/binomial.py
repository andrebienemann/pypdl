import math


def _binomial(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))


class Binomial:

    def __init__(self, n, p):
        """
        This is the discrete probability distribution of the number of successes
        in a sequence of size n independent experiments with probability of success p \n
        :param n: Size of sequence
        :param p: Probability of success
        """
        self.n = n
        self.p = p
        self.mean = n * p
        self.var = n * p * (1 - p)

    def pmf(self, x):
        """
        Probability mass function \n
        :param x: Value of the random variable X
        :return: Probability that X will take a value exactly equal to x
        """
        return _binomial(self.n, x) * self.p ** x * (1 - self.p) ** (self.n - x)

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
