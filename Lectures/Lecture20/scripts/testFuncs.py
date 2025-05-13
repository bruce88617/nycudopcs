"""
Test Functions for Lecture 20
"""


import numpy as np
import matplotlib.pyplot as plt
from scripts.basicFuncs import gaussDist, createData4example, sampleNormal, student_t
from scripts.utils import run_1sample_Z_Test, run_1sample_T_Test, run_2sample_T_Test


def test1(target=170, pVar=5.5):
    """
    Run z-test for data

    Parameters:
        target:   target value for hypothesis checking
        pVar:     variance of population
    """

    data = np.load("./data/example1.npz")
    treatmentHeights, controlHeights = data["treatmentHeights"], data["controlHeights"]
    zValue, pValue = run_1sample_Z_Test(
        data = treatmentHeights, 
        target = target,
        pVar = pVar,
    )

    print("z-value = {:.03f}".format(zValue))
    print("Probability = {:.05f}".format(pValue))

    x = np.linspace(-7, 7, 101)
    x2 = np.linspace(-zValue, zValue, 101)

    fig = plt.figure(figsize=(5,4), dpi=100, layout="constrained", facecolor="w")
    ax1 = fig.add_subplot(111)
    ax1.plot(x, gaussDist(x), 'b', label="Mean = {}\nSTD = {}".format(0, 1))
    ax1.vlines([-zValue, zValue], ymin=0, ymax=0.5, colors='r', linestyles='dashed', label="Z-value = {:.03f}".format(zValue))
    ax1.plot(zValue, pValue+0.01, 'rv', markersize=5, label="Probability = {:.05f}".format(pValue))
    ax1.fill_between(x2, y1=gaussDist(x2), y2=0, color='g', alpha=0.2)
    ax1.set_title("Normalized Distribution")
    ax1.set_xlabel("Z")
    ax1.set_ylabel("Probability")
    ax1.set_xlim([-7, 7])
    ax1.set_ylim([0, 0.5])
    ax1.legend(loc=2)    # upper left
        
    plt.show()

    return None


def test2(numSamples=10):
    """
    Run z-test for small number of samples

    Parameters:
        numSamples:   number of samples
    """

    treatmentHeights, controlHeights = createData4example(numSamples=numSamples)
    mTreat, sTreat = np.mean(treatmentHeights), np.std(treatmentHeights)
    mControl, sControl = np.mean(controlHeights), np.std(controlHeights)
    print("sTreat = {:.02f}, sControl = {:.02f}".format(sTreat, sControl))
    zValue, pValue = run_1sample_Z_Test(
        data = treatmentHeights, 
        target = 170,
        pVar = 5.5,
    )

    print("z-value = {:.03f}".format(zValue))
    print("Probability = {}".format(pValue))

    fig = plt.figure(figsize=(10,4), dpi=100, layout="constrained", facecolor="w")
        
    ax1 = fig.add_subplot(121)

    ax1.plot(treatmentHeights, 'ro', label="Treatmean group (mean = {:.02f})".format(np.mean(treatmentHeights)))
    ax1.plot(controlHeights, 'b^', label="Control group (mean = {:.02f})".format(np.mean(controlHeights)))
    ax1.set_title("Test of Vaccine, Number of Samples = {}".format(numSamples))
    ax1.set_xlabel("Sample")
    ax1.set_ylabel("Height on 20 yrs old")
    ax1.set_ylim([150, 190])
    ax1.legend(loc="best")

    x = np.linspace(-7, 7, 101)
    x1 = np.linspace(-7, -zValue, 51)
    x2 = np.linspace(-zValue, zValue, 51)
    x3 = np.linspace(zValue, 7, 51)

    ax2 = fig.add_subplot(122)
    ax2.plot(x, gaussDist(x), 'b', label="Mean = {}\nSTD = {}".format(0, 1))
    ax2.vlines([-zValue, zValue], ymin=0, ymax=0.5, colors='r', linestyles='dashed', label="Z-value = {:.03f}".format(zValue))
    ax2.plot(zValue, pValue+0.01, 'rv', markersize=5, label="Probability = {:.05f}".format(pValue))
    ax2.fill_between(x1, y1=gaussDist(x1), y2=0, color='r', alpha=0.2)
    ax2.fill_between(x2, y1=gaussDist(x2), y2=0, color='g', alpha=0.2)
    ax2.fill_between(x3, y1=gaussDist(x3), y2=0, color='r', alpha=0.2)
    ax2.set_title("Hypothesis Checking, Number of Samples = {}".format(numSamples))
    ax2.set_xlabel("Z")
    ax2.set_ylabel("Probability")
    ax2.set_xlim([-7, 7])
    ax2.set_ylim([0, 0.5])
    ax2.legend(loc=2)    # upper left
        
    plt.show()

    return None


