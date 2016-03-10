A = ["Q1","Q1","Q2","Q2","Q3","Q3"]
B = ["X1","X1","X2","X2","X3","X3"]



def choosePiece(X):
	print "Choose a piece from: "
	print X
	piece = raw_input()
	return piece


def placePiece(board, piece, cell):
	board[cell] = piece


def deletePiece(X, piece):
	for i, elem in enumerate(X):
		if X[i] == piece:
			X[i] = ' '
			break


def isSpaceFree(board, cell):

	# Return true if the passed move is free on the passed board.
	return board[cell] == ' '


def chooseCell(board):

	# Let the player type in their move.
	cell = ' '
	#while cell not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(cell)):
	print('Choose a free cell (1-9)')
	cell = input()
	return int(cell)



def drawBoard(board):

	# This function prints out the board that it was passed.
	# "board" is a list of 10 strings representing the board (ignore index 0)

	print('   |   |')
	print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
	print('   |   |')

#return true if player has won
def isWinner(bo, x1, x2, x3):
	return (((bo[1] == x1 or bo[1] == x2 or bo[1] == x3) and (bo[2] == x1 or bo[2] == x2 or bo[2] == x3) and (bo[3] == x1 or bo[3] == x2 or bo[3] == x3)) or # across the top
	((bo[4] == x1 or bo[4] == x2 or bo[4] == x3) and (bo[5] == x1 or bo[5] == x2 or bo[5] == x3) and (bo[6] == x1 or bo[6] == x2 or bo[6] == x3)) or # across the middle
	((bo[7] == x1 or bo[7] == x2 or bo[7] == x3) and (bo[8] == x1 or bo[8] == x2 or bo[8] == x3) and (bo[9] == x1 or bo[9] == x2 or bo[9] == x3)) or # across the bottom
	((bo[1] == x1 or bo[1] == x2 or bo[1] == x3) and (bo[4] == x1 or bo[4] == x2 or bo[4] == x3) and (bo[7] == x1 or bo[7] == x2 or bo[7] == x3)) or # down left side
	((bo[2] == x1 or bo[2] == x2 or bo[2] == x3) and (bo[5] == x1 or bo[5] == x2 or bo[5] == x3) and (bo[8] == x1 or bo[8] == x2 or bo[8] == x3)) or # down middle
	((bo[3] == x1 or bo[3] == x2 or bo[3] == x3) and (bo[6] == x1 or bo[6] == x2 or bo[6] == x3) and (bo[9] == x1 or bo[9] == x2 or bo[9] == x3)) or # down right side
	((bo[1] == x1 or bo[1] == x2 or bo[1] == x3) and (bo[5] == x1 or bo[5] == x2 or bo[5] == x3) and (bo[9] == x1 or bo[9] == x2 or bo[9] == x3)) or # diagonal
	((bo[3] == x1 or bo[3] == x2 or bo[3] == x3) and (bo[5] == x1 or bo[5] == x2 or bo[5] == x3) and (bo[7] == x1 or bo[7] == x2 or bo[7] == x3))) # diagonal



#main loop
theBoard = [' '] * 10
gameIsPlaying = True
while gameIsPlaying:
	#Player 1
	drawBoard(theBoard)
	piece = choosePiece(A)
	cell = chooseCell(theBoard)
	placePiece(theBoard, piece, cell)
	deletePiece(A, piece)
	if isWinner(theBoard, "Q1", "Q2", "Q3"):
		print "Player 1 with Q Won!"
		gameIsPlaying = False
		break
	#Player 2
	drawBoard(theBoard)
	piece = choosePiece(B)
	cell = chooseCell(theBoard)
	placePiece(theBoard, piece, cell)
	deletePiece(B, piece)
	if isWinner(theBoard, "X1", "X2", "X3"):
		print "Player 2 with X Won!"
		gameIsPlaying = False
		break








