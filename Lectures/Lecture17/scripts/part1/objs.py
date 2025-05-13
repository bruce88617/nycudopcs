"""
Objects for Lecture 17

Part I: Random Walk
"""


import random


class Location:
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def move(self, deltaX, deltaY):
        return Location(self.x+deltaX, self.y+deltaY)
    
    def getX(self):
        return self.x

    def getY(self):
        return self.y
    
    def distFrom(self, other):
        ox, oy = other.x, other.y
        xDist, yDist = self.x-ox, self.y-oy
        return (xDist**2 + yDist**2)**0.5
    
    def __str__(self):
        return "<{}, {}>".format(self.x, self.y)


class Field:
    def __init__(self):
        self.drunks = {}
    
    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError("Duplicate drunk")
        else:
            self.drunks[drunk] = loc
    
    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError("Drunk not in field")
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        self.drunks[drunk] = currentLocation.move(xDist, yDist)
    
    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError("Drunk not in field")
        return self.drunks[drunk]


class Drunk:
    def __init__(self, name=None):
        self.name = name
    
    def __str__(self):
        if self.name != None:
            return self.name
        return "Anonymous"


class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0,1), (0,-1), (1,0), (-1,0)]
        return random.choice(stepChoices)


class HeatAvoidDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.,1.), (0.,-2.), (1.,0.), (-1.,0.)]
        return random.choice(stepChoices)


class EastWardDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.,1.), (0.,-1.), (2.,0.)]
        return random.choice(stepChoices)


class MysteriousField(Field):
    def __init__(self,):
        super(MysteriousField, self).__init__()
        self.wormholes = {}

    def addWormholes(self, xLoc, yLoc, newX=None, newY=None, maxRange=20):
        if newX is None:
            newX = random.randint(-maxRange, maxRange)
        if newY is None:
            newY = random.randint(-maxRange, maxRange)
        self.wormholes[(xLoc, yLoc)] = Location(newX, newY)

    def moveDrunk(self, drunk):
        super(MysteriousField, self).moveDrunk(drunk)
        x = self.drunks[drunk].getX()
        y = self.drunks[drunk].getY()
        if (x, y) in self.wormholes:
            self.drunks[drunk] = self.wormholes[(x,y)]
    
    def getWormholesLocs(self):
        wLocs = []
        for k in self.wormholes.keys():
            wLocs.append((k[0], k[1], self.wormholes[k].getX(), self.wormholes[k].getY()))
        return wLocs


