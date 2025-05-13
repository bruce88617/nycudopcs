"""Test Functions for Lecture 16"""

from scripts.part1.utils import buildItems, value, weightInverse, density, genPowerset, buildManyItems
from scripts.part1.funcs import greedy, chooseBest, searchDT, fastSearchDT


def test1(availWeight=20):
    items = buildItems()
    print("Use greedy by value to fill knapsack of size {}".format(availWeight))
    greedy(items, availWeight, value)
    print("Use greedy by weight to fill knapsack of size {}".format(availWeight))
    greedy(items, availWeight, weightInverse)
    print("Use greedy by density to fill knapsack of size {}".format(availWeight))
    greedy(items, availWeight, density)


def test2(availWeight=20):
    items = buildItems()
    pset = genPowerset(items)
    taken, val = chooseBest(pset, availWeight)
    print("Total value of items taken is {}".format(val))
    try:
        for item in taken:
            print(item)
    except:
        print("Nothing is taken.")


def test3(availWeight=20, numItems=10, maxVal=200, maxWeight=20):
    items = buildManyItems(numItems, maxVal, maxWeight)
    pset = genPowerset(items)
    taken, val = chooseBest(pset, availWeight)
    print("Total value of items taken is {}".format(val))
    try:
        for item in taken:
            print(item)
    except:
        print("Nothing is taken.")


def testDT1(availWeight=5):
    print("Decision Tree Test 1 (max. weight = {}):".format(availWeight))
    items = buildItems()
    val, taken = searchDT(items, availWeight)
    print("    Items taken:")
    try:
        for item in taken:
            print("        ", item)
    except:
        print("        Nothing is taken.")
    print("    Total value of items taken = {}".format(val))


def testDT2(availWeight=5, numItems=10, maxVal=200, maxWeight=20):
    print("Decision Tree Test 2 (max. weight = {}):".format(availWeight))
    items = buildManyItems(numItems, maxVal, maxWeight)
    val, taken = searchDT(items, availWeight)
    print("    Items taken:")
    try:
        for item in taken:
            print("        ", item)
    except:
        print("        Nothing is taken.")
    print("    Total value of items taken = {}".format(val))


def testDT3(availWeight=5, numItems=10, maxVal=200, maxWeight=20):
    print("Decision Tree Test 2 (max. weight = {}):".format(availWeight))
    items = buildManyItems(numItems, maxVal, maxWeight)
    val, taken = fastSearchDT(items, availWeight)
    print("    Items taken:")
    if taken != ():
        for item in taken:
            print("        ", item)
    else:
        print("        Nothing is taken.")
    print("    Total value of items taken = {}".format(val))


