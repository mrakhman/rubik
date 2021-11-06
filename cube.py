import numpy as np
import random
from copy import deepcopy
class Cube:
    def __init__(self):
        ''' positioning of sides of rubik's cube is following:

        '''

        self.state = np.arange(0,27).reshape(3,3,3)
        self.actions = []
        self.func_list = [self.front_prime,  self.up_prime, self.front, self.front_double,  self.right, self.right_prime, self.right_double, 
                          self.up, self.up_double,  self.left, self.left_prime, self.left_double, 
                          self.back, self.back_prime, self.back_double,  self.down, self.down_prime, self.down_double] 

        self.graph_of_moves = {
            self.front: [self.front_double,  self.right, self.right_prime, self.right_double, 
                                self.up, self.up_prime, self.up_double,  self.left, self.left_prime, self.left_double, 
                                self.back, self.back_prime, self.back_double,  self.down, self.down_prime, self.down_double],
            self.front_prime: [self.front_double,  self.right, self.right_prime, self.right_double, 
                                self.up, self.up_prime, self.up_double,  self.left, self.left_prime, self.left_double, 
                                self.back, self.back_prime, self.back_double,  self.down, self.down_prime, self.down_double],
            self.front_double: [self.front, self.front_prime,  self.right, self.right_prime, self.right_double, 
                                self.up, self.up_prime, self.up_double,  self.left, self.left_prime, self.left_double, 
                                self.back, self.back_prime, self.back_double,  self.down, self.down_prime, self.down_double],
            self.right:     [self.front, self.front_prime, self.front_double, self.right_double, 
                                self.up, self.up_prime, self.up_double,  self.left, self.left_prime, self.left_double, 
                                self.back, self.back_prime, self.back_double,  self.down, self.down_prime, self.down_double],
            self.right_prime: [self.front, self.front_prime, self.front_double,  self.right_double, 
                                self.up, self.up_prime, self.up_double,  self.left, self.left_prime, self.left_double, 
                                self.back, self.back_prime, self.back_double,  self.down, self.down_prime, self.down_double],
            self.right_double: [self.front, self.front_prime, self.front_double,  self.right, self.right_prime, 
                                self.up, self.up_prime, self.up_double,  self.left, self.left_prime, self.left_double, 
                                self.back, self.back_prime, self.back_double,  self.down, self.down_prime, self.down_double],
            self.left: [self.front, self.front_prime, self.front_double,  self.right, self.right_prime, self.right_double, 
                                self.up, self.up_prime, self.up_double,  self.left_double, 
                                self.back, self.back_prime, self.back_double,  self.down, self.down_prime, self.down_double],
            self.left_prime: [self.front, self.front_prime, self.front_double,  self.right, self.right_prime, self.right_double, 
                                self.up, self.up_prime, self.up_double,   self.left_double, 
                                self.back, self.back_prime, self.back_double,  self.down, self.down_prime, self.down_double],
            self.left_double: [self.front, self.front_prime, self.front_double,  self.right, self.right_prime, self.right_double, 
                                self.up, self.up_prime, self.up_double,  self.left, self.left_prime,
                                self.back, self.back_prime, self.back_double,  self.down, self.down_prime, self.down_double],
            self.up: [self.front, self.front_prime, self.front_double,  self.right, self.right_prime, self.right_double, 
                                self.up_double,  self.left, self.left_prime, self.left_double, 
                                self.back, self.back_prime, self.back_double,  self.down, self.down_prime, self.down_double],
            self.up_prime: [self.front, self.front_prime, self.front_double,  self.right, self.right_prime, self.right_double, 
                                self.up_double,  self.left, self.left_prime, self.left_double, 
                                self.back, self.back_prime, self.back_double,  self.down, self.down_prime, self.down_double],
            self.up_double: [self.front, self.front_prime, self.front_double,  self.right, self.right_prime, self.right_double, 
                                self.up, self.up_prime,  self.left, self.left_prime, self.left_double, 
                                self.back, self.back_prime, self.back_double,  self.down, self.down_prime, self.down_double],
            self.down: [self.front, self.front_prime, self.front_double,  self.right, self.right_prime, self.right_double, 
                                self.up, self.up_prime, self.up_double,  self.left, self.left_prime, self.left_double, 
                                self.back, self.back_prime, self.back_double,  self.down_double],

            self.down_prime: [self.front, self.front_prime, self.front_double,  self.right, self.right_prime, self.right_double, 
                                self.up, self.up_prime, self.up_double,  self.left, self.left_prime, self.left_double, 
                                self.back, self.back_prime, self.back_double,  self.down_double],
            self.down_double: [self.front, self.front_prime, self.front_double,  self.right, self.right_prime, self.right_double, 
                                self.up, self.up_prime, self.up_double,  self.left, self.left_prime, self.left_double, 
                                self.back, self.back_prime, self.back_double,  self.down, self.down_prime],
            self.back: [self.front, self.front_prime, self.front_double,  self.right, self.right_prime, self.right_double, 
                                self.up, self.up_prime, self.up_double,  self.left, self.left_prime, self.left_double, 
                                self.back_double,  self.down, self.down_prime, self.down_double],
            self.back_prime: [self.front, self.front_prime, self.front_double,  self.right, self.right_prime, self.right_double, 
                                self.up, self.up_prime, self.up_double,  self.left, self.left_prime, self.left_double, 
                                self.back_double,  self.down, self.down_prime, self.down_double],
            self.back_double: [self.front, self.front_prime, self.front_double,  self.right, self.right_prime, self.right_double, 
                                self.up, self.up_prime, self.up_double,  self.left, self.left_prime, self.left_double, 
                                self.back, self.back_prime, self.down, self.down_prime, self.down_double]
                }
        # self.func_list = [self.front, self.front_prime, self.up_prime]
    def __eq__(self, other):
        equal = False
        if (isinstance(other, self.__class__)):
            equal = (self.state == other.state).all()
        return equal

    def __ne__(self, other):
        return not self.__eq__(other)

    def front(self):
        tmp = deepcopy(self)
        tmp.state[0] = np.rot90(tmp.state[0], k=-1)
        return tmp

    def front_prime(self):
        tmp = deepcopy(self)
        tmp.state[0] = np.rot90(tmp.state[0], k=1)
        return tmp

    def front_double(self):
        tmp = deepcopy(self)
        tmp.state[0] = np.rot90(tmp.state[0], k=2)
        return tmp

    def right(self):
        tmp = deepcopy(self)
        tmp.state[:, :, 2] = np.rot90(tmp.state[:, :, 2], k=1)
        return tmp

    def right_prime(self):
        tmp = deepcopy(self)
        tmp.state[:, :, 2] = np.rot90(tmp.state[:,:, 2], k=-1)
        return tmp
    
    def right_double(self):
        tmp = deepcopy(self)
        tmp.state[:,:, 2] = np.rot90(tmp.state[:, :, 2], k=2)
        return tmp

    def left(self):
        tmp = deepcopy(self)
        tmp.state[:, :, 0] = np.rot90(tmp.state[:, :, 0], k=1)
        return tmp
   
    def left_prime(self):
        tmp = deepcopy(self)
        tmp.state[:, :, 0] = np.rot90(tmp.state[:,:, 0], k=-1)
        return tmp

    def left_double(self):
        tmp = deepcopy(self)
        tmp.state[:,:, 0] = np.rot90(tmp.state[:, :, 0], k=2)
        return tmp

    def up(self):
        tmp = deepcopy(self)
        tmp.state[:, 0, :] = np.rot90(tmp.state[:, 0, :], k=1)
        return tmp
    
    def up_prime(self):
        tmp = deepcopy(self)
        tmp.state[:, 0, :] = np.rot90(tmp.state[:, 0, :], k=-1)
        return tmp
    
    def up_double(self):
        tmp = deepcopy(self)
        tmp.state[:, 0, :] = np.rot90(tmp.state[:, 0, :], k=2)
        return tmp

    def back(self):
        tmp = deepcopy(self)
        tmp.state[2] = np.rot90(tmp.state[2], k=1)
        return tmp

    def back_prime(self):
        tmp = deepcopy(self)
        tmp.state[2] = np.rot90(tmp.state[2], k=-1)
        return tmp

    def back_double(self):
        tmp = deepcopy(self)
        tmp.state[2] = np.rot90(tmp.state[2], k=2)
        return tmp

    def down(self):
        tmp = deepcopy(self)
        tmp.state[:,2,:] = np.rot90(tmp.state[:,2,:], k=-1)
        return tmp
    
    def down_prime(self):
        tmp = deepcopy(self)
        tmp.state[:,2,:] = np.rot90(self.state[:,2,:], k=1)
        return tmp

    def down_double(self):
        tmp = deepcopy(self)
        tmp.state[:, 2,:] = np.rot90(self.state[:,2,:], k=2)
        return tmp

    def shuffle(self, num_shuffles, verbose=True):
        for i in range(num_shuffles):
            move = random.choice(self.func_list)
            move()
            if verbose:
                print(move)