def test3(numSamples=(5, 100), numTrials=10000):
    """Test for distribution of variance"""
    var1, var2 = sampleNormal(
        numTrials=numTrials, 
        numSamples=numSamples,
    )

    fig = plt.figure(figsize=(5,4), dpi=100, layout="constrained", facecolor="w")
        
    ax1 = fig.add_subplot(111)
    ax1.hist(var1, bins=20, color='r', alpha=0.2, label="N = {}".format(numSamples[0]))
    ax1.hist(var2, bins=20, color='b', alpha=0.2, label="N = {}".format(numSamples[1]))
    ax1.set_title("Distribution of Variance, Number of Trials = {}".format(numTrials))
    ax1.set_xlabel("Variance")
    ax1.set_ylabel("Counts")
    ax1.legend(loc="best")

    plt.show()


def test4():
    """Plot student's t and normal distributions"""
    L = 10
    x = np.linspace(-L, L, 101)
    nuList = [1, 2, 5, 11, 21, 30]
    gauss = gaussDist(x, mu=0, sigma=1, N=101)
    styles = ['r--', 'g--', 'b--', 'c', 'm', 'y']

    fig = plt.figure(figsize=(5,4), dpi=100, layout="constrained", facecolor="w")
        
    ax1 = fig.add_subplot(111)

    for nu, style in zip(nuList, styles):
        ax1.plot(x, student_t(x, nu=nu), style, label="DF = {}".format(nu))

    ax1.plot(x, gauss, 'k', label="Normal")
    ax1.set_title("Normal & Student's T Distributions")
    ax1.set_xlabel("x")
    ax1.set_ylabel("Probability")
    ax1.set_xlim([-L, L])
    ax1.set_ylim([0, 0.5])
    ax1.legend(loc=1)

    plt.show()


def test5(numSamples=10):
    """
    Run 1-sample t-test for small number of samples

    Parameters:
        numSamples:   number of samples
    """

    N = numSamples
    treatmentHeights, controlHeights = createData4example(numSamples=N)

    # z-test
    zValue, pValue = run_1sample_Z_Test(
        data = treatmentHeights, 
        target = 170,
        pVar = 5.5,
    )
    print("z-value = {:.03f}".format(zValue))
    print("Probability = {:.03f}".format(pValue))

    # Plot the results
    fig = plt.figure(figsize=(12,4), dpi=100, layout="constrained", facecolor="w")
    # Data distributions
    ax1 = fig.add_subplot(131)
    ax1.plot(treatmentHeights, 'ro', label="Treatmean group (mean = {:.02f})".format(np.mean(treatmentHeights)))
    ax1.plot(controlHeights, 'b^', label="Control group (mean = {:.02f})".format(np.mean(controlHeights)))
    ax1.set_title("Test of Vaccine, Number of Samples = {}".format(N))
    ax1.set_xlabel("Sample")
    ax1.set_ylabel("Height on 20 yrs old")
    ax1.set_ylim([150, 190])
    ax1.legend(loc="best")

    x = np.linspace(-7, 7, 101)
    x1 = np.linspace(-7, -zValue, 51)
    x2 = np.linspace(-zValue, zValue, 51)
    x3 = np.linspace(zValue, 7, 51)
    # Result of z-test
    ax2 = fig.add_subplot(132)
    ax2.plot(x, gaussDist(x), 'b', label="Mean = {}\nSTD = {}".format(0, 1))
    ax2.vlines([-zValue, zValue], ymin=0, ymax=0.5, colors='r', linestyles='dashed', label="Z-value = {:.03f}".format(zValue))
    ax2.plot(zValue, pValue+0.01, 'rv', markersize=5, label="Probability = {:.03f}".format(pValue))
    ax2.fill_between(x1, y1=gaussDist(x1), y2=0, color='r', alpha=0.2)
    ax2.fill_between(x2, y1=gaussDist(x2), y2=0, color='g', alpha=0.2)
    ax2.fill_between(x3, y1=gaussDist(x3), y2=0, color='r', alpha=0.2)
    ax2.set_title("1-sample Z-test, Number of Samples = {}".format(N))
    ax2.set_xlabel("Z")
    ax2.set_ylabel("Probability")
    ax2.set_xlim([-7, 7])
    ax2.set_ylim([0, 0.5])
    ax2.legend(loc=2)    # upper left

    # t-test
    tValue, pValue = run_1sample_T_Test(
        data = treatmentHeights, 
        target = 170,
    )
    print("t-value = {:.03f}".format(tValue))
    print("Probability = {:.03f}".format(pValue))

    x1 = np.linspace(-7, -tValue, 51)
    x2 = np.linspace(-tValue, tValue, 51)
    x3 = np.linspace(tValue, 7, 51)
    # Result of t-test
    ax3 = fig.add_subplot(133)
    ax3.plot(x, student_t(x), 'b', label="Mean = {}\nSTD = {}".format(0, 1))
    ax3.vlines([-tValue, tValue], ymin=0, ymax=0.5, colors='r', linestyles='dashed', label="T-value = {:.03f}".format(tValue))
    ax3.plot(tValue, pValue+0.01, 'rv', markersize=5, label="Probability = {:.03f}".format(pValue))
    ax3.fill_between(x1, y1=student_t(x1), y2=0, color='r', alpha=0.2)
    ax3.fill_between(x2, y1=student_t(x2), y2=0, color='g', alpha=0.2)
    ax3.fill_between(x3, y1=student_t(x3), y2=0, color='r', alpha=0.2)
    ax3.set_title("T-test, Number of Samples = {}".format(N))
    ax3.set_xlabel("T")
    ax3.set_ylabel("Probability")
    ax3.set_xlim([-7, 7])
    ax3.set_ylim([0, 0.5])
    ax3.legend(loc=2)    # upper left
        
    plt.show()


