#tic tac toe
board = [' '] * 10
player = 1
running, draw, win = 0, -1, 1
game = running

def drawBoard():
  print("\n".join([
      f"{board[1]} | {board[2]} | {board[3]}",
      "---------",
      f"{board[4]} | {board[5]} | {board[6]}",
      "---------",
      f"{board[7]} | {board[8]} | {board[9]}",
      "---------",
  ]))

def checkWin():
  wins = [(1,2,3), 
          (4,5,6),
          (7,8,9),
          (1,4,7),
          (2,5,8),
          (3,6,9),
          (1,5,9),
          (3,5,7)]
  for a,b,c in wins:
    if board[a] == board[b] == board[c] != ' ':
      return win
  return draw if ' ' not in board[1: ] else running

drawBoard()

while game==running:
  choice = int(input(f"\nPlayer {player}'s chance: "))
  if choice>9 or choice<1:
    print("\nInvalid")
    continue;
  if board[choice] == ' ':
    board[choice] = 'X' if player == 1 else 'O'
    player = 1 if player==2 else 2
    game = checkWin()
    drawBoard()
  else:
    print("Occupied")

if game==draw:
  print("Draw")
else:
  print(f"Player {1 if player==2 else 2} won")