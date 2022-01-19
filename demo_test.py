from masha.solver import Solver
from masha.cube import Cube


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
    print("Initial cube:")
    cube = Cube()
    cube.print_state()
    print()

    print("Shuffled cube:")
    shuffle_moves = ['R2', 'L2', 'D', "B'", "R'", 'B2', 'U2', 'D', 'L', "B'", 'D2', 'L', 'B2', 'D2', 'R', 'F2', 'U2', 'L', 'U2']
    cube.shuffle(shuffle_moves)
    cube.print_state()
    print()

    print("Solving spins:")
    solver = run_solver(cube)
    print(len(solver.solving_moves))
    solver.print_solving_spins()
    print()

    print("Solved cube:")
    cube.print_state()
    print()


    test_spins_on_new_cube(solver, cube.shuffle_spins)




## Demo moved for cube:
# cube.run_moves(["R", "U", "R'", "U'", "L", "B"])
# cube.run_moves(['R2', 'L2', 'D', "B'", "R'", 'B2', 'U2', 'D', 'L', "B'", 'D2', 'L', 'B2', 'D2', 'R', 'F2', 'U2', 'L', 'U2'])
# cube.run_moves(['U', 'R2', 'F', 'B', 'R', 'B2', 'R', 'U2', 'L', 'B2', 'R', "U'", "D'", 'R2', 'F', "R'", 'L', 'B2', 'U2', 'F2'])
# cube.run_moves(['F', 'R', 'U', 'B', 'L', 'D'])
# cube.run_moves(['R', 'B', 'L', 'F'])
# cube.run_moves(['F', 'F', 'U2', "B'", "L'", "D'"])
# cube.run_moves(['F', 'R', 'U2', "B'", "L'", "D'"])
# cube.run_moves(['F', 'D', 'U2', "F'", 'B2', 'R', 'U', 'L', 'D2', "U'", 'D2', "B'", 'F2', 'L', 'D'])
