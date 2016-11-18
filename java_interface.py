#!/pkg/python/3.5.1/bin/python3

import sys
import player
import board_model

go = True

while go:

  data = sys.stdin.readline().split(' ')

  if data[0]=='end' or data[0]=='end\n':
    go = False
    break
 
  if data[0]!='makeMoveWithState:':
    print('Bad input!');
  
  gravity = bool(data[1])
  cols,rows = int(data[2]),int(data[3])
  lastMoveCol,lastMoveRow = int(data[4]),int(data[5])
  deadline = int(data[6])
  k = int(data[7])
  
  board = [int(v) for v in reversed(data[8:])]
  
  state = board_model.BoardModel(cols,rows,k,gravity)
  count = 0
  for c in range(cols):
    for r in range(rows):
      state.pieces[c][r] = int(board.pop())
      if state.pieces[c][r] != 0: count += 1
  
  playerNumber = count % 2 + 1

  ai = player.AIPlayer(playerNumber,state,'ConnectKSource_python/LucidDreamAI.py')
  
  move = ai.get_move_with_time(state,deadline)
  
  print("ReturningTheMoveMade {} {}".format(move[0],move[1]))
  sys.stdout.flush()

exit()
