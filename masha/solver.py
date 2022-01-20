from masha.constants import *

class Solver():
    def __init__(self, cube):
        self.cube = cube
        self.run_moves = cube.run_moves
        self.state = cube.state
        self.solving_moves = []


    @property
    def white_side_corners(self):
        # don't change the order in the dict
        return {
            'BL': [self.state['U'][0][0], self.state['L'][0][0], self.state['B'][0][2]], # 'wrg'
            'RB': [self.state['U'][0][2], self.state['B'][0][0], self.state['R'][0][2]], # 'wgo'
            'FR': [self.state['U'][2][2], self.state['R'][0][0], self.state['F'][0][2]], # 'wob'
            'LF': [self.state['U'][2][0], self.state['F'][0][0], self.state['L'][0][2]], # 'wbr'
        }


    @property
    def yellow_side_corners(self):
        # don't change the order in the dict
        return {
            'BL': [self.state['D'][2][0], self.state['B'][2][2], self.state['L'][2][0]], # 'ygr'
            'RB': [self.state['D'][2][2], self.state['R'][2][2], self.state['B'][2][0]], # 'yog'
            'FR': [self.state['D'][0][2], self.state['F'][2][2], self.state['R'][2][0]], # 'ybo'
            'LF': [self.state['D'][0][0], self.state['L'][2][2], self.state['F'][2][0]], # 'yrb'
        }


    @property
    def yellow_side_edges(self):
        return {
            'DF': [self.state['D'][0][1], self.state['F'][2][1]], # yb
            'DR': [self.state['D'][1][2], self.state['R'][2][1]], # yo
            'DB': [self.state['D'][2][1], self.state['B'][2][1]], # yg
            'DL': [self.state['D'][1][0], self.state['L'][2][1]], # yr
        }


    @property
    def second_layer_edges(self):
        return {
            'FR': [self.state['F'][1][2], self.state['R'][1][0]], # bo
            'RB': [self.state['R'][1][2], self.state['B'][1][0]], # og
            'BL': [self.state['B'][1][2], self.state['L'][1][0]], # gr
            'LF': [self.state['L'][1][2], self.state['F'][1][0]], # rb
        }


    def is_sticker_on_correct_side(self, sticker, side):
        return self.state[side][1][1] == sticker


################ Step 1 #########################
############# Yellow cross ######################
    # validation
    def has_white_cross(self):
        if (self.state['U'][1][1] == 'w'
        and self.state['U'][0][1] == 'w'
        and self.state['U'][2][1] == 'w'
        and self.state['U'][1][0] == 'w'
        and self.state['U'][1][2] == 'w'):
            return True
        return False


    # validation
    def has_correct_side_centers(self):
        if (self.state['R'][0][1] == self.state['R'][1][1]
        and self.state['L'][0][1] == self.state['L'][1][1]
        and self.state['F'][0][1] == self.state['F'][1][1]
        and self.state['B'][0][1] == self.state['B'][1][1]):
            return True
        return False


    # helper method
    def __solve_cross_from_first_layer(self):
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
        return self.has_white_cross()


    # validation
    def has_white_cross_piece_on_second_layer_or_down_side(self):
        for side in WHITE_CROSS_SIDES:
            if self.state[side][1][0] == 'w' or self.state[side][1][2] == 'w':
                return True
        if self.state['D'][0][1] == 'w' or self.state['D'][1][0] == 'w' or self.state['D'][1][2] == 'w' or self.state['D'][2][1] == 'w':
            return True
        return False


    # helper method
    def __solve_cross_from_second_layer(self):
        """
        look for a cross by spinning the Up side + previous step
        """
        while self.has_white_cross_piece_on_second_layer_or_down_side():
            self.run_moves(['U'])
            self.__solve_cross_from_first_layer()
        return self.has_white_cross()


    # validation
    def has_white_cross_piece_on_third_layer(self):
        for side in WHITE_CROSS_SIDES:
            if self.state[side][0][1] == 'w' or self.state[side][2][1] == 'w':
                return True
        return False


    # helper method
    def __solve_cross_from_third_layer(self):
        """
        solve white pieces on third layer
        """
        for side in WHITE_CROSS_SIDES:
            if self.state['U'][WHITE_CROSS[side][0]][WHITE_CROSS[side][1]] != 'w':
                n_spins = 0
                while self.state[side][0][1] != 'w' and self.state[side][2][1] != 'w' and n_spins < 4:
                    self.run_moves(['D'])
                    n_spins += 1
                if self.state[side][0][1] == 'w' or self.state[side][2][1] == 'w':
                    if self.state[side][0][1] == 'w':
                        self.run_moves([side + '2'])
                    next_move = WHITE_CROSS_SIDES[WHITE_CROSS_SIDES.index(side) - 1]
                    self.run_moves(["D", next_move, side + "'", next_move + "'"])
        return self.has_white_cross()


    def solve_white_cross(self):
        if self.has_white_cross():
            return True
        if self.has_white_cross_piece_on_second_layer_or_down_side():
            self.__solve_cross_from_first_layer()
        if self.has_white_cross_piece_on_second_layer_or_down_side():
            self.__solve_cross_from_second_layer()
        if self.has_white_cross_piece_on_third_layer():
            self.__solve_cross_from_third_layer()
        return self.solve_white_cross()


    def solve_correct_side_centers(self):
        for side in WHITE_CROSS_SIDES:
            self.run_moves([side + '2'])

        for side in WHITE_CROSS_SIDES:
            while (self.state[side][2][1] != self.state[side][1][1]) or (self.yellow_side_edges['D' + side][0] != 'w'):
                self.run_moves(['D'])
            self.run_moves([side + '2'])


    def step_1(self):
        if self.has_white_cross() and self.has_correct_side_centers():
            return True
        if not self.has_white_cross():
            self.solve_white_cross()
        if not self.has_correct_side_centers():
            self.solve_correct_side_centers()
        return self.step_1()


