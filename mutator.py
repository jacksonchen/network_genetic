from random import randint
from classes.graph import Graph

def mutate(g):
    mutateEdge(g)

# Asexually mutates a graph with respect to its edges. It randomly picks an edge,
# removes it, and then connect two previously non-adjacent vertices.
# Input: Adjacency matrix
# Output: Nothing
def mutateEdge(g):
    if (g.e == g.n ** 2 - g.n): # Complete graph
        return

    edge = randint(1, g.e) # Randomly chosen edge to remove
    empty = randint(1, g.n ** 2 - g.n - g.e) # Randomly chosen nonedge to add

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

# Crossover sexual reproduction between 2 graphs. It randomly selects a subrectangle
# in g1 that will be replaced with g2's edges, and vise versa
# Input: Two graphs
# Output: Two children graphs
def crossover(g1, g2):
    if g1.n != g2.n: # The dimensions of the graphs don't match
        return []

    # Sub-rectangle dimensions
    left = randint(0, g1.n - 2)
    right = randint(left + 1, g1.n - 1)
    top = randint(0, g1.n - 2)
    bottom = randint(top + 1, g1.n - 1)

    child1 = Graph(g1.n, g1.e, g1.connected, g1.weighted)
    child2 = Graph(g2.n, g2.e, g2.connected, g2.weighted)

    for r in range(g1.n):
        for c in range(g1.n):
            # If r, c indices not in the subrectangle
            if r < top or r > bottom or c < left or c > right:
                child1.adj[r][c] = g1.adj[r][c]
            else:
                child1.adj[r][c] = g2.adj[r][c]

    for r in range(g2.n):
        for c in range(g2.n):
            # If r, c indices not in the subrectangle
            if r < top or r > bottom or c < left or c > right:
                child2.adj[r][c] = g2.adj[r][c]
            else:
                child2.adj[r][c] = g1.adj[r][c]

    return [child1, child2]
