"""
Testing Functions for Lecture 17

Part II: Stochastic Programs
"""


from .utils import rollSim, bernoulliSim, geometricSim, binomialSim, pascalSim, poissonSim
from .basicFuncs import binCoeff, factI
import matplotlib.pyplot as plt
import numpy as np


def test1(numRollsPerTrial=5, numTrials=5, seed=False):
    print("Rolling a fair dice {} times".format(numRollsPerTrial))
    for t in range(numTrials):
        print("    {} trials: {}".format(t+1, rollSim(numTimes=numRollsPerTrial, seed=seed)))


def test2(numTrials=1000, p=0.5):
    """Bernoulli distribution"""
    result = bernoulliSim(numTrials=numTrials, p=p)
    avg = [sum(result[:i])/i for i in range(1, numTrials+1)]
    fig = plt.figure(1, figsize=(5,4), dpi=100, layout="constrained")
    ax = fig.add_subplot(111)
    ax.plot(range(1, numTrials+1), avg)
    ax.set(
        xlabel="Number of Trials",
        ylabel="Fraction of Success",
        xlim=[0,numTrials],
        ylim=[0,1],
        title="Bernoulli({:.2f})".format(p),
    )
    plt.show()


def test3(numTrials=1000, p=0.5):
    """Geometric distribution"""
    # Generate random samples
    result = geometricSim(numTrials=numTrials, p=p)
    # Theoretical value
    k = np.arange(1, 25)
    P_k = [p * (1-p)**(i) for i in k]

    fig = plt.figure(1, figsize=(5,4), dpi=100, layout="constrained")
    ax = fig.add_subplot(111)
    ax.plot(k, P_k, label="Theoretical mean = {:.2f}".format(1/p))
    count, bins, _ = ax.hist(
        result, 
        bins=50 if numTrials>1000 else numTrials//50, 
        density=True, 
        label="Histogram of samples, sample mean = {:.2f}".format(np.mean(result)),
    )
    ax.set(
        xlabel=r"$k$",
        ylabel=r"$P_X(k)$",
        xlim=[0, max(k)],
        ylim=[0, max(P_k)*1.2],
        title="Geometric({:.2f})".format(p),
    )
    ax.legend()
    plt.show()


def test4(numTrials=1000, n=10, p=0.2):
    """Binomial distribution"""
    # Generate random samples
    result = binomialSim(numTrials=numTrials, n=n, p=p)
    # Theoretical value
    k = np.arange(n+1)
    P_k = [binCoeff(n=n, k=i) * p**i * (1-p)**(n-i) for i in k]

    fig = plt.figure(1, figsize=(5,4), dpi=100, layout="constrained")
    ax = fig.add_subplot(111)
    ax.plot(k, P_k, label="Theoretical mean = {:.2f}".format(n*p))
    count, bins, _ = ax.hist(
        result, 
        bins=n+1, 
        density=True, 
        label="Histogram of samples, sample mean = {:.2f}".format(np.mean(result)),
    )
    ax.set(
        xlabel=r"$k$",
        ylabel=r"$P_X(k)$",
        xlim=[0, max(k)],
        ylim=[0, max(P_k)*1.2],
        title="Binomial({:d}, {:.2f})".format(n, p),
    )
    ax.legend()
    plt.show()


def test5(numTrials=1000, m=10, p=0.2):
    """Pascal distribution"""
    # Generate random samples
    result = pascalSim(numTrials=numTrials, m=m, p=p)
    # Theoretical value
    k = np.arange(m*10)
    P_k = [binCoeff(n=i-1, k=m-1) * p**m * (1-p)**(i-m) for i in k]

    fig = plt.figure(1, figsize=(5,4), dpi=100, layout="constrained")
    ax = fig.add_subplot(111)
    ax.plot(k, P_k, label="Theoretical mean = {:.2f}".format(m/p))
    count, bins, _ = ax.hist(
        result, 
        bins=50 if numTrials>1000 else numTrials//50, 
        density=True, 
        label="Histogram of samples, sample mean = {:.2f}".format(np.mean(result)),
    )
    ax.set(
        xlabel=r"$k$",
        ylabel=r"$P_X(k)$",
        xlim=[0, max(k)],
        ylim=[0, max(count)*1.5],
        title="Pascal({:d}, {:.1f})".format(m, p),
    )
    ax.legend()
    plt.show()


def test6(numTrials=1000, lamb=1):
    """Pascal distribution"""
    # Generate random samples
    result = poissonSim(numTrials=numTrials, lamb=lamb)
    # Theoretical value
    k = np.arange(20)
    P_k = [np.exp(-lamb)*lamb**i / factI(i) for i in k]

    fig = plt.figure(1, figsize=(5,4), dpi=100, layout="constrained")
    ax = fig.add_subplot(111)
    ax.plot(k, P_k, label="Theoretical mean = {:.2f}".format(lamb))
    count, bins, _ = ax.hist(
        result, 
        bins=50 if numTrials>1000 else numTrials//50, 
        density=True, 
        label="Histogram of samples, sample mean = {:.2f}".format(np.mean(result)),
    )
    ax.set(
        xlabel=r"$k$",
        ylabel=r"$P_X(k)$",
        xlim=[0, max(k)],
        ylim=[0, max(count)*1.5],
        title="Poisson({:.1f})".format(lamb),
    )
    ax.legend()
    plt.show()


