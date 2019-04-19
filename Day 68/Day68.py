from enum import Enum


class Position:
    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def __add__(self, other):
        self.X = self.X + other.X
        self.Y = self.Y + other.Y
        return self

    def __repr__(self):
        return "({0},{1})".format(self.X, self.Y)

    def __str__(self):
        return "({0},{1})".format(self.X, self.Y)

    def __eq__(self, other):
        if self.X is other.X and self.Y is other.Y:
            return True
        elif self.X is other.Y and self.Y is other.X:
            return True
        else:
            return False


class Directions(Enum):
    top_left = 1
    top_right = 2
    bottem_left = 3
    bottem_right = 4


def print_board(board):
    for row in board:
        print(*row)


def build_board(bishops: Position, M):
    board = [[0 for j in range(M)] for i in range(M)]
    for bishop in bishops:
        board[bishop.X][bishop.Y] = 'b'
    return board


def diagonals(board, bishop, direction: str):
    res = []
    current_pos = Position(bishop.X, bishop.Y)
    while True:
        # update Position
        if direction is "tl":
            current_pos = current_pos + Position(-1, -1)
        elif direction is "tr":
            current_pos = current_pos + Position(1, -1)
        elif direction is "bl":
            current_pos = current_pos + Position(-1, 1)
        elif direction is "br":
            current_pos = current_pos + Position(1, 1)

        if direction is "tl":
            if current_pos.X < 0 or current_pos.Y < 0:
                break
        elif direction is "tr":
            if current_pos.X >= len(board) or current_pos.Y < 0:
                break
        elif direction is "bl":
            if current_pos.X < 0 or current_pos.Y >= len(board):
                break
        elif direction is "br":
            if current_pos.X >= len(board) or current_pos.Y >= len(board):
                break

        if board[current_pos.X][current_pos.Y] is 'b':
            res.append((Position(current_pos.X, current_pos.Y), bishop))
    return res


def check_all_diagonals(board, bishop):
    res = []
    top_left = diagonals(board, bishop, "tl")
    top_right = diagonals(board, bishop, "tr")
    bottem_left = diagonals(board, bishop, "bl")
    bottem_right = diagonals(board, bishop, "br")
    if len(top_left) is not 0:
        res.extend(top_left)
    if len(top_right) is not 0:
        res.extend(top_right)
    if len(bottem_left) is not 0:
        res.extend(bottem_left)
    if len(bottem_right) is not 0:
        res.extend(bottem_right)
    return res


def get_attack_count(board, bishops, M):
    unfiltered_res = []
    for bishop in bishops:
        cur_res = check_all_diagonals(board, bishop)
        if len(cur_res) is not 0:
            unfiltered_res.extend(cur_res)
    res = []
    for i in unfiltered_res:
        if i not in res and tuple(reversed(i)) not in res:
            res.append(i)
    return res


# build board
bishops = [Position(0, 0), Position(1, 2), Position(2, 2), Position(4, 0)]
M = 5
board = build_board(bishops, M)
# get attacks
final_results = get_attack_count(board, bishops, M)
# print Results
print_board(board)
print()
for index, final_result in enumerate(final_results):
    print(
        f"{index+1}) Bishop at Position {final_result[0]} attacks bishop at Position {final_result[1]}")