def test6():
    """
    Run 2-sample t-test for data
    """

    data = np.load("./data/example1.npz")
    treatmentHeights, controlHeights = data["treatmentHeights"], data["controlHeights"]
    N = len(treatmentHeights)

    fig = plt.figure(figsize=(10,4), dpi=100, layout="constrained", facecolor="w")
        
    ax1 = fig.add_subplot(121)

    ax1.plot(treatmentHeights, 'ro', label="Treatmean group (mean = {:.02f})".format(np.mean(treatmentHeights)))
    ax1.plot(controlHeights, 'b^', label="Control group (mean = {:.02f})".format(np.mean(controlHeights)))
    ax1.set_title("Distribution of Samples")
    ax1.set_xlabel("Sample")
    ax1.set_ylabel("Height on 20 yrs old")
    ax1.set_ylim([150, 190])
    ax1.legend(loc="best")

    # t-test
    tValue, pValue = run_2sample_T_Test(
        data1 = treatmentHeights,
        data2 = controlHeights,
    )

    print("t-value = {:.03f}".format(tValue))
    print("Probability = {:.03f}".format(pValue))

    x = np.linspace(-7, 7, 101)
    x1 = np.linspace(-7, -tValue, 51)
    x2 = np.linspace(-tValue, tValue, 51)
    x3 = np.linspace(tValue, 7, 51)

    ax3 = fig.add_subplot(122)
    ax3.plot(x, student_t(x, nu=2*N-2), 'b', label="DF = {}".format(2*N-2))
    ax3.vlines([-tValue, tValue], ymin=0, ymax=0.5, colors='r', linestyles='dashed', label="T-value = {:.03f}".format(tValue))
    ax3.plot(tValue, student_t(tValue, nu=2*N-2), 'ro', markersize=5, label="Probability = {:.03f}".format(pValue))
    ax3.fill_between(x1, y1=student_t(x1, nu=2*N-2), y2=0, color='r', alpha=0.2)
    ax3.fill_between(x2, y1=student_t(x2, nu=2*N-2), y2=0, color='g', alpha=0.2)
    ax3.fill_between(x3, y1=student_t(x3, nu=2*N-2), y2=0, color='r', alpha=0.2)
    ax3.set_title("Result of 2-sample T-test")
    ax3.set_xlabel("T")
    ax3.set_ylabel("Probability")
    ax3.set_xlim([-7, 7])
    ax3.set_ylim([0, 0.5])
    ax3.legend(loc=2)    # upper left
        
    plt.show()

##############################################
##############  Scipy result  ################
##############################################
from scipy.stats import ttest_ind, ttest_1samp


def test7():
    """
    Run scipy results
    """

    data = np.load("./data/example1.npz")
    treatmentHeights, controlHeights = data["treatmentHeights"], data["controlHeights"]
    
    oneSampleTest = ttest_1samp(treatmentHeights, 170)

    print("1-sample T-statistic = {}".format(oneSampleTest[0]))
    print("1-sample p-value = {}".format(oneSampleTest[1]))
    print(oneSampleTest)

    twoSampleTest = ttest_ind(treatmentHeights, controlHeights, equal_var=False)

    print("2-sample T-statistic = {}".format(twoSampleTest[0]))
    print("2-sample p-value = {}".format(twoSampleTest[1]))
    print(twoSampleTest)



