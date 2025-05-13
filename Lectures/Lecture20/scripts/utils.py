"""
Utility Functions for Lecture 20
"""


import numpy as np
from scripts.basicFuncs import calProb, calTProb


def run_1sample_Z_Test(data, target, pVar, twoTail=True):
    """
    Run z-test for input data

    Parameters:
        data:     data for z-test
        target:   target value for hypothesis checking
        pVar:     variance of population
        twoTail:  True for 2 tailed test, False for 1 tailed
    
    Returns:
        zValue:   result of test statistic
        pValue:   probability of test statistic
    """
    N = len(data)
    zValue = (np.mean(data) - target) / (pVar/np.sqrt(N))
    if twoTail:
        pValue = calProb(zValue)
    else:
        pValue = calProb(zValue, symmetric=False)
    return zValue, pValue


def run_1sample_T_Test(data, target, twoTail=True):
    """
    Run 1-sample t-test for input data

    Parameters:
        data:     data for t-test
        target:   target value for hypothesis checking
        twoTail:  True for 2 tailed test, False for 1 tailed
    
    Returns:
        tValue:   result of test statistic
        pValue:   probability of test statistic
    """

    N = len(data)
    mTreat, sTreat = np.mean(data), np.std(data, ddof=1)
    tValue = (mTreat - target) / (sTreat/np.sqrt(N))
    if twoTail:
        pValue = calTProb(tValue, nu=N-1)
    else:
        pValue = calTProb(tValue, nu=N-1, symmetric=False)
    return tValue, pValue


def run_2sample_T_Test(data1, data2, twoTail=True):
    """
    Run 2-sample t-test for input data

    Parameters:
        data:     data for 2-sample t-test
        target:   target value for hypothesis checking
        twoTail:  True for 2 tailed test, False for 1 tailed
    
    Returns:
        tValue:   result of test statistic
        pValue:   probability of test statistic
    """
    n1 = len(data1)
    n2 = len(data2)
    mTreat, sTreat = np.mean(data1), np.std(data1, ddof=1)
    mControl, sControl = np.mean(data2), np.std(data2, ddof=1)
    
    sp = np.sqrt(
        ((n1-1)*sTreat**2 + (n2-1)*sControl**2) / (n1 + n2 - 2)
    )

    tValue = (mTreat - mControl) / (np.sqrt(1/n1 + 1/n2) * sp)

    if twoTail:
        pValue = calTProb(tValue, nu=n1+n2-2)
    else:
        pValue = calTProb(tValue, nu=n1+n2-2, symmetric=False)

    return tValue, pValue


