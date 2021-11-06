from cube import Cube

class Solver:
    def __init__(self, cube):
        self.cube = cube
        self.solved_cube = Cube()
    def solve(self, cube):
        moves = cube.func_list
        for move in moves:
            tmp = move()
            print(tmp.state)
            if (tmp == self.solved_cube):
                print('solved with ', move)
                exit()
        for move in moves:
            self.solve(move())
    def is_solved(self, cube):
        if cube == self.solved_cube:
            return True
        return False

    def dls(self, curr, target, max_depth, list_of_actions):
        if (curr == target):
            return True, list_of_actions
        
        if (max_depth <= 0): return False
        for i in curr.graph_of_moves[list_of_actions[-1]]:
                list_of_actions.append(i)
                curr = i()
                solved, list_of_actions = self.dls(curr, target, max_depth - 1, list_of_actions)
                if (solved):
                    return True, list_of_actions
        return False, []

    def iddfs(self, start_cube, min_depth, max_depth, list_of_actions):

        if (start_cube == self.solved_cube):
            return True, []
        for depth in range(min_depth, max_depth):
            for i in start_cube.func_list:
                list_of_actions = []
                list_of_actions.append(i)
                curr = i()
                solved, list_actions = self.dls(curr, self.solved_cube, max_depth, list_of_actions)
                if (solved):
                    print(list_actions)
                    exit()
            



test = Cube()

print(test.graph_of_moves)
test = test.front()
test = test.up()
print("INITIAL STATE:", test.state)
solver = Solver(test)
solver.iddfs(test, 0, 1, [])