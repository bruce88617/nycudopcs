"""
Testing Functions for Lecture 17

Part I: Random Walk
"""

from .utils import simWalks, getFinalLocs, getTrajectory, getTrajectory2, styleIterator, styleIterator2
from .objs import UsualDrunk, EastWardDrunk, HeatAvoidDrunk
import numpy as np
import matplotlib.pyplot as plt


def test1(numTrials=100, dClass=0, name=""):
    if dClass == 1: 
        dClass = EastWardDrunk
    elif dClass == 2:
        dClass = HeatAvoidDrunk
    else:
        dClass = UsualDrunk

    
    if name == "":
        name = "HoHoChen"


    print("Run Test #1: Random Walk of Drunkard {}".format(name))

    walkLengths = (10, 100, 1000, 10000)

    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials, dClass, name)
        print("    {} random walk of {} steps".format(dClass.__name__, numSteps))
        print("        Mean = {:.03f}, Max = {}, Min = {}".format(sum(distances)/len(distances), max(distances), min(distances)))

    print("=="*10, "End of Test 1", "=="*10)


def test2(numTrials=100, dClass=0, name=""):
    if dClass == 1: 
        dClass = EastWardDrunk
    elif dClass == 2:
        dClass = HeatAvoidDrunk
    else:
        dClass = UsualDrunk


    if name == "":
        name = "YenYenChen"

    print("Run Test #2: Random Walk of Drunkard {}".format(name))

    steps = np.round(np.logspace(0, 5, 11, dtype=int))
    result = []

    for numSteps in steps:
        distances = simWalks(numSteps, numTrials, dClass, name)
        result.append(np.mean(distances))

    fig = plt.figure(1, figsize=(4,3), dpi=100, layout="constrained")
    ax = fig.add_subplot(111)
    ax.plot(steps, result, label="{} random walk".format(dClass.__name__))
    ax.plot(steps, np.sqrt(steps), "r-.", label="Square root of steps")
    ax.set_xlabel("Number of Steps")
    ax.set_ylabel("Distance from Origin")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_title("Mean Distance from Origin ({} trials)".format(numTrials))
    ax.legend(loc="best")

    plt.show()


def test3(numTrials=100, name=""):
    if name == "":
        name = "YingYingChen"

    drunkKinds = (UsualDrunk, HeatAvoidDrunk, EastWardDrunk)

    print("Run Test #3: Random Walk of Drunkard {}".format(name))

    walkLengths = (100, 1000)

    for dClass in drunkKinds:
        for numSteps in walkLengths:
            distances = simWalks(numSteps, numTrials, dClass, name)
            print("    {} random walk of {} steps".format(dClass.__name__, numSteps))
            print("        Mean = {:.03f}, Max = {}, Min = {}".format(sum(distances)/len(distances), max(distances), min(distances)))
    
    print("=="*10, "End of Test 3", "=="*10)


def test4(numTrials=100, name=""):  
    if name == "":
        name = "ChihChihChen"

    drunkKinds = (UsualDrunk, HeatAvoidDrunk, EastWardDrunk)

    print("Run Test #4: Random Walk of Drunkard {}".format(name))

    steps = np.round(np.logspace(0, 5, 11, dtype=int))
    result = np.zeros((len(steps), len(drunkKinds)))

    for k in range(len(drunkKinds)):
        for i in range(len(steps)):
            distances = simWalks(steps[i], numTrials, drunkKinds[k], name)
            result[i,k] = np.mean(distances)

    fig = plt.figure(1, figsize=(4,3), dpi=100, layout="constrained")
    ax = fig.add_subplot(111)
    ax.plot(steps, result[:,0], "m-", label="{} random walk".format(drunkKinds[0].__name__))
    ax.plot(steps, result[:,1], "r:", label="{} random walk".format(drunkKinds[1].__name__))
    ax.plot(steps, result[:,2], "k-.", label="{} random walk".format(drunkKinds[2].__name__))
    ax.set_xlabel("Number of Steps")
    ax.set_ylabel("Distance from Origin")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_title("Mean Distance from Origin ({} trials)".format(numTrials))
    ax.legend(loc="best")

    plt.show()


