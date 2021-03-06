from copy import deepcopy


class Colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    PINK = '\033[95m' # pink
    CYAN = '\033[96m' # light blue
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Cube:
    def  __init__(self):
        self.state = {
            'F': [
                ['b', 'b', 'b'],
                ['b', 'b', 'b'],
                ['b', 'b', 'b']],
            'R': [
                ['o', 'o', 'o'],
                ['o', 'o', 'o'],
                ['o', 'o', 'o']],
            'U': [
                ['w', 'w', 'w'],
                ['w', 'w', 'w'],
                ['w', 'w', 'w']],
            'B': [
                ['g', 'g', 'g'],
                ['g', 'g', 'g'],
                ['g', 'g', 'g']],
            'L': [
                ['r', 'r', 'r'],
                ['r', 'r', 'r'],
                ['r', 'r', 'r']],
            'D': [
                ['y', 'y', 'y'],
                ['y', 'y', 'y'],
                ['y', 'y', 'y']]
        }
        self.n_spins = 0
        self.runned_spins = []
        self.shuffle_spins = []


    @staticmethod
    def is_side_solved(side):
        first_row = side[0]
        for row in side:
            if not row == first_row:
                return False
        return True

    def is_cube_solved(self):
        for side in self.state:
            if not self.is_side_solved(self.state[side]):
                return False
        return True

    @staticmethod
    def print_inline(row):
        for i in range(len(row)):
            if row[i] == 'r':
                print(Colors.RED + Colors.BOLD + row[i] + Colors.ENDC, end =" ")
            elif row[i] == 'y':
                print(Colors.YELLOW + Colors.BOLD + row[i] + Colors.ENDC, end =" ")
            elif row[i] == 'b':
                print(Colors.BLUE + Colors.BOLD + row[i] + Colors.ENDC, end =" ")
            elif row[i] == 'g':
                print(Colors.GREEN + Colors.BOLD + row[i] + Colors.ENDC, end =" ")
            elif row[i] == 'o':
                print(Colors.PINK + Colors.BOLD + row[i] + Colors.ENDC, end =" ")
            else:
                print(Colors.BOLD + row[i] + Colors.ENDC, end =" ")

    def print_state(self):
        for row in self.state['U']:
            print("       ", end= " ")
            self.print_inline(row)
            print()
        print()

        for i in range(len(self.state['L'])):
            self.print_inline(self.state['L'][i])
            print(" ", end= " ")
            self.print_inline(self.state['F'][i])
            print(" ", end= " ")
            self.print_inline(self.state['R'][i])
            print(" ", end= " ")
            self.print_inline(self.state['B'][i])
            print()

        print()
        for row in self.state['D']:
            print("       ", end= " ")
            self.print_inline(row)
            print()
        print()

    def front(self):
        self.n_spins += 1
        prev_state = deepcopy(self.state)
        # L -> U
        self.state['U'][2][0] = prev_state['L'][2][2]
        self.state['U'][2][1] = prev_state['L'][1][2]
        self.state['U'][2][2] = prev_state['L'][0][2]
        # D -> L
        self.state['L'][0][2] = prev_state['D'][0][0]
        self.state['L'][1][2] = prev_state['D'][0][1]
        self.state['L'][2][2] = prev_state['D'][0][2]
        # R -> D
        self.state['D'][0][0] = prev_state['R'][2][0]
        self.state['D'][0][1] = prev_state['R'][1][0]
        self.state['D'][0][2] = prev_state['R'][0][0]
        # U -> R
        self.state['R'][0][0] = prev_state['U'][2][0]
        self.state['R'][1][0] = prev_state['U'][2][1]
        self.state['R'][2][0] = prev_state['U'][2][2]

        # F rotate +90
        self.state['F'] = list(map(list, zip(*prev_state['F'][::-1])))

    def front_prime(self):
        self.n_spins += 1
        prev_state = deepcopy(self.state)
        # U -> L
        self.state['L'][0][2] = prev_state['U'][2][2]
        self.state['L'][1][2] = prev_state['U'][2][1]
        self.state['L'][2][2] = prev_state['U'][2][0]
        # L -> D
        self.state['D'][0][0] = prev_state['L'][0][2]
        self.state['D'][0][1] = prev_state['L'][1][2]
        self.state['D'][0][2] = prev_state['L'][2][2]
        # D -> R
        self.state['R'][2][0] = prev_state['D'][0][0]
        self.state['R'][1][0] = prev_state['D'][0][1]
        self.state['R'][0][0] = prev_state['D'][0][2]
        # R -> U
        self.state['U'][2][0] = prev_state['R'][0][0]
        self.state['U'][2][1] = prev_state['R'][1][0]
        self.state['U'][2][2] = prev_state['R'][2][0]

        # F rotate -90
        self.state['F'] = list(map(list, zip(*prev_state['F'])))[::-1]

    def front_double(self):
        self.front()
        self.front()
        self.n_spins -= 1 # extract 1 spin because 2 self.front() give us 2 spins, and we want to count double spin as 1 spin

    def right(self):
        self.n_spins += 1
        prev_state = deepcopy(self.state)
        # F -> U
        self.state['U'][0][2] = prev_state['F'][0][2]
        self.state['U'][1][2] = prev_state['F'][1][2]
        self.state['U'][2][2] = prev_state['F'][2][2]
        # D -> F
        self.state['F'][0][2] = prev_state['D'][0][2]
        self.state['F'][1][2] = prev_state['D'][1][2]
        self.state['F'][2][2] = prev_state['D'][2][2]
        # B -> D
        self.state['D'][0][2] = prev_state['B'][2][0]
        self.state['D'][1][2] = prev_state['B'][1][0]
        self.state['D'][2][2] = prev_state['B'][0][0]
        # U -> B
        self.state['B'][0][0] = prev_state['U'][2][2]
        self.state['B'][1][0] = prev_state['U'][1][2]
        self.state['B'][2][0] = prev_state['U'][0][2]

        # R rotate +90
        self.state['R'] = list(map(list, zip(*prev_state['R'][::-1])))

    def right_prime(self):
        self.n_spins += 1
        prev_state = deepcopy(self.state)
        # U -> F
        self.state['F'][0][2] = prev_state['U'][0][2]
        self.state['F'][1][2] = prev_state['U'][1][2]
        self.state['F'][2][2] = prev_state['U'][2][2]
        # F -> D
        self.state['D'][0][2] = prev_state['F'][0][2]
        self.state['D'][1][2] = prev_state['F'][1][2]
        self.state['D'][2][2] = prev_state['F'][2][2]
        # D -> B
        self.state['B'][2][0] = prev_state['D'][0][2]
        self.state['B'][1][0] = prev_state['D'][1][2]
        self.state['B'][0][0] = prev_state['D'][2][2]
        # B -> U
        self.state['U'][2][2] = prev_state['B'][0][0]
        self.state['U'][1][2] = prev_state['B'][1][0]
        self.state['U'][0][2] = prev_state['B'][2][0]

        # R rotate -90
        self.state['R'] = list(map(list, zip(*prev_state['R'])))[::-1]

    def right_double(self):
        self.right()
        self.right()
        self.n_spins -= 1 # extract 1 spin because 2 self.right() give us 2 spins, and we want to count double spin as 1 spin

    def left(self):
        self.n_spins += 1
        prev_state = deepcopy(self.state)
        # B -> U
        self.state['U'][2][0] = prev_state['B'][0][2]
        self.state['U'][1][0] = prev_state['B'][1][2]
        self.state['U'][0][0] = prev_state['B'][2][2]
        # D -> B
        self.state['B'][0][2] = prev_state['D'][2][0]
        self.state['B'][1][2] = prev_state['D'][1][0]
        self.state['B'][2][2] = prev_state['D'][0][0]
        # F -> D
        self.state['D'][0][0] = prev_state['F'][0][0]
        self.state['D'][1][0] = prev_state['F'][1][0]
        self.state['D'][2][0] = prev_state['F'][2][0]
        # U -> F
        self.state['F'][0][0] = prev_state['U'][0][0]
        self.state['F'][1][0] = prev_state['U'][1][0]
        self.state['F'][2][0] = prev_state['U'][2][0]

        # L rotate +90
        self.state['L'] = list(map(list, zip(*prev_state['L'][::-1])))

    def left_prime(self):
        self.n_spins += 1
        prev_state = deepcopy(self.state)
        # U -> B
        self.state['B'][0][2] = prev_state['U'][2][0]
        self.state['B'][1][2] = prev_state['U'][1][0]
        self.state['B'][2][2] = prev_state['U'][0][0]
        # B -> D
        self.state['D'][2][0] = prev_state['B'][0][2]
        self.state['D'][1][0] = prev_state['B'][1][2]
        self.state['D'][0][0] = prev_state['B'][2][2]
        # D -> F
        self.state['F'][0][0] = prev_state['D'][0][0]
        self.state['F'][1][0] = prev_state['D'][1][0]
        self.state['F'][2][0] = prev_state['D'][2][0]
        # F -> U
        self.state['U'][0][0] = prev_state['F'][0][0]
        self.state['U'][1][0] = prev_state['F'][1][0]
        self.state['U'][2][0] = prev_state['F'][2][0]

        # L rotate -90
        self.state['L'] = list(map(list, zip(*prev_state['L'])))[::-1]

    def left_double(self):
        self.left()
        self.left()
        self.n_spins -= 1 # extract 1 spin because 2 self.left() give us 2 spins, and we want to count double spin as 1 spin

    def back(self):
        self.n_spins += 1
        prev_state = deepcopy(self.state)
        # U -> L
        self.state['L'][0][0] = prev_state['U'][0][2]
        self.state['L'][1][0] = prev_state['U'][0][1]
        self.state['L'][2][0] = prev_state['U'][0][0]
        # L -> D
        self.state['D'][2][0] = prev_state['L'][0][0]
        self.state['D'][2][1] = prev_state['L'][1][0]
        self.state['D'][2][2] = prev_state['L'][2][0]
        # D -> R
        self.state['R'][2][2] = prev_state['D'][2][0]
        self.state['R'][1][2] = prev_state['D'][2][1]
        self.state['R'][0][2] = prev_state['D'][2][2]
        # R -> U
        self.state['U'][0][0] = prev_state['R'][0][2]
        self.state['U'][0][1] = prev_state['R'][1][2]
        self.state['U'][0][2] = prev_state['R'][2][2]

        # B rotate +90
        self.state['B'] = list(map(list, zip(*prev_state['B'][::-1])))

    def back_prime(self):
        self.n_spins += 1
        prev_state = deepcopy(self.state)
        # L -> U
        self.state['U'][0][0] = prev_state['L'][2][0]
        self.state['U'][0][1] = prev_state['L'][1][0]
        self.state['U'][0][2] = prev_state['L'][0][0]
        # D -> L
        self.state['L'][0][0] = prev_state['D'][2][0]
        self.state['L'][1][0] = prev_state['D'][2][1]
        self.state['L'][2][0] = prev_state['D'][2][2]
        # R -> D
        self.state['D'][2][0] = prev_state['R'][2][2]
        self.state['D'][2][1] = prev_state['R'][1][2]
        self.state['D'][2][2] = prev_state['R'][0][2]
        # U -> R
        self.state['R'][0][2] = prev_state['U'][0][0]
        self.state['R'][1][2] = prev_state['U'][0][1]
        self.state['R'][2][2] = prev_state['U'][0][2]

        # B rotate -90
        self.state['B'] = list(map(list, zip(*prev_state['B'])))[::-1]

    def back_double(self):
        self.back()
        self.back()
        self.n_spins -= 1 # extract 1 spin because 2 self.back() give us 2 spins, and we want to count double spin as 1 spin

    def up(self):
        self.n_spins += 1
        prev_state = deepcopy(self.state)
        # L -> B
        self.state['B'][0][0] = prev_state['L'][0][0]
        self.state['B'][0][1] = prev_state['L'][0][1]
        self.state['B'][0][2] = prev_state['L'][0][2]
        # F -> L
        self.state['L'][0][0] = prev_state['F'][0][0]
        self.state['L'][0][1] = prev_state['F'][0][1]
        self.state['L'][0][2] = prev_state['F'][0][2]
        # R -> F
        self.state['F'][0][0] = prev_state['R'][0][0]
        self.state['F'][0][1] = prev_state['R'][0][1]
        self.state['F'][0][2] = prev_state['R'][0][2]
        # B -> R
        self.state['R'][0][0] = prev_state['B'][0][0]
        self.state['R'][0][1] = prev_state['B'][0][1]
        self.state['R'][0][2] = prev_state['B'][0][2]

        # U rotate +90
        self.state['U'] = list(map(list, zip(*prev_state['U'][::-1])))

    def up_prime(self):
        self.n_spins += 1
        prev_state = deepcopy(self.state)
        # B -> L
        self.state['L'][0][0] = prev_state['B'][0][0]
        self.state['L'][0][1] = prev_state['B'][0][1]
        self.state['L'][0][2] = prev_state['B'][0][2]
        # L -> F
        self.state['F'][0][0] = prev_state['L'][0][0]
        self.state['F'][0][1] = prev_state['L'][0][1]
        self.state['F'][0][2] = prev_state['L'][0][2]
        # F -> R
        self.state['R'][0][0] = prev_state['F'][0][0]
        self.state['R'][0][1] = prev_state['F'][0][1]
        self.state['R'][0][2] = prev_state['F'][0][2]
        # R -> B
        self.state['B'][0][0] = prev_state['R'][0][0]
        self.state['B'][0][1] = prev_state['R'][0][1]
        self.state['B'][0][2] = prev_state['R'][0][2]

        # U rotate -90
        self.state['U'] = list(map(list, zip(*prev_state['U'])))[::-1]

    def up_double(self):
        self.up()
        self.up()
        self.n_spins -= 1 # extract 1 spin because 2 self.up() give us 2 spins, and we want to count double spin as 1 spin

    def down(self):
        self.n_spins += 1
        prev_state = deepcopy(self.state)
        # L -> F
        self.state['F'][2][0] = prev_state['L'][2][0]
        self.state['F'][2][1] = prev_state['L'][2][1]
        self.state['F'][2][2] = prev_state['L'][2][2]
        # B -> L
        self.state['L'][2][0] = prev_state['B'][2][0]
        self.state['L'][2][1] = prev_state['B'][2][1]
        self.state['L'][2][2] = prev_state['B'][2][2]
        # R -> B
        self.state['B'][2][0] = prev_state['R'][2][0]
        self.state['B'][2][1] = prev_state['R'][2][1]
        self.state['B'][2][2] = prev_state['R'][2][2]
        # F -> R
        self.state['R'][2][0] = prev_state['F'][2][0]
        self.state['R'][2][1] = prev_state['F'][2][1]
        self.state['R'][2][2] = prev_state['F'][2][2]

        # D rotate +90
        self.state['D'] = list(map(list, zip(*prev_state['D'][::-1])))

    def down_prime(self):
        self.n_spins += 1
        prev_state = deepcopy(self.state)
        # F -> L
        self.state['L'][2][0] = prev_state['F'][2][0]
        self.state['L'][2][1] = prev_state['F'][2][1]
        self.state['L'][2][2] = prev_state['F'][2][2]
        # L -> B
        self.state['B'][2][0] = prev_state['L'][2][0]
        self.state['B'][2][1] = prev_state['L'][2][1]
        self.state['B'][2][2] = prev_state['L'][2][2]
        # B -> R
        self.state['R'][2][0] = prev_state['B'][2][0]
        self.state['R'][2][1] = prev_state['B'][2][1]
        self.state['R'][2][2] = prev_state['B'][2][2]
        # R -> F
        self.state['F'][2][0] = prev_state['R'][2][0]
        self.state['F'][2][1] = prev_state['R'][2][1]
        self.state['F'][2][2] = prev_state['R'][2][2]

        # D rotate -90
        self.state['D'] = list(map(list, zip(*prev_state['D'])))[::-1]

    def down_double(self):
        self.down()
        self.down()
        self.n_spins -= 1 # extract 1 spin because 2 self.down() give us 2 spins, and we want to count double spin as 1 spin


    def run_moves(self, moves, is_shuffle = False):
        mapper = {
            'F': self.front,
            "F'": self.front_prime,
            'F2': self.front_double,

            'R': self.right,
            "R'": self.right_prime,
            'R2': self.right_double,

            'U': self.up,
            "U'": self.up_prime,
            'U2': self.up_double,

            'B': self.back,
            "B'": self.back_prime,
            'B2': self.back_double,

            'L': self.left,
            "L'": self.left_prime,
            'L2': self.left_double,

            'D': self.down,
            "D'": self.down_prime,
            'D2': self.down_double,
        }

        for move in moves:
            mapper[move]()
            if is_shuffle:
                self.shuffle_spins.append(move)
            else:
                self.runned_spins.append(move)


    def shuffle(self, moves):
        self.run_moves(moves, True)
