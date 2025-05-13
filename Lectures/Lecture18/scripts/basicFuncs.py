"""
Basic Functions for Lecture 18
"""


import numpy as np


def bernoulli(p):
    rng = np.random.default_rng()
    U = rng.random()
    return U < p


def binomial(n, p):
    rng = np.random.default_rng()
    U = rng.random(n)
    return sum(U < p)


def poisson(lam):
    rng = np.random.default_rng()
    U = rng.random()
    i = 0
    Y = -np.log(U)/lam
    result = Y
    while result <= 1:
        U = rng.random()
        Y = -np.log(U)/lam
        result += Y
        i = i+1
    return i


def variance(X):
    mean = sum(X)/len(X)
    tot = 0.
    for x in X:
        tot += (x-mean)**2
    return tot/len(X)


def stdDev(X):
    return variance(X)**0.5


def CV(X):
    mean = sum(X)/len(X)
    try:
        return stdDev(X)/mean
    except ZeroDivisionError:
        return float('nan')


def gaussDist(x=None, mu=0, sigma=1, N=100):
    coeff = 1/(sigma*np.sqrt(2*np.pi))
    if x is None:
        x = np.linspace(mu-5*sigma, mu+5*sigma, N)
    return coeff*np.exp(-((x-mu)**2)/(2*sigma**2))


def factI(n):
    output = 1
    for i in range(n):
        output *= i+1
    return output


def binCoeff(n, k):
    return factI(n)/(factI(k)*factI(n-k))


