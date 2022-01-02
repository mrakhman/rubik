from masha.constants import VALID_MOVES
import sys


def parse_user_input():
    args = sys.argv
    if len(args) < 2:
        print("Error: Not enough arguments, add 1 string of moves")
        return False
    if len(args) > 2:
        print("Error: Too many arguments, only 1 string of moves is allowed")
        return False

    moves = list(args[1].split())

    for move in moves:
        if not move in VALID_MOVES:
            print("Error: Invalid moves")
            return False
    return moves
