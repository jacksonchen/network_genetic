from queue import Queue

# def evaluate():

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
