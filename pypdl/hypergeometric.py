import math


def _binomial(n, r):
    return math.factorial(n) / (math.factorial(r) * math.factorial(n - r))


class Hypergeometric:
    """
    This is a discrete probability distribution that describes the probability of M
    successes in n draws, without replacement, from a finite population of size N
    """

    def __init__(self, n, N, M):
        """
        :param n: Draws
        :param N: Size of population
        :param M: Number of
        """
        self.n = n
        self.N = N
        self.M = M
        self.mean = n * M / N
        self.var = n * M / N * (1 - M / N) * (N - n) / (N - 1)

    def pmf(self, x):
        """
        Probability mass function \n
        :param x: Value of the random variable X
        :return: Probability that X will take a value exactly equal to x
        """
        return _binomial(self.M, x) * _binomial(self.N - self.M, self.n - x) / _binomial(self.N, self.n)

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
