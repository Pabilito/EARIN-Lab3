#Those imports probably will not be useful in final algorithm
import random 
import time
import copy

class Algorithm:
    def selectPoint(self, currentBoardState, player):
        #Current Board State is a 3x3 array with 'X' and 'O' and '' if empty
        self.player = player
        bestRow = 1
        bestColumn = 1
        
        #WRITE ALGORITHM HERE - THIS ONE IS ONLY FOR TESTING
        time.sleep(1)
        '''
        while(currentBoardState[bestRow][bestColumn]!=""):
            bestRow = random.randint(0,2)
            bestColumn = random.randint(0,2)
        '''
        self.__alpha_beta(currentBoardState, 0, 0, 1)

        #END OF TEST ALGORITHM

        #Return row and collumn
        return bestRow, bestColumn
    def __threeInLine(self, state, player):
        if( #There are 8 conditions (3x rows, 3x columns, 2x diagonnally)
        state[0][0]==state[0][1]==state[0][2]==player or 
        state[1][0]==state[1][1]==state[1][2]==player or 
        state[2][0]==state[2][1]==state[2][2]==player or 
        state[0][0]==state[1][0]==state[2][0]==player or 
        state[0][1]==state[1][1]==state[2][1]==player or 
        state[0][2]==state[1][2]==state[2][2]==player or
        state[0][0]==state[1][1]==state[2][2]==player or
        state[0][2]==state[1][1]==state[2][0]==player):
            return True
        return False

    def __twoInLine(self, state, player):
        value = 0
        #linear cases
        if state[0][0]==state[0][1]==player and state[0][2] == "":
            value += 10
        if state[0][1]==state[0][2]==player and state[0][0] == "":
            value += 10
        if state[1][0]==state[1][1]==player and state[1][2] == "":
            value += 10
        if state[1][1]==state[1][2]==player and state[1][0] == "":
            value += 10
        if state[2][0]==state[2][1]==player and state[2][2] == "":
            value += 10
        if state[2][1]==state[2][2]==player and state[2][0] == "":
            value += 10

        #Diagonal cases
        if state[0][0]==state[1][1]==player and state[2][2] == "":
            value += 10
        if state[2][0]==state[1][1]==player and state[0][2] == "":
            value += 10
        if state[0][2]==state[1][1]==player and state[2][0] == "":
            value += 10
        if state[2][2]==state[1][1]==player and state[0][0] == "":
            value += 10
        return value

    def __testSingleField(self, state, i, j):
        try:
            if state[i][j] == "":
                return 1
        except IndexError:
            return 0
        return 0
    
    def __singleCase(self, state, player):
        value = 0
        for i in range(3):
            for j in range(3):
                if state[i][j] == player:
                    value += self.__testSingleField(state, i-1, j)
                    value += self.__testSingleField(state, i+1, j)
                    value += self.__testSingleField(state, i, j+1)
                    value += self.__testSingleField(state, i, j-1)
                    value += self.__testSingleField(state, i-1, j-1)
                    value += self.__testSingleField(state, i+1, j+1)
                    value += self.__testSingleField(state, i-1, j+1)
                    value += self.__testSingleField(state, i+1, j-1)
        return value

    def __playerMoveEvaluation(self, state, player):
        '''
        Evaluates the heuristic value of the given move for one player
        '''
        evaluation = 0
        if self.__threeInLine(state, player):
            return 1000 #in stead of infinity, we use here 1000
        evaluation += self.__twoInLine(state, player)
        evaluation += self.__singleCase(state, player)
        return evaluation        

    
    def __heuristicFunction(self, state, player):
        '''
        Return evaluated value considering the opponent moves
        '''
        evaluation = __playeMoveEvaluation(state, player)
        evaluation -= __playerMoveEvaluation(state, "X" if player == "O" else "X")
        if player != self.player:
            evaluation *= -1
        return evaluation

    def __successors(self, state, player):
        '''
        it represents movements (possible actions), it returns the set of next states according to the game rules
        '''
        U = []
        for i in range(3):
            for j in range(3):
                if state[i][j] == "":
                    buffer_state = copy.deepcopy(state)
                    U.append(buffer_state)
                    U[-1][i][j] = player
        return U

    def __alpha_beta(self, state, alpha, beta, player, depth=3):
        '''
        state - state with information who is moving
        alpha, beta - parameters for alpha beta pruning alg.
        depth - is max depth of the

        T - set of the terminal states
        '''
        best_move = None
        if self.__threeInLine(state, player):
            return 1000 #the final state reached, game over
        elif depth == 0:
            return __heuristicFunction(state, player)
        
        if self.player == player: #computer's turn
            U = self.__successors(state, player)
            for u in U:
                next_player = "X" if player == "O" else "X"
                alpha = max(alpha, self.__alpha_beta(u, alpha, beta, next_player, depth-1))
                if alpha >= beta:
                    best_move = u
                    return beta
            return alpha
        else: #human turn
            U = self.__successors(state, player)
            for u in U:
                next_player = "X" if player == "O" else "X"
                beta = min(self.__alpha_beta(u, alpha, beta, next_player, depth-1), beta)
                if alpha <= beta:
                    return alpha
            return beta
