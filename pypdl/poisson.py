import math


class Poisson:

    def __init__(self, λ):
        """
        This is a discrete probability distribution that expresses the probability
        of a given number of events occurring in a fixed interval of time or space \n
        :param λ: Average number of events
        """
        self.λ = λ
        self.mean = self.λ
        self.var = self.λ

    def pmf(self, x):
        """
        Probability mass function \n
        :param x: Value of the random variable X
        :return: Probability that X will take a value exactly equal to x
        """
        return (self.λ ** x) * (math.e ** (-self.λ)) / math.factorial(x)

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
