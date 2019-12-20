# Sudoku Solver
import pprint
from random import randrange
from random import sample

# creates a 9 x 9 matrix
def pattern(r,c): 
    return (3*(r%3)+r//3+c)%9

# randomizes numbers
def shuffle(s): 
    return sample(s,len(s)) 

def create_solved_board():
    rows  = [ g*3 + r for g in shuffle(range(3)) for r in shuffle(range(3)) ] 
    cols  = [ g*3 + c for g in shuffle(range(3)) for c in shuffle(range(3)) ]
    nums  = shuffle(range(1,10))
    
    board = [[nums[pattern(r,c)] for c in cols] for r in rows]
    return board

def add_empty_spaces(board):
    num_empty = randrange(0,81)
    cols = len(board)
    rows = len(board)
    for i in range(rows):
        for j in range(cols):
            coin_flip = randrange(0,2)
            if coin_flip != 1 and num_empty > 0: 
                board[i][j] = 0
                num_empty = num_empty - 1

def is_empty (bored): 
    cols = len(bored)
    rows = len(bored[0])
    for i in range(rows):
        for j in range(cols):
            if(bored[i][j] == 0):
                return (i, j) # (row, col)

    return None

def valid_input (bored, num, tup):
    cols = len(bored)
    rows = len(bored[0])
    row_num = tup[0]
    col_num = tup[1]

    # checks rows
    for i in range(rows):
        if bored[row_num][i] == num and col_num != i: 
            return False

    # checks cols
    for i in range(cols):
        if bored[i][col_num] == num and row_num != i: 
            return False
    
    # checks the 3x3 grid
    # divide by 3 to get grid index then multiply by 3 to find coordinates of top left corner of the 3x3 grid
    square_x = (col_num // 3) * 3
    square_y = (row_num // 3) * 3

    for i in range(square_y, square_y + 3):
        for j in range(square_x, square_x + 3):
            if bored[i][j] == num and (i,j) != tup:
                return False
    
    return True

def solver(bored):
    coordinate_tup = is_empty(bored)

    if not coordinate_tup:
        return True
    else:
        row, col = coordinate_tup

    for num in range(1,10):
        if valid_input(bored, num, coordinate_tup):
            bored[row][col] = num

            #checks if new input is valid for the rest of the board
            if solver(bored):
                return True
            
            #otherwise it makes the input 0 and then backtracks 
            bored[row][col] = 0

    return False


def print_board (bored):
    cols = len(bored)
    rows = len(bored[0])

    for i in range(rows):
        if i % 3 == 0 and i != 0: 
            print("-------------------")
        for j in range(cols):
            if j % 3 == 0 and j != 0:
                print("|", end = '')
            if j < 8:
                print(str(bored[i][j]) + " ", end = '')
            else:
                print(str(bored[i][j]) + " ")


test_board = [
                [7,8,0,4,0,0,1,2,0],
                [6,0,0,0,7,5,0,0,9],
                [0,0,0,6,0,1,0,7,8],
                [0,0,7,0,4,0,2,6,0],
                [0,0,1,0,5,0,9,3,0],
                [9,0,4,0,6,0,0,0,5],
                [0,7,0,3,0,0,0,1,2],
                [1,2,0,0,0,7,4,0,0],
                [0,4,9,2,0,6,0,0,7]
                ]

def main():
    print("THIS IS SOLVED BOARD")
    board = create_solved_board()
    print_board(board)
    print("\nTHIS IS AFTER ADDING EMPTY SPACES")
    add_empty_spaces(board)
    print_board(board)
    print("\nTHIS IS AFTER SOLVED")
    solver(board)
    print_board(board)

main()