################ Step 2 #########################
############## White side #######################
    # validation
    def has_correct_white_side(self):
        if not self.has_white_cross() or not self.has_correct_side_centers():
            print("White cross got broken")
            return False
        for side in WHITE_CROSS_SIDES:
            if not self.state[side][0] == [self.state[side][1][1]] * 3:
                return False
        if self.state['U'] != [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']]:
            return False
        return True


    # helper method
    @staticmethod
    def has_color_in_pieces_list(color, pieces):
        for piece in pieces:
            if color in piece:
                return True
        return False


    # helper method
    @staticmethod
    def is_piece_between_its_centers(current_piece, correct_piece):
        return all(sticker in correct_piece for sticker in current_piece)


    # helper method
    def __move_correct_white_corner_to_correct_position(self, corner):
        is_white_corner_in_correct_position = self.white_side_corners[corner] == WHITE_SIDE_CORRECT_CORNERS[corner]
        while (not is_white_corner_in_correct_position):
            self.run_moves([corner[0], 'D', corner[0] + "'", "D'"])
            is_white_corner_in_correct_position = self.white_side_corners[corner] == WHITE_SIDE_CORRECT_CORNERS[corner]


    def solve_white_corners_on_yellow_side(self):
        for corner in list(self.yellow_side_corners.keys()):
            is_white_corner_between_its_centers = self.is_piece_between_its_centers(self.yellow_side_corners[corner], WHITE_SIDE_CORRECT_CORNERS[corner])
            is_white_corner_in_correct_position = self.white_side_corners[corner] == WHITE_SIDE_CORRECT_CORNERS[corner]

            if not is_white_corner_in_correct_position:
                n_spins = 0
                while not is_white_corner_between_its_centers and n_spins < 4:
                    self.run_moves(['D'])
                    is_white_corner_between_its_centers = self.is_piece_between_its_centers(self.yellow_side_corners[corner], WHITE_SIDE_CORRECT_CORNERS[corner])
                    n_spins += 1
                if is_white_corner_between_its_centers:
                    self.__move_correct_white_corner_to_correct_position(corner)


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
        if self.has_color_in_pieces_list('w', list(self.yellow_side_corners.values())):
            self.solve_white_corners_on_yellow_side()
        else:
            self.solve_white_corners_on_white_side()
        return self.step_2()


################ Step 3 #########################
############# Second layer ######################
    # validation
    def has_correct_second_layer(self):
        if not self.has_correct_white_side():
            print("White side got broken")
            return False

        for side in WHITE_CROSS_SIDES:
            if (not self.state[side][1][0] == self.state[side][1][1]) or (not self.state[side][1][2] == self.state[side][1][1]):
                return False
        return True


    # helper method
    def __piece_goes_to_left(self, first_edge, second_edge):
        self.run_moves([first_edge + "'", "D'", first_edge, 'D']) # left hand
        self.run_moves([second_edge, 'D', second_edge + "'", "D'"]) # right hand


    # helper method
    def __piece_goes_to_right(self, first_edge, second_edge):
        self.run_moves([first_edge, 'D', first_edge + "'", "D'"])
        self.run_moves([second_edge + "'", "D'", second_edge, 'D'])


    def solve_second_layer_from_yellow_side(self):
        def get_first_correct_edge_on_yellow_side():
            for edge in list(self.yellow_side_edges.keys()):
                if not 'y' in self.yellow_side_edges[edge]:
                    return [edge, self.yellow_side_edges[edge]]
            return None

        correct_edge_on_yellow_side = get_first_correct_edge_on_yellow_side()
        if not correct_edge_on_yellow_side:
            return True

        edge, piece = correct_edge_on_yellow_side
        n_spins = 0
        while edge[1] != OPPOSITE_COLOR_SIDES[piece[0]] and n_spins < 4:
            self.run_moves(['D'])
            edge = list(self.yellow_side_edges.keys())[list(self.yellow_side_edges.values()).index(piece)]
            n_spins += 1

        first_edge = COLOR_SIDE[piece[0]]
        second_edge = COLOR_SIDE[piece[1]]
        if piece in GOES_TO_LEFT:
            self.__piece_goes_to_left(first_edge, second_edge)
        elif piece in GOES_TO_RIGHT:
            self.__piece_goes_to_right(first_edge, second_edge)


    def move_correct_second_layer_edges_on_yellow_side(self):
        def get_first_correct_edge_on_second_layer():
            for edge in list(self.second_layer_edges.keys()):
                edge_in_correct_place = self.is_sticker_on_correct_side(self.second_layer_edges[edge][0], edge[0]) and self.is_sticker_on_correct_side(self.second_layer_edges[edge][1], edge[1])
                if (not 'y' in self.second_layer_edges[edge]) and (not edge_in_correct_place):
                    return edge
            return None
        edge = get_first_correct_edge_on_second_layer()
        if not edge:
            return True

        n_spins = 0
        opposite_side = OPPOSITE_SIDES[edge[0]]
        while self.state[opposite_side][2][1] != 'y' and self.yellow_side_edges['D' + opposite_side][1] != 'y' and n_spins < 4:
            self.run_moves(['D'])
            n_spins += 1

        first_edge = edge[0]
        second_edge = edge[1]
        self.__piece_goes_to_right(first_edge, second_edge)


    # helper method
    def __is_second_layer_edge_on_yellow_side(self):
        for piece in list(self.yellow_side_edges.values()):
            if piece[0] != 'y' and piece[1] != 'y':
                return True
        return False


    def step_3(self):
        if self.has_correct_second_layer():
            return True
        if self.__is_second_layer_edge_on_yellow_side():
            self.solve_second_layer_from_yellow_side()
        else:
            self.move_correct_second_layer_edges_on_yellow_side()
        return self.step_3()


################ Step 4 #########################
############# Yellow cross ######################
    # validation
    def has_yellow_cross(self):
        if not self.has_correct_second_layer():
            return False
        if (self.state['D'][1][1] != 'y'
        or self.state['D'][0][1] != 'y'
        or self.state['D'][2][1] != 'y'
        or self.state['D'][1][0] != 'y'
        or self.state['D'][1][2] != 'y'):
            return False
        return True


    # validation
    def __has_yellow_stick(self):
        has_yellow_stick_front = self.state['D'][1][0] == 'y' and self.state['D'][1][2] == 'y'
        if has_yellow_stick_front:
            return 'F'
        has_yellow_stick_right = self.state['D'][0][1] == 'y' and self.state['D'][2][1] == 'y'
        if has_yellow_stick_right:
            return 'R'
        return False


    def solve_yellow_cross_from_stick(self):
        yellow_stick = self.__has_yellow_stick()
        if yellow_stick == 'F':
            self.run_moves(['F', 'L', 'D', "L'", "D'", "F'"])
        if yellow_stick == 'R':
            self.run_moves(['R', 'F', 'D', "F'", "D'", "R'"])

    # validation
    def __has_yellow_nine_o_clock(self):
        if self.__has_yellow_stick():
            return False
        nine_o_clock_FR = self.state['D'][0][1] == 'y' and self.state['D'][1][2] == 'y'
        if nine_o_clock_FR:
            return 'FR'
        nine_o_clock_RB = self.state['D'][1][2] == 'y' and self.state['D'][2][1] == 'y'
        if nine_o_clock_RB:
            return 'RB'
        nine_o_clock_BL = self.state['D'][2][1] == 'y' and self.state['D'][1][0] == 'y'
        if nine_o_clock_BL:
            return 'BL'
        nine_o_clock_LF = self.state['D'][1][0] == 'y' and self.state['D'][0][1] == 'y'
        if nine_o_clock_LF:
            return 'LF'
        return False


    def solve_yellow_cross_from_nine_o_clock(self):
        nine_o_clock = self.__has_yellow_nine_o_clock()
        first_spin = OPPOSITE_SIDES[nine_o_clock[1]]
        second_spin = OPPOSITE_SIDES[nine_o_clock[0]]
        right_hand_algo = [second_spin, 'D', second_spin + "'", "D'"]
        self.run_moves([first_spin] + right_hand_algo + right_hand_algo + [first_spin + "'"])


    def solve_yellow_stick_from_dot(self):
        right_hand_algo = ['L', 'D', "L'", "D'"]
        self.run_moves(['F'] + right_hand_algo + right_hand_algo + ["F'"])


    def step_4(self):
        if self.has_yellow_cross():
            return True
        if self.__has_yellow_stick():
            self.solve_yellow_cross_from_stick()
        elif self.__has_yellow_nine_o_clock():
            self.solve_yellow_cross_from_nine_o_clock()
        else:
            self.solve_yellow_stick_from_dot()
        return self.step_4()


################ Step 5 #########################
############## Yellow side ######################
    # validation
    def has_yellow_side(self):
        if not self.has_yellow_cross():
            return False

        if len(self.__get_wrong_yellow_side_corners()) != 0:
            return False

        for corner in self.yellow_side_corners:
            if self.yellow_side_corners[corner] != YELLOW_SIDE_CORRECT_CORNERS[corner]:
                return False
        return True


    # helper method
    def __get_wrong_yellow_side_corners(self):
        wrong_corners = []
        for corner in list(self.yellow_side_corners.keys()):
            is_corner_between_its_centers = self.is_piece_between_its_centers(self.yellow_side_corners[corner], YELLOW_SIDE_CORRECT_CORNERS[corner])
            if not is_corner_between_its_centers:
                wrong_corners.append(corner)

        if len(wrong_corners) == 2 or len(wrong_corners) == 0:
            return wrong_corners
        self.run_moves(['D'])
        return self.__get_wrong_yellow_side_corners()


    # helper method
    def __swap_one_side_yellow_corners(self):
        corners = self.__get_wrong_yellow_side_corners()
        common_side = None
        if corners[0][0] == corners[1][1]:
            common_side = corners[0][0]
            left_hand_side = corners[0][1]
        elif corners[0][1] == corners[1][0]:
            common_side = corners[0][1]
            left_hand_side = corners[1][1]

        right_hand_algo = [common_side, 'D', common_side + "'", "D'"]
        self.run_moves(right_hand_algo * 3)
        left_hand_algo = [left_hand_side + "'", "D'", left_hand_side, 'D']
        self.run_moves(left_hand_algo * 3)


    # helper method
    def __swap_diagonal_yellow_corners(self):
        corners = self.__get_wrong_yellow_side_corners()
        right_hand_side = corners[0][1]
        right_hand_algo = [right_hand_side, 'D', right_hand_side + "'", "D'"]
        self.run_moves(right_hand_algo * 3)
        left_hand_side = corners[1][0]
        left_hand_algo = [left_hand_side + "'", "D'", left_hand_side, 'D']
        self.run_moves(left_hand_algo * 3)


    def put_yellow_side_corners_between_its_centers(self):
        wrong_corners = self.__get_wrong_yellow_side_corners()
        if len(wrong_corners) == 0:
            return True
        if wrong_corners[0][0] == wrong_corners[1][1] or wrong_corners[0][1] == wrong_corners[1][0]:
            self.__swap_one_side_yellow_corners()
        else:
            self.__swap_diagonal_yellow_corners()
        return self.put_yellow_side_corners_between_its_centers()


    def solve_yellow_side_corners(self):
        static_corner = list(YELLOW_SIDE_CORRECT_CORNERS.keys())[0] # 'BL'
        first_move_for_all_corners = static_corner[1] # 'L'
        for correct_corner in list(YELLOW_SIDE_CORRECT_CORNERS.keys()):
            is_yellow_corner_in_correct_position = self.yellow_side_corners[static_corner] == YELLOW_SIDE_CORRECT_CORNERS[correct_corner]
            while not is_yellow_corner_in_correct_position:
                self.run_moves([first_move_for_all_corners, 'U', first_move_for_all_corners + "'", "U'"])
                is_yellow_corner_in_correct_position = self.yellow_side_corners[static_corner] == YELLOW_SIDE_CORRECT_CORNERS[correct_corner]
            self.run_moves(["D"])


    def step_5(self):
        if self.has_yellow_side():
            return True
        if len(self.__get_wrong_yellow_side_corners()) != 0:
            self.put_yellow_side_corners_between_its_centers()
        else:
            self.solve_yellow_side_corners()
        return self.step_5()

################ Step 6 #########################
####### Edges on third layer centers ###############
    # validation
    def has_solved_cube(self):
        for side in self.state:
            if not self.is_side_solved(self.state[side]):
                return False
        return True


    # helper method
    @staticmethod
    def is_side_solved(side):
        first_row = side[0]
        for row in side:
            if not row == first_row:
                return False
        return True


    # helper method
    def __has_one_solved_edge(self):
        for side in WHITE_CROSS_SIDES:
            if self.is_side_solved(self.state[side]):
                return side
        return False


    def step_6(self):
        if self.has_solved_cube():
            return True
        solved_side = self.__has_one_solved_edge()
        if solved_side:
            right_hand = OPPOSITE_SIDES[WHITE_CROSS_SIDES[WHITE_CROSS_SIDES.index(solved_side) - 1]]
            left_hand = OPPOSITE_SIDES[right_hand]
            right_hand_algo = [right_hand, 'D', right_hand + "'", "D'"]
            left_hand_algo = [left_hand + "'", "D'", left_hand, 'D']
            self.run_moves(right_hand_algo + left_hand_algo)
            self.run_moves(right_hand_algo * 5)
            self.run_moves(left_hand_algo * 5)
        else:
            tmp_solved_side = 'F'
            right_hand = OPPOSITE_SIDES[WHITE_CROSS_SIDES[WHITE_CROSS_SIDES.index(tmp_solved_side) - 1]]
            left_hand = OPPOSITE_SIDES[right_hand]
            right_hand_algo = [right_hand, 'D', right_hand + "'", "D'"]
            left_hand_algo = [left_hand + "'", "D'", left_hand, 'D']
            self.run_moves(right_hand_algo + left_hand_algo)
            self.run_moves(right_hand_algo * 5)
            self.run_moves(left_hand_algo * 5)
        return self.step_6()


################ Beautify #########################
    def __squeeze_spins(self, tmp):
        if len(tmp) > 1 and len(tmp[-1]) > 1 and tmp[-1][1] == '2':
            self.solving_moves.extend(tmp)
        elif len(tmp) == 2:
            if len(tmp[-1]) > 1 and tmp[-1][1] == "'":
                self.solving_moves.append(tmp[-1][0] + '2')
            else:
                self.solving_moves.append(tmp[-1] + '2')
        elif len(tmp) == 3:
            if len(tmp[-1]) > 1 and tmp[-1][1] == "'":
                self.solving_moves.append(tmp[-1][0])
            else:
                self.solving_moves.append(tmp[-1] + "'")
        elif len(tmp) == 4:
            pass
        elif len(tmp) > 4:
            ignore = 4 * (len(tmp) // 4)
            self.solving_moves.extend(tmp[ignore:])
        else:
            self.solving_moves.extend(tmp)


    def remove_extra_spins(self):
        self.solving_moves = []
        spins = self.cube.runned_spins
        if len(spins) > 0:
            tmp = [spins[0]]
        else:
            return
        for i in range(1, len(spins)):
            if spins[i] == spins[i - 1]:
                tmp.append(spins[i])
            else:
                self.__squeeze_spins(tmp)
                tmp = [spins[i]]
            if i == len(spins) - 1:
                self.__squeeze_spins(tmp)


    def print_solving_spins(self):
        if len(self.solving_moves) > 0:
            for move in self.solving_moves:
                print(move, end =" ")
            print()


    def solve_cube(self):
        self.step_1()
        self.step_2()
        self.step_3()
        self.step_4()
        self.step_5()
        self.step_6()
        self.remove_extra_spins()
        return True







# cube = CubeBeginner()
# # cube.run_moves(["R", "U", "R'", "U'", "L", "B"])
# cube.run_moves(['U', 'R2', 'F', 'B', 'R', 'B2', 'R', 'U2', 'L', 'B2', 'R', "U'", "D'", 'R2', 'F', "R'", 'L', 'B2', 'U2', 'F2'])

# start_time = time.time()
# new = SolverBeginner(cube)
# new.print_state()



# new.step_1()
# # new.print_state()
# print("White cross:", new.has_white_cross(), new.has_correct_side_centers())


# new.step_2()
# # new.print_state()
# print("White side:", new.has_correct_white_side())


# new.step_3()
# # new.print_state()
# print("Second layer:", new.has_correct_second_layer())


# print()
# new.step_4()
# # new.print_state()
# print("Yellow cross:", new.has_yellow_cross())


# new.step_5()
# # new.print_state()
# print("Yellow side:", new.has_yellow_side())


# new.step_6()
# new.print_state()
# print("Solved cube:", new.has_solved_cube())
# print(len(new.runned_spins), new.runned_spins)

# print()
# print("--- %s seconds ---" % (time.time() - start_time))
