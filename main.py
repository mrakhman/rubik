from masha.solver import Solver
from masha.cube import Cube
import time
from masha.parse_input import parse_user_input


def run_solver_with_timer(cube):
    start_time = time.time()
    solver = Solver(cube)
    solver.solve_cube()
    print("--- %s seconds to solve ---" % (time.time() - start_time))
    print()
    return solver


def print_initial_cube(cube):
    print('Shuffled cube:')
    cube.print_state()
    print()
    print()


def print_solving_spins(solver, cube):
    print("Solving spins:")
    solver.print_solving_spins()
    print()
    print("-", len(cube.runned_spins), "spins initially")
    print("-", len(solver.solving_moves), "spins after compression")
    print()
    print()


def print_solved_cube(cube):
    print('Solved cube:')
    cube.print_state()


if __name__ == "__main__":
    cube = Cube()
    shuffle_spins = parse_user_input()
    if shuffle_spins:
        cube.shuffle(shuffle_spins)

        print_initial_cube(cube)
        solver = run_solver_with_timer(cube)
        print_solving_spins(solver, cube)
        print_solved_cube(cube)

    # else:
    #     shuffle_moves = ['R2', 'L2', 'D', "B'", "R'", 'B2', 'U2', 'D', 'L', "B'", 'D2', 'L', 'B2', 'D2', 'R', 'F2', 'U2', 'L', 'U2']
    #     cube.shuffle(shuffle_moves)

    #     print_initial_cube(cube)
    #     solver = run_solver_with_timer(cube)
    #     print_solving_spins(solver, cube)
    #     print_solved_cube(cube)



## Demo moved for cube:
# shuffle_moves = ["R", "U", "R'", "U'", "L", "B"]
# shuffle_moves = ['R2', 'L2', 'D', "B'", "R'", 'B2', 'U2', 'D', 'L', "B'", 'D2', 'L', 'B2', 'D2', 'R', 'F2', 'U2', 'L', 'U2']
# shuffle_moves = ['U', 'R2', 'F', 'B', 'R', 'B2', 'R', 'U2', 'L', 'B2', 'R', "U'", "D'", 'R2', 'F', "R'", 'L', 'B2', 'U2', 'F2']
# shuffle_moves = ['F', 'R', 'U', 'B', 'L', 'D']
# shuffle_moves = ['R', 'B', 'L', 'F']
# shuffle_moves = ['F', 'F', 'U2', "B'", "L'", "D'"]
# shuffle_moves = ['F', 'R', 'U2', "B'", "L'", "D'"]
# shuffle_moves = ['F', 'D', 'U2', "F'", 'B2', 'R', 'U', 'L', 'D2', "U'", 'D2', "B'", 'F2', 'L', 'D']
