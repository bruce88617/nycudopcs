from scripts.part2.utils import buildGraph1, buildGraph2, buildGraph3, buildGraph4, shortestPath, printPath
from scripts.part2.search import DFS, BFS


def test1():
    """Find the shortest path from node 0 to node 5 in the graph 1 by BFS"""
    g = buildGraph1()
    start = g.getNode(0)
    end = g.getNode(5)
    found = BFS(g, start, end, toPrint=True)
    shortest, minLength = shortestPath(found, g)
    print("Result of BFS:\n", [printPath(path) for path in found])
    print("Shortest path:\n {}, path length = {}".format(printPath(shortest), minLength))


def test2(start_idx=0, end_idx=-1):
    """Find the shortest path in the graph 2 by BFS"""
    g = buildGraph2()

    if (start_idx > len(g.getAllNodes())-1) or (end_idx > len(g.getAllNodes())-1):
        raise ValueError(
            "No such node index. " + \
            "Available node index: [0, {:d}]".format(len(g.getAllNodes())-1)
        )
    
    start = g.getNode(node_idx=start_idx)
    end = g.getNode(node_idx=end_idx)

    found = BFS(g, start, end, toPrint=True)
    shortest, minLength = shortestPath(found, g)
    print("Result of BFS:\n", [printPath(path) for path in found])
    print("Shortest path:\n {}, path length = {}".format(printPath(shortest), minLength))


def test3():
    """Find the shortest path from node 0 to node 5 in the graph 1 by DFS"""
    g = buildGraph1()
    start = g.getNode(0)
    end = g.getNode(5)
    found = DFS(g, start, end, [], toPrint=False)
    shortest, minLength = shortestPath(found, g)
    print("Result of DFS:\n", [printPath(path) for path in found])
    print("Shortest path:\n {}, path length = {}".format(printPath(shortest), minLength))


def test4(start_idx=0, end_idx=-1):
    """Find the shortest path in the graph 2 by DFS"""
    g = buildGraph2()

    if (start_idx > len(g.getAllNodes())-1) or (end_idx > len(g.getAllNodes())-1):
        raise ValueError(
            "No such node index. " + \
            "Available node index: [0, {:d}]".format(len(g.getAllNodes())-1)
        )
    
    start = g.getNode(node_idx=start_idx)
    end = g.getNode(node_idx=end_idx)

    found = DFS(g, start, end, [], toPrint=True)
    shortest, minLength = shortestPath(found, g)
    print("Result of DFS:\n", [printPath(path) for path in found])
    print("Shortest path:\n {}, path length = {}".format(printPath(shortest), minLength))


def test5(start_idx=0, end_idx=-1):
    """Find the shortest path in the graph 3 by BFS"""
    g = buildGraph3()

    if (start_idx > len(g.getAllNodes())-1) or (end_idx > len(g.getAllNodes())-1):
        raise ValueError(
            "No such node index. " + \
            "Available node index: [0, {:d}]".format(len(g.getAllNodes())-1)
        )

    start = g.getNode(node_idx=start_idx)
    end = g.getNode(node_idx=end_idx)

    found = BFS(g, start, end, toPrint=True)
    shortest, minLength = shortestPath(found, g)
    print("Result of BFS:\n", [printPath(path) for path in found])
    print("Shortest path:\n {}, path length = {}".format(printPath(shortest), minLength))


def test6(start_idx=0, end_idx=-1):
    """Find the shortest path in the graph 3 by DFS"""
    g = buildGraph3()

    if (start_idx > len(g.getAllNodes())-1) or (end_idx > len(g.getAllNodes())-1):
        raise ValueError(
            "No such node index. " + \
            "Available node index: [0, {:d}]".format(len(g.getAllNodes())-1)
        )

    start = g.getNode(node_idx=start_idx)
    end = g.getNode(node_idx=end_idx)

    found = DFS(g, start, end, [], toPrint=True)
    shortest, minLength = shortestPath(found, g)
    print("Result of DFS:\n", [printPath(path) for path in found])
    print("Shortest path:\n {}, path length = {}".format(printPath(shortest), minLength))


def test7(start_idx=0, end_idx=-1):
    """Find the shortest path in the graph 4 by BFS"""
    g = buildGraph4()

    if (start_idx > len(g.getAllNodes())-1) or (end_idx > len(g.getAllNodes())-1):
        raise ValueError(
            "No such node index. " + \
            "Available node index: [0, {:d}]".format(len(g.getAllNodes())-1)
        )

    start = g.getNode(node_idx=start_idx)
    end = g.getNode(node_idx=end_idx)

    found = BFS(g, start, end, toPrint=True)
    shortest, minLength = shortestPath(found, g)
    print("Result of BFS:\n", [printPath(path) for path in found])
    print("Shortest path:\n {}, path length = {}".format(printPath(shortest), minLength))


def test8(start_idx=0, end_idx=-1):
    """Find the shortest path in the graph 4 by DFS"""
    g = buildGraph4()

    if (start_idx > len(g.getAllNodes())-1) or (end_idx > len(g.getAllNodes())-1):
        raise ValueError(
            "No such node index. " + \
            "Available node index: [0, {:d}]".format(len(g.getAllNodes())-1)
        )

    start = g.getNode(node_idx=start_idx)
    end = g.getNode(node_idx=end_idx)

    found = DFS(g, start, end, [], toPrint=True)
    shortest, minLength = shortestPath(found, g)
    print("Result of DFS:\n", [printPath(path) for path in found])
    print("Shortest path:\n {}, path length = {}".format(printPath(shortest), minLength))


