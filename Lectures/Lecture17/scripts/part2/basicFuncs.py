"""
Basic Functions for Lecture 17

Part II: Stochastic Programs
"""


import numpy as np


def bernoulli(p):
    rng = np.random.default_rng()
    U = rng.random()
    return U < p


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


def factI(n):
    output = 1
    for i in range(n):
        output *= i+1
    return output


def binCoeff(n, k):
    return factI(n)/(factI(k)*factI(n-k))


