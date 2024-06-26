#water jug
from collections import defaultdict

def waterJug(x, y):
  if visited[(x,y)]:
    return False
  visited[(x,y)] = True
  print(x, y)
  if x==aim or y==aim:
    return True
  return (waterJug(0, y) or
          waterJug(x, 0) or
          waterJug(jug1, y) or
          waterJug(x, jug2) or
          waterJug(x + min(y, jug1-x), y - min(y, jug1-x)) or
          waterJug(x - min(x, jug2-y), y + min(x, jug2-y)))
  
jug1 = 4
jug2 = 3
aim = 2
visited = defaultdict(bool)
waterJug(jug1, jug2)