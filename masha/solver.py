from copy import deepcopy
from masha.masha_cube import Cube_beginner

SIDE_FACES = ['F', 'B', 'R', 'L']

class Solver_beginner(Cube_beginner):
    def __init__(self, cube):
        self.state = deepcopy(cube.state)
        self.n_spins = cube.n_spins
        self.runned_spins = cube.runned_spins
        self.solving_moves = []

    def right_hand_algo(self):
        self.run_moves(["R", "U", "R'", "U'"])

    def left_hand_algo(self):
        self.run_moves(["L'", "U'", "L", "U"])
    # step 1 - white cross
    def has_white_cross(self):
        if (self.state['U'][1][1] == 'w'
        and self.state['U'][0][1] == 'w'
        and self.state['U'][2][1] == 'w'
        and self.state['U'][1][0] == 'w'
        and self.state['U'][1][2] == 'w'):
            return True
        return False
    
    def has_same_color_sides(self):
        if (self.state['R'][0][1] == self.state['R'][1][1]
        and self.state['L'][0][1] == self.state['L'][1][1]
        and self.state['F'][0][1] == self.state['F'][1][1]
        and self.state['B'][0][1] == self.state['B'][1][1]):
            return True
        return False
    
    def solve_white_cross(self):
        # spin each of 6 sides to check if cross is there
        for side in SIDE_FACES:
            n_spins = 0
            while (self.state['U'][2][1] != 'w'
            or self.state['U'][0][1] != 'w'
            or self.state['U'][0][1] != 'w'
            or n_spins < 3):
                self.run_moves([side])
                n_spins += 1

        





cube = Cube_beginner()
cube.run_moves(["R", "U", "R'", "U'"])

new = Solver_beginner(cube)
print(new.has_white_cross())

# new.run_moves(["R"])

new.print_state()
print(new.has_white_cross())
new.solve_white_cross()
new.print_state()
print(new.has_white_cross())


