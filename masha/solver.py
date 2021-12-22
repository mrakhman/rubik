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
    def calculated_white_side_corners(self):
        # don't change the order inside dict!
        return {
            'BL': [self.state['U'][0][0], self.state['L'][0][0], self.state['B'][0][2]],# 'wrg'],
            'RB': [self.state['U'][0][2], self.state['B'][0][0], self.state['R'][0][2]],# 'wgo'],
            'FR': [self.state['U'][2][2], self.state['R'][0][0], self.state['F'][0][2]],# 'wob'],
            'LF': [self.state['U'][2][0], self.state['F'][0][0], self.state['L'][0][2]],# 'wbr'],
        }

    @property
    def calculated_yellow_side_corners(self):
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
        # self.print_state()
        # print(self.runned_spins)

        self.solve_correct_side_centers()
        self.print_state()
        # print(self.runned_spins)
        return True

    # def __get_white_side_corners(self):
    #     return {
    #         'ULB': [self.state['U'][0][0], self.state['L'][0][0], self.state['B'][0][2], 'wrg'],
    #         'UBR': [self.state['U'][0][2], self.state['B'][0][0], self.state['R'][0][2], 'wgo'],
    #         'URF': [self.state['U'][2][2], self.state['R'][0][0], self.state['F'][0][2], 'wob'],
    #         'UFL': [self.state['U'][2][0], self.state['F'][0][0], self.state['L'][0][2], 'wbr'],
    #     }

    # def __get_yellow_side_corners(self):
    #     return {
    #         'DLF': [self.state['D'][0][0], self.state['L'][2][2], self.state['F'][2][0], 'yrb'],
    #         'DFR': [self.state['D'][0][2], self.state['F'][2][2], self.state['R'][2][0], 'ybo'],
    #         'DRB': [self.state['D'][2][2], self.state['R'][2][2], self.state['B'][2][0], 'yog'],
    #         'DBL': [self.state['D'][2][0], self.state['B'][2][2], self.state['L'][2][0], 'ygr'],
    #     }

    # step 2
    def solve_white_side(self):
        """
        Check if there are white corners, but in a wrong place, move them out
        """
        # white_side_corners = self.__get_white_side_corners()
        # for corner in list(white_side_corners.keys()):
        #     is_corner_white = white_side_corners[corner][0] == 'w'
        #     is_corner_in_correct_place_and_position = white_side_corners[corner][0] == 'w' and white_side_corners[corner][1] == SIDE_COLORS[corner[1]] and white_side_corners[corner][2] == SIDE_COLORS[corner[2]]
        #     is_corner_between_its_centers = 
        #     if is_corner_white:
        #         if not is_corner_in_place:
        #             self.run_moves([corner[2], 'B', corner[2] + "'", "B'"])

        """
        Move correct white corner to correct side
        """
        # yellow_side_corners = self.__get_yellow_side_corners()
        
        # on yellow side find an element with white sticker
        # put this element between its centers

        # white_corner_on_yellow_side = list(yellow_side_corners.keys())[list(yellow_side_corners.values()).index(16)]
        # def place_one_white_corner_from_yellow_side(yellow_side_corners):
    
    @staticmethod
    def contains_color_in_corners(corners, color):
        for corner in corners:
            if color in corner:
                return True
        return False


    def solve_white_corners_on_yellow_side(self):
        for corner in list(self.calculated_white_side_corners.keys()):
            print(corner, self.calculated_yellow_side_corners[corner])
            is_white_corner = 'w' in self.calculated_yellow_side_corners[corner]
            if is_white_corner:
                print('hohoho')
                is_white_corner_between_its_centers = all(item in ['w', UP_DOWN_CORRECT_CORNERS[corner][0], UP_DOWN_CORRECT_CORNERS[corner][1]] for item in self.calculated_yellow_side_corners[corner])
                print('is_white_corner_between_its_centers', is_white_corner_between_its_centers)
                if not is_white_corner_between_its_centers:
                    self.run_moves(['D'])
                
                else:
                    is_white_corner_in_correct_position = WHITE_SIDE_CORRECT_CORNERS[corner] == self.calculated_yellow_side_corners[corner]
                    n_spins = 0
                    while (not is_white_corner_in_correct_position):
                        self.run_moves([corner[0], 'B', corner[0] + "'", "B'"])
                        is_white_corner_in_correct_position = WHITE_SIDE_CORRECT_CORNERS[corner] == self.calculated_yellow_side_corners[corner]
                        n_spins += 1
        
        if self.contains_color_in_corners(list(self.calculated_yellow_side_corners.values()), 'w'):
            print('yes')
            return self.solve_white_corners_on_yellow_side()
        else:
            print(list(self.calculated_yellow_side_corners.values()))
            return True

        # self.print_state()


            
            




        





cube = Cube_beginner()
# cube.run_moves(["R", "U", "R'", "U'", "L", "B"])
cube.run_moves(['U', 'R2', 'F', 'B', 'R', 'B2', 'R', 'U2', 'L', 'B2', 'R', "U'", "D'", 'R2', 'F', "R'", 'L', 'B2', 'U2', 'F2'])

new = Solver_beginner(cube)
print(new.has_white_cross())


# new.print_state()
new.solve_white_cross_with_correct_side_centers()
# print(new.has_white_cross(), new.has_correct_side_centers())

new.solve_white_corners_on_yellow_side()
new.print_state()
