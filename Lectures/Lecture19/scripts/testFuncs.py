"""
Testing Functions for Lecture 19
"""


from .basicFuncs import geometricSim
from .utils import runPascal
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2, t


def test1(n1=100, n2=1, numExp=100):
    """Simulation of Bias and MSE"""
    result1, result2 = [], []
    theoretical_value = 1-(35/36)**24

    for i in range(numExp):
        result1.append(runPascal(numTrials=n1))
        result2.append(runPascal(numTrials=n2))

    print("n = {:d}:".format(n1))
    print("    Bias = {:.07f}".format(np.mean(result1) - theoretical_value))
    print("    MSE = {:0.7f}".format(np.mean(np.array(result1) - theoretical_value)**2))
    
    print("n = {:d}:".format(n2))
    print("    Bias = {:.07f}".format(np.mean(result2) - theoretical_value))
    print("    MSE = {:0.7f}".format(np.mean(np.array(result2) - theoretical_value)**2))


def test2(p=0.05, numTrials=100, a=0, b=1):
    """Simulation of Point Estimators for Variance"""
    rng = np.random.default_rng()
    for idx, numExp in enumerate((2, 100)):
        sampleVars1, sampleVars2 = [], []

        # n Trials in each experiment
        samples = geometricSim(numTrials=numTrials, p=p)
        # samples = (b-a) * rng.random(numTrials) + a
        sampleMean = np.sum(samples)/numTrials
        sampleVars1.append((1/numTrials) * (np.sum((samples - sampleMean)**2)))
        sampleVars2.append((1/(numTrials-1)) * (np.sum((samples - sampleMean)**2)))
        
        print("Number of Experiment = {:d}:".format(numExp))
        print("    Theoretical value of Variance = {:.07f}".format(
            # (1-p)/p**2
            (b-a)**2 / 12
        ))
        print("    Result of biased estimator of variance = {:.07f}".format(
            np.mean(sampleVars1)
        ))
        print("    Result of unbiased estimator of variance = {:.07f}".format(
            np.mean(sampleVars2)
        ))


def test3(n=10, numSamples=10000, alpha=0.05):
    """Simulation of Chi-Squared Distribution"""
    # Degree of freedom
    x = np.linspace(0.01, 25, 100)
    y = chi2.pdf(x, df=n)
    # Generate random samples
    samples = chi2.rvs(df=n, size=numSamples)

    fig = plt.figure(1, figsize=(5,4), dpi=100, layout="constrained")
    ax = fig.add_subplot(111)
    ax.plot(x, y, label="Theoretical mean = {:.2f}".format(n))
    # Add vertical line
    x_vline = chi2.ppf(1 - alpha, df=n)
    print("Chi-squared(p={:.2f}, n={:d}) = {:.2f}".format(alpha, n, x_vline))
    ax.vlines(x=x_vline, ymin=0, ymax=chi2.pdf(x_vline, df=n), colors='r')
    # Add text
    ax.text(
        x=x_vline+1,
        y=chi2.pdf(x_vline, df=n)*0.1,
        s="Area = {:.2f}".format(1 - chi2.cdf(x=x_vline, df=n)),
        color='k',
    )
    # Fill color
    ax.fill_between(
        x=np.linspace(x_vline, x[-1], 10),
        y1=np.zeros_like(np.linspace(x_vline, x[-1], 10)),
        y2=chi2.pdf(x=np.linspace(x_vline, x[-1], 10), df=n),
        alpha=0.5,
        color='r',
    )
    # Histogram
    count, bins, _ = ax.hist(
        samples, 
        bins=numSamples//50, 
        density=True, 
        alpha=0.5,
        label="Histogram of samples, sample mean = {:.2f}".format(np.mean(samples)),
    )
    ax.set(
        xlim=[x[0], x[-1]],
        ylabel=r"$f_Y(y)$",
        title=r'$Y \sim \chi^2$' + "({:d})".format(n),
    )
    ax.legend()
    plt.show()


def test4(n=10, numSamples=10000, alpha=0.05):
    """Simulation of t-Distribution"""
    x = np.linspace(t.ppf(q=0.05, df=1), t.ppf(q=0.95, df=1), 100)
    # Standard normal
    f_x = np.exp(-(x)**2/2) / np.sqrt(2*np.pi)

    fig = plt.figure(dpi=100, figsize=(10,4), layout="constrained")
    # Subplot 1
    ax1 = fig.add_subplot(121)
    ax1.plot(x, f_x, 'k--', label="N(0, 1)")
    # Degrees of freedom: (1, 6, 11, 16)
    for idx, df in enumerate(np.arange(1, 21, 5)):
        ax1.plot(x, t.pdf(x, df=df), alpha=0.6, label=r"$\nu$ = "+"{:d}".format(df))
    ax1.set(
        title=r"$t$-distribution",
        xlim=[t.ppf(0.05, 1), t.ppf(0.95, 1)],
        ylim=[0, 0.5],
    )
    ax1.legend()

    # Subplot 2
    x = np.linspace(t.ppf(0.05, 1), t.ppf(0.95, 1), 100)
    samples = t.rvs(df=n, size=numSamples)

    ax2 = fig.add_subplot(122)
    ax2.plot(x, t.pdf(x, df=n), 'k', label="Theoretical curve: (Mean, Var) = ({:.2f}, {:.2f})".format(0, n/(n-2)))
    ax2.hist(
        x=samples,
        bins=numSamples//50,
        density=True,
        alpha=0.3,
        label="Histogram of samples: (Mean, Var) = ({:.2f}, {:.2f})".format(np.mean(samples), np.var(samples)),
    )
    # Add vertical line
    x_vline = t.ppf(1-alpha/2, df=n)
    ax2.vlines(
        x=[-x_vline, x_vline], 
        ymin=[0, 0], 
        ymax=[t.pdf(-x_vline, df=n), t.pdf(x_vline, df=n)], 
        colors='r'
    )
    # Fill color
    ax2.fill_between(
        x=np.linspace(x[0], -x_vline, 10),
        y1=np.zeros_like(np.linspace(x[0], -x_vline, 10)),
        y2=t.pdf(np.linspace(x[0], -x_vline, 10), df=n),
        alpha=0.2,
        color='r',
    )
    ax2.fill_between(
        x=np.linspace(x_vline, x[-1], 10),
        y1=np.zeros_like(np.linspace(x_vline, x[-1], 10)),
        y2=t.pdf(x=np.linspace(x_vline, x[-1], 10), df=n),
        alpha=0.2,
        color='r',
    )
    # Add text
    ax2.text(
        x=x[0]+.5,
        y=t.pdf(-x_vline, df=n),
        s="t = {:.2f}\nArea = {:.3f}".format(-x_vline, t.cdf(x=-x_vline, df=n)),
        color='r',
    )
    ax2.text(
        x=x_vline+.5,
        y=t.pdf(x_vline, df=n),
        s="t = {:.2f}\nArea = {:.3f}".format(x_vline, 1-t.cdf(x=x_vline, df=n)),
        color='r',
    )
    ax2.set(
        xlim=[t.ppf(0.05, 1), t.ppf(0.95, 1)],
        ylim=[0, 0.5],
        ylabel=r"$f_T(t)$",
        title=r'$T \sim t$' + "({:.2f})".format(n),
    )
    ax2.legend()

    plt.show()


