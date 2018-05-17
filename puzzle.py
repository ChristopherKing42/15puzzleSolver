win = ((1,2,3,4),(5,6,7,8),(9,10,11,12),(13,14,15,None))
def null_piece(position):
    for row in range(4):
        for column in range(4):
            if position[row][column] == None:
                return row, column
                
