#Author: Toluwanimi Salako
import queue
from collections import defaultdict
import random
import time

team_name = "LucidDream"

class StudentAI():
    def __init__(self, player, state):
        self.last_move = state.get_last_move()
        self.player = player
        self.opponent = 2 if player==1 else 1
        self.k = state.get_k_length()
        self.connect = False
        self.width = state.get_width()
        self.height = state.get_height()
        self.model = state
        self.deadline = 5
        self.winner = state.winner()
        self.maxDepth = 6
    
    def get_available_moves(self,model):
        spaces = defaultdict(int)
        for i in range(self.width):
            for j in range(self.height):
                spaces[(i,j)] = model.get_space(i, j)
        moves = [k for k in spaces.keys() if spaces[k] == 0]
        return moves    
        
        
        
    def heuristic(self,model,player):
        if player == 1:
            opp = 2
        else:
            opp = 1
        connect_k = self.check(model,player,self.k,self.width,self.height)
        connect_k1 = self.check(model,player,self.k-1,self.width,self.height)
        connect_k2 = self.check(model,player,self.k-2,self.width,self.height)
        opp = self.check(model,opp,self.k,self.width,self.height)
        opp_k1 = self.check(model,opp,self.k-1,self.width,self.height)
        opp_k2 = self.check(model,opp,self.k-2,self.width,self.height)
        #print("score: ",pow(4,connect_k)+pow(4,connect_k1) - (pow(4,opp)+pow(4,opp_k1)))
        #return pow(4,connect_k)+pow(4,connect_k1) - (pow(4,opp)+pow(4,opp_k1))
        #print(connect_k*1000+connect_k1*100+connect_k2*10 - (opp*1000+opp_k1*100+opp_k2*10))
        return connect_k*1000+connect_k1*100+connect_k2*10 - (opp*1000+opp_k1*100+opp_k2*10)
        
    def check(self,model,player,connectk,row,col):
        count = 0
        for i in range(row):
            for j in range(col):
                if model.get_space(i,j) == player:
                    count += self.verticalCheck(i,j,model,connectk)
                    count += self.horizontalCheck(i,j,model,connectk)
                    count += self.diagonalCheck(i,j,model,connectk)
        return count
        
    def horizontalCheck(self,row,col,model,connectk):
        connect = 0
        for i in range(col,self.height):
            if model.get_space(row,i) == model.get_space(row,col):
                connect+=1
            else:
                break
        if connect >= connectk:
            return 1
        else:
            return 0                
        
    def verticalCheck(self,row,col,model,connectk):
        connect = 0
        for i in range(row,self.width):
            if model.get_space(i,col) == model.get_space(row,col):
                connect+=1
            else:
                break
        if connect >= connectk:
            return 1
        else:
            return 0
    
    def diagonalCheck(self,row,col,model,connectk):
        sumConnectk,connect,k = 0,0,col
        for i in range(row,self.width):
            #print("i,j: ",i,k)
           
            if k >= self.width:
                break
            elif model.get_space(i,k) == model.get_space(row,col):
                connect+=1
            else:
                break
            k+=1
        if connect >= connectk:
            sumConnectk+=1
        connect = 0
        k = col
        for i in range(row,-1,-1):
            if k>=self.height:
                break
            elif model.get_space(i,k) == model.get_space(row,col):
                connect+=1
            else:
                break
            k+=1
        if connect >= connectk:
            sumConnectk +=1
        return sumConnectk
        
#player 1 or 2
#IDS and Sorting means IDS first and start the shallower depth's best move first
#At depth#0, player run through all the available moves, and uses a priority queue to store it. 
#at depth#1, dequeue from the priority queue and begin more depth search.
#for example, if at depth#0 we have a best move is (5,5), we store in the queue. when depth#1 begins,
#(5,5) will be the first to search at depth#1
    def minimax(self,model):
        begin = time.clock()
        print(begin)
        print("getting moves........")
        #storeMoves stores each explored game node
        #storeMoves = {}
#        mydepth = 2
        moves = self.get_available_moves(model)
        bestScore = float('-inf')
        #check if we can win within one move
        #check opponent can win within one move, block it.   
#        for move in moves:
#            if model.clone().place_piece(move,self.player).self.winner() == self.player:
 #               print(model.clone().place_piece(move,self.player).self.winner())
                #return move
#        for move in moves:
 #           if model.clone().place_piece(move,self.opponent).self.winner() == self.opponent:
 #               return move
        #start IDS 
        #max size of queue is 11
        for depthLimit in range(self.maxDepth):
            nextMove = []
            moveValue = []
            end = time.clock()
            print("end - begin: ", end-begin)
            if end - begin < self.deadline:
                alpha = float('-inf')
                beta = float('inf')
                if len(nextMove) == 0:  
                    for move in moves:
                        clone_state = model.clone()
                        scoreForMove = self.min_play(depthLimit,clone_state.place_piece(move,self.player),alpha,beta)
                        #print('scoreForMove',scoreForMove)
                        if scoreForMove > bestScore:
                            nextMove.append(move)
                            moveValue.append(scoreForMove)
                            bestScore = scoreForMove
                            bestMove = move
                    moveForNext = dict(zip(nextMove,moveValue))
                #if the tree has been made, choose one to start with
                else:
                    while(len(moveForNext) != 0):
                        move = nextMove.pop()
                        clone_state = model.clone()
                        scoreForMove = self.min_play(depthLimit,clone_state.place_piece(move,self.player),alpha,beta)
                        if scoreForMove > bestScore:
                            nextMove.append(move)
                            moveValue.append(scoreForMove)
                            bestScore = scoreForMove
                            bestMove = move
            else:
                return bestMove
                        
#        print('player1',self.player)
#        print('player2',self.opponent)
#        print(model)
        return bestMove


    def min_play(self,depth,model,alpha,beta):
        if depth <= 0:
            #print('min depth: ', depth)
            #passing clone state to huristic
            #print(self.huristic(self.player,model))
            return self.heuristic(model,self.player)
        moves = self.get_available_moves(model)
        minScore = float('inf')
        for m in moves:
            clone_state = model.clone()
            #print('minplay state')
            #print(clone_state.place_piece(m,self.opponent))            
            minScore = min(minScore,self.max_play(depth-1,clone_state.place_piece(m,self.opponent),alpha,beta))
            if minScore <= alpha:
                return minScore
            beta = min(beta,minScore)
        return minScore

    
    def max_play(self,depth,model,alpha,beta):
        if depth <= 0:
            #print('max depth: ' ,depth)
            #print(self.heuristic(self.player,model))
            return self.heuristic(model,self.player)
        
        moves = self.get_available_moves(model)
        maxScore = float('-inf')
        for m in moves:
            clone_state = model.clone()
            #print('self.player: ', self.player)
            #print('maxplay state')
            #print(clone_state.place_piece(m,self.player))
            maxScore = max(maxScore,self.min_play(depth-1,clone_state.place_piece(m,self.player),alpha,beta))
            #print('scoreForMove',scoreForMove)
            if maxScore >= beta:
                #print('in the max_play: ')
                #print('beta: ',beta,'\n')
                return maxScore
            alpha = max(alpha,maxScore)
            #print('alpha: ',alpha,'\n')
        return maxScore
        
        
    def make_move(self, *args):
        model = self.model
        if (len(args) == 2):
            model = args[0]
            deadline = args[1]
        else:
            deadline = args[0]
        '''Write AI Here. Return a tuple (col, row)'''
        return self.minimax(model)

