import string

def formatBoard(board):
	board = [i for i in range(9, 0, -1)]
	for i in range(0, 9):
		board[i] = str(board[i])

	return board
#----------------------------------------------------------------------------------------------------------------------------
def replay():
	answer = input("Do you want to play again? (Type Y/N): ").upper()
	while answer not in ['Y', 'N']:
		print("Invalid input. Please try again")
		answer = input("Do you want to play again? (Type Y/N): ").upper()
	
	return answer == 'Y'
#----------------------------------------------------------------------------------------------------------------------------
def getPlayersShape():
	shape = input("Player 1, please select a shape (Type X/O): ").upper()
	while shape not in ['X', 'O']:
		print("Invalid input. Please try again")
		shape = input("Player 1, please select a shape (Type X/O): ").upper()

	return shape
#----------------------------------------------------------------------------------------------------------------------------
def resetBoard(board):
	board = [' '] * 9

	return board
#----------------------------------------------------------------------------------------------------------------------------
def isFreeCell(board, cell):
	return board[9 - cell] == ' '
#----------------------------------------------------------------------------------------------------------------------------
def printBoard(board):
	horizontal = ''.join(['- ' * 6])
	for i in range(2, 9, 3):
		print(''.join([' ', board[i], ' ', '|', ' ', board[i - 1], ' ', '|', ' ', board[i - 2], ' ']))
		if(i in [2, 5]):
			print(horizontal)
	print()
#----------------------------------------------------------------------------------------------------------------------------
def isGameOver(board, player1Turn):
	over = False
	if(verticalWin(board) or horizontalWin(board) or diagonalWin(board)):
		if(player1Turn):
			winner = '2'
		else:
			winner = '1'
		print(f"\nPlayer{winner} won! Congrats!\n")
		over = True
		
	elif(Tie(board)):
		print("\nIt's a tie!\n")
		over = True
	if(over):
		printBoard(board)

	return over

#----------------------------------------------------------------------------------------------------------------------------
def verticalWin(board):
	for i in [1, 2, 3]:
		if(board[i - 1] == board[i + 3 - 1] == board[i + 6 - 1] and board[i - 1] in ['X', 'O']):
			return True
	
	return False
#----------------------------------------------------------------------------------------------------------------------------
def horizontalWin(board):
	for i in [1, 4, 7]:
		if(board[i - 1] == board[i + 1 - 1] == board[i + 2 - 1] and board[i - 1] in ['X', 'O']):
			return True
	
	return False
#----------------------------------------------------------------------------------------------------------------------------
def diagonalWin(board):
	return ((board[1 - 1] == board[5 - 1] == board[9 - 1] or board[3 - 1] == board[5 - 1] == board[7 - 1]) and board[5 - 1] in ['X', 'O'])
#----------------------------------------------------------------------------------------------------------------------------
def Tie(board):
	return (' ' not in board)
#----------------------------------------------------------------------------------------------------------------------------


#Driver Code
player1Shape = player2Shape  = None
firstPlay = player1Turn = True
board = None
while(firstPlay or replay()):
	player1Shape = getPlayersShape()
	if(player1Shape == 'X'):
		player2Shape = 'O'
	else:
		player2Shape = 'X'
	board = formatBoard(board)
	print("Board format:")
	printBoard(board)
	board = resetBoard(board)
	
	while not isGameOver(board, player1Turn):
		printBoard(board)
		cell = input("Choose cell number: ")
		while (not cell.isdigit() or int(cell) not in range(1, 10) or not isFreeCell(board, int(cell))):
			if(not cell.isdigit() or int(cell) not in range(1, 10)):
				print("Invalid input!")
			else:
				print("Occupied cell. Please try again.")
			cell = input("Choose cell number: ")
		cell = int(cell)
		if(player1Turn):
			ch = player1Shape
		else:
			ch = player2Shape
		board[9 - cell] = ch
		player1Turn = not player1Turn
	
	if(firstPlay):
		firstPlay = False