VALID_MOVES = ('F', 'R', 'U', 'B', 'L', 'D', 'F2', 'R2', 'U2', 'B2', 'L2', 'D2', "F'", "R'", "U'", "B'", "L'", "D'")

# ['F'] side is ['U'][2][1], ['L'] is ['U'][1][0], ['B'] is ['U'][0][1] ...
WHITE_CROSS = {
            'F': [2, 1],
            'L': [1, 0],
            'B': [0, 1],
            'R': [1, 2],
        }

WHITE_CROSS_SIDES = ['F', 'L', 'B', 'R']

# WHITE_CORNERS = {
#     'wrg': {'up_coordinate': [0, 0], 'first_color_coord': []},
#     'wgo': [0, 2],
#     'wob': [2, 2],
#     'wbr': [2, 0],
# }

SIDE_COLORS = {
    'U': 'w',
    'L': 'r',
    'R': 'o',
    'F': 'b',
    'B': 'g',
    'D': 'y',
}


UP_DOWN_CORRECT_CORNERS = {
    'BL': ['g', 'r'],
    'RB': ['o', 'g'],
    'FR': ['b', 'o'],
    'LF': ['r', 'b'],
}

WHITE_SIDE_CORRECT_CORNERS = {
    'BL': ['w', 'r', 'g'],
    'RB': ['w', 'g', 'o'],
    'FR': ['w', 'o', 'b'],
    'LF': ['w', 'b', 'r'],
}

# YELLOW_SIDE_CORRECT_CORNERS = {
#     'DBL': ['y', 'g', 'r'],
#     'DRB': ['y', 'o', 'g'],
#     'DFR': ['y', 'b', 'o'],
#     'DLF': ['y', 'r', 'b'],
# }

# WHITE_SIDE_CORRECT_CORNERS = {
#     'ULB': ['w', 'r', 'g'],
#     'UBR': ['w', 'g', 'o'],
#     'URF': ['w', 'o', 'b'],
#     'UFL': ['w', 'b', 'r'],
# }
