"""
Testing Functions for Lecture 18
"""


from .utils import runPascal, getPiEst, getAreaEst, getIntegralEst, getIntegralEst2d
import matplotlib.pyplot as plt
import numpy as np


def test1():
    print("Run Simulation of Pascal's Game")

    p = []
    xAxis = np.geomspace(1, 2**12, 12, dtype=np.int64)

    for numTrials in xAxis:
        p.append(runPascal(numTrials))

    print("    Probability of winning = {:.04f}".format(p[-1]))

    fig = plt.figure(figsize=(5,4), dpi=100, layout="constrained", facecolor="w")
    
    ax1 = fig.add_subplot(111)
    ax1.plot(
        xAxis,
        p, 
        'ko', 
        label="Experimental results\nEstimated probability = {:.04f}".format(p[-1]),
    )
    ax1.set_title("Simulation of Pascal's Problem")
    ax1.set_xlabel("Number of Trials")
    ax1.set_ylabel("Winning Probability")
    ax1.set_xscale("log")
    ax1.set_ylim([0, 1])

    xMin, xMax = ax1.get_xlim()
    ax1.hlines(
        1-(35/36)**24, 
        xmin = xMin, 
        xmax = xMax, 
        colors = 'r', 
        alpha = 0.5,
        label = "Theoretical value = {:.04f}".format(1-(35/36)**24)
    )
    ax1.legend(loc="best")
    
    plt.show()


def test2(numTrials=100, numData=2**15, toPrint=False):

    xVals, yEsts, yStds= [], [], []

    xAxis = np.geomspace(1, numData, 16, dtype=np.int64)

    for val in xAxis:
        curEst, std = getPiEst(numData=val, numTrials=numTrials)
        
        xVals.append(val)
        yStds.append(std)
        yEsts.append(curEst)

        if toPrint:
            print("Est. = {:.06f}, STD = {:.06f}, numData = {}".format(curEst, std, val))
    
    fig = plt.figure(figsize=(5,4), dpi=100, layout="constrained", facecolor="w")
    
    ax1 = fig.add_subplot(111)
    ax1.errorbar(
        x=xVals,
        y=yEsts,
        yerr=yStds,
    )
    ax1.plot(
        xAxis, 
        yEsts, 
        'ko', 
        label="Estimations\nEstimated value = {:.06f}".format(yEsts[-1]),
    )
    ax1.set_title(r"Simulation of $\pi$ Estimation")
    ax1.set_xlabel("Number of Data")
    ax1.set_ylabel("Estimated Value")
    ax1.set_xscale("log")

    xMin, xMax = ax1.get_xlim()
    ax1.hlines(
        np.pi, 
        xmin = xMin, 
        xmax = xMax, 
        colors = 'r', 
        alpha = 0.5,
        label = "Theoretical value = {:.06f}".format(np.pi)
    )
    ax1.legend(loc="best")
    
    plt.show()


def test3(numTrials=100, numData=2**15, toPrint=False):

    xVals, yEsts, yStds= [], [], []

    xAxis = np.geomspace(1, numData, 16, dtype=np.int64)

    for val in xAxis:
        curEst, std = getAreaEst(numData=val, numTrials=numTrials)
        
        xVals.append(val)
        yStds.append(std)
        yEsts.append(curEst)

        if toPrint:
            print("Est. = {:.05f}, STD = {:.05f}, numData = {}".format(curEst, std, val))
    
    fig = plt.figure(figsize=(5,4), dpi=100, layout="constrained", facecolor="w")
    
    ax1 = fig.add_subplot(111)
    ax1.errorbar(
        x=xVals,
        y=yEsts,
        yerr=yStds,
    )
    ax1.plot(
        xAxis, 
        yEsts, 
        'ko', 
        label="Estimations\nEstimated value = {:.06f}".format(yEsts[-1])
    )
    ax1.set_title("Simulation of Area Estimation")
    ax1.set_xlabel("Number of Data")
    ax1.set_ylabel("Estimated Value")
    ax1.set_xscale("log")

    xMin, xMax = ax1.get_xlim()
    ax1.hlines(
        np.pi/2 - 1, 
        xmin = xMin, 
        xmax = xMax, 
        colors = 'r', 
        alpha = 0.5,
        label = "Analytical value = {:.06f}".format(np.pi/2 - 1)
    )
    ax1.legend(loc="best")
    
    plt.show()


def test4(numTrials=100, numData=2**15, **kwargs):
    a = kwargs.get("a", 1.2)
    b = kwargs.get("b", 3.5)
    func = kwargs.get("func", lambda x: 0.5*x)
    toPrint = kwargs.get("toPrint", True)

    xVals, yEsts, yStds= [], [], []

    xAxis = np.geomspace(1, numData, 16, dtype=np.int64)

    for val in xAxis:
        curEst, std = getIntegralEst(
            numData=val, 
            numTrials=numTrials, 
            a=a, 
            b=b, 
            func=func
        )
        
        xVals.append(val)
        yStds.append(std)
        yEsts.append(curEst)

        if toPrint:
            print("Est. = {:.05f}, STD = {:.05f}, numData = {}".format(curEst, std, val))
    
    fig = plt.figure(figsize=(5,4), dpi=100, layout="constrained", facecolor="w")
    
    ax1 = fig.add_subplot(111)
    ax1.errorbar(
        x=xVals,
        y=yEsts,
        yerr=yStds,
    )
    ax1.plot(
        xAxis, 
        yEsts, 
        'ko', 
        label="Estimations\nEstimated value = {:.05f}".format(yEsts[-1]),
    )
    ax1.set_title("Simulation of Monte Carlo Integration")
    ax1.set_xlabel("Number of Data")
    ax1.set_ylabel("Estimated Value")
    ax1.set_xscale("log")

    xMin, xMax = ax1.get_xlim()
    ax1.hlines(
        2.7025, 
        xmin = xMin, 
        xmax = xMax, 
        colors = 'r', 
        alpha = 0.5,
        label = "Analytical value = {:.05f}".format(2.7025)
    )
    ax1.legend(loc="best")
    
    plt.show()


def test5(numTrials=100, numData=2**15, **kwargs):
    a = kwargs.get("a", (-1, -1))
    b = kwargs.get("b", (1, 1))
    toPrint = kwargs.get("toPrint", True)

    xVals, yEsts, yStds= [], [], []

    xAxis = np.geomspace(1, numData, 16, dtype=np.int64)

    for val in xAxis:
        curEst, std = getIntegralEst2d(
            numData=val, 
            numTrials=numTrials, 
            a=a, 
            b=b, 
        )
        
        xVals.append(val)
        yStds.append(std)
        yEsts.append(curEst)

        if toPrint:
            print("Est. = {:.05f}, STD = {:.05f}, numData = {}".format(curEst, std, val))
    
    fig = plt.figure(figsize=(5,4), dpi=100, layout="constrained", facecolor="w")
    
    ax1 = fig.add_subplot(111)
    ax1.errorbar(
        x=xVals,
        y=yEsts,
        yerr=yStds,
    )
    ax1.plot(xAxis, yEsts, 'ko', label="Estimations")
    ax1.set_title("Simulation of 2D Monte Carlo Integration")
    ax1.set_xlabel("Number of Data")
    ax1.set_ylabel("Estimated Value")
    ax1.set_xscale("log")

    xMin, xMax = ax1.get_xlim()
    ax1.hlines(
        1 - np.exp(-0.5),
        xmin = xMin, 
        xmax = xMax, 
        colors = 'r', 
        alpha = 0.5,
        label = "{:.05f}".format(1 - np.exp(-0.5))
    )

    ax1.legend(loc="best")
    
    plt.show()


