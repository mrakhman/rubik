from masha.solver import SolverBeginner
from masha.cube_beginner import CubeBeginner
import time


cube = CubeBeginner()
# cube.run_moves(["R", "U", "R'", "U'", "L", "B"])
# cube.run_moves(['U', 'R2', 'F', 'B', 'R', 'B2', 'R', 'U2', 'L', 'B2', 'R', "U'", "D'", 'R2', 'F', "R'", 'L', 'B2', 'U2', 'F2'])
cube.run_moves(['R', 'B', 'L', 'F'])

start_time = time.time()
new = SolverBeginner(cube)
new.print_state()


print('Solved:')
new.solve_cube()

print(len(new.runned_spins), new.runned_spins)

print()
print("--- %s seconds ---" % (time.time() - start_time))


test = CubeBeginner()
moves = new.solving_moves
test.run_moves(moves)
test.print_state()
print(len(new.solving_moves), new.solving_moves)


