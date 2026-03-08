import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
A = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
count = 0

def dfs(v):
  visited[v] = True
  
  for i in range(len(A[v])):
    if not visited[A[v][i]]:
      dfs(A[v][i])
    
for _ in range(m):
  n1, n2 = map(int, input().split())
  A[n1].append(n2)
  A[n2].append(n1)

for i in range(1, n + 1):
  if not visited[i]:
    dfs(i)
    count += 1

print(count)