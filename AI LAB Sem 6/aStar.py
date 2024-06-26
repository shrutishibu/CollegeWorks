#aStar
def aStar(graph, start, stop, heuristics):
  openSet = {start}
  closedSet = set()
  parents = {start: start}
  g = {start: 0}
  while openSet: 
    n = min(openSet, key = lambda v: g[v] + heuristics[v])
    if n == stop:
      path = []
      while parents[n] != n:
        path.append(n)
        n = parents[n]
      path.append(start)
      path.reverse()
      return path
    openSet.remove(n)
    closedSet.add(n)
    for m, weight in graph.get(n, []):
      if m in closedSet: 
        continue
      tentativeG = g[n] + weight
      if m not in openSet:
        openSet.add(m)
      elif tentativeG >= g[m]:
        continue
      parents[m] = n
      g[m] = tentativeG
  return None

graph = eval(input("\nEnter graph: "))
for key, value in graph.items():
  print(f"{key} : {value}")
heuristics = eval(input("Enter heuristics as key-value pairs"))
start = input("Enter start node: ")
stop = input("Enter goal node: ")
path = aStar(graph, start, stop, heuristics)
if path: 
  print(f"Path: {path}")
else:
  print("\nNo solution")
#{'A': 11, 'B': 6, 'C': 99, 'D': 1, 'E': 7, 'G': 0}
#{'A': [('B', 2), ('E', 3)], 'B': [('A', 2), ('C', 1), ('G', 9)], 'C': [('B', 1)], 'D': [('E', 6), ('G', 1)], 'E': [('A', 3), ('D', 6)], 'G': [('B', 9), ('D', 1)]}