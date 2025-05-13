"""Utility Functions for Lecture 16"""


from scripts.part2.objs import Node, Edge, WeightedEdge, Digraph, Graph


def printPath(path):
    result = ""
    for i in range(len(path)):
        result += str(path[i])
        if i != len(path)-1:
            result += "->"
    return result


def shortestPath(paths, graph):
    shortest = None
    minLength = None
    for path in paths:
        pathLength = 0
        for i in range(len(path)-1):
            src = path[i]
            dest = path[i+1]
            pathLength += src.getCost()
            pathLength += graph.getWeight(src, dest)
            if dest == path[-1]:
                pathLength += dest.getCost()
        
        if minLength==None or pathLength<minLength:
            shortest = path
            minLength = pathLength

    return shortest, minLength


def buildGraph1():
    nodes = []
    g = Digraph()

    for name in range(6):
        nodes.append(Node(str(name)))

    for n in nodes:
        g.addNode(n)

    g.addEdge(Edge(nodes[0], nodes[1]))
    g.addEdge(Edge(nodes[1], nodes[2]))
    g.addEdge(Edge(nodes[2], nodes[3]))
    g.addEdge(Edge(nodes[2], nodes[4]))
    g.addEdge(Edge(nodes[3], nodes[4]))
    g.addEdge(Edge(nodes[3], nodes[5]))
    g.addEdge(Edge(nodes[0], nodes[2]))
    g.addEdge(Edge(nodes[1], nodes[0]))
    g.addEdge(Edge(nodes[3], nodes[1]))
    g.addEdge(Edge(nodes[4], nodes[0]))

    return g


def buildGraph2():
    nodes = []
    names = ["A", "B", "C", "D", "E", "F", "G", "H"]
    g = Digraph()

    for i in range(len(names)):
        nodes.append(Node(str(names[i])))

    for n in nodes:
        g.addNode(n)

    g.addEdge(Edge(nodes[0], nodes[1]))
    g.addEdge(Edge(nodes[0], nodes[4]))
    g.addEdge(Edge(nodes[0], nodes[6]))
    g.addEdge(Edge(nodes[1], nodes[2]))
    g.addEdge(Edge(nodes[1], nodes[3]))
    g.addEdge(Edge(nodes[1], nodes[4]))
    g.addEdge(Edge(nodes[2], nodes[7]))
    g.addEdge(Edge(nodes[3], nodes[2]))
    g.addEdge(Edge(nodes[3], nodes[7]))
    g.addEdge(Edge(nodes[4], nodes[3]))
    g.addEdge(Edge(nodes[4], nodes[5]))
    g.addEdge(Edge(nodes[5], nodes[3]))
    g.addEdge(Edge(nodes[5], nodes[7]))
    g.addEdge(Edge(nodes[6], nodes[4]))
    g.addEdge(Edge(nodes[6], nodes[5]))
    g.addEdge(Edge(nodes[6], nodes[7]))

    return g


def buildGraph3():
    nodes = []
    names = ["A", "B", "C", "D", "E", "F", "G", "H"]
    times = [0, 5, 17, 14, 8, 13, 9, 7]
    g = Digraph()

    for i in range(len(names)):
        nodes.append(Node(str(names[i]), times[i]))

    for n in nodes:
        g.addNode(n)

    g.addEdge(WeightedEdge(nodes[0], nodes[1], 5))
    g.addEdge(WeightedEdge(nodes[0], nodes[4], 18))
    g.addEdge(WeightedEdge(nodes[0], nodes[6], 49))
    g.addEdge(WeightedEdge(nodes[1], nodes[2], 15))
    g.addEdge(WeightedEdge(nodes[1], nodes[3], 12))
    g.addEdge(WeightedEdge(nodes[1], nodes[4], 4))
    g.addEdge(WeightedEdge(nodes[2], nodes[7], 9))
    g.addEdge(WeightedEdge(nodes[3], nodes[2], 87))
    g.addEdge(WeightedEdge(nodes[3], nodes[7], 11))
    g.addEdge(WeightedEdge(nodes[4], nodes[3], 17))
    g.addEdge(WeightedEdge(nodes[4], nodes[5], 56))
    g.addEdge(WeightedEdge(nodes[5], nodes[3], 1))
    g.addEdge(WeightedEdge(nodes[5], nodes[7], 13))
    g.addEdge(WeightedEdge(nodes[6], nodes[4], 5))
    g.addEdge(WeightedEdge(nodes[6], nodes[5], 4))
    g.addEdge(WeightedEdge(nodes[6], nodes[7], 20))

    return g


def buildGraph4():
    nodes = []
    names = ["A", "B", "C", "D", "E", "F", "G", "H"]
    times = [0, 5, 17, 14, 8, 13, 9, 7]
    g = Graph()

    for i in range(len(names)):
        nodes.append(Node(str(names[i]), times[i]))

    for n in nodes:
        g.addNode(n)

    g.addEdge(WeightedEdge(nodes[0], nodes[1], 5))
    g.addEdge(WeightedEdge(nodes[0], nodes[4], 18))
    g.addEdge(WeightedEdge(nodes[0], nodes[6], 49))
    g.addEdge(WeightedEdge(nodes[1], nodes[2], 15))
    g.addEdge(WeightedEdge(nodes[1], nodes[3], 12))
    g.addEdge(WeightedEdge(nodes[1], nodes[4], 4))
    g.addEdge(WeightedEdge(nodes[2], nodes[7], 9))
    g.addEdge(WeightedEdge(nodes[3], nodes[2], 87))
    g.addEdge(WeightedEdge(nodes[3], nodes[7], 11))
    g.addEdge(WeightedEdge(nodes[4], nodes[3], 17))
    g.addEdge(WeightedEdge(nodes[4], nodes[5], 56))
    g.addEdge(WeightedEdge(nodes[5], nodes[3], 1))
    g.addEdge(WeightedEdge(nodes[5], nodes[7], 13))
    g.addEdge(WeightedEdge(nodes[6], nodes[4], 5))
    g.addEdge(WeightedEdge(nodes[6], nodes[5], 4))
    g.addEdge(WeightedEdge(nodes[6], nodes[7], 20))

    return g

