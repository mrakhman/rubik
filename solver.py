from cube import *
import time
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

	def dls(self, move, curr, target, max_depth, list_of_actions):
		list_of_actions.append(move)
		tmp = move(curr)
		if (tmp == target):
			return True, list_of_actions
		if (max_depth <= 0):
			return False, list_of_actions
		for i in curr.graph_of_moves[list_of_actions[-1]]:
			solved, ret_list_of_actions = self.dls(i, tmp, target, max_depth - 1, deepcopy(list_of_actions))
			if (solved):
				return True, ret_list_of_actions
		return False, list_of_actions

	def iddfs(self, start_cube, min_depth, max_depth, list_of_actions):

		if (start_cube == self.solved_cube):
			return True, []
		for depth in range(min_depth, max_depth):
			print(depth)
			for i in start_cube.func_list:
				curr = start_cube
				solved, ret_list_actions = self.dls(i, curr,  self.solved_cube, depth, [])
				if (solved):
					print("solved:",  ret_list_actions)
					exit()
			



test = Cube()

test = shuffle(test, 26)
print("INITIAL STATE:", test.state)
solver = Solver(test)
start = time.time()
solver.iddfs(test, 0, 6, [])
end = time.time()
print(end - start)
