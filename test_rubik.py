import unittest
from solve_cube.cube import Cube
from solve_cube.solver import Solver


class TestCube(unittest.TestCase):
    def test_one(self):
        cube = Cube()
        shuffle = ["R", "U", "R'", "U'", "L", "B"]
        cube.shuffle(shuffle)
        solver = Solver(cube)
        result = solver.solve_cube()
        self.assertTrue(result)

        cube_test = Cube()
        cube_test.shuffle(shuffle)
        cube_test.run_moves(solver.solving_moves)
        self.assertTrue(cube_test.is_cube_solved())


    def test_two(self):
        cube = Cube()
        shuffle = ['R2', 'L2', 'D', "B'", "R'", 'B2', 'U2', 'D', 'L', "B'", 'D2', 'L', 'B2', 'D2', 'R', 'F2', 'U2', 'L', 'U2']
        cube.shuffle(shuffle)
        solver = Solver(cube)
        result = solver.solve_cube()
        self.assertTrue(result)

        cube_test = Cube()
        cube_test.shuffle(shuffle)
        cube_test.run_moves(solver.solving_moves)
        self.assertTrue(cube_test.is_cube_solved())


    def test_three(self):
        cube = Cube()
        cube.shuffle(['U', 'R2', 'F', 'B', 'R', 'B2', 'R', 'U2', 'L', 'B2', 'R', "U'", "D'", 'R2', 'F', "R'", 'L', 'B2', 'U2', 'F2'])
        solver = Solver(cube)
        result = solver.solve_cube()
        self.assertTrue(result)


    def test_four(self):
        cube = Cube()
        cube.shuffle(['F', 'R', 'U', 'B', 'L', 'D'])
        solver = Solver(cube)
        result = solver.solve_cube()
        self.assertTrue(result)


    def test_five(self):
        cube = Cube()
        cube.shuffle(['R', 'B', 'L', 'F'])
        solver = Solver(cube)
        result = solver.solve_cube()
        self.assertTrue(result)


    def test_six(self):
        cube = Cube()
        cube.shuffle(['F', 'F', 'U2', "B'", "L'", "D'"])
        solver = Solver(cube)
        result = solver.solve_cube()
        self.assertTrue(result)


    def test_seven(self):
        cube = Cube()
        cube.shuffle(['F', 'R', 'U2', "B'", "L'", "D'"])
        solver = Solver(cube)
        result = solver.solve_cube()
        self.assertTrue(result)


    def test_eight(self):
        cube = Cube()
        cube.shuffle(['F', 'D', 'U2', "F'", 'B2', 'R', 'U', 'L', 'D2', "U'", 'D2', "B'", 'F2', 'L', 'D'])
        solver = Solver(cube)
        result = solver.solve_cube()
        self.assertTrue(result)


    def test_nine(self):
        cube = Cube()
        cube.run_moves(['L', "D'", "U'", 'L2', 'R', 'B', "F'", "U'", 'B2', 'F', "U'", "R'", 'D2', "F'", 'L2', 'R2', 'U', "L'", 'B2', 'F', "L'", 'R', 'D', "U'", 'L', "R'", "D'", 'U2', 'B', 'F2'])
        solver = Solver(cube)
        result = solver.solve_cube()
        self.assertTrue(result)


    def test_ten(self):
        cube = Cube()
        cube.shuffle(["R'", 'B', 'L', 'R2', 'D', "R'", "D'", 'U2', "F'", 'R', "B'", "L'", "R'", 'B', 'D2', "L'", 'B2', 'F', "D'", 'L', 'R', 'D', 'U2', 'L2', "R'", "B'", "F'", 'L', 'R2', 'F2'])
        solver = Solver(cube)
        result = solver.solve_cube()
        self.assertTrue(result)


    def test_eleven(self):
        cube = Cube()
        cube.shuffle(['U', "F'", 'R', 'B2', "F'", 'D2', 'F', 'D2', "L'", "U'", "F'", 'U2', "L'", 'D', 'F2', "L'", 'F', "R'", "D'", 'U2', "B'", "F'", 'U2', 'R', 'B', "F'", "D'", "R'", "B'", 'F', 'L', "B'", "F'", "D'", 'U2', "F'", 'D', "U'", 'L2', "B'"])
        solver = Solver(cube)
        result = solver.solve_cube()
        self.assertTrue(result)


    def test_twelve(self):
        cube = Cube()
        cube.shuffle(['R', "U'", "R'", 'B2', 'F2', "L'", 'U2', "L'", 'B2', "F'", 'L', "R'", 'F2', 'L2', 'R', 'D2', "U'", 'F', 'L', "R'", "B'", "L'", 'R', 'B', "F'", 'U', "R'", 'D2', "B'", "F'", "D'", 'U2', 'B', "F'", 'U', 'R', 'U2', "R'", 'U', 'L2'])
        solver = Solver(cube)
        result = solver.solve_cube()
        self.assertTrue(result)


    def test_thirteen(self):
        cube = Cube()
        cube.shuffle(['L2', "U'", 'F2', "U'", "B'", "F'", 'U2', 'B2', 'U2', 'L', 'R', 'D2', 'B2', 'L', 'R', 'F2', "D'", 'U2', 'F', "L'", 'U', 'L2', "R'", "U'", "F'", "D'", 'R2', "F'", 'L2', 'U2', "L'", 'D2', "F'", 'R2', 'D2', "B'", 'F', "L'", "R'", 'B2'])
        solver = Solver(cube)
        result = solver.solve_cube()
        self.assertTrue(result)


    def test_fourteen(self):
        cube = Cube()
        cube.shuffle(['R2', "U'", "B'", "D'", 'B2', 'F2', 'R2', 'F2', "L'", 'B2', "F'", 'U2', 'B', 'D', "U'", "F'", 'L2', 'R', "B'", "L'", 'U', 'B2', 'F2', 'D', 'B2', "F'", 'L', "B'", "D'", 'F2', 'D2', "U'", "B'", "R'", 'D', 'U', 'F2', "U'", 'B', 'D2', 'L2', 'B', 'L2', 'R2', "U'", 'L', "B'", 'F', 'D2', "U'"])
        solver = Solver(cube)
        result = solver.solve_cube()
        self.assertTrue(result)


if __name__ ==  '__main__':
    unittest.main()
