"""
Utility Functions for Lecture 18
"""


import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def rollDie():
    rng = np.random.default_rng()
    return rng.choice((1,2,3,4,5,6))


def runPascal(numTrials):
    numWins = 0

    for i in range(numTrials):
        for j in range(24):
            d1 = rollDie()
            d2 = rollDie()
            if d1==6 and d2==6:
                numWins += 1
                break

    return numWins/numTrials


def estPi(numData):
    inCircle = 0
    for data in range(numData):
        x, y = random.random(), random.random()
        if (x**2 + y**2)**0.5 <= 1:
            inCircle += 1
    return 4*(inCircle/numData)


def getPiEst(numData, numTrials):
    estimates = []
    for t in range(numTrials):
        piGuess = estPi(numData)
        estimates.append(piGuess)
    std = np.std(estimates)
    curEst = sum(estimates)/len(estimates)
    return (curEst, std)


def throwData(numData):
    count = 0
    for data in range(numData):
        x, y = random.random(), random.random()
        if ((x**2 + y**2)**0.5 <= 1) and \
              (((x-1)**2 + (y-1)**2)**0.5 <= 1):
            count += 1
    return count/numData


def getAreaEst(numData, numTrials):
    estimates = []
    for t in range(numTrials):
        areaGuess = throwData(numData)
        estimates.append(areaGuess)
    std = np.std(estimates)
    curEst = sum(estimates)/len(estimates)
    return (curEst, std)


def mcIntegral1d(numData, a, b, func):
    """
    Parameters
        a: lower bound of definite integral
        b: upper bound of definite integral
        func: target function to calculate
    """
    I = 0.

    for data in range(numData):
        x = (b-a)*random.random() + a
        I += func(x)

    return (b-a)*I/numData


def getIntegralEst(numData, numTrials, **kwargs):
    a = kwargs.get("a", 0)
    b = kwargs.get("b", 1)
    func = kwargs.get("func", lambda x: x)

    estimates = []

    for t in range(numTrials):
        integralGuess = mcIntegral1d(numData, a=a, b=b, func=func)
        estimates.append(integralGuess)

    std = np.std(estimates)
    curEst = sum(estimates)/len(estimates)
    return (curEst, std)


def mcIntegral2d(numData, a, b):
    """
    Parameters
        a1: lower bound of 1st dimension
        b1: upper bound of 1st dimension
        a2: lower bound of 2nd dimension
        b2: upper bound of 2nd dimension
        func: target function to calculate
    """
    I = 0.
    a1, a2, b1, b2 = a[0], a[1], b[0], b[1]
    func = lambda x, y, mean, sigma: np.exp(-0.5 * (((x - mean[0])/sigma[0])**2 + ((y - mean[1])/sigma[1])**2)) \
            * (2 * np.pi * sigma[0] * sigma[1])**(-1)
    
    for data in range(numData):
        x = (b1-a1)*random.random() + a1
        y = (b2-a2)*random.random() + a2

        if np.sqrt(x**2 + y**2) <= 1:
            I += func(x, y, (0, 0), (1, 1))

    ans = (b1-a1)*(b2-a2)*I/numData
    return ans


def getIntegralEst2d(numData, numTrials, **kwargs):
    a = kwargs.get("a", (-1, -1))
    b = kwargs.get("b", (1, 1))

    estimates = []

    for t in range(numTrials):
        integralGuess = mcIntegral2d(numData, a=a, b=b)
        estimates.append(integralGuess)

    std = np.std(estimates)
    curEst = sum(estimates)/len(estimates)
    return (curEst, std)

