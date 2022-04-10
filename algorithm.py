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
        alpha = self.__alpha_beta(state, -1000, 1000, player, 3)
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
                if i < 0 or j < 0:
                    raise IndexError
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
        evaluation += self.__twoInLine(state, player)
        evaluation += self.__singleCase(state, player)
        #        print(evaluation, state)
        return evaluation      

    
    def __heuristicFunction(self, state, player):
        '''
        Returns evaluated value considering the opponent moves
        '''
        evaluation = self.__playerMoveEvaluation(state, player)
        evaluation -= self.__playerMoveEvaluation(state, "X" if player == "O" else "X")
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

    def __bestStateCoordinates(self, state, best_state):
        '''
        Returns the coordinates of the best state
        '''
        for i in range(3):
            for j in range(3):
                if state[i][j] != best_state[i][j]:
                    return i, j

    def __alpha_beta(self, state, alpha, beta, player, depth=3):
        '''
        state - state with information who is moving
        alpha, beta - parameters for alpha beta pruning alg.
        depth - is max depth of the

        T - set of the terminal states
        '''
        next_player = "X" if player == "O" else "O"
        if self.__threeInLine(state, player):
             #the final state reached, game over
            return 100 if player == self.player else -100
        elif depth == 0:
            return self.__heuristicFunction(state, next_player)
        

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
