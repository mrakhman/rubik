import numpy as np

class Cube_beginner:
    def  __init__(self):
        self.state = {
            'F': [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]],
            'R': [
                [1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]],
            'U': [
                [2, 2, 2],
                [2, 2, 2],
                [2, 2, 2]],
            'B': [
                [3, 3, 3],
                [3, 3, 3],
                [3, 3, 3]],
            'L': [
                [4, 4, 4],
                [4, 4, 4],
                [4, 4, 4]],
            'D': [
                [5, 5, 5],
                [5, 5, 5],
                [5, 5, 5]]
        }

    def front(self):
        tmp = self.state
        self.state['U'] = tmp.state['L']


test = Cube_beginner()
print(test.state['F'])
print(test.state['F'])
