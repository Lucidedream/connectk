# -*- coding: utf-8 -*-
def check(model,player,connectk,row,col):
    count = 0
    for i in range(row):
        for j in range(col):
            if model[i][j] == player:
                count += verticalStreak(i,j,model,connectk)
                count += horizontalStreak(i,j,model,connectk)
                count += diagonalCheck(i,j,model,connectk)
               
    return count
    
def verticalStreak(row, col, state, streak):
    consecutiveCount = 0
    for i in range(row, 3):
        if state[i][col] == state[row][col]:
            consecutiveCount += 1
        else:
            break
    
    if consecutiveCount >= streak:
        return 1
    else:
        return 0
    
def horizontalStreak(row, col, state, streak):
    consecutiveCount = 0
    for j in range(col, 3):
        if state[row][j] == state[row][col]:
            consecutiveCount += 1
        else:
            break
    if consecutiveCount >= streak:
        return 1
    else:
        return 0
    
def diagonalCheck(row, col, state, streak):
    total = 0
        # check for diagonals with positive slope
    consecutiveCount = 0
    j = col
    for i in range(row, 3):
        print("i,j: ",i,j)
        if j >= 3:
            break
        elif state[i][j] == state[row][col]:
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
        if j >= 3:
            break
        elif state[i][j] == state[row][col]:
            consecutiveCount += 1
        else:
            break
        j += 1 # increment column when row is incremented
    if consecutiveCount >= streak:
        total += 1
    return total
if __name__ == '__main__':
    model = [[1,1,2],[1,2,0],[1,2,0]]
    print(check(model,1,2,3,3))