import random

def mutate(g):
    mutateEdge(g)

# Moves an edge to two previously non-adjacent vertices
# Input: Adjacency matrix
# Output: Nothing
def mutateEdge(g):
    if (g.e == g.n ** 2 - g.n): # Complete graph
        return

    edge = random.randint(1, g.e) # Randomly chosen edge to remove
    empty = random.randint(1, g.n ** 2 - g.n - g.e) # Randomly chosen nonedge to add

    removeCounter = 0
    removeIndices = []
    addCounter = 0
    addIndices = []

    for r in range(g.n):
        for c in range(g.n):
            if g.adj[r][c] > 0:
                removeCounter += 1
            elif r != c:
                addCounter += 1

            # Remove the edge
            if removeCounter == edge:
                removeIndices = [r, c]
                removeCounter += 1
                if len(addIndices) > 0: break

            if addCounter == empty:
                addIndices = [r, c]
                addCounter += 1
                if len(removeIndices) > 0: break

    g.adj[addIndices[0]][addIndices[1]] = g.adj[removeIndices[0]][removeIndices[1]]
    g.adj[removeIndices[0]][removeIndices[1]] = 0

def crossover(g):
    return
