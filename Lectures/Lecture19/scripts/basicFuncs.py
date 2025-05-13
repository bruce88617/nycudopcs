"""
Basic Functions for Lecture 19
"""


import numpy as np


def rollDie():
    rng = np.random.default_rng()
    return rng.choice((1,2,3,4,5,6))


def geometricSim(numTrials, p):
    rng = np.random.default_rng()
    return rng.geometric(p=p, size=numTrials)

