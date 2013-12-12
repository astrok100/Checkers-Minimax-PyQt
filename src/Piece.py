""" Piece Class"""

class Piece:
    # default constructor
    def __init__(self):
        self.type = 0
        self.owner = ""
    
    #setup assigns owner and type to itself
    def setup(self,owner1,type1):
        self.type = type1
        self.owner = owner1
    
    #returns type
    def getType(self):
        return self.type
    
    #returns owner
    def getOwner(self):
        return self.owner

    #prints owner and type    
    def printPiece(self):
        print("Owner =" , self.owner )
        print("Type =" , self.type )      
