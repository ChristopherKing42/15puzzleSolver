win=((1,2,3,4),(5,6,7,8),(9,10,11,12),(13,14,15,None))
in_puzzle=((1,7,2,12),(4,6,3,11),(8,10,15,5),(14,13,9,None)) #The puzzle which we are attempting to solve

def null_piece(position):
    for row in range(4):
        for column in range(4):
            if position[row][column] == None:
                return row, column
  
def neighbors((x,y)):
    return [(x_,y_) for (x_,y_) in [(x-1,y),(x+1,y),(x,y-1),(x,y+1)]
            if 0 <= x_ and x_ < 4 and 0 <= y_ and y_ < 4]

def moves(position):
    null_cell = null_piece(position)
    movable = neighbors(null_cell)
    rep = [position]
    for (x,y) in movable:
        new_position = []
        for row in range(4):
            new_row = []
            for column in range(4):
                if (row,column) == null_cell:
                    new_row.append(position[x][y])
                elif (row,column) == (x,y):
                    new_row.append(position[null_cell[0]][null_cell[1]])
                else:
                    new_row.append(position[row][column])
            new_position.append(tuple(new_row))
        rep.append(tuple(new_position))
    return rep

def display(position):
    for row in range(4):
        for column in range(4):
            if position[row][column]:
                print "{:>2} ".format(position[row][column]),
            else:
                print " _ ",
        print

def eval_pos(board):
    total=0
    for i in range(4):
        for x in range(4):
            if board[i][x] == win[i][x]:
                total +=1
    return total
