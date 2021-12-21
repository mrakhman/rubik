from copy import deepcopy
from masha.masha_cube import Cube_beginner
from masha.constants import WHITE_CROSS, WHITE_CROSS_SIDES


class Solver_beginner(Cube_beginner):
    def __init__(self, cube):
        self.state = deepcopy(cube.state)
        self.n_spins = cube.n_spins
        self.runned_spins = cube.runned_spins
        self.solving_moves = []

    # TODO: unused
    def right_hand_algo(self):
        self.run_moves(["R", "U", "R'", "U'"])

    # TODO: unused
    def left_hand_algo(self):
        self.run_moves(["L'", "U'", "L", "U"])

    # helper method for step 1
    def has_white_cross(self):
        if (self.state['U'][1][1] == 'w'
        and self.state['U'][0][1] == 'w'
        and self.state['U'][2][1] == 'w'
        and self.state['U'][1][0] == 'w'
        and self.state['U'][1][2] == 'w'):
            return True
        return False

    # helper method for step 1
    def has_correct_side_centers(self):
        if (self.state['R'][0][1] == self.state['R'][1][1]
        and self.state['L'][0][1] == self.state['L'][1][1]
        and self.state['F'][0][1] == self.state['F'][1][1]
        and self.state['B'][0][1] == self.state['B'][1][1]):
            return True
        return False

    def solve_white_cross(self):
        if self.has_white_cross():
            return True

        """
        spin each of [L R F B] sides 4 times to check if cross is already there
        """
        for side in WHITE_CROSS_SIDES:
            n_spins = 0
            is_white_cross_piece_in_place = self.state['U'][WHITE_CROSS[side][0]][WHITE_CROSS[side][1]] == 'w'
            while (not is_white_cross_piece_in_place and n_spins < 4):
                self.run_moves([side])
                is_white_cross_piece_in_place = self.state['U'][WHITE_CROSS[side][0]][WHITE_CROSS[side][1]] == 'w'
                n_spins += 1
        
        if self.has_white_cross():
            return True

        """
        look for a cross by spinning the Up side + previous step
        """
        for side in WHITE_CROSS_SIDES:
            n_spins = 0
            is_white_cross_piece_in_place = self.state['U'][WHITE_CROSS[side][0]][WHITE_CROSS[side][1]] == 'w'
            while (not is_white_cross_piece_in_place and n_spins < 4):
                self.run_moves([side])
                is_white_cross_piece_in_place = self.state['U'][WHITE_CROSS[side][0]][WHITE_CROSS[side][1]] == 'w'
                n_spins += 1
            if not is_white_cross_piece_in_place:
                self.run_moves(['U'])

        if self.has_white_cross():
            return True
        # self.print_state()
        # print(self.runned_spins)

        """
        solve white pieces on third layer
        """
        for side in WHITE_CROSS_SIDES:
            if self.state['U'][WHITE_CROSS[side][0]][WHITE_CROSS[side][1]] != 'w':
                while self.state[side][0][1] != 'w' and self.state[side][2][1] != 'w':
                    self.run_moves(['D'])

                if self.state[side][0][1] == 'w':
                    self.run_moves([side + '2'])
                next_move = WHITE_CROSS_SIDES[WHITE_CROSS_SIDES.index(side) - 1]
                self.run_moves(["D", next_move, side + "'", next_move + "'"])

                # checkup, remove after tests
                if self.state['U'][WHITE_CROSS[side][0]][WHITE_CROSS[side][1]] == 'w':
                    print("good, third layer whte cross piece solved")
        # self.print_state()
        # print(self.runned_spins)
        return self.has_white_cross()

    def solve_correct_side_centers(self):
        if self.has_correct_side_centers():
            return True
        
        if not self.has_white_cross():
            print("White cross not solved")
            return False
        
        for side in WHITE_CROSS_SIDES:
            self.run_moves([side + '2'])
        
        for side in WHITE_CROSS_SIDES:
            while self.state[side][2][1] != self.state[side][1][1]:
                self.run_moves(['D'])
            self.run_moves([side + '2'])
        
        if self.has_correct_side_centers():
            return True
        
        
    # step 1
    def solve_white_cross_with_correct_side_centers(self):
        self.solve_white_cross()
        self.print_state()
        print(self.runned_spins)

        self.solve_correct_side_centers()
        self.print_state()
        print(self.runned_spins)
        return True

    # step 2
    def solve_white_side(self):
        pass
        # TODO: white side
    




        





cube = Cube_beginner()
cube.run_moves(["R", "U", "R'", "U'", "L", "B"])
# cube.run_moves(["R", "U"])

new = Solver_beginner(cube)
print(new.has_white_cross())


# new.print_state()
new.solve_white_cross_with_correct_side_centers()
print(new.has_white_cross(), new.has_correct_side_centers())

