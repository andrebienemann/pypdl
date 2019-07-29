class Uniform:
    """
    TODO
    """

    def __init__(self, a, b):
        """
        :param a: TODO
        :type a: TODO
        :param b: TODO
        :type b: TODO
        """
        self.a = a
        self.b = b
        self.mean = (a + b) / 2
        self.var = (b - a) ** 2 / 12

    def pdf(self, x):
        """
        Probability Density Function \n
        :param x: Value of the random variable X
        :return: Relative likelihood that the value of the random variable would lie in the sample space
        """
        return 1 / (self.b - self.a)

    def cdf(self, x):
        """
        Cumulative Distribution Function \n
        :param x: value of the random variable X
        :return: probability that X will take a value less than or equal to x
        """
        # TODO
        pass
