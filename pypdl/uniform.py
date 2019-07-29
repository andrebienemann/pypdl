class Uniform:
    """
    This is the continuous distribution of the random variable X in interval [a; b]
    where any value of X has an equal probability
    """

    def __init__(self, a, b):
        """
        :param a: minimum value of X
        :type a: float
        :param b: maximum value of X
        :type b: float
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
        if x <= self.a:
            return 0.0
        elif x >= self.b:
            return 1.0
        else:
            return (x - self.a) / (self.b - self.a)
