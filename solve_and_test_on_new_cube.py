from solve_cube.solver import Solver
from solve_cube.cube import Cube
from solve_cube.parse_input import parse_user_input


def run_solver(cube):
    solver = Solver(cube)
    solver.solve_cube()
    return solver


def test_spins_on_new_cube(solver, shuffle_spins):
    test_cube = Cube()
    test_cube.run_moves(shuffle_spins)
    test_cube.run_moves(solver.solving_moves)
    print("Run same shuffle and solving moves on a new cube:")
    test_cube.print_state()



if __name__ == "__main__":
    shuffle_spins = parse_user_input()
    if shuffle_spins:
        print("Initial cube:")
        cube = Cube()
        cube.print_state()
        print()
        print()

        print("Shuffled cube:")
        cube.shuffle(shuffle_spins)
        cube.print_state()
        print()
        print()

        print("Solving spins:")
        solver = run_solver(cube)
        solver.print_solving_spins()
        print()
        print("-", len(cube.runned_spins), "spins initially")
        print("-", len(solver.solving_moves), "spins after compression")
        print()
        print()

        print("Solved cube:")
        cube.print_state()
        print()


        test_spins_on_new_cube(solver, cube.shuffle_spins)




## Demo moved for cube:
# shuffle_moves = ["R", "U", "R'", "U'", "L", "B"]
# shuffle_moves = ['R2', 'L2', 'D', "B'", "R'", 'B2', 'U2', 'D', 'L', "B'", 'D2', 'L', 'B2', 'D2', 'R', 'F2', 'U2', 'L', 'U2']
# shuffle_moves = ['U', 'R2', 'F', 'B', 'R', 'B2', 'R', 'U2', 'L', 'B2', 'R', "U'", "D'", 'R2', 'F', "R'", 'L', 'B2', 'U2', 'F2']
# shuffle_moves = ['F', 'R', 'U', 'B', 'L', 'D']
# shuffle_moves = ['R', 'B', 'L', 'F']
# shuffle_moves = ['F', 'F', 'U2', "B'", "L'", "D'"]
# shuffle_moves = ['F', 'R', 'U2', "B'", "L'", "D'"]
# shuffle_moves = ['F', 'D', 'U2', "F'", 'B2', 'R', 'U', 'L', 'D2', "U'", 'D2', "B'", 'F2', 'L', 'D']
