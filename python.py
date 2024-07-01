def main():
    solve(board)
    print_board(board)

board = [
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

def solve(bo):
    # base case, once we reach this case, ie we return True
    # we have found our solution
    # find will be set as  the index i,j = row,col
    find = find_empty(bo)
    # if there are no more empty spaces, end the recurssion
    if not find:
        return True
    else:
        row,col = find
    for i in range(1,10):
        if valid(bo, i, (row,col)):
            # if valid add to the board
            bo[row][col] = i
            # will call solve again with the added value we just did
            if solve(bo):
                return True
            bo[row][col] = 0
    # if we looped through the whole thing and none of them are valid
    # we will backtrack with bo[row][col] is incorrect
    return False




# checks to see if a board is valid or not
def valid(bo, num, pos):
    # check row 

    for i in range(len(bo[0])):
        # makes sure that if it the position we just inserted, we ignore that position
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    # check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    
    # check box, uses integer division to see what box we are in
    # integer division
    # box will be labeled as 
    # 00 01 02
    # 10 11 12
    # 20 21 22

    box_x = pos[1] // 3
    box_y = pos[0] // 3
# why multiply by 3? well, for the furest right we be used if we get a 2, this index starts at 6
# if we are at 2, we need to multiply by 3 to get to index 6
    for i in range(box_y * 3, box_y*3+3):
        for j in range(box_x * 3, box_x*3+3):
            # checks to see if any value we just place already exits to return False
            if bo[i][j] == num and (i,j) != pos:
                return False
    return True

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            # this separates the board for better UI, after there rows we get this line diver
            print("- - - - - - - - - - - -")
        # length of rows
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end ="")

def find_empty(bo):
    # 9
    for i in range(len(bo)):
        # 9
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i,j) #row, col
    # if there are no squares equal to zero, will return True as well in the solve function
    return None

if __name__ == "__main__":
    main()