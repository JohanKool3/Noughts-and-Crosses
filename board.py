class Board(object):
    
    def __init__(self):
        
        self.emptySlots = 0
        self._validPositions = []
        self.playerTurn = True
        self._board = [[" ", " ", " "],
                       [" ", " ", " "],
                       [" ", " ", " "]]
        
        self.winner = None
        
    def __str__(self) -> str:

        """ Takes a board input and prints it in an easy to understand way """
        
        output = ""
        startNum = 3
        for index, row in enumerate(self._board[::-1]):
            strRow = f"{startNum - index}. ["
            for item in row:
                
                if strRow == " ":
                    strRow += "[ ]"
                    
                else:
                    strRow += f"[{item}]"
            output += strRow + "]\n"
            
        output += "    1   2   3\n"
            
        return output
    
    def _notFull(self) -> int:
        """ Gets the amount of empty slots on the board """
        
        emptySlots = 0
        
        for row in self.board:
            for entry in row:
                
                if entry == " ":
                    emptySlots += 1
                    
        self.emptySlots = emptySlots
        
    def getValidPositions(self):
        self._validPositions = self._getPositionsWhere(" ")
        return self._getPositionsWhere(" ")

    def _getPositionsWhere(self, character):
        positions = []
        
        for y,row in enumerate(self._board):
            
            for x, item in enumerate(row):
                
                if item == character:
                    positions.append((x + 1, y + 1)) # Need to convert from 0 format to normal coords
                    
        return positions
        
    def playMove(self, option, player="O"):
    
        position = self._validPositions[option - 1]
        
        for y, row in enumerate(self._board):
            
            for x, _ in enumerate(row):
                
                if x == position[0] - 1 and y == position[1] - 1:
                    self._board[y][x] = player
                    break

    def _displayAvailablePositions(self):
        for index, position in enumerate(self._validPositions):
            print(f"{index + 1}. {position}")
            

    def _checkWinner(self):
        """ Checks for a winner """
        
        if self.playerTurn:
            symbol = "X"
            player = "CPU"
            # Find taken positions and convert to coordinates
            
        else:
            symbol = "O"
            player = "Player"
            
        takenPositions = self._getPositionsWhere(symbol)
        
        if len(takenPositions) < 3:
            return False
        
        else:
            
            # Check for 3 of the same x
            # Check for 3 of the same y
            xCoords = {}
            yCoords = {}
            
            
            ## Primitive checks
            for position in takenPositions:
                print(takenPositions)


    def takePlayerTurn(self) -> None:
        
        def getInput():
            """ Takes a user's input in form x, y and places it onto the board """
            validInp = False
            
            while not validInp:
                try:
                    userInp = int(input(f"Please enter a number between 1 and {len(self._validPositions)}: "))
                    
                    if userInp >= 1 and userInp <= len(self._validPositions):
                        return userInp
                    
                    else:
                        print(f"Must be between 1 and {self._validPositions}")
                
                except:
                    print("Invalid input, must be an integer between 1 and 3")
        
        if(self._checkWinner()): # Check to see if the CPU has won
            print(f"Player : {self.winner} wins the game!")
            
        
        else:
            print(self)
            ## Fetch the valid positions
            self.getValidPositions()
            self._displayAvailablePositions()
            
            # Take user input on a move
            userOpt = getInput()
            self.playMove(userOpt)
            print(userOpt, self._validPositions[userOpt -1 ])
            print(self)


if __name__ == "__main__":
    
    testObj = Board()
    
    testObj.takePlayerTurn()