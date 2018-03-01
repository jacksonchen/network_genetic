from queue import Queue
from functools import reduce

# Calculates G, or the survival fitness function, for a given graph g
# Input: A graph
# Output: A fitness score
def evaluate(g):
    normEff = 0
    return normEff

# Calculates the efficiency of the graph by analyzing distances between every pair of
# nodes. This uses the Floyd Warshall algorithm
# Input: A graph
# Output: The efficiency value
def efficiency(g):
    # Find the distance for every pair of nodes
    dist = [[0 for c in range(g.n)] for r in range(g.n)]
    INF = 999

    for r in range(g.n):
        for c in range(g.n):
            dist[r][c] = g.adj[r][c]
            if r != c and g.adj[r][c] == 0: # No edge exists between r and c
                dist[r][c] = INF

    for k in range(g.n):
        for i in range(g.n):
            for j in range(g.n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # Calculation for average APSP for the given graph
    APSP = 0
    for r in dist:
        APSP += reduce(lambda x, y: x + y, r)
    APSP /= g.n * (g.n - 1)

    # APSP for a star
    starAPSP = 2 * (1 - 1 / g.n)

    return starAPSP / APSP
def robustness(g):
    return 0

def cost(g):
    return 0

# Check if a graph is connected. Uses Kosaraju algorithm for BFS.
# Input: Adjacency matrix
# Output: Boolean
def isConnected(adj):
    if len(adj) == 0:
        return True

    if not bfs(adj):
        return False

    # Transpose adjacency matrix
    transposeAdj = [[adj[j][i] for j in range(len(adj))] for i in range(len(adj[0]))]
    return bfs(transposeAdj)


# Breadth first search that always starts with node 0
# Input: Adjacency matrix
# Output: Boolean for if it visited every node from 0 via BFS
def bfs(adj):
    if len(adj) == 0:
        return true

    explored = [0] * len(adj)
    q = Queue(len(adj) ** 2)
    q.put_nowait(0)

    while not q.empty():
        n = q.get_nowait() # Visit node
        if explored[n] == 0:
            explored[n] = 1
            # Find neighbors
            for neighbor in range(len(adj[n])):
                if adj[n][neighbor] > 0:
                    q.put(neighbor)

    for nodeState in explored:
        if nodeState == 0:
            return False
    return True
