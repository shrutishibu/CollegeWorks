#8 queens problem
N = int(input("\nEnter number of queens: "))
board = [[0]*N for _ in range(N)]

def isSafe(row, col):
  for i in range(col):
    if board[row][i] == 1:
      return False
  for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
    if board[i][j] == 1:
      return False
  for i, j in zip(range(row, N), range(col, -1, -1)):
    if board[i][j] == 1:
      return False
  return True

def solveQueens(col):
  if col >= N:
    return True
  for i in range(N):
    if isSafe(i, col):
      board[i][col] = 1
      if solveQueens(col+1):
        return True
      board[i][col] = 0
  return False

if solveQueens(0):
  for row in board:
    print(row)
else:
  print("No solution!")