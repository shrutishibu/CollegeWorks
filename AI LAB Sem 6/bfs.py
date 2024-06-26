#bfs
from collections import deque
def bfs(start):
  visited[start] = 1
  queue = deque([start])
  while queue:
    node = queue.popleft()
    print(node, end=" ")
    for i in range(n):
      if graph[node][i] == 1 and not visited[i]:
        queue.append(i)
        visited[i] = 1

def takeInput():
  for i in range(n):
    graph[i] = list(map(int, input().split()))

n = int(input("Enter number of nodes: "))
graph = [[0] * n for _ in range(n)]
takeInput()
start = int(input("Enter start node: "))
visited = [0] * n
print("Path: ")
bfs(start)
