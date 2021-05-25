class Polynomial(list):
    '''
    Polynomial class, essentially a list of coefficients with
    a nice string representation, and correctly behaving addition,
    multiplication, etc.
    '''
    def __init__(self, *coeffs):
        from collections.abc import Sequence
        if isinstance(coeffs[0], Sequence):
            coeffs = coeffs[0]
        list.__init__(self, coeffs)
        self.degree = self.find_degree()

    def find_degree(self):
        '''
        Find the degree of the polynomial.
        This is not necessarily the length of the polynomial
        as a list, since there may be redundant 0 terms at the end
        '''
        for i, coefficient in enumerate(self):
            if coefficient != 0:
                degree = i
        return degree

    def display_monomial(self, degree, coefficient):
        '''
        Correctly give a string representation of the given monomial
        '''
        if degree == 0:
            return str(coefficient)
        if degree == 1 and coefficient == 1:
            return self.symbol
        elif degree == 1 and coefficient != 1:
            return "{}{}".format(coefficient, "x")
        elif coefficient == 1:
            return "{}^{}".format("x", degree)
        else:
            return "{}{}^{}".format(coefficient, "x", degree)


    def __str__(self):
        monos = [self.display_monomial(k, coeff) for k, coeff in enumerate(self) if coeff != 0]
        return " + ".join(monos)


    def __call__(self, point):
        '''
        Evaluates the polynomial at the specified input
        '''
        return sum([co*point**i for i, co in enumerate(self)])


    def match_length(self, p):
        '''
        Adding polynomials requires them to be same length
        This method returns the same polynomial with additional zeros added to the end
        to match the length of the polynomial p
        '''
        added_zeros = [0 for i in range(len(p) - len(self))]
        return Polynomial(list(self) + added_zeros)

    def isnumber(self, p):
        from numbers import Number
        return isinstance(p, Number)
                    
                    
    def __add__(self, p):
        from numbers import Number
        # First, if we add a number rather than another polynomial,
        # we just return a polynomial whose constant (0th) term has
        # p added
        if self.isnumber(p):
            return self + Polynomial(p)

        polys = [self, p]
        polys.sort(key=len)
        matched_length = polys[0].match_length(polys[1])
        return Polynomial([co[0] + co[1] for co in zip(polys[1], matched_length)])

    def __neg__(self):
        return Polynomial([-a for a in self])

    def __sub__(self, p):
        return self + (-p)

    def same_sum_pairs(self, i, j): 
        '''
        Generates tuples containing pairs of powers
        having the same sum, upto required degree
        '''
        from itertools import product
        for k in range(i + j - 1): # need to -1 here because polynomial degree = highest power =
            yield (pair for pair in product(range(i), range(j)) if pair[0] + pair[1] == k)

    def __mul__(self,p):
        # Multiplication by a number just multiplies each
        # term by the number
        if self.isnumber(p):
            return self * Polynomial(p)
        deg1, deg2 = len(self), len(p)
        terms = [[self[i]*p[j] for i, j in degree_pairs] # list comprehensions within list comprehensions
                for degree_pairs in self.same_sum_pairs(deg1, deg2)] # never go deeper!
        return Polynomial([sum(term) for term in terms])

    def __radd__(self, p):
        return self + p 

    def __rmul__(self, p):
        return self * p

    def derivative(self):
        coefficients = [i*coef for i, coef in enumerate(self)]
        return Polynomial(coefficients[1:])


D = lambda p: p.derivative()
