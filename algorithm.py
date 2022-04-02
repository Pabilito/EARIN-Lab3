#Those imports probably will not be useful in final algorithm
import random 
import time

class Algorithm:
    def selectPoint(self, currentBoardState):
        #Current Board State is a 3x3 array with 'X' and 'O' and '' if empty
        bestRow = 1
        bestColumn = 1
        
        #WRITE ALGORITHM HERE - THIS ONE IS ONLY FOR TESTING
        time.sleep(1)
        while(currentBoardState[bestRow][bestColumn]!=""):
            bestRow = random.randint(0,2)
            bestColumn = random.randint(0,2)

        #Return row and collumn
        return bestRow, bestColumn