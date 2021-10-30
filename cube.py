import numpy as np
import random
import copy
class Cube:
    def __init__(self):
        ''' positioning of sides of rubik's cube is following:

        '''

        self.state = np.arange(0,27).reshape(3,3,3)
        self.actions = []
        self.func_list = [self.front, self.front_prime, self.front_double,  self.right, self.right_prime, self.right_double, 
                          self.up, self.up_prime, self.up_double,  self.left, self.left_prime, self.left_double, 
                          self.back, self.back_prime, self.back_double,  self.down, self.down_prime, self.down_double] 
    def __eq__(self, other):
        equal = False
        if (isinstance(other, self.__class__)):
            equal = (self.state == other.state).all()
        return equal
    def __ne__(self, other):
        return not self.__eq__(other)
    def front(self):
        self.state[0] = np.rot90(self.state[0], k=-1)

    def front_prime(self):
        self.state[0] = np.rot90(self.state[0], k=1)

    def front_double(self):
        self.state[0] = np.rot90(self.state[0], k=2)

    def right(self):
        self.state[:, :, 2] = np.rot90(self.state[:, :, 2], k=1)
    
    def right_prime(self):
        self.state[:, :, 2] = np.rot90(self.state[:,:, 2], k=-1)
    
    def right_double(self):
        self.state[:,:, 2] = np.rot90(self.state[:, :, 2], k=2)

    def left(self):
        self.state[:, :, 0] = np.rot90(self.state[:, :, 0], k=1)
    
    def left_prime(self):
        self.state[:, :, 0] = np.rot90(self.state[:,:, 0], k=-1)
    
    def left_double(self):
        self.state[:,:, 0] = np.rot90(self.state[:, :, 0], k=2)

    def up(self):
        self.state[:, 0, :] = np.rot90(self.state[:, 0, :], k=1)
    
    def up_prime(self):
        self.state[:, 0, :] = np.rot90(self.state[:, 0, :], k=-1)
    
    def up_double(self):
        self.state[:, 0, :] = np.rot90(self.state[:, 0, :], k=2)

    def back(self):
        self.state[2] = np.rot90(self.state[2], k=1)
    def back_prime(self):
        self.state[2] = np.rot90(self.state[2], k=-1)
    def back_double(self):
        self.state[2] = np.rot90(self.state[2], k=2)

    def down(self):
        self.state[:,2,:] = np.rot90(self.state[:,2,:], k=-1)
    
    def down_prime(self):
        self.state[:,2,:] = np.rot90(self.state[:,2,:], k=1)
    def down_double(self):
        self.state[:, 2,:] = np.rot90(self.state[:,2,:], k=2)


    def shuffle(self, num_shuffles, verbose=True):
        for i in range(num_shuffles):
            move = random.choice(self.func_list)
            move()
            if verbose:
                print(move)

check = Cube()
# check.shuffle(5)
print(check.state)
check.up_double()
print(check.state)
check.up_double()
print(check.state)
