from masha.solver import Solver
from masha.cube import Cube
import time
from masha.parse_input import parse_user_input


def run_solver_with_timer(cube):
    start_time = time.time()
    solver = Solver(cube)
    cube.print_state()
    print('Solved:')
    solver.solve_cube()
    print(len(solver.solving_moves))
    solver.print_solving_spins()
    cube.print_state()
    print()
    print("--- %s seconds ---" % (time.time() - start_time))
    print()
    return solver


def run_tester_cube(solver, shuffle_spins = []):
    test = Cube()
    test.run_moves(shuffle_spins)
    test.run_moves(solver.solving_moves)
    print("Run same shuffle and solving moves on new cube:")
    test.print_state()
    # print(len(solved_cube.solving_moves), solved_cube.solving_moves)



if __name__ == "__main__":
    cube = Cube()
    shuffle = parse_user_input()
    if shuffle:
        cube.run_moves(shuffle, True)
        solver = run_solver_with_timer(cube)
        run_tester_cube(solver, shuffle)
    else:
        # cube.run_moves(["R", "U", "R'", "U'", "L", "B"])
        cube.run_moves(['R2', 'L2', 'D', "B'", "R'", 'B2', 'U2', 'D', 'L', "B'", 'D2', 'L', 'B2', 'D2', 'R', 'F2', 'U2', 'L', 'U2'])
        # cube.run_moves(['U', 'R2', 'F', 'B', 'R', 'B2', 'R', 'U2', 'L', 'B2', 'R', "U'", "D'", 'R2', 'F', "R'", 'L', 'B2', 'U2', 'F2'])
        # cube.run_moves(['F', 'R', 'U', 'B', 'L', 'D'])
        # cube.run_moves(['R', 'B', 'L', 'F'])
        # cube.run_moves(['F', 'F', 'U2', "B'", "L'", "D'"])
        # cube.run_moves(['F', 'R', 'U2', "B'", "L'", "D'"])
        # cube.run_moves(['F', 'D', 'U2', "F'", 'B2', 'R', 'U', 'L', 'D2', "U'", 'D2', "B'", 'F2', 'L', 'D'])
        solver = run_solver_with_timer(cube)
        print(solver.solving_moves)
        cube.print_state()
        run_tester_cube(solver)

