"""Algorithms for Lecture 16"""


def greedy(items, maxWeight, keyFunction):
    itemsCopy = sorted(items, key=keyFunction, reverse=True)
    result = []
    totalValue, totalWeight = 0., 0.

    for i in range(len(itemsCopy)):

        if (totalWeight + itemsCopy[i].getWeight()) <= maxWeight:

            result.append(itemsCopy[i])
            totalWeight += itemsCopy[i].getWeight()
            totalValue += itemsCopy[i].getValue()

    print("Total value of items taken is {}.".format(totalValue))
    
    for item in result:
        print("    {}".format(item))

    return (result, totalValue)


def chooseBest(pset, maxWeight):
    bestVal = 0.
    bestSet = None
    for items in pset:
        itemsVal = 0.
        itemsWeight = 0.
        for item in items:
            itemsVal += item.getValue()
            itemsWeight += item.getWeight()
        if itemsWeight <= maxWeight and itemsVal > bestVal:
            bestVal = itemsVal
            bestSet = items
    return (bestSet, bestVal)


def searchDT(toConsider, avail):
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getWeight() > avail:
        # Right branch only
        result = searchDT(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        # Left branch
        withVal, withToTake = searchDT(toConsider[1:], avail - nextItem.getWeight())
        withVal += nextItem.getValue()
        # Right branch
        withoutVal, withoutToTake = searchDT(toConsider[1:], avail)
        # Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake+(nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result


def fastSearchDT(toConsider, avail, memo={}):
    if (len(toConsider), avail) in memo:
        result = memo[(len(toConsider), avail)]
    elif toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0].getWeight() > avail:
        # Right branch only
        result = fastSearchDT(toConsider[1:], avail, memo)
    else:
        nextItem = toConsider[0]
        # Left branch
        withVal, withToTake = fastSearchDT(toConsider[1:], avail-nextItem.getWeight(), memo)
        withVal += nextItem.getValue()
        # Right branch
        withoutVal, withoutToTake = fastSearchDT(toConsider[1:], avail, memo)
        # Choose better branch
        if withVal > withoutVal:
            result = (withVal, withToTake+(nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    memo[(len(toConsider), avail)] = result
    return result



