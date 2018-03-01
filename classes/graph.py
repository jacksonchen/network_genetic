class Graph:
    def __init__(self, n):
        self.n = n
        # Initialize adjacency matrix
        self.adj = [[0 for i in range(n)] for j in range(n)]
    def __str__(self):
        printStr = "   "
        for i in range(self.n):
            printStr += str(i) + ", "
        printStr += "\n"
        for i in range(self.n):
            printStr += str(i) + " " + str(self.adj[i]) + "\n"
        return printStr
