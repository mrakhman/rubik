from enum import Enum
from masha.constants import VALID_MOVES
class Moves(Enum):
    D = "D"
    D_DOUBLE = "D2"
    D_PRIME = "D'"


def parse_input():
    moves = list(input().split())
    for move in moves:
        if not move in VALID_MOVES:
            return False
    
    return True

print(parse_input())
