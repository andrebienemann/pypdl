class Bernoulli:

    def __init__(self, p):
        """
        This is the discrete probability distribution of
        a random variable which takes either value 1 or 0 \n
        :param p: Probability of the positive outcome of the experiment
        """
        self.p = p
        self.mean = p
        self.var = p * (1 - p)

    def pmf(self, x):
        """
        Probability mass function \n
        :param x: Value of the random variable X
        :return: Probability that X will take a value exactly equal to x
        """
        if x == 0:
            return 1 - self.p
        else:
            return self.p

    def cdf(self, x):
        """
        Cumulative distribution function \n
        :param x: Value of the random variable X
        :return: Probability that X will take a value less than or equal to x
        """
        if x == 0:
            return 1 - self.p
        else:
            return 1
