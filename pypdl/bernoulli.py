class Bernoulli:
    """
    This is the discrete probability distribution of
    a random variable which takes either value 1 or 0
    """

    def __init__(self, p):
        """
        :param p: probability of the positive outcome of the experiment
        :type p: float
        """
        self.p = p
        self.mean = p
        self.var = p * (1 - p)

    def pmf(self, x):
        """
        Probability Mass Function \n
        :param x: value of the random variable X
        :type x: int
        :return: probability that X will take a value exactly equal to x
        """
        if x == 0:
            return 1 - self.p
        else:
            return self.p

    def cdf(self, x):
        """
        Cumulative Distribution Function \n
        :param x: value of the random variable X
        :type x: int
        :return: probability that X will take a value less than or equal to x
        """
        if x == 0:
            return 1 - self.p
        else:
            return 1
