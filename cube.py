import numpy as np
import random
from copy import deepcopy


class Cube:
	def __init__(self):
		''' positioning of sides of rubik's cube is following:

		'''
		self.state = np.arange(0,27).reshape(3,3,3)
		self.actions = []
		self.func_list = [front_prime,  up_prime, front, front_double,  right, right_prime, right_double, 
						  up, up_double,  left, left_prime, left_double, 
						  back, back_prime, back_double,  down, down_prime, down_double] 
		self.graph_of_moves = {
			front: [front_double,  right, right_prime, right_double, 
								up, up_prime, up_double,  left, left_prime, left_double, 
								back, back_prime, back_double,  down, down_prime, down_double],
			front_prime: [front_double,  right, right_prime, right_double, 
								up, up_prime, up_double,  left, left_prime, left_double, 
								back, back_prime, back_double,  down, down_prime, down_double],
			front_double: [front, front_prime,  right, right_prime, right_double, 
								up, up_prime, up_double,  left, left_prime, left_double, 
								back, back_prime, back_double,  down, down_prime, down_double],
			right:     [front, front_prime, front_double, right_double, 
								up, up_prime, up_double,  left, left_prime, left_double, 
								back, back_prime, back_double,  down, down_prime, down_double],
			right_prime: [front, front_prime, front_double,  right_double, 
								up, up_prime, up_double,  left, left_prime, left_double, 
								back, back_prime, back_double,  down, down_prime, down_double],
			right_double: [front, front_prime, front_double,  right, right_prime, 
								up, up_prime, up_double,  left, left_prime, left_double, 
								back, back_prime, back_double,  down, down_prime, down_double],
			left: [front, front_prime, front_double,  right, right_prime, right_double, 
								up, up_prime, up_double,  left_double, 
								back, back_prime, back_double,  down, down_prime, down_double],
			left_prime: [front, front_prime, front_double,  right, right_prime, right_double, 
								up, up_prime, up_double,   left_double, 
								back, back_prime, back_double,  down, down_prime, down_double],
			left_double: [front, front_prime, front_double,  right, right_prime, right_double, 
								up, up_prime, up_double,  left, left_prime,
								back, back_prime, back_double,  down, down_prime, down_double],
			up: [front, front_prime, front_double,  right, right_prime, right_double, 
								up_double,  left, left_prime, left_double, 
								back, back_prime, back_double,  down, down_prime, down_double],
			up_prime: [front, front_prime, front_double,  right, right_prime, right_double, 
								up_double,  left, left_prime, left_double, 
								back, back_prime, back_double,  down, down_prime, down_double],
			up_double: [front, front_prime, front_double,  right, right_prime, right_double, 
								up, up_prime,  left, left_prime, left_double, 
								back, back_prime, back_double,  down, down_prime, down_double],
			down: [front, front_prime, front_double,  right, right_prime, right_double, 
								up, up_prime, up_double,  left, left_prime, left_double, 
								back, back_prime, back_double,  down_double],

			down_prime: [front, front_prime, front_double,  right, right_prime, right_double, 
								up, up_prime, up_double,  left, left_prime, left_double, 
								back, back_prime, back_double,  down_double],
			down_double: [front, front_prime, front_double,  right, right_prime, right_double, 
								up, up_prime, up_double,  left, left_prime, left_double, 
								back, back_prime, back_double,  down, down_prime],
			back: [front, front_prime, front_double,  right, right_prime, right_double, 
								up, up_prime, up_double,  left, left_prime, left_double, 
								back_double,  down, down_prime, down_double],
			back_prime: [front, front_prime, front_double,  right, right_prime, right_double, 
								up, up_prime, up_double,  left, left_prime, left_double, 
								back_double,  down, down_prime, down_double],
			back_double: [front, front_prime, front_double,  right, right_prime, right_double, 
								up, up_prime, up_double,  left, left_prime, left_double, 
								back, back_prime, down, down_prime, down_double]
				}


		# self.func_list = [self.front, self.front_prime, self.up_prime]
	def __eq__(self, other):
		equal = False
		if (isinstance(other, self.__class__)):
			equal = (self.state == other.state).all()
		return equal

	def __ne__(self, other):
		return not self.__eq__(other)

def front(cube):
	tmp = deepcopy(cube)
	tmp.state[0] = np.rot90(tmp.state[0], k=-1)
	return tmp

def front_prime(cube):
	tmp = deepcopy(cube)
	tmp.state[0] = np.rot90(tmp.state[0], k=1)
	return tmp

def front_double(cube):
	tmp = deepcopy(cube)
	tmp.state[0] = np.rot90(tmp.state[0], k=2)
	return tmp

def right(cube):
	tmp = deepcopy(cube)
	tmp.state[:, :, 2] = np.rot90(tmp.state[:, :, 2], k=1)
	return tmp

def right_prime(cube):
	tmp = deepcopy(cube)
	tmp.state[:, :, 2] = np.rot90(tmp.state[:,:, 2], k=-1)
	return tmp
	
def right_double(cube):
	tmp = deepcopy(cube)
	tmp.state[:,:, 2] = np.rot90(tmp.state[:, :, 2], k=2)
	return tmp

def left(cube):
	tmp = deepcopy(cube)
	tmp.state[:, :, 0] = np.rot90(tmp.state[:, :, 0], k=1)
	return tmp
   
def left_prime(cube):
	tmp = deepcopy(cube)
	tmp.state[:, :, 0] = np.rot90(tmp.state[:,:, 0], k=-1)
	return tmp

def left_double(cube):
	tmp = deepcopy(cube)
	tmp.state[:,:, 0] = np.rot90(tmp.state[:, :, 0], k=2)
	return tmp

def up(cube):
	tmp = deepcopy(cube)
	tmp.state[:, 0, :] = np.rot90(tmp.state[:, 0, :], k=1)
	return tmp
	
def up_prime(cube):
	tmp = deepcopy(cube)
	tmp.state[:, 0, :] = np.rot90(tmp.state[:, 0, :], k=-1)
	return tmp
	
def up_double(cube):
	tmp = deepcopy(cube)
	tmp.state[:, 0, :] = np.rot90(tmp.state[:, 0, :], k=2)
	return tmp

def back(cube):
	tmp = deepcopy(cube)
	tmp.state[2] = np.rot90(tmp.state[2], k=1)
	return tmp

def back_prime(cube):
	tmp = deepcopy(cube)
	tmp.state[2] = np.rot90(tmp.state[2], k=-1)
	return tmp

def back_double(cube):
	tmp = deepcopy(cube)
	tmp.state[2] = np.rot90(tmp.state[2], k=2)
	return tmp

def down(cube):
	tmp = deepcopy(cube)
	tmp.state[:,2,:] = np.rot90(tmp.state[:,2,:], k=-1)
	return tmp
	
def down_prime(cube):
	tmp = deepcopy(cube)
	tmp.state[:,2,:] = np.rot90(cube.state[:,2,:], k=1)
	return tmp

def down_double(cube):
	tmp = deepcopy(cube)
	tmp.state[:, 2,:] = np.rot90(cube.state[:,2,:], k=2)
	return tmp

def shuffle(cube, num_shuffles, verbose=True):
	for i in range(num_shuffles):
		move = random.choice(cube.func_list)
		cube = move(cube)
		if verbose:
			print(move)
	return cube
