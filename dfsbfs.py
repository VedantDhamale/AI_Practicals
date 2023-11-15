visited=[]
def dfs(matrix,start):
    if start not in visited:
       visited.append(start)
       for i in range(len(matrix)):
          if(matrix[start][i]==1):
             dfs(matrix,i)

q=[]
v=[]
def bfs(matrix,start):
    if start not in v:
        if start not in q:
            q.append(start)
        for i in range(len(matrix)):
          if(matrix[start][i]==1 and i not in q and i not in v):
             q.append(i)
        v.append(q[0])
        q.pop(0)
    if(q):
        bfs(matrix,q[0])

      

n=int(input("Enter Number of Nodes : "))
M=[]
print("Enter Adjecency Matrix : ")
for i in range(n):
   entry=list(map(int,input().split()))
   M.append(entry)

dfs(M,0)
bfs(M,0)
print("DFS : ",visited)
print("BFS : ",v)

