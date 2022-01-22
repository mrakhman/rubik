from solve_cube.solver import Solver
from solve_cube.cube import Cube
from solve_cube.parse_input import parse_user_input, write_to_file


def print_spins_inline(spins):
    if len(spins) > 0:
        for spin in spins:
            print(spin, end =" ")
        print()

def print_this_step_moves(prev_step_moves_len, solver, arr_of_steps):
    solver.remove_extra_spins()
    current_step_moves = solver.solving_moves
    current_step_moves_len = len(current_step_moves)
    print("N spins =", current_step_moves_len - prev_step_moves_len)
    print()
    print_spins_inline(current_step_moves[prev_step_moves_len:])
    print()
    arr_of_steps.append(current_step_moves[prev_step_moves_len:])

    cube.print_state()
    print("__________________________________________________\n")
    return current_step_moves_len


if __name__ == "__main__":
    arr_of_steps = []
    cube = Cube()
    shuffle_spins = parse_user_input()
    if shuffle_spins:

        cube.shuffle(shuffle_spins)
        solver = Solver(cube)

        print("Shuffled cube:\n")
        cube.print_state()
        print("__________________________________________________\n")


        print("Step 1 - solve white cross:\n")
        solver.step_1()
        step_1_moves_len = print_this_step_moves(0, solver, arr_of_steps)


        print("Step 2 - solve white side:\n")
        solver.step_2()
        step_2_moves_len = print_this_step_moves(step_1_moves_len, solver, arr_of_steps)


        print("Step 3 - second layer:\n")
        solver.step_3()
        step_3_moves_len = print_this_step_moves(step_2_moves_len, solver, arr_of_steps)


        print("Step 4 - yellow cross:\n")
        solver.step_4()
        step_4_moves_len = print_this_step_moves(step_3_moves_len, solver, arr_of_steps)


        print("Step 5 - yellow side:\n")
        solver.step_5()
        step_5_moves_len = print_this_step_moves(step_4_moves_len, solver, arr_of_steps)


        print("Step 6 - final step - Edges on third layer centers:\n")
        solver.step_6()
        step_6_moves_len = print_this_step_moves(step_5_moves_len, solver, arr_of_steps)


        print("Total number of spins:", len(solver.solving_moves))
        print()
        solver.print_solving_spins()

        write_to_file(shuffle_spins, *arr_of_steps)
