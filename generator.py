from random import random

from classes.graph import Graph
from evaluator import isConnected
from evaluator import efficiency

# Generates a set of random graphs with the specified parameters
# Input: number of nodes (int), number of edges (int), pool size (int), connectedness (boolean), weighted (boolean), directedness (boolean)
# Output: Graphs array
def generate(n, e, pool, needConnected, weighted, directed):
    graphs = []

    for i in range(pool):
        g = Graph(n, e, needConnected, weighted)
        randomizeEdge(g, directed)
        while needConnected and not isConnected(g.adj):
            g.resetEdges()
            randomizeEdge(g, directed)
        graphs.append(g)

    return graphs

# Randomize edges in a graph
# See https://stackoverflow.com/questions/48087/select-n-random-elements-from-a-listt-in-c-sharp/48089#48089
# Input: A graph, directedness (boolean)
# Output: N/A
def randomizeEdge(g, directed):
    eNeeded = g.e
    remaining = g.n ** 2 - g.n; # All possibilities except for main diagonal of adj matrix
    if not directed: # Cut the possibilities in half if undirected graph
        remaining /= 2

    for i in range(g.n ** 2): # Flatten adj matrix into 1D array
        if i % (g.n + 1) != 0: # Ignore elements on main diagonal
            r = i // g.n
            c = i % g.n

            if directed: # Directed graph
                if random() < eNeeded / remaining: # Normalize probability of adding edge
                    if g.weighted:
                        g.adj[r][c] = random()
                    else:
                        g.adj[r][c] = 1
                    eNeeded -= 1
                remaining -= 1
            else: # Undirected graph
                if r < c:
                    if random() < eNeeded / remaining: # Normalize probability of adding edge
                        if g.weighted:
                            g.adj[r][c] = random()
                        else:
                            g.adj[r][c] = 1
                        eNeeded -= 1
                    remaining -= 1
                else:
                    g.adj[r][c] = g.adj[c][r]
