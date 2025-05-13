"""
Utility Functions for Lecture 17

Part II: Stochastic Programs
"""


import random
import numpy as np
from .basicFuncs import bernoulli


def rollDie():
    return random.choice((1,2,3,4,5,6))


def rollSim(numTimes=5, seed=False):
    if seed:
        random.seed(0)
    result = ""
    for t in range(numTimes):
        result += str(rollDie())
    return result


def flipCoin():
    return random.choice(("H", "T"))


def flip(numFlips):
    numHeads = 0
    for i in range(numFlips):
        if flipCoin() == "H":
            numHeads += 1
    numTails = numFlips - numHeads
    return (numHeads, numTails)


def bernoulliSim(numTrials, p):
    fracSuccess = []
    for i in range(numTrials):
        if bernoulli(p=p):
            fracSuccess.append(1)
        else:
            fracSuccess.append(0)
    return fracSuccess


def geometricSim(numTrials, p):
    rng = np.random.default_rng()
    return rng.geometric(p=p, size=numTrials)


def binomialSim(numTrials, n, p):
    rng = np.random.default_rng()
    return rng.binomial(n=n, p=p, size=numTrials)


def pascalSim(numTrials, m, p):
    rng = np.random.default_rng()
    # return rng.negative_binomial(n=m, p=p, size=numTrials)
    samples = []
    for i in range(numTrials):
        samples.append(sum([rng.geometric(p=p) for j in range(m)]))
    return samples


def poissonSim(numTrials, lamb):
    rng = np.random.default_rng()
    return rng.poisson(lam=lamb, size=numTrials)

