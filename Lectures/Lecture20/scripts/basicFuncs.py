"""Basic Functions for Lecture 20"""

import numpy as np
import random
from scipy.integrate import quad
from scipy.special import gamma

def createData4example(numSamples=100):
    treatmeantDist = (173., 4.)
    controlDist = (170., 5.5)
    sampleSize = numSamples

    treatmeantHeights, controlHeights = [], []

    for s in range(sampleSize):
        treatmeantHeights.append(random.gauss(treatmeantDist[0], treatmeantDist[1]))
        controlHeights.append(random.gauss(controlDist[0], controlDist[1]))

    treatmeantHeights = np.array(treatmeantHeights)
    controlHeights = np.array(controlHeights)
    
    return treatmeantHeights, controlHeights


def gaussDist(x=None, mu=0, sigma=1, N=100):
    coeff = 1/(sigma*np.sqrt(2*np.pi))
    if x is None:
        x = np.linspace(mu-5*sigma, mu+5*sigma, N)
    return coeff*np.exp(-((x-mu)**2)/(2*sigma**2))


def calProb(x, mu=0, sigma=1, symmetric=True):
    coeff = 1/(sigma*np.sqrt(2*np.pi))
    func = lambda x: coeff*np.exp(-((x-mu)**2)/(2*sigma**2))
    if symmetric:
        prob = quad(func, 0, np.abs(x))[0]
        result = (0.5 - prob)*2
    else:
        prob = quad(func, -np.inf, x)[0]
        result = 1 - prob
    return result


def student_t(x, nu=1):
    const = gamma((nu+1)/2) / (np.sqrt(np.pi*nu) * gamma(nu/2))
    return const * (1 + x**2/nu)**(-(nu+1)/2)


def calTProb(x, nu, symmetric=True):
    func = lambda x, nu: student_t(x=x, nu=nu)
    if symmetric:
        prob = quad(func, 0, np.abs(x), args=(nu,))[0]
        result = (0.5 - prob)*2
    else:
        prob = quad(func, -np.inf, x, args=(nu,))[0]
        result = 1 - prob
    return result


def sampleNormal(numTrials=10000, numSamples=(2**2, 2**8)):
    v1, v2 = [], []

    for t in range(numTrials):
        sample1, sample2 = [], []
        for n1 in range(numSamples[0]):
            sample1.append(random.gauss(0, 1))
        for n2 in range(numSamples[1]):
            sample2.append(random.gauss(0, 1))
        
        # Calculate variance
        v1.append(np.var(np.array(sample1)))
        v2.append(np.var(np.array(sample2)))

    v1, v2 = np.array(v1), np.array(v2)

    return v1, v2

