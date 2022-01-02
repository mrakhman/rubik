from masha.solver import SolverBeginner
from masha.cube_beginner import CubeBeginner
import time
from masha.parse_input import parse_user_input


cube = CubeBeginner()


def run_solver_with_timer(cube):
    start_time = time.time()
    new = SolverBeginner(cube)
    new.print_state()
    print('Solved:')
    new.solve_cube()
    # print(len(new.runned_spins), new.runned_spins)
    print(len(new.solving_moves))
    new.print_solving_spins()
    print()
    print("--- %s seconds ---" % (time.time() - start_time))
    print()
    return new


def run_tester_cube(solved_cube, shuffle_spins = []):
    test = CubeBeginner()
    test.run_moves(shuffle_spins)
    test.run_moves(solved_cube.solving_moves)
    print("Run same shuffle and solving moves on new cube:")
    test.print_state()
    # print(len(solved_cube.solving_moves), solved_cube.solving_moves)


shuffle = parse_user_input()

if shuffle:
    cube.run_moves(shuffle, True)
    solved_cube = run_solver_with_timer(cube)
    run_tester_cube(solved_cube, shuffle)

else:
    # cube.run_moves(["R", "U", "R'", "U'", "L", "B"])
    # cube.run_moves(['U', 'R2', 'F', 'B', 'R', 'B2', 'R', 'U2', 'L', 'B2', 'R', "U'", "D'", 'R2', 'F', "R'", 'L', 'B2', 'U2', 'F2'])
    cube.run_moves(['R2', 'L2', 'D', "B'", "R'", 'B2', 'U2', 'D', 'L', "B'", 'D2', 'L', 'B2', 'D2', 'R', 'F2', 'U2', 'L', 'U2'])
    # cube.run_moves(['F', 'R', 'U', 'B', 'L', 'D'])
    # cube.run_moves(['R', 'B', 'L', 'F'])
    # cube.run_moves(['F', 'F', 'U2', "B'", "L'", "D'"])
    # cube.run_moves(['F', 'R', 'U2', "B'", "L'", "D'"])
    # cube.run_moves(['F', 'D', 'U2', "F'", 'B2', 'R', 'U', 'L', 'D2', "U'", 'D2', "B'", 'F2', 'L', 'D'])

    solved_cube = run_solver_with_timer(cube)
    run_tester_cube(solved_cube)

    # print('rha:')
    # one = CubeBeginner()
    # rha = ['R', 'U', "R'", "U'"]
    # one.run_moves(rha * 5)
    # one.print_state()

    # print('Anti rha:')
    # two = CubeBeginner()
    # anti_rha = ["R'", "U'", 'R', 'U']
    # # anti_rha = ["U'", "R'", 'U', 'R']
    # two.run_moves(anti_rha)
    # two.print_state()
