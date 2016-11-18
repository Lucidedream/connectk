# -*- coding: utf-8 -*-

def value(state, color):
        """ Simple heuristic to evaluate board configurations
            Heuristic is (num of 4-in-a-rows)*99999 + (num of 3-in-a-rows)*100 + 
            (num of 2-in-a-rows)*10 - (num of opponent 4-in-a-rows)*99999 - (num of opponent
            3-in-a-rows)*100 - (num of opponent 2-in-a-rows)*10
        """
    if color == self.colors[0]:
        o_color = self.colors[1]
    else:
        o_color = self.colors[0]
        
    my_fours = self.checkForStreak(state, color, 4)
    my_threes = self.checkForStreak(state, color, 3)
    my_twos = self.checkForStreak(state, color, 2)
    opp_fours = self.checkForStreak(state, o_color, 4)
        #opp_threes = self.checkForStreak(state, o_color, 3)
        #opp_twos = self.checkForStreak(state, o_color, 2)
    if opp_fours > 0:
        return -100000
    else:
        return my_fours*100000 + my_threes*100 + my_twos
            
def checkForStreak(self, state, color, streak):
    count = 0
        # for each piece in the board...
    for i in range(6):
        for j in range(7):
                # ...that is of the color we're looking for...
            if state[i][j].lower() == color.lower():
                    # check if a vertical streak starts at (i, j)
                count += self.verticalStreak(i, j, state, streak)
                    
                    # check if a horizontal four-in-a-row starts at (i, j)
                count += self.horizontalStreak(i, j, state, streak)
                    
                    # check if a diagonal (either way) four-in-a-row starts at (i, j)
                count += self.diagonalCheck(i, j, state, streak)
        # return the sum of streaks of length 'streak'
    return count
            
def verticalStreak(self, row, col, state, streak):
    consecutiveCount = 0
    for i in range(row, 6):
        if state[i][col].lower() == state[row][col].lower():
            consecutiveCount += 1
         else:
             break
    
    if consecutiveCount >= streak:
        return 1
    else:
        return 0
    
 def horizontalStreak(self, row, col, state, streak):
     consecutiveCount = 0
     for j in range(col, 7):
         if state[row][j].lower() == state[row][col].lower():
             consecutiveCount += 1
        else:
            break
    if consecutiveCount >= streak:
        return 1
    else:
        return 0
    
 def diagonalCheck(self, row, col, state, streak):
     total = 0
        # check for diagonals with positive slope
     consecutiveCount = 0
     j = col
     for i in range(row, 6):
         if j > 6:
             break
         elif state[i][j].lower() == state[row][col].lower():
             consecutiveCount += 1
        else:
            break
        j += 1 # increment column when row is incremented
    if consecutiveCount >= streak:
        total += 1

        # check for diagonals with negative slope
    consecutiveCount = 0
    j = col
    for i in range(row, -1, -1):
        if j > 6:
            break
        elif state[i][j].lower() == state[row][col].lower():
            consecutiveCount += 1
        else:
            break
        j += 1 # increment column when row is incremented
    if consecutiveCount >= streak:
        total += 1
    return total

        
        
if __name__ == '__main__':
    model = [[0,0,2],[1,2,0],[1,2,0]]
    print(heuristic(1,model))