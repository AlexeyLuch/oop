from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print (" ".join(row))

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

def random_row_coal(board):
  return randint(0, len(board[1]) - 1)


ship_row = random_row(board)
ship_col = random_col(board)
ship_rec = random_row_coal(board)
print(ship_row)
print(ship_col)
print(ship_rec)
for turn in range(4):
  guess_row_coal = int(input("Guess Row_Col: "))
  guess_row = int(input("Guess Row: "))
  guess_col = int(input("Guess Col: "))

  if guess_row > 5 or guess_col > 5 or guess_row_coal > 5:
    print("must be less than equal to 5 ")


  if guess_row == ship_row and guess_col == ship_col and guess_row_coal== ship_rec:
    print ("Congratulations! You sank my battleship!")
    break
  else:
    if guess_row not in range(5) or guess_col not in range(5) or guess_row_coal not in range(5):
      print ()
    elif board[guess_row][guess_col]== "X":
      print("You guessed that one already.")
    else:
      print ("You missed my battleship!")
      board[guess_row][guess_col]= "X"
    print_board(board)
    if turn == 3:
      print("Game Over")
      break
    print("Turn", turn + 1)
