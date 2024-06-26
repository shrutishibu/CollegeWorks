#connect four
import numpy as np
import random

board = np.zeros((6,7), dtype=int)

def mov(piece, col):
  for row in range(5, -1, -1):
    if board[row][col] == 0:
      board[row][col] = piece
      return

def isFull(col):
  if board[0][col] != 0:
    return True

def checkWin(piece):
  for c in range(4):
    for r in range(6):
      if all(board[r,c+i] == piece for i in range(4)):
        return True
  for r in range(3):
    for c in range(7):
      if all(board[r+i,c] == piece for i in range(4)):
        return True
  for r in range(3):
    for c in range(7):
      if all(board[r+i, c+i] == piece for i in range(4)):
        return True
    for r in range(3,6):
      for c in range(4):
        if all(board[r-i, c+i] == piece for i in range(4)):
          return True
    return False

def printBoard():
  print(np.flip(board,0))
  print("\n")

def getValidCol():
  while True:
    try:
      col = int(input("\nEnter column: ")) - 1
      if 0<=col<=6 and not isFull(col):
        return col
      else:
        print("Column is full")
    except ValueError:
      print("Invalid input")
  
print("\nPlayer: 2\nComputer: 1")
while True:
  printBoard()
  print("\nYour turn")
  col = getValidCol()
  mov(2, col)
  if checkWin(2):
    print("\nYou won")
    break
  print("\nComputer")
  col = random.choice([c for c in range(7) if not isFull(c)])
  mov(1, col)
  printBoard()
  if checkWin(1):
    print("\nComputer won")
    break
