# import numpy as np
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

class Cube_beginner:
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
    
    def front_double(self):
        self.front()
        self.front()
        self.n_spins -= 1 # extract 1 spin because 2 self.front() give us 2 spins, and we want to count double spin as 1 spin


test = Cube_beginner()
test.print_state()
test.front_double()


test.front_prime()
test.front_prime()
print('________________________________')
test.print_state()

print(test.n_spins)
