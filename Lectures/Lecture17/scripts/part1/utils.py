"""
Utility Functions for Lecture 17

Part I: Random Walk
"""


from .objs import Location, Field, MysteriousField


def walk(field, target, numSteps):
    start = field.getLoc(target)
    for s in range(numSteps):
        field.moveDrunk(target)
    return start.distFrom(field.getLoc(target))


def simWalks(numSteps, numTrials, dClass, name):
    drunkard = dClass(name)
    origin = Location(0,0)
    distances = []

    for t in range(numTrials):
        f = Field()
        f.addDrunk(drunkard, origin)
        distances.append(round(walk(f, drunkard, numSteps), 1))
    return distances


def simAll(drunkKinds, walkLengths, numTrials, name):
    for dClass in drunkKinds:
        simWalks(walkLengths, numTrials, dClass, name)


def getFinalLocs(numSteps, numTrials, dClass):
    locs = []
    d = dClass()
    for t in range(numTrials):
        f = Field()
        f.addDrunk(d, Location(0,0))
        for s in range(numSteps):
            f.moveDrunk(d)
        locs.append(f.getLoc(d))
    return locs


def getTrajectory(numSteps, dClass):
    locs = []
    d = dClass()
    f = Field()
    f.addDrunk(d, Location(0,0))
    for s in range(numSteps):
        f.moveDrunk(d)
        locs.append(f.getLoc(d))
    return locs


class styleIterator:
    def __init__(self, styles):
        self.index = 0
        self.styles = styles
    
    def nextStyle(self):
        result = self.styles[self.index]
        if self.index == len(self.styles)-1:
            self.index = 0
        else:
            self.index += 1
        return result


class styleIterator2:
    def __init__(self, colors, markers):
        self.index = 0
        self.colors = colors
        self.markers = markers
    
    def nextStyle(self):
        color = self.colors[self.index]
        marker = self.markers[self.index]
        if self.index == len(self.colors)-1:
            self.index = 0
        else:
            self.index += 1
        return color, marker


def getTrajectory2(numSteps, dClass, wormholes={}, maxRange=20):
    locs = []
    d = dClass()
    f = MysteriousField()
    f.addDrunk(d, Location(0,0))

    # Add wormholes
    if wormholes == {}:
        f.addWormholes(3, 0, maxRange=maxRange)
        f.addWormholes(-3, 3, maxRange=maxRange)
    else:
        for k in wormholes.keys():
            f.addWormholes(k[0], k[1], wormholes[k][0], wormholes[k][1], maxRange=maxRange)

    for s in range(numSteps):
        f.moveDrunk(d)
        locs.append(f.getLoc(d))

    wLocs = f.getWormholesLocs()

    return locs, wLocs


