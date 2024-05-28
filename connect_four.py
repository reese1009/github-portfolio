# print the board
def print_board(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j], end=' ')
        print()


# set each element to '-'
def initialize_board(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            array[i][j] = '-'


# insert the given chip in the chosen column
def insert_chip(array, col, chip_type):
    for i in range(len(array) - 1):
        # go down till the last free slot in a column is found
        if array[i][col] == '-' and array[i + 1][col] != '-':
            array[i][col] = chip_type
            return i
    # if no found, this means last row it is
    array[len(array) - 1][col] = chip_type
    return len(array) - 1


# check possible winner
def check_if_winner(array, col, row, chip_type):
    lefttill, righttill = col - 1, col + 1
    r, c = len(array), len(array[0])
    # check how far to the left the current chip streak goes
    while lefttill >= 0:
        if array[row][lefttill] != chip_type:
            break
        lefttill -= 1
    # check same for right, up, and down
    while righttill < c:
        if array[row][righttill] != chip_type:
            break
        righttill += 1
    uptill, downtill = row - 1, row + 1
    while uptill >= 0:
        if array[uptill][col] != chip_type:
            break
        uptill -= 1
    while downtill < r:
        if array[downtill][col] != chip_type:
            break
        downtill += 1
    # if there is total of at least 4 chips, there is a winner
    if (righttill - lefttill - 1) >= 4 or (downtill - uptill - 1) >= 4: # change to meet requiremnets , filling board but not win
        return True
    return False


def board_is_full(board):
    for row in board:
        for chip in row:
            if chip == '-':
                return False
    return True


if __name__ == "__main__":

    # main logic
    height = int(input('What would you like the height of the board to be? '))
    length = int(input('What would you like the length of the board to be? '))
    # create and initialize board
    board = [[None for i in range(length)] for j in range(height)]
    initialize_board(board)
    number = 0
    chips = ['x', 'o']
    iteration = 1
    draw = True
    statement = True


    # loop till each plot is full
    while iteration <= height * length:
        print_board(board)
        if statement == True:
            print('\nPlayer 1: x')
            print('Player 2: o')
        statement = False

        # input which column
        col = int(input('\nPlayer ' + str(number + 1) + ': Which column would you like to choose? '))
        # insert in that column
        row = insert_chip(board, col, chips[number])
        # determine if last output results in a winner
        if check_if_winner(board, col, row, chips[number]):
            print_board(board)
            print("\nPlayer", (number + 1), "won the game!")
            draw = False
            break
        # for upcoming player
        number = (number + 1) % 2

        if board_is_full(board):
            print_board(board)
            print('\nDraw. Nobody wins.')
            break
