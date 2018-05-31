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
    rep = []
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

def find_piece(position, num = None):
    for row in range(4):
        for column in range(4):
            if position[row][column] == num:
                return row, column

def eval_pos(board, pathlength):
    total=0
    for num in [None]+range(1,15+1):
        (x,y) = find_piece(board,num)
        (x_,y_) = find_piece(win,num)
        total += abs(x-x_) + abs(y-y_)
    return total+pathlength


start = ([([in_puzzle], 0, eval_pos(in_puzzle,0))],set())

def Astar((tree,old)):
    best_f = 1000000 # Big number
    best_node = None
    for node in tree:
        if node[2] < best_f:
            best_f = node[2]
            best_node = node

    tree.remove(best_node)
    old.add(best_node[0][0])
    #best_node is now the node with the best distance+heuristic
    new_poss = moves(best_node[0][0])
    for pos in new_poss:
        if pos in old:
            continue
        g = best_node[1] + 1
        f = eval_pos(pos, g)
        tree.append(([pos]+best_node[0], g, f))
    return best_node

def mainloop():
    x=0
    best_node = Astar(start)
    while True:
        if x == 1000:
            display(best_node[0][0])
            print
            x=0
        best_node = Astar(start)
        x+=1
    
# mainloop()
