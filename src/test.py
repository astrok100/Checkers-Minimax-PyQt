'''
Created on Feb 19, 2012

@author: k100
'''
import os,sys
import random
# Import Qt modules
from PyQt4.QtCore import*
from PyQt4.QtGui import *
from Board import *
from Piece import *
import time

class Checkers():
    def __init__(self):
        self.board = Board(8,8)
        self.size = 8
        self.turn = 0
        for y in range(0,3):
            for x in range(self.size):
                if(y%2 ==0 and x%2 ==1 ):
                    self.board.addPiece("AI", 0, x, y)
                if(y%2==1 and x%2 ==0):
                    self.board.addPiece("AI", 0, x, y)
        
        for y in range(5,self.size):
            for x in range(self.size):
                if(y%2 ==0 and x%2 ==1 ):
                    self.board.addPiece("Player", 0, x, y)
                if(y%2==1 and x%2 ==0):
                    self.board.addPiece("Player", 0, x, y)
        
    def ifPieceExists(self,x,y):
        return self.board.pieceAt(x, y)
    
    def getPiece(self,x,y):
        return self.board.getPieceAt(int(x),int (y))
    
    def forceJump(self):
        moves = []
        for i in range (self.board.getSize()):
            for j in range (self.board.getSize()):
                tmp = self.board.getPieceAt(i, j)    
                if(tmp != False):
                    if(self.getTurn() == tmp.getOwner() ):
                        jumpF = self.canJump(i, j)
                        if(jumpF != False):
                            print("appened")
                            moves.append(str(i)+","+str(j))
                            break
        return moves

        
    def printGame(self):
        count = 0
        tmp = "|"
        for y in range (self.board.getSize()): 
            for x in range (self.board.getSize()):
                if(self.board.pieceAt(x, y)== True):
                    count+=1
                    pi = Piece()
                    pi =self.board.getPieceAt(x, y)
                    if(pi.getOwner() == "AI"):
                        tmp = tmp + "0|"
                    else:
                        tmp = tmp + "X|"
                else:
                    tmp = tmp + " |"
            tmp += "\n|"
        print (str(tmp))

    def checkWin(self):
        if(self.board.getPiecePlayer() ==0 or self.board.getPieceAI() ==0):
            return True
        else: 
            return False

    def validMove(self,x,y,x1,y1):
        if((x1 < self.board.getSize() and x1>= 0 and y1 >= 0 and y1 < self.board.getSize()) ):
            if(self.board.pieceAt(x1, y1)== False):
                return True
        else:
            return False
    def movePiece(self,x,y,x1,y1):
        moves = []
        jump = []
        jump = self.forceJump()
        print("Jump", jump)
        moved = False
        moves = self.pieceMovable(x, y)
        move = str(x1)+","+str(y1)
        selected = str(x)+","+str(y)
        p = self.board.getPieceAt(x, y)
        if(self.checkWin() == False):
            #gets an array of movable positions x y given by user
            print(selected)
            if jump :
                print("jump != False")
                print(len(jump))
                for i in range (len(jump)):
 	                   print(jump[i])
                    if(jump[i] == selected):

                        for i in range (len(moves)):
                            if moves[i] == move and self.getTurn()== p.getOwner():

                                self.board.movePiece(x, y, x1, y1)
                            # checks if a jump is true then remove the piece being jumped        
                                removePieceX = (x + (x1))/2
                                removePieceY = (y + (y1))/2
                                self.board.removePiece(removePieceX, removePieceY)
                                    # implement if piece can jump again 
                                
                                jump = self.canJump(x1, y1)
                                if not jump :
                                    moved = True
                                    break
                                else:
                                    selected = str(x1)+","+str(y1)
            elif moves != None:
            # checks if the second input from user equals any possible moves
                for i in range (len(moves)):
                    if(moves[i] == move):
                        
                        #checks if the piece selected is the owners turn
                        if(self.getTurn()== p.getOwner()):
                            self.board.movePiece(x, y, x1, y1)
                            moved = True
                            
                            # it has moved then checks if it can be kinged and updates the piece to a king
            if(self.kingPiece(x1,y1)):
                self.board.updatePiece(x1,y1)
                                
        if moved:
            self.turn+=1  
        return moved
    
    def AI(self):
        movableP = []
        tmpMoves = []
        for i in range (self.board.getSize()):
            for j in range (self.board.getSize()):
                if(self.ifPieceExists(i, j)):
                    tmp = Piece()
                    tmp = self.getPiece(i, j)
                    if( tmp.getOwner() == "AI"):
                        
                        tmpMoves =self.pieceMovable(i, j)
                        
                        if len(tmpMoves) != 0:
                            movableP.append(str(i)+","+str(j))
        u = random.randint(0,len(movableP)-1 )
        movstr = movableP[u]
        tmpMovess = [] 
        x1 = int(movstr[:1])
        y1 = int(movstr[2:])
        tmpMovess = self.pieceMovable(x1, y1)
        movstr = tmpMovess[0]
        x2 = int(movstr[:1])
        y2 = int(movstr[len(movstr)-1])
        m = self.movePiece(x1, y1, x2, y2)            
        if m == True :
            print("print tur")
            return (str(x1)+ ","+str(y1)+" "+ str(x2)+","+str(y2))  
        else: 
            print("NONONONO")
            return ""         

    def getTurn(self):
        if(self.turn % 2 == 0):
            return "Player"
        else:
            return "AI"
    ## checks if a piece can be Kinged when AI piece hits bottom of board 
    ## or Player piece hits the top of the board
    def kingPiece(self,x,y):
        self.p = Piece()
        self.p = self.board.getPieceAt(x, y)
        if(self.board.pieceAt(x, y)):
            if(self.p.getOwner() == "AI" and self.p.getY()== self.board.getSize()-1 ):
                return True
            elif(self.p.getOwner() == "Player" and self.p.getY()== 0 ):
                return True
            else:
                return False

    def canJump(self,x,y):
                
        if(self.board.pieceAt(x, y)):
          
            tmp = self.board.getPieceAt(x, y)
            t = tmp.getOwner()
            start = 0
            finish = 0
            moves = []
            if(tmp.getType() == 0):
                if(t == "Player"):
                    start = -1
                    finish = 0
        
                if(t == "AI"):
                    start = 1
                    finish = 2
            # jump part    Ai  # +1,-1 #-1 -1  player # +1 +1#-1 +1
                for i in range(-1,2):
                    for j in range (start,finish):
                        if (x +i < self.board.getSize() and x+i >=0) and (y+j <self.board.getSize() and y+j >=0):
                           tmp1 = Piece()
                           if self.board.pieceAt(x+i, y+j):
                               tmp1 = self.board.getPieceAt(x+i, y+j)
                               if(t != tmp1.getOwner() ):
                                    if(self.validMove(x, y, x+i+i, y+j+j)):
                                        moves.append(str(x+i+i)+","+str(y+j+j))

            #if piece is king then will try get all directions
            if(tmp.getType() == 1):
                for i in range(-1,2):
                    for j in range (-1,2):
                        if (x +i < self.board.getSize() and x+i >=0) and (y+j <self.board.getSize() and y+j >=0):
                            tmp1 = Piece()
                            if self.board.pieceAt(x+i, y+j):
                               tmp1 = self.board.getPieceAt(x+i, y+j)
                               if(t != tmp1.getOwner() ):
                                   if(self.validMove(x, y, x+i+i, y+j+j)):
                                       moves.append(str(x+i+i)+","+str(y+j+j))
            if moves:
                return moves
            else:
                #print(False)
                return False

    def pieceMovable(self,x,y):
        self.removePieceX = None
        self.removePieceY = None
        moves = []
        jmps  = []
        jmps = self.canJump(x, y)
        if jmps:
            print("eeeeemmememmememe BOO")
            return jmps
        
        tmp = self.getPiece(x, y)

        if tmp != False:
            
            t = tmp.getOwner()              

            
            if tmp.getType() == 1:
                if(self.validMove(x, y, x-1, y-1)):
                    moves.append(str(x-1)+","+str(y-1))
    
                if(self.validMove(x, y, x+1, y-1)):
                    moves.append(str(x+1)+","+str(y-1))
                    
                if(self.validMove(x, y, x-1, y+1)):
                    moves.append(str(x-1)+","+str(y+1))
    
                if(self.validMove(x, y, x+1, y+1)):
                    moves.append(str(x+1)+","+str(y+1))
                         
            elif(t == "Player" and tmp.getType() == 0):
                    
    
                if(self.validMove(x, y, x-1, y-1)):
                    moves.append(str(x-1)+","+str(y-1))
                if(self.validMove(x, y, x+1, y-1)):
                    moves.append(str(x+1)+","+str(y-1))
    
            # Players pieces which will always be at the bottom        
            elif(t == "AI" and tmp.getType() == 0):
    
            #down and right   
                if(self.validMove(x, y, x+1, y+1)):
                        moves.append(str(x+1)+","+str(y+1))
        #down and left
                if(self.validMove(x, y, x-1, y+1)):
                    moves.append(str(x-1)+","+str(y+1))            
    
            return moves

