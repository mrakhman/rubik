from cube import *
import time

#be problem instances must be at least 18 moves from the goal st
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

	def count_solved_corners(self, state):
		"""
	Count the number of aligned corners
		"""
		counter = 0
		for corner, corner_solved in zip(state[:, ::2, 0], self.solved_cube.state[:, ::2, 0]):
			if corner[0] == corner_solved[0]:
				counter += 1
			if(corner[1] == corner_solved[1]):
				counter += 1

		
		for corner, corner_solved in zip(state[:, ::2, 2], self.solved_cube.state[:, ::2, 2]):
			if corner[0] == corner_solved[0]:
				counter += 1
			if(corner[1] == corner_solved[1]):
				counter += 1
		return counter

	def count_solved_edges(self, state):
		"""
		Count the number of aligned edges
		"""
		counter = 0
		for edge, edge_solved in zip(state[:, ::2, :], self.solved_cube.state[:, ::2, :]):
			if (edge[0] == edge_solved[0]).all():
				counter += 1
			if (edge[1] == edge_solved[1]).all():
				counter += 1
		for edge, edge_solved in zip(state[:, :, 0], self.solved_cube.state[:, :, 0]):

			if (edge == edge_solved).all():
				counter += 1
			# if (edge[1] == edge_solved[1]).all():
			# 	counter += 1

		for edge, edge_solved in zip(state[:, :, 2], self.solved_cube.state[:, :, 2]):
			if (edge == edge_solved).all():
				counter += 1
			# if (edge[1] == edge_solved[1]).all():
			# 	counter += 1						
		return counter


	def prune(self, depth, state):
		"""
		Returns True if it makes no sense to proceed with the search further
		"""
		if depth == 1 and (self.count_solved_corners(state) < 4 or self.count_solved_edges(state) < 8):
			#If there are less than 4 corners aligned with the remaining 1 hand, or if there are less than 8 aligned edges, they will no longer be aligned.
			return True
		if depth == 2 and self.count_solved_edges(state) < 4:
			#If there are less than 4 edges aligned with the remaining 2 hands, they will not be aligned anymore
			return True
		if depth == 3 and self.count_solved_edges(state) < 2:
			#If there are less than 2 edges that are aligned with the remaining 3 hands, they will not be aligned anymore
			return True
		return False

	def dls(self, move, curr, target, max_depth, list_of_actions):
		list_of_actions.append(move)
		tmp = move(curr)
		if (tmp == target):
			return True, list_of_actions
		if (max_depth <= 0):
			return False, list_of_actions
		if (self.prune(max_depth, tmp.state) and curr != self.cube):
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

test = shuffle(test, 8)
print("INITIAL STATE:", test.state)
solver = Solver(test)
# print(solver.solved_cube.state)
# print(solver.count_solved_edges(test.state))
start = time.time()
solver.iddfs(test, 0, 20, [])
end = time.time()
print(end - start)/
