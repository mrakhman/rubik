from enum import Enum
from masha.constants import VALID_MOVES
import sys

class Moves(Enum):
    D = "D"
    D_DOUBLE = "D2"
    D_PRIME = "D'"


def parse_user_input():
    args = sys.argv
    if len(args) < 2:
        return "Error: Add 1 argument - moves string"
    if len(args) > 2:
        return "Error: Too many arguments, only 1 moves string is allowed"
    
    moves = list(args[1].split())

    for move in moves:
        if not move in VALID_MOVES:
            return "Error: Invalid moves"
    return moves

# print(parse_user_input())



# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]]

# # +90
# rot_clockwise = list(map(list, zip(*matrix[::-1])))

# # -90
# rot_conter_clockwise = list(map(list, zip(*matrix)))[::-1]

# print(rot_clockwise)
# # 7, 4, 1
# # 8, 5, 2
# # 9, 6, 3

# print(rot_conter_clockwise)
# # 3, 6, 9
# # 2, 5, 8
# # 1, 4, 7


# print(matrix)
