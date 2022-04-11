#Those imports probably will not be useful in final algorithm
import random 
import time
import copy

class Algorithm:
    def selectPoint(self, state, player):
        #Current Board State is a 3x3 array with 'X' and 'O' and '' if empty
        self.player = player
        
        #WRITE ALGORITHM HERE - THIS ONE IS ONLY FOR TESTING
        time.sleep(1)
        
        self.best_state = None
        alpha = self.__alpha_beta(state, -1000, 1000, player, 4)
        best_row, best_column = self.__bestStateCoordinates(state, self.best_state)
        #END OF TEST ALGORITHM

        #Return row and collumn
        return best_row, best_column
    
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

    def __bestStateCoordinates(self, state, best_state):
        '''
        Returns the coordinates of the best state
        '''
        for i in range(3):
            for j in range(3):
                if state[i][j] != best_state[i][j]:
                    return i, j

    def __heuristicFunction(self, state, player):
        if self.__threeInLine(state, player):
            if player == self.player:
                return 1
            else:
                return -1
        else:
            if self.__isBoardEmpty(state):
                return 0
        return None
            
    def __isBoardEmpty(self, state):
        for i in state:
            for j in i:
                if j == "":
                    return False
        return True

    def __alpha_beta(self, state, alpha, beta, player, depth=3):
        '''
        alpha-beta pruning algorithm
        
        state - current state of a board
        alpha, beta - parameters for alpha beta pruning alg.
        depth - is max depth of the recursion
        '''
        next_player = "X" if player == "O" else "O"

        value = self.__heuristicFunction(state, player)
        if value != None:
            return value

        U = self.__successors(state, player)
        best_state = state
        if self.player == player: #computer's turn
            for u in U:
                new_value = self.__alpha_beta(u, alpha, beta, next_player, depth-1)
                if new_value > alpha:
                    best_state = u
                    alpha = new_value
                if alpha >= beta:
                    return beta
            self.best_state = best_state
            return alpha
        else: #human turn
            for u in U:
                new_value = self.__alpha_beta(u, alpha, beta, next_player, depth-1)
                if new_value < beta:
                    beta = new_value
                    best_state = u
                if alpha >= beta:
                    return beta
            self.best_state = best_state
            return beta
