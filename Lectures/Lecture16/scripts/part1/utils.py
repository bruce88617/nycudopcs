"""Utility Functions for Lecture 16"""

from .objs import Item
import random


def value(item):
    return item.getValue()


def weightInverse(item):
    return 1/item.getWeight()


def density(item):
    return item.getValue()/item.getWeight()


def buildItems():
    names = ["book", "violin", "camera", "TV", "painting", "wine"]
    values = [10, 175, 50, 200, 90, 20]
    weights = [1, 10, 2, 20, 9, 4]
    Items =[]

    for i in range(len(values)):
        Items.append(Item(names[i], values[i], weights[i]))

    return Items


def buildManyItems(numItems, maxVal, maxWeight):
    Items = []

    for i in range(numItems):
        Items.append(Item(str(i), random.randint(1,maxVal), random.randint(1,maxWeight)))

    return Items


def genPowerset(L):
    powerset = []

    for i in range(0, 2**len(L)):
        binStr = "{:b}".format(i).zfill(len(L))
        subset = []

        for j in range(len(L)):

            if binStr[j] == "1":
                subset.append(L[j])

        powerset.append(subset)

    return powerset


