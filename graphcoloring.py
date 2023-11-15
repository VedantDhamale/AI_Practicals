class graph:
    def __init__(self, maxcol, matrix):
        self.maxcol = maxcol
        self.matrix = matrix
        self.colors = []
        for i in range(len(matrix)):
            self.colors.append(None)

    def graphcoloring(self):
        for i in range(len(self.matrix)):
            flag = 0
            for col in range(self.maxcol):
                if (self.check(i, col) == True):
                    self.colors[i] = col
                    flag = 1
            if (flag == 0):
                print("connect find the solution")
                return
        self.print()

    def check(self, i, col):
        for k in range(len(self.matrix)):
            if (self.matrix[i][k] == 1):
                if (self.colors[k] == col):
                    return False
        return True

    def print(self):
        for i in range(len(self.colors)):
            print("Node %d has %d color " % (i, self.colors[i]))


n = int(input("Enter the total nodes : "))
matrix = []
print("Enter the adjacency matrix : ")
for i in range(n):
    entry = list(map(int, input().split()))
    matrix.append(entry)

maxcol = int(input("Enter the total colors :"))
g = graph(maxcol, matrix)
g.graphcoloring()
