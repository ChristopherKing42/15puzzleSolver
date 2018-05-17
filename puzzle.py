win=((1,2,3,4),(5,6,7,8),(9,10,11,12),(13,14,15,None))

def null_piece(position):
    for row in range(4):
        for column in range(4):
            if position[row][column] == None:
                return row, column
                
def neighbors((x,y)): return [(x_,y_) for (x_,y_) in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)] if 0 <= x_ and x_ < 4 and 0 <= y_ and y_ < 4]

def moves(position):
    return [position]

def eval_pos(board):
    total=0
    for i in range(4):
        for x in range(4):
            if board[i][x] == win[i][x]:
                total +=1
    return total
