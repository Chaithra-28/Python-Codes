def createBoard(rows,cols):
	board=[]
	for row in range(rows):
		row_list=[]
		for col in range(cols):
			row_list.append("|__|")
		board.append(row_list)
	return board

def printBoard(mat):
	for row in mat:
		for col in row:
			print(col,end="")
		print("")

def genMoves(horsePos):
	offsets=[[2,1],[2,-1],[1,2],[1,-2],[-1,2],[-1,-2],[-2,1],[-2,-1]]
	moves=[]
	for offset in offsets:
		moves.append([horsePos[0]+offset[0],horsePos[1]+offset[1]])
	return moves

def isValidMove(board,move):
	x,y=move
	if x<0 or x>=len(board) or y<0 or y>=len(board[0]):
		return False
	return True

def updateBoard(board,horsePos,moves):
	board[horsePos[1]][horsePos[0]]='|H_|'
	for move in moves:
		row,col=move
		if isValidMove(board,move):
			board[row][col]='|x_|'
		

board=createBoard(8,8)
printBoard(board)
moves=genMoves([2,4])
updateBoard(board,[2,4],moves)
printBoard(board)