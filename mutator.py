from random import randint
from classes.graph import Graph

# Mutates a pool of candidate graphs with their fitness score.
# Picks the best 2, reproduces them, and then mutate their children
# Input: Pool of parents, respective array of fitness scores
# Output: Pool of children (same size as parents)
def mutate(pool, fitness):
    # Indices for the best performing parents
    parent1 = 0
    parent2 = 1

    # Find the best two parents
    for i in range(2, len(fitness)):
        if fitness[i] > fitness[parent1]:
            parent2 = parent1
            parent1 = i
        elif fitness[i] > fitness[parent2]:
            parent2 = i

    # Reproduction
    children = crossover(pool[parent1], pool[parent2], len(pool) - 1) # Tweak this if adding best back

    # Mutation to revert to previous edge count
    for child in children:
        mutateEdge(child, pool[parent1].e)

    children.append(pool[parent1]) # Add the best parent back into children
    # children.append(pool[parent2]) # Add the second best parent back into children
    return children

# Asexually mutates a graph with respect to its edges. It checks if the graph has
# the correct number of edges and does mutations either to revert it to the correct
# number of edges, or just randomly moves edges around.
# Input: Adjacency matrix, correct number of edges
# Output: Nothing
def mutateEdge(g, edges):
    if (g.e == g.n ** 2 - g.n): # Complete graph
        return

    if (g.e > edges):
        while g.e != edges:
            removeEdge(g)
            g.e -= 1
    elif (g.e < edges):
        while g.e != edges:
            addEdge(g)
            g.e += 1
    else: # Edge count is correct, just do an edge swap for the mutation
        removeEdge(g)
        addEdge(g)

# Removes an edge from a graph
# Input: A graph
# Output: Nothing
def removeEdge(g):
    edge = randint(1, g.e) # Randomly chosen edge to remove
    removeCounter = 0 # Count up to the number "edge"

    for r in range(g.n):
        for c in range(g.n):
            if g.adj[r][c] > 0:
                removeCounter += 1

                if removeCounter == edge: # Remove the edge once we reach "edge"
                    g.adj[r][c] = 0
                    return

# Adds an edge to a graph
# Input: A graph
# Output: Nothing
def addEdge(g):
    empty = randint(1, g.n ** 2 - g.n - g.e) # Randomly chosen nonedge to add
    addCounter = 0 # Count up to the number "empty"

    for r in range(g.n):
        for c in range(g.n):
            if r != c and g.adj[r][c] == 0:
                addCounter += 1

                if addCounter == empty: # Add edge once we reach "empty"
                    g.adj[r][c] = 1
                    return

# Crossover sexual reproduction between 2 graphs. It randomly selects a subrectangle
# in g1 that will be replaced with g2's edges, and vise versa
# Input: Two graphs, number of children
# Output: n children graphs
def crossover(g1, g2, nChild):
    if g1.n != g2.n: # The dimensions of the graphs don't match
        raise AttributeError('Dimensions of graphs do not match')

    children = [None] * nChild
    base = None
    addendum = None

    for i in range(nChild):
        # Randomly pick which graph is the base to be added upon
        if (randint(0, 1) == 1):
            base = g1
            addendum = g2
        else:
            base = g2
            addendum = g1

        # Sub-rectangle dimensions
        left = randint(0, base.n - 2)
        right = randint(left + 1, base.n - 1)
        top = randint(0, base.n - 2)
        bottom = randint(top + 1, base.n - 1)

        children[i] = Graph(base.n, base.e, base.connected, base.weighted)
        childrenEdges = 0

        for r in range(base.n):
            for c in range(base.n):
                # If r, c indices not in the subrectangle
                if r < top or r > bottom or c < left or c > right:
                    children[i].adj[r][c] = base.adj[r][c]
                else:
                    children[i].adj[r][c] = addendum.adj[r][c]

                if children[i].adj[r][c] == 1:
                    childrenEdges += 1
        children[i].e = childrenEdges # Properly update the edge count

    return children
