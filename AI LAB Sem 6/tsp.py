#travelling salesman problem
n=0
minpath = []
graph = []
visited = []
mincost = 99999

def takeInput():
  global n, visited, graph
  n = int(input("Enter number of cities: "))
  visited = [False] * n
  for _ in range(n):
    graph.append(list(map(int, input().split())))

def tsp(city, count, currentcost, path):
  global n, mincost, minpath, visited, graph
  visited[city] = True
  path.append(city)
  if count == n-1 and graph[city][0] != 0:
    totalcost = currentcost + graph[city][0]
    if totalcost <= mincost:
      mincost = totalcost
      minpath[:] = path[:]
  else:
    for nextcity in range(n):
      if not visited[nextcity] and graph[city][nextcity] != 0:
        tsp(nextcity, count+1, currentcost + graph[city][nextcity], path)
  visited[city] = False
  path.pop()

takeInput()
tsp(0, 0, 0, [])
print(mincost)
print('->'.join(map(str, minpath + [minpath[0]])))