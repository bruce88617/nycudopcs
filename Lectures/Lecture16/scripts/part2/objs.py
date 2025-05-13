"""Objects for Lecture 16"""

class Node:
    def __init__(self, name, wait=0):
        self.name = name
        self.costTime = wait
    
    def getName(self):
        return self.name
    
    def getCost(self):
        return self.costTime
    
    def __str__(self):
        return self.name

class Edge:
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    
    def getSource(self):
        return self.src
    
    def getDestination(self):
        return self.dest
    
    def __str__(self):
        return "{} -> {}".format(self.src, self.dest)

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight=1):
        super(WeightedEdge, self).__init__(src, dest)
        self.weight = weight
    
    def getWeight(self):
        return self.weight
    
    def __str__(self):
        return "{} -({})-> {}".format(self.src, self.weight, self.dest)

class Digraph:
    def __init__(self):
        self.nodes = []
        self.edges = {}
        self.weights = {}

    
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError("Node already exists, idiot")
        else:
            self.nodes.append(node)
            self.edges[node] = []
            self.weights[node] = {}

    
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.nodes and dest in self.nodes):
            raise ValueError("Node is not in graph, idiot")
        self.edges[src].append(dest)
        if edge.__class__.__name__ == "WeightedEdge":
            wt = edge.getWeight()
            self.weights[src][dest] = wt
        else:
            self.weights[src][dest] = 1

    
    def childrenOf(self, node):
        return self.edges[node]
    
    
    def hasNode(self, node):
        return node in self.nodes
    
    
    def getNode(self, node_idx):
        if not self.nodes[node_idx] in self.nodes:
            raise ValueError("Node is not in graph, idiot")
        return self.nodes[node_idx]
    

    def getWeight(self, src, dest):
        return self.weights[src][dest]
    

    def getAllNodes(self,):
        return self.nodes
    
    
    def __str__(self):
        result = ""
        for src in self.nodes:
            for dest in self.edges[src]:
                result += "{} -> {}\n".format(src.getName(), dest.getName())
        return result[:-1]
    


class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)

