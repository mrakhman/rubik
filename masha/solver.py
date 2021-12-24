from copy import deepcopy
from masha.masha_cube import Cube_beginner
from masha.constants import WHITE_CROSS, WHITE_CROSS_SIDES, SIDE_COLORS, UP_DOWN_CORRECT_CORNERS, WHITE_SIDE_CORRECT_CORNERS


class Solver_beginner(Cube_beginner):
    def __init__(self, cube):
        self.state = deepcopy(cube.state)
        self.n_spins = cube.n_spins
        self.runned_spins = cube.runned_spins
        self.solving_moves = []

    @property
    def white_side_corners(self):
        # don't change the order inside dict!
        return {
            'BL': [self.state['U'][0][0], self.state['L'][0][0], self.state['B'][0][2]],# 'wrg'],
            'RB': [self.state['U'][0][2], self.state['B'][0][0], self.state['R'][0][2]],# 'wgo'],
            'FR': [self.state['U'][2][2], self.state['R'][0][0], self.state['F'][0][2]],# 'wob'],
            'LF': [self.state['U'][2][0], self.state['F'][0][0], self.state['L'][0][2]],# 'wbr'],
        }

    @property
    def yellow_side_corners(self):
        # don't change the order inside dict!
        return {
            'BL': [self.state['D'][2][0], self.state['B'][2][2], self.state['L'][2][0]],# 'ygr'],
            'RB': [self.state['D'][2][2], self.state['R'][2][2], self.state['B'][2][0]],# 'yog'],
            'FR': [self.state['D'][0][2], self.state['F'][2][2], self.state['R'][2][0]],# 'ybo'],
            'LF': [self.state['D'][0][0], self.state['L'][2][2], self.state['F'][2][0]],# 'yrb'],
        }

    # TODO: unused
    def right_hand_algo(self):
        self.run_moves(["R", "U", "R'", "U'"])

    # TODO: unused
    def left_hand_algo(self):
        self.run_moves(["L'", "U'", "L", "U"])



################ Step 1 #########################

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
            if self.state[side][2][1] != self.state[side][1][1]:
                self.run_moves([side + '2'])
        
        for side in WHITE_CROSS_SIDES:
            while self.state[side][2][1] != self.state[side][1][1]:
                self.run_moves(['D'])
            self.run_moves([side + '2'])
        
        if self.has_correct_side_centers():
            return True
        

    def step_1(self):
        self.solve_white_cross()
        self.solve_correct_side_centers()
        return True
    

################ Step 2 #########################
    
    # helper method for step 2
    @staticmethod
    def has_color_in_pieces(color, corners):
        for corner in corners:
            if color in corner:
                return True
        return False

    # helper method for step 2
    @staticmethod
    def is_piece_between_its_centers(current_piece, correct_piece):
        return all(sticker in correct_piece for sticker in current_piece)

    # helper method for step 2
    def has_correct_white_side(self):
        for side in WHITE_CROSS_SIDES:
            if not self.state[side][0] == [self.state[side][1][1]] * 3:
                return False
        if self.state['U'] != [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']]:
            return False
        return True


    def solve_white_corners_on_yellow_side(self):
        for corner in list(self.white_side_corners.keys()):
            is_white_corner = 'w' in self.yellow_side_corners[corner]
            if is_white_corner:
                is_white_corner_between_its_centers = self.is_piece_between_its_centers(self.yellow_side_corners[corner], WHITE_SIDE_CORRECT_CORNERS[corner])
                if is_white_corner_between_its_centers:
                    is_white_corner_in_correct_position = self.white_side_corners[corner] == WHITE_SIDE_CORRECT_CORNERS[corner]
                    n_spins = 0
                    while (not is_white_corner_in_correct_position):
                        self.run_moves([corner[0], 'D', corner[0] + "'", "D'"])
                        is_white_corner_in_correct_position = self.white_side_corners[corner] == WHITE_SIDE_CORRECT_CORNERS[corner]
                        n_spins += 1
                else:
                    self.run_moves(['D'])


    def solve_white_corners_on_white_side(self):
        for corner in list(self.white_side_corners.keys()):
            is_white_corner_between_its_centers = self.is_piece_between_its_centers(self.white_side_corners[corner], WHITE_SIDE_CORRECT_CORNERS[corner])
            is_white_corner_in_correct_position = self.white_side_corners[corner] == WHITE_SIDE_CORRECT_CORNERS[corner]
            if is_white_corner_between_its_centers:
                while (not is_white_corner_in_correct_position):
                    self.run_moves([corner[0], 'D', corner[0] + "'", "D'"])
                    is_white_corner_in_correct_position = self.white_side_corners[corner] == WHITE_SIDE_CORRECT_CORNERS[corner]
            else:
                # Check if there are white corners, but in a wrong place, move them out and solve
                self.run_moves([corner[0], 'D', corner[0] + "'", "D'"])


    def step_2(self):
        if self.has_correct_white_side():
            return True
        if self.has_color_in_pieces('w', list(self.yellow_side_corners.values())):
            self.solve_white_corners_on_yellow_side()
        else:
            self.solve_white_corners_on_white_side()
        return self.step_2()


################ Step 3 #########################
    # def 
    def solse_second_layer(self):
        pass
    def step_3(self):
        pass


            
            




        





cube = Cube_beginner()
# cube.run_moves(["R", "U", "R'", "U'", "L", "B"])
cube.run_moves(['U', 'R2', 'F', 'B', 'R', 'B2', 'R', 'U2', 'L', 'B2', 'R', "U'", "D'", 'R2', 'F', "R'", 'L', 'B2', 'U2', 'F2'])

new = Solver_beginner(cube)
print(new.has_white_cross())
new.print_state()



new.step_1()
# print(new.runned_spins)
# new.print_state()
print(new.has_white_cross(), new.has_correct_side_centers())

# new.solve_white_corners_on_yellow_side()
# new.do_sketchy_shit()
# new.solve_white_corners_on_white_side()

new.step_2()

new.print_state()

print(new.has_correct_white_side())
