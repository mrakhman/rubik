VALID_MOVES = ('F', 'R', 'U', 'B', 'L', 'D', 'F2', 'R2', 'U2', 'B2', 'L2', 'D2', "F'", "R'", "U'", "B'", "L'", "D'")

# ['F'] side is ['U'][2][1], ['L'] is ['U'][1][0], ['B'] is ['U'][0][1] ...
WHITE_CROSS = {
            'F': [2, 1],
            'L': [1, 0],
            'B': [0, 1],
            'R': [1, 2],
        }

WHITE_CROSS_SIDES = ['F', 'L', 'B', 'R']
