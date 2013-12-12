from Checkers import *
from Piece import *
from Board import *

def checkersTest():
	game = Checkers()
	"""print(game.evaluate("Player"))
	print(game.evaluate("AI"))
	print(game.getTurn())
	game.turnEnd()
	print(game.getTurn())
	game.printGame()
	
	board = Board(8)
	board.addPiece("Player",0,1,1)
	game.loadBoard(board)
	game.printGame()
	print(game.checkWin(), game.isOver())
	board = Board(8)
	board.addPiece("AI",0,1,1)
	game.loadBoard(board)
	game.printGame()
	print(game.checkWin(), game.isOver())
	"""
	board = Board(8)
	board.addPiece("Player",0,1,0)
	board.addPiece("Player",0,4,4)
	board.addPiece("AI",0,5,3)
	board.addPiece("Player",0,2,2)
	board.addPiece("AI",0,0,7)
	board.addPiece("AI",0,3,3)
	board.addPiece("AI",0,1,6)
	game.loadBoard(board)
	print("validMove  from 2,2 to 1,1",game.validMove(1,1))
	print("Movable","2,2",game.pieceMovable(2, 2) )
	print("Movable","0,7",game.pieceMovable(1, 6) )
	
	
	print("King", game.isKing(3,3))
	print("King", game.isKing(1,6))
	print("King", game.isKing(1,0))
	print("King", game.isKing(0,7))
	print("CAN 4,4 Jump?", game.canJump(4, 4))
	print("ForceJump Player", game.forceJump("Player"))
	print("CAN 5,3 Jump?", game.canJump(5, 3))
	print("ForceJump AI", game.forceJump("AI"))
	
	
	board = Board(8)
	
	board.addPiece("Player",0,1,0)
	board.addPiece("Player",0,5,4)
	board.addPiece("AI",0,0,7)
	board.addPiece("AI",0,4,3)
	board.addPiece("AI",0,7,0)
	board.addPiece("Player",0,1,6)
	board.addPiece("Player",0,6,7)
	board.updatePiece(1, 0, 7)
	board.updatePiece(1, 1, 0)

	game.loadBoard(board)

	print(game.movePiece("Player",1, 0, 0, 1))
	print(game.movePiece("AI",7, 0, 6, 1))
	print(game.movePiece("AI",0, 7, 2, 5))
	print(game.movePiece("Player",5, 4, 3, 2))
	
	board2 = Board(8)
	
	board2.addPiece("Player",0,1,0)
	board2.addPiece("Player",0,5,4)
	board2.addPiece("AI",0,0,7)
	board2.addPiece("AI",0,4,3)
	board2.addPiece("AI",0,7,0)
	board2.addPiece("Player",0,1,6)
	board2.addPiece("Player",0,6,7)
	board2.updatePiece(1, 0, 7)
	board2.updatePiece(1, 1, 0)

	game2 = Checkers()
	game2.printGame()
	game2.loadBoard(board2)
	game2.printGame()
	print(game.movePiece("AI",0, 7, 2, 5))
	print(game.movePiece("Player",5, 4, 3, 2))
	print(game.movePiece("AI",7, 0, 6, 1))
	print(game.movePiece("Player",1, 0, 0, 1))
	
	"""while not game.isOver():
		print(game.getTurn())
		game.turnEnd()
		game.AI()
		game.printGame()"""

def boardTest():
	board = Board(8)
	board.printBoard()
	board2 = Board(3)
	board2.printBoard()
	print(board.getSize())
	print(board2.getSize())
	board.addPiece("AI",0,1,1)
	board.addPiece("Player",0,6,6)
	print(board.countAiPieces(), board.countPlayerPieces())
	board.printBoard()
	board.removePiece(1,1)
	print(board.countAiPieces(), board.countPlayerPieces())
	board.printBoard()
	board2.addPiece("test",0,1,1)
	board2.addPiece("AI",3,1,2)
	board2.printBoard()
	board2.addPiece("AI",1,2,1)
	print(board2.countAiPieces(), board2.countPlayerPieces())
	board2.printBoard()
	
	board3 = Board(4)
	board3.addPiece("AI",0,1,1)
	board3.printBoard()
	print(board3.pieceAt(1, 1))
	piece = board3.getPieceAt(1, 1)
	piece.printPiece()
	board3.movePiece(1, 1, 2, 1)
	board3.printBoard()
	
	# move piece and resign to do left.
	
def pieceTest():
	testPiece = Piece()
	testPiece.setup("Player", 0)
	testPiece.printPiece()
	testPiece.setup("AI", 0)
	testPiece.printPiece()
	testPiece.setup("Player",1)
	testPiece.printPiece()
	testPiece.setup("AI",1)
	testPiece.printPiece()
	testPiece.setup(293,"hello")
	testPiece.printPiece()
	testPiece.setup(1,3)
	testPiece.printPiece()
	
#pieceTest()
#boardTest()
checkersTest()