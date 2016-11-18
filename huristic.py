# -*- coding: utf-8 -*-
"""
Created on Sun Oct 23 15:05:44 2016

@author: Liu Qi
"""

    def huristic(self,current_player,model):
        aiScore = 0
        humanScore = 0
        cp1 = 0
        cp2 = 0
        if current_player == 1:
            opponent = 2
        else:
            opponent = 1
        #print('current_player',current_player,'\n')
        #print('opponent',opponent,'\n')
        c = self.k
        self.connect = False
        width = model.get_width()
        height = model.get_height()
#        print('w',width)
#        print('h',height)
        #search for winning lines
        #horizontally
        for i in range(width-c):
                for j in range(height):
                    for s in range(self.k):
                        if model.get_space(i+s,j) == current_player:
                            cp1+=1
                            #print('cp1 ',cp1,'\n')

                        elif  model.get_space(i+s,j) == opponent:
                            cp2+=1
                            #print('cp2 ',cp2,'\n') 
                    if cp1 > 0 and cp2==0:
                        aiScore+=self.weight(cp1)
                        self.connect = self.staticTest(current_player,cp1)
                    elif cp2>0 and cp1==0:
                        #beware
                        humanScore+=self.weight(cp2)
                        self.connect = self.staticTest(opponent,cp2)
                    cp1=0
                    cp2=0
      #vertically

        for i in range(width):
            for j in range(height-c):
                    for s in range(self.k):
                        if model.get_space(i,j+s) == current_player:
                            cp1+=1
                        elif model.get_space(i,j+s) == opponent:
                            cp2+=1
                    if cp1>0 and cp2==0:
                        #beware
                        aiScore+=self.weight(cp1)
                        self.connect = self.staticTest(current_player,cp1)
                    elif  cp2>0 and cp1==0:
                        #beware
                        humanScore+=self.weight(cp2)
                        self.connect = self.staticTest(opponent,cp2)
                    #print('cp1 ',cp1,'\n')
                    #print('cp2 ',cp2,'\n')                       
                    cp1=0
                    cp2=0
        #diagonal northern east
        for i in range(width-c):
                for j in range(height-c):
                    for s in range(self.k):
                        if model.get_space(i+s,j+s) == current_player:
                            cp1+=1
                        elif model.get_space(i+s,j+s) == opponent:
                            cp2+=1
                    if cp1>0 and cp2==0:
                        #beware
                        aiScore+=self.weight(cp1)
                        self.connect = self.staticTest(current_player,cp1)
                    elif  cp2>0 and cp1==0:
                        #beware
                        humanScore+=self.weight(cp2)
                        self.connect = self.staticTest(opponent,cp2)
                    #print('cp1 ',cp1,'\n')
                    #print('cp2 ',cp2,'\n')
                    cp1=0
                    cp2=0
        #diagonal southern west
        for i in range(width,0):
                for j in range(height-c):
                    for s in range(self.k): 
                        if model.get_space(i-s,j+s) == current_player:
                            cp1+=1
                        elif model.get_space(i-s,j+s) == opponent:
                            cp2+=1
                    if cp1>0 and cp2==0:
                        #beware
                        aiScore+=self.weight(cp1)
                        self.connect = self.staticTest(current_player,cp1)
                    elif  cp2>0 and cp1==0:
                        #beware
                        humanScore+=self.weight(cp2)
                        self.connect = self.staticTest(opponent,cp2)
#                    print('cp1 ',cp1,'\n')
#                    print('cp2 ',cp2,'\n')
                    cp1=0
                    cp2=0

        #print('current_player ',aiScore,'\n')
        #print('oppenent ',humanScore,'\n')

        finalScore = aiScore-humanScore
        #print('finalScore',finalScore,'\n')
        return finalScore
        
        
    def huristic(self,model,x,y):
        huristicValue = [0,0]
        currentPiece = model.get_space(x,y)
 #       print('currentPiece: ',currentPiece)
        for direction in range(0,4):
#            print('direction ',direction)
            temp = 0;
            connect = True            
            counter = 1            
            w = x
            h = y
            while counter < self.k:
                if direction == 0:
                    w+=1
                    if w >= self.width:
                        w = self.width-1
                elif direction == 1:
                    w+=1
                    h+=1
                    if w >= self.width:
                        w = self.width-1
                    if h >= self.height:
                        h = self.height-1
                elif direction == 2:
                    h+=1
                    if h >= self.height:
                        h = self.height-1
                else:
                    w-=1
                    h+=1
                    if w >= self.width:
                        w = self.width-1
                    if h >= self.height:
                        h = self.height-1
                    if w < 0:
                       w = 0
                if w < self.width or h < self.height or w >=0:
                    if currentPiece == 0:
                        connect = False
#                        print("w and h value :",w,h,'\n')
                        if model.get_space(w,h) == 0 or model.get_space(w,h) == temp:
                            counter+=1
#                            print('counter: ',counter,'\n')
                        elif temp == 0:
                            temp = model.get_space(w,h)
                            counter+=1
                        else:
                            break
                    else:
                        if model.get_space(w,h) == currentPiece:
                            counter+=1
                        else:
                            break
                else:
                    break
            if counter == self.k:
                if currentPiece == self.player:
                    if connect:
                        huristicValue[0] = float('inf')
                        return huristicValue
                    huristicValue[0]+=1
                elif currentPiece == self.opponent:
                    if connect:
                        huristicValue[1] = float('inf')
                        return huristicValue
                    huristicValue[1]+=1
                else:
                    if temp == 0:
                        huristicValue[0]+=1
                        huristicValue[1]+=1
                    elif temp == self.player:
                        huristicValue[0] +=1
                    else:
                        huristicValue[1]+=1
        return huristicValue
        
        
    def gethuristic(self,model):
        playerScore = 0
        opponentScore = 0
        for w in range(self.width):
            for h in range(self.height):
                huristicValue = self.huristic(model,w,h)
                if huristicValue[0] == float('inf'):
                    return float('inf')
                if huristicValue[1] == float('inf'):
                    return float('-inf')
                playerScore += huristicValue[0]
                opponentScore += huristicValue[1]
#        print('Final Score: ', playerScore - opponentScore)
        return playerScore - opponentScore
        
    def get_available_moves(self,model):
        spaces = defaultdict(int)
        for i in range(self.width):
            for j in range(self.height):
                spaces[(i,j)] = model.get_space(i, j)
        moves = [k for k in spaces.keys() if spaces[k] == 0]
        return moves
        
    def safe(self,model,row,col,visited):
        return row>=0 and row < self.width and col >= 0 and col < self.height and visited == False and model[row][col]
        
    def dfs(self,model,row,col,visited,player):
        kmove = []
        rowNum = [-1,-1,-1,0,0,1,1,1]
        colNum = [-1,0,1,-1,1,-1,0,1]
        visited[row][col] = True
        for k in range(8):
            if self.safe(model,row+rowNum[k],col+colNum[k],visited):
                kmove.append(k)
                print('kmove: ',kmove)

                if model.get_space(row+row[k],col+colNum[k]) == player:
                    self.dfs(model,row+rowNum[k],col+colNum[k],visited)
    #count the number of paths to win, similar to tic tax toe eval function
    def 1heuristic(self,player1,model):
        p1Score = 0
        p2Score = 0
        p1Count = 0
        p2Count = 0
        if player1 == 1:
            player2 = 2
        else:
            player2 = 1
            player1 = 2
 #       c = self.k # default 4
        width = model.get_width() #default 4
        height = model.get_height() #default 4
        #initialized the boolean matrix
        visited = [[False for x in range(height)] for y in range(width)]
        #print(visited)
        
        for i in range(width):
            for j in range(height):
                if model.get_space(i,j) == player1 and visited[i][j]==False:
                    self.dfs(model,i,j,visited,player1)
                    p1Count+=1

                elif model.get_space(i,j) == player2 and visited[i][j]==False:
                    self.dfs(model,i,j,visited,player2)
                    p2Count+=1
                    
                    
        #print('p1Count: ',p1Count)
        #print('p2Count: ',p2Count)   
        p1Score = pow(4,p1Count)
        p2Score = pow(4,p2Count)
        #print("this is p1Score: ",p1Score)
        #print("this is p2Score: ",p2Score)
        finalScore = p1Score-p2Score
        #print('finalScore',finalScore,'\n')
        #print (visited)
        return finalScore
        
