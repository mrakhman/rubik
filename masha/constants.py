VALID_MOVES = ('F', 'R', 'U', 'B', 'L', 'D', 'F2', 'R2', 'U2', 'B2', 'L2', 'D2', "F'", "R'", "U'", "B'", "L'", "D'")

# ['F'] side is ['U'][2][1], ['L'] is ['U'][1][0], ['B'] is ['U'][0][1] ...
WHITE_CROSS = {
            'F': [2, 1],
            'L': [1, 0],
            'B': [0, 1],
            'R': [1, 2],
        }

WHITE_CROSS_SIDES = ['F', 'L', 'B', 'R']

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

SIDE_COLOR = {
    'U': 'w',
    'L': 'r',
    'R': 'o',
    'F': 'b',
    'B': 'g',
    'D': 'y',
}

COLOR_SIDE = {
    'w': 'U',
    'r': 'L',
    'o': 'R',
    'b': 'F',
    'g': 'B',
    'y': 'D',
}

GOES_TO_RIGHT = [['o', 'g'], ['g', 'r'], ['r', 'b'], ['b', 'o']]

GOES_TO_LEFT = [['o', 'b'], ['g', 'o'], ['r', 'g'], ['b', 'r']]

# ob - left, og - right
# go - left, gr - right
# rg - left, rb - right
# br - left, bo - right
