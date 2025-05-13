"""Objects in Lecture 16"""

class Item:
    def __init__(self, n, v, w):
        self.name = n
        self.value = v
        self.weight = w
    
    def getName(self):
        return self.name

    def getValue(self):
        return self.value
    
    def getWeight(self):
        return self.weight
    
    def __str__(self):
        result = "<{}, {}, {}>".format(self.name, self.value, self.weight)
        return result


