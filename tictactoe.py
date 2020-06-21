

# print('Enter cells: > ')
# raw = list(input())


grid = [['_' for x in range(3)] for y in range(3)]
print('---------')
for x in range(3):
    print('| ', end='')
    for y in range(3):
        # grid[x][y] = raw[x * 3 + y]
        print(grid[x][y], end=' ')
    print(' |')
print('---------')


#
def win():
    if (column() == 'x win') or (row() == 'x win') or (main_d() == 'x win') or (off_d() == 'x win'):
        return 'x win'
    if (column() == 'o win') or (row() == 'o win') or (main_d() == 'o win') or (off_d() == 'o win'):
        return 'o win'
    if (column() == 'impossible') or (row() == 'impossible') or (main_d() == 'impossible') or (
            off_d() == 'impossible'):
        return 'impossible'


#
#
def column():
    x = 0
    x_win = ""
    o_win = ""
    for y in range(3):
        if grid[x][y] == grid[x + 1][y] == grid[x + 2][y]:
            if grid[x][y] == 'X':
                x_win = 'x win'
            if grid[x][y] == 'O':
                o_win = 'o win'
    if (x_win == 'x win') & (o_win == 'o win'):
        return 'impossible'
    elif x_win == 'x win':
        return 'x win'
    elif o_win == 'o win':
        return 'o win'


def row():
    y = 0
    x_win = ""
    o_win = ""
    for x in range(3):
        if grid[x][y] == grid[x][y + 1] == grid[x][y + 2]:
            if grid[x][y] == 'X':
                x_win = 'x win'
            if grid[x][y] == 'O':
                o_win = 'o win'
    if (x_win == 'x win') & (o_win == 'o win'):
        return 'impossible'
    elif x_win == 'x win':
        return 'x win'
    elif o_win == 'o win':
        return 'o win'


def main_d():
    x_win = ""
    o_win = ""

    if grid[0][0] == grid[1][1] == grid[2][2]:
        if grid[0][0] == 'X':
            x_win = 'x win'
        if grid[0][0] == 'O':
            o_win = 'o win'
    if (x_win == 'x win') & (o_win == 'o win'):
        return 'impossible'
    elif x_win == 'x win':
        return 'x win'
    elif o_win == 'o win':
        return 'o win'


def off_d():
    x_win = ""
    o_win = ""
    if grid[0][2] == grid[1][1] == grid[2][0]:
        if grid[0][2] == 'X':
            x_win = 'x win'
        if grid[0][2] == "O":
            o_win = 'o win'
    if (x_win == 'x win') & (o_win == 'o win'):
        return 'impossible'
    elif x_win == 'x win':
        return 'x win'
    elif o_win == 'o win':
        return 'o win'


#
#
def draw():
    check: int = 0
    for x in range(3):
        for y in range(3):
            if grid[x][y] == '_':
                check = 1
    if (win() != 'x win') & (win() != 'o win') & (check != 1):
        return True
    else:
        return False


#
# def notfinished():
#     check: int = 0
#     for x in range(3):
#         for y in range(3):
#             if grid[x][y] == '_':
#                 check = 1
#     if (win() != 'x win') & (win() != 'o win') & (check == 1):
#         return True
#     else:
#         return False
#
#
# def impossible():
#     xno: int = 0
#     ono: int = 0
#     for x in range(3):
#         for y in range(3):
#             if grid[x][y] == 'X':
#                 xno = xno + 1
#             if grid[x][y] == 'O':
#                 ono = ono + 1
#     if (abs(xno - ono) >= 2) or (win() == 'impossible'):
#         return True
#     else:
#         return False
#
#
# if impossible():
#     print("Impossible")
#
# elif win() == "x win":
#     print("X wins")
#
# elif win() == "o win":
#     print("O wins")
#
# elif draw():
#     print("Draw")
#
# elif notfinished():
#     print("Game not finished")
iterate = 0
while iterate < 9:

    def val():
        print("Enter the coordinates: > ")
        val = input()
        conv = val.split()

        # cartesian = convert(conv)
        return conv


    def move(x):
        coordinate = x
        global iterate
        if grid[coordinate[0]][coordinate[1]] == "_":
            if iterate % 2 == 0:
                grid[coordinate[0]][coordinate[1]] = "X"

            else:
                grid[coordinate[0]][coordinate[1]] = "O"

        print('---------')
        for x in range(3):
            print('| ', end='')
            for y in range(3):
                print(grid[x][y], end=' ')
            print(' |')
        print('---------')
        if win() == "x win":
            print("X wins")
            exit()

        elif win() == "o win":
            print("O wins")
            exit()

        elif draw():
            print("Draw")
            exit()

        iterate = iterate + 1


    def condition():

        conv = val()

        a = 0
        for y in conv:
            if y.isdigit():
                a = a + 1

        if a != 2:
            print("You should enter numbers!")
            condition()
        cartesian = [3 - int(conv[1]), int(conv[0]) - 1]
        coordinate = cartesian

        if not ((-1 < coordinate[0] < 3) and (-1 < coordinate[1] < 3)):
            print("Coordinates should be from 1 to 3")
            condition()

        elif grid[coordinate[0]][coordinate[1]] != "_":
            print("The cell is occupied! Choose another one!")
            condition()

        else:
            move(coordinate)


    # def convert(x):
    #     conv = x
    #     cartesian = [3 - int(conv[1]), int(conv[0]) - 1]
    #     return cartesian

    condition()
