import random

from classes.graph import Graph
from evaluator import isConnected

# Randomize edges in a graph
# Input: Adjacency Matrix
# Output: N/A
def randomizeEdge(adj):
    if len(adj) > 0 and len(adj[0]) > 0: # Check if graph
        for r in range(len(adj)):
            for c in range(len(adj[0])):
                if r != c:
                    adj[r][c] = random.randint(0, 1)

# Generates a set of random graphs with the specified parameters
# Input: number of nodes (int), pool size (int), connectedness (boolean)
# Output: Graphs array
def generate(n, pool, needConnected):
    graphs = []

    for i in range(pool):
        g = Graph(n)
        randomizeEdge(g.adj)
        while needConnected and not isConnected(g.adj):
            randomizeEdge(g.adj)
        graphs.append(g)
    return graphs
