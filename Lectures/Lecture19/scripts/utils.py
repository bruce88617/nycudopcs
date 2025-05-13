"""
Utility Functions for Lecture 19
"""


import numpy as np
from .basicFuncs import rollDie


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






