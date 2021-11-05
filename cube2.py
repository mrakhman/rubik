import numpy as np
import random
from copy import deepcopy
class Cube:
    def __init__(self):
        ''' positioning of sides of rubik's cube is following:
            0 - front
            1 - left
            2 - right
            3 - back
            4 - up
            5 - down
        '''

        self.state = np.zeros((6, 3, 3))
        for i in range(6):
            self.state[i] = np.full((3,3), i)
        self.actions = []

    def __eq__(self, other):
        equal = False
        if (isinstance(other, self.__class__)):
            equal = (self.state == other.state).all()
        return equal
    def __ne__(self, other):
        return not self.__eq__(other)
    def front(self):
        self.state[0] = np.rot90(self.state[0], k=-1)
        buf = deepcopy(self.state[1, :, 2])
        self.state[1, :, 2] = self.state[5, 0, :]
        buf2 = deepcopy(self.state[4, 2, :])
        print(buf2)
        self.state[4, 2, :] = buf
        buf = deepcopy(self.state[2, :, 0])
        self.state[2, :, 0] = buf2
        self.state[5, 0, :] = buf

    def front_prime(self):
        self.state[0] = np.rot90(self.state[0], k=1)
        buf = deepcopy(self.state[1, :, 2])
        self.state[1, :, 2] = self.state[4, 2, :]
        buf2 = deepcopy(self.state[5, 0, :])
        print(buf2)
        self.state[5, 0, :] = buf
        buf = deepcopy(self.state[2, :, 0])
        self.state[2, :, 0] = buf2
        self.state[4, 2, :] = buf


    def front_double(self):
        self.state[0] = np.rot90(self.state[0], k=2)
        buf = deepcopy(self.state[1, :, 2])
        self.state[1, :, 2] = self.state[2, :, 0]
        self.state[2, :, 0] = buf
        buf = deepcopy(self.state[5,0,:])
        self.state[5,0,:] = self.state[4,2,:]
        self.state[4,2,:] = buf

    def right(self):
        self.state[2] = np.rot90(self.state[2], k=1)
        self.state[]
    # def right(self):
    #     self.state[:, :, 2] = np.rot90(self.state[:, :, 2], k=1)
    
    # def right_prime(self):
    #     self.state[:, :, 2] = np.rot90(self.state[:,:, 2], k=-1)
    
    # def right_double(self):
    #     self.state[:,:, 2] = np.rot90(self.state[:, :, 2], k=2)

    # def left(self):
    #     self.state[:, :, 0] = np.rot90(self.state[:, :, 0], k=1)
    
    # def left_prime(self):
    #     self.state[:, :, 0] = np.rot90(self.state[:,:, 0], k=-1)
    
    # def left_double(self):
    #     self.state[:,:, 0] = np.rot90(self.state[:, :, 0], k=2)

    # def up(self):
    #     self.state[:, 0, :] = np.rot90(self.state[:, 0, :], k=1)
    
    # def up_prime(self):
    #     self.state[:, 0, :] = np.rot90(self.state[:, 0, :], k=-1)
    
    # def up_double(self):
    #     self.state[:, 0, :] = np.rot90(self.state[:, 0, :], k=2)

    # def back(self):
    #     self.state[2] = np.rot90(self.state[2], k=1)
    # def back_prime(self):
    #     self.state[2] = np.rot90(self.state[2], k=-1)
    # def back_double(self):
    #     self.state[2] = np.rot90(self.state[2], k=2)

    # def down(self):
    #     self.state[:,2,:] = np.rot90(self.state[:,2,:], k=-1)
    
    # def down_prime(self):
    #     self.state[:,2,:] = np.rot90(self.state[:,2,:], k=1)
    # def down_double(self):
    #     self.state[:, 2,:] = np.rot90(self.state[:,2,:], k=2)


    def shuffle(self, num_shuffles, verbose=True):
        for i in range(num_shuffles):
            move = random.choice(self.func_list)
            move()
            if verbose:
                print(move)

check = Cube()
# check.shuffle(5)
# print(check.state)
# check.up_double()
# printcheck.state)
check.front_double()
print(check.state)
# check.up_double()
# print(check.state)
