from masha.constants import VALID_MOVES
import sys


def give_valid_moves_example():
    print("Allowed moves: F R U B L D + F' R' U' B' L' D' + F2 R2 U2 B2 L2 D2\n")
    print("Valid string of moves: \"R2 B F D B2 F' D B L R' U' F2 U' L U2 B' F L' D2 U2 R F' U B F' L' R2 U2 B D2\"")


def parse_user_input():
    args = sys.argv
    if len(args) < 2 or len(args[1]) == 0:
        print("Error: Not enough arguments, add 1 string of moves\n")
        give_valid_moves_example()
        return False
    if len(args) > 2:
        print("Error: Too many arguments, only 1 string of moves is allowed\n")
        give_valid_moves_example()
        return False

    moves = list(args[1].split())

    for move in moves:
        if not move in VALID_MOVES:
            print("Error: Invalid moves\n")
            give_valid_moves_example()
            return False
    return moves
