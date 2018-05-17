ideal_board=((1,2,3,4),(5,6,7,8),(9,10,11,12),(13,14,15,None))

def eval_pos(board):
    total=0
    for i in range(4):
        for x in range(4):
            if board[i][x] == ideal_board[i][x]:
                total +=1
    return total