def test5(numSteps=100, numTrials=100, name="", style_list=None):
    if name == "":
        name = "Peter"

    if style_list is None:
        style_list = styleIterator(("k+", "r^", "mo"))

    drunkKinds = (UsualDrunk, HeatAvoidDrunk, EastWardDrunk)

    print("Run Test #5: Where is the Drunkard {}?".format(name))

    fig = plt.figure(1, figsize=(6,5), dpi=100, layout="constrained")
    ax = fig.add_subplot(111)

    for dClass in drunkKinds:
        xVals, yVals = [], []
        locs = getFinalLocs(numSteps, numTrials, dClass)
        for loc in locs:
            xVals.append(loc.getX())
            yVals.append(loc.getY())
        meanX = np.mean(xVals)
        meanY = np.mean(yVals)
        
        style = style_list.nextStyle()
        ax.plot(xVals, yVals, style, label="{}, mean location = ({:.2f}, {:.2f})".format(dClass.__name__, meanX, meanY))
    
    ax.set_xlabel("East/West of Origin")
    ax.set_ylabel("North/South Origin")
    ax.set_title("Location at End of Walks ({} steps)".format(numSteps))
    ax.grid()
    ax.legend(loc="best")

    plt.show()


def test6(numSteps=100, name="", style_list=None):
    if name == "":
        name = "Peter"

    if style_list is None:
        style_list = styleIterator2(colors=("k", "r", "m"), markers=(".", "v", "4"))

    drunkKinds = (UsualDrunk, HeatAvoidDrunk, EastWardDrunk)

    print("Run Test #6: Trajectory of the Drunkard {}".format(name))

    fig = plt.figure(1, figsize=(6,5), dpi=100, layout="constrained")
    ax = fig.add_subplot(111)

    a = np.linspace(0.3, 1, numSteps)
    # s = np.linspace(0, 50, numSteps)
    s = (np.copy(a)**2)*50

    for dClass in drunkKinds:
        locs = getTrajectory(numSteps, dClass)
        xVals, yVals = [], []

        color, marker = style_list.nextStyle()

        for i, loc in enumerate(locs):
            xVals.append(loc.getX())
            yVals.append(loc.getY())
            ax.scatter(loc.getX(), loc.getY(), s=s[i], alpha=a[i], c=color, marker=marker)

        ax.scatter(loc.getX(), loc.getY(), s=s[i], alpha=a[i], c=color, marker=marker, label=dClass.__name__)

    ax.scatter(0,0, s=50, marker="D", c="b", label="Origin")    
    ax.set_xlabel("East/West of Origin")
    ax.set_ylabel("North/South Origin")
    ax.set_title("Trajectory of Walks ({} steps)".format(numSteps))
    ax.grid()
    ax.legend(loc="best")

    plt.show()


def test7(wormholes={}, numSteps=100, name="", style_list=None):
    if name == "":
        name = "Peter"

    if style_list is None:
        style_list = styleIterator2(colors=("k", "r", "m"), markers=(".", "v", "4"))

    drunkKinds = (UsualDrunk, HeatAvoidDrunk, EastWardDrunk)

    print("Run Test #7: Trajectory of {} in a Mysterious Field".format(name))

    fig = plt.figure(1, figsize=(6,5), dpi=100, layout="constrained")
    ax = fig.add_subplot(111)

    a = np.linspace(0.3, 1, numSteps)
    # s = np.linspace(0, 50, numSteps)
    s = (np.copy(a)**2)*50

    for dClass in drunkKinds:
        locs, wLocs = getTrajectory2(numSteps, dClass, wormholes=wormholes)
        xVals, yVals = [], []

        color, marker = style_list.nextStyle()

        for i, loc in enumerate(locs):
            xVals.append(loc.getX())
            yVals.append(loc.getY())
            ax.scatter(loc.getX(), loc.getY(), s=s[i], alpha=a[i], c=color, marker=marker)

        ax.scatter(loc.getX(), loc.getY(), s=s[i], alpha=a[i], c=color, marker=marker, label=dClass.__name__)

    style_list2 = styleIterator(("co", "go", "bo"))
    style_list3 = styleIterator(("cx", "gx", "bx"))
    
    for i, w in enumerate(wLocs):
        style2 = style_list2.nextStyle()
        style3 = style_list3.nextStyle()
        ax.plot(w[0],w[1], style2, label="Wormhole #{}".format(i+1), markersize=3)
        ax.plot(w[2],w[3], style3, label="Wormhole #{}".format(i+1), markersize=3)

    ax.scatter(0,0, s=50, marker="D", c="b", label="Origin")    
    ax.set_xlabel("East/West of Origin")
    ax.set_ylabel("North/South Origin")
    ax.set_title("Trajectory of Walks ({} steps)".format(numSteps))
    ax.grid()
    ax.legend(loc="best")

    plt.show()