def test7(numTrials=1000, a=0, b=1):
    """Uniform distribution"""
    # Generate random samples
    rng = np.random.default_rng()
    result = (b-a) * rng.random(numTrials) + a
    # Theoretical value
    x = np.linspace(-1+a, 1+b, 100)
    f_x = np.ones_like(x)/(b-a)
    f_x[x < a] = 0
    f_x[x > b] = 0

    fig = plt.figure(1, figsize=(5,4), dpi=100, layout="constrained")
    ax = fig.add_subplot(111)
    ax.plot(x, f_x, label="Theoretical mean = {:.2f}".format((b+a)/2))
    count, bins, _ = ax.hist(
        result, 
        bins=50 if numTrials>1000 else numTrials//50, 
        density=True, 
        label="Histogram of samples, sample mean = {:.2f}".format(np.mean(result)),
    )
    ax.set(
        xlabel=r"$x$",
        ylabel=r"$f_X(x)$",
        xlim=[min(x), max(x)],
        ylim=[0, 1.5/(b-a)],
        title="Uniform({:.1f}, {:.1f})".format(a, b),
    )
    ax.legend()
    plt.show()


def test8(numTrials=1000, lamb=1):
    """Exponential distribution"""
    if lamb <= 0: 
        raise ValueError("Lambda should be positive.")
    # Generate random samples
    rng = np.random.default_rng()
    result = rng.exponential(scale=1/lamb, size=numTrials)
    # Theoretical value
    x = np.linspace(0, 5/lamb, 100)
    f_x = lamb * np.exp(-lamb*x)

    fig = plt.figure(1, figsize=(5,4), dpi=100, layout="constrained")
    ax = fig.add_subplot(111)
    ax.plot(x, f_x, label="Theoretical mean = {:.2f}".format(1/lamb))
    count, bins, _ = ax.hist(
        result, 
        bins=50 if numTrials>1000 else numTrials//50, 
        density=True, 
        label="Histogram of samples, sample mean = {:.2f}".format(np.mean(result)),
    )
    ax.set(
        xlabel=r"$x$",
        ylabel=r"$f_X(x)$",
        xlim=[min(x), max(x)],
        ylim=[0, max(f_x)],
        title="Exponential({:.1f})".format(lamb),
    )
    ax.legend()
    plt.show()


def test9(numTrials=1000, mu=0, sigma=1):
    """Gaussian distribution"""
    if sigma <= 0: 
        raise ValueError("Standard deviation should be positive.")
    # Generate random samples
    rng = np.random.default_rng()
    result = rng.normal(loc=mu, scale=sigma, size=numTrials)
    # Theoretical value
    x = np.linspace(-4*sigma, 4*sigma, 100)
    f_x = (2*np.pi*sigma**2)**(-0.5) * np.exp(-(x-mu)**2/(2*sigma**2))

    fig = plt.figure(1, figsize=(5,4), dpi=100, layout="constrained")
    ax = fig.add_subplot(111)
    ax.plot(x, f_x, label="Theoretical mean = {:.2f}".format(mu))
    count, bins, _ = ax.hist(
        result, 
        bins=50 if numTrials>1000 else numTrials//50, 
        density=True, 
        label="Histogram of samples, sample mean = {:.2f}".format(np.mean(result)),
    )
    ax.set(
        xlabel=r"$x$",
        ylabel=r"$f_X(x)$",
        xlim=[min(x), max(x)],
        ylim=[0, 0.5],
        title="Normal({:.1f}, {:.1f})".format(mu, sigma),
    )
    ax.legend()
    plt.show()


from scipy.special import gamma

def test10(numTrials=1000, alpha=1, lamb=1):
    """Gamma distribution"""
    if lamb <= 0 or alpha <=0: 
        raise ValueError("Alpha and Lambda should be positive.")
    # Generate random samples
    rng = np.random.default_rng()
    result = rng.gamma(shape=alpha, scale=1/lamb, size=numTrials)
    # Theoretical value
    x = np.linspace(0, 10/lamb, 100)
    f_x = lamb**alpha * x**(alpha-1) * np.exp(-lamb*x) / gamma(alpha)

    fig = plt.figure(1, figsize=(5,4), dpi=100, layout="constrained")
    ax = fig.add_subplot(111)
    ax.plot(x, f_x, label="Theoretical mean = {:.2f}".format(alpha/lamb))
    count, bins, _ = ax.hist(
        result, 
        bins=50 if numTrials>1000 else numTrials//50, 
        density=True, 
        label="Histogram of samples, sample mean = {:.2f}".format(np.mean(result)),
    )
    ax.set(
        xlabel=r"$x$",
        ylabel=r"$f_X(x)$",
        xlim=[min(x), max(x)],
        ylim=[0, max(f_x)*2],
        title="Gamma({:.1f}, {:.1f})".format(alpha, lamb),
    )
    ax.legend()
    plt.show()
