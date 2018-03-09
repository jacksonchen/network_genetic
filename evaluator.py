from queue import Queue
from functools import reduce

# Calculates G, or the survival fitness function, for a given graph g
# Input: A graph
# Output: A fitness score
def evaluate(g):
    normEff = efficiency(g)
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

    # Floyd Warshall
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

# Calculates the structural and functional robustness of a graph
# Input: A graph
# Output: The robustness value
def robustness(g):
    strucR = [0] * g.n # Structural robustness with respect to each node
    for j in range(g.n):
        modifiedAdj = []

        for r in len(g.n):
            if r != j:
                tmpArr = []
                for c in len(g.n):
                    if c != j:
                        tmpArr.push(g.adj[r][c])
                modifiedAdj.push(tmpArr)
        strucR[j] = structuralRobustness(modifiedAdj) / (g.n - 2)

    funcR = [0] * g.n # Functional robustness
    return min(strucR)

# Calculates the effective accessibility of a graph.
# It does this by computing two DFS using Kosaraju's algorithm
# Input: An adjacency matrix
# Output: The effective accessibility of the graph
def structuralRobustness(adj):
    visited = [False] * len(adj)
    stack = []
    accessibility = 0

    for i in range(len(adj)):
        if visited[i] == False:
            dfsStackRecurse(adj, i, visited, stack)

    # Transpose adjacency matrix
    transposeAdj = [[adj[j][i] for j in range(len(adj))] for i in range(len(adj[0]))]

    visited = [False] * len(adj)
    while len(stack) > 0:
        i = stack.pop()
        if visited[i] == False:
            accessibility += dfsSCCRecurse(adj, i, visited) - 1
    return accessibility

# Runs a DFS of the graph and populates a stack with deepest nodes first
# Input: Adjacency matrix, node, boolean array of visited values, stack
# Output: Nothing
def dfsStackRecurse(adj, i, visited, stack):
    visited[i] = True
    for j in range(len(adj[i])):
        if adj[i][j] == 1 and visited[j] == False:
            dfsStackRecurse(adj, j, visited, stack)
    stack = stack.append(i)

# Runs a DFS on a graph and sums up the number of nodes of the strongly
# connected component (SCC) that contains node i
# Input: Adjacency matrix, node, boolean array of visited values
# Output: Node count in the respective SCC (int)
def dfsSCCRecurse(adj, i, visited):
    visited[i] = True
    components = 1
    for j in range(len(adj[i])):
        if adj[i][j] == 1 and visited[j] == False:
            components += dfsSCCRecurse(adj, j, visited)
    return components

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
