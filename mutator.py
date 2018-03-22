from random import randint
from classes.graph import Graph

# Mutates a pool of candidate graphs with their fitness score.
# Picks the best 2, reproduces them, and then mutate their children
# Input: Pool of parents, respective array of fitness scores, directedness (boolean)
# Output: Pool of children (same size as parents)
def mutate(pool, fitness, directed):
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
    children = crossover(pool[parent1], pool[parent2], len(pool) - 1, directed) # Tweak this if adding best back

    # Mutation to revert to previous edge count
    for child in children:
        mutateEdge(child, pool[parent1].e, directed)

    children.append(pool[parent1]) # Add the best parent back into children
    # children.append(pool[parent2]) # Add the second best parent back into children
    return children

# Asexually mutates a graph with respect to its edges. It checks if the graph has
# the correct number of edges and does mutations either to revert it to the correct
# number of edges, or just randomly moves edges around.
# Input: Adjacency matrix, correct number of edges, directedness (boolean)
# Output: Nothing
def mutateEdge(g, edges, directed):
    if (g.e == g.n ** 2 - g.n): # Complete graph
        return

    if (g.e > edges):
        while g.e != edges:
            removeEdge(g, directed)
            g.e -= 1
    elif (g.e < edges):
        while g.e != edges:
            addEdge(g, directed)
            g.e += 1
    else: # Edge count is correct, just do an edge swap for the mutation
        removeEdge(g, directed)
        addEdge(g, directed)

# Removes an edge from a graph
# Input: A graph, directedness
# Output: Nothing
def removeEdge(g, directed):
    edge = randint(1, g.e) # Randomly chosen edge to remove
    removeCounter = 0 # Count up to the number "edge"

    for r in range(g.n):
        for c in range(g.n):
            if directed and g.adj[r][c] > 0:
                removeCounter += 1

                if removeCounter == edge: # Remove the edge once we reach "edge"
                    g.adj[r][c] = 0
                    return
            elif not directed and r < c and g.adj[r][c] > 0:
                removeCounter += 1

                if removeCounter == edge: # Remove the edge once we reach "edge"
                    g.adj[r][c] = 0
                    g.adj[c][r] = 0
                    return


# Adds an edge to a graph
# Input: A graph, directedness
# Output: Nothing
def addEdge(g, directed):
    empty = randint(1, g.n ** 2 - g.n - g.e) # Randomly chosen nonedge to add
    addCounter = 0 # Count up to the number "empty"

    for r in range(g.n):
        for c in range(g.n):
            if directed and r != c and g.adj[r][c] == 0:
                addCounter += 1

                if addCounter == empty: # Add edge once we reach "empty"
                    g.adj[r][c] = 1
                    return
            elif not directed and r < c and g.adj[r][c] == 0:
                addCounter += 1

                if addCounter == empty: # Add edge once we reach "empty"
                    g.adj[r][c] = 1
                    g.adj[c][r] = 1
                    return

# Generating unbiased sub-rectangle dimensions
def generateRectangle(n):
    col1 = randint(0, n - 1)
    col2 = randint(0, n - 1)
    while col1 == col2: # Make sure col2 does not equal col1
        col2 = randint(0, n - 1)
    left = min(col1, col2)
    right = max(col1, col2)

    row1 = randint(0, n - 1)
    row2 = randint(0, n - 1)
    while row1 == row2: # Make sure row2 does not equal row1
        row2 = randint(0, n - 1)
    top = min(col1, col2)
    bottom = max(col1, col2)

    return {
        'left': left,
        'right': right,
        'top': top,
        'bottom': bottom,
    }

# Crossover sexual reproduction between 2 graphs. It randomly selects a subrectangle
# in g1 that will be replaced with g2's edges, and vise versa
# Input: Two graphs, number of children, directedness (boolean)
# Output: n children graphs
def crossover(g1, g2, nChild, directed):
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

        children[i] = Graph(base.n, base.e, base.connected, base.weighted)
        childrenEdges = 0
        rect = generateRectangle(base.n)

        if directed: # Directed graph
            for r in range(base.n):
                for c in range(base.n):
                    # If r, c indices not in the subrectangle
                    if r < rect['top'] or r > rect['bottom'] or c < rect['left'] or c > rect['right']:
                        children[i].adj[r][c] = base.adj[r][c]
                    else:
                        children[i].adj[r][c] = addendum.adj[r][c]

                    if children[i].adj[r][c] == 1:
                        childrenEdges += 1
            children[i].e = childrenEdges # Properly update the edge count
        else: # Undirected graph
            while (rect['bottom'] < rect['right'] and rect['top'] < rect['left']):
                rect = generateRectangle(base.n)

            for r in range(base.n):
                for c in range(base.n):
                    if c < r:
                        children[i].adj[r][c] = base.adj[c][r]
                    elif c > r:
                        # If r, c indices not in the subrectangle
                        if r < rect['top'] or r > rect['bottom'] or c < rect['left'] or c > rect['right']:
                            children[i].adj[r][c] = base.adj[r][c]
                        else:
                            children[i].adj[r][c] = addendum.adj[r][c]

                        if children[i].adj[r][c] == 1:
                            childrenEdges += 1
            children[i].e = childrenEdges # Properly update the edge count


    return children
