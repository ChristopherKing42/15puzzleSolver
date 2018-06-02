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
        moved = position[x][y]
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
            new_position.append((tuple(new_row)))
        rep.append((moved,tuple(new_position)))
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

def signmatch(n1,n2):
    if n1>0 and n2>0:
        return True
    elif n1<0 and n2<0:
        return True
    else:
        return False

def find_linear_conflicts(in_board): #Add only 1 per piece in linear conflict. This will lead to a total of 2 for every conflicted pair.
    lin_conf_total=0
    for i in range(4): #rows
        for z in range(4): #pieces
            tile=in_board[i][z]
            ny,nx=find_piece(in_board, tile)
            ny_,nx_=find_piece(win, tile)
            for o in range(4): #other tiles in that row
                other_tile=in_board[i][o]
                if other_tile != tile:
                    oy,ox=find_piece(in_board, other_tile)
                    oy_,ox_=find_piece(win, other_tile)
                    if ny==oy and ny_==oy_:
                        if (nx_>ox>nx) or (nx>ox>nx_) or (ox<nx<ox_) or (ox>nx>ox_) or (nx==ox_ and not signmatch(nx_-nx,ox_-ox)): #The last part is so that, if they are traveling in the same direction, they aren't counted
                            lin_conf_total+=1
            for j in range(4): #other tiles in that column
                other_tile=in_board[j][z]
                if other_tile != tile:
                    oy,ox=find_piece(in_board, other_tile)
                    oy_,ox_=find_piece(win, other_tile)
                    if nx==ox and nx_==ox_:
                        if (ny_>oy>ny) or (ny>oy>ny_) or (oy<ny<oy_) or (oy>ny>oy_) or (ny==oy_ and not signmatch(ny_-ny,oy_-oy)):
                            lin_conf_total+=1                       
    return lin_conf_total
            
def eval_pos(board, pathlength,e):
    total=0
    for num in [None]+range(1,15+1):
        (x,y) = find_piece(board,num)
        (x_,y_) = find_piece(win,num)
        total += abs(x-x_) + abs(y-y_)
    total+=find_linear_conflicts(board)
    return total*e+pathlength

epsilon=int(raw_input("What epsilon would you like? "))

start = ([(in_puzzle, 0, eval_pos(in_puzzle,0,epsilon),[])],set())

def Astar((tree,old)):
    best_f = 1000000000 # Big number
    best_node = None
    for node in tree:
        if node[2] < best_f:
            best_f = node[2]
            best_node = node

    tree.remove(best_node)
    old.add(best_node[0])
    #best_node is now the node with the best distance+heuristic
    new_poss = moves(best_node[0])
    for (moved,pos) in new_poss:
        if pos in old:
            continue
        g = best_node[1] + 1
        f = eval_pos(pos, g, epsilon)
        tree.append((pos, g, f, best_node[3]+[moved]))
    return best_node

def mainloop():
    x=1000
    best_node = Astar(start)
    while best_node[0] != win:
        if x == 1000:
            display(best_node[0])
            print best_node[1]
            print
            x=0
        best_node = Astar(start)
        x+=1
    print best_node
mainloop()
