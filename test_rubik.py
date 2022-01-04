import unittest
from masha.cube_beginner import CubeBeginner
from masha.solver import SolverBeginner


class TestCube(unittest.TestCase):
    def test_one(self):
        cube = CubeBeginner()
        cube.run_moves(["R", "U", "R'", "U'", "L", "B"])
        solver = SolverBeginner(cube)
        result = solver.solve_cube()
        self.assertTrue(result)


    def test_two(self):
        cube = CubeBeginner()
        cube.run_moves(['R2', 'L2', 'D', "B'", "R'", 'B2', 'U2', 'D', 'L', "B'", 'D2', 'L', 'B2', 'D2', 'R', 'F2', 'U2', 'L', 'U2'])
        solver = SolverBeginner(cube)
        result = solver.solve_cube()
        self.assertTrue(result)


    def test_three(self):
        cube = CubeBeginner()
        cube.run_moves(['U', 'R2', 'F', 'B', 'R', 'B2', 'R', 'U2', 'L', 'B2', 'R', "U'", "D'", 'R2', 'F', "R'", 'L', 'B2', 'U2', 'F2'])
        solver = SolverBeginner(cube)
        result = solver.solve_cube()
        self.assertTrue(result)


    def test_four(self):
        cube = CubeBeginner()
        cube.run_moves(['F', 'R', 'U', 'B', 'L', 'D'])
        solver = SolverBeginner(cube)
        result = solver.solve_cube()
        self.assertTrue(result)


    def test_five(self):
        cube = CubeBeginner()
        cube.run_moves(['R', 'B', 'L', 'F'])
        solver = SolverBeginner(cube)
        result = solver.solve_cube()
        self.assertTrue(result)


    def test_six(self):
        cube = CubeBeginner()
        cube.run_moves(['F', 'F', 'U2', "B'", "L'", "D'"])
        solver = SolverBeginner(cube)
        result = solver.solve_cube()
        self.assertTrue(result)


    def test_seven(self):
        cube = CubeBeginner()
        cube.run_moves(['F', 'R', 'U2', "B'", "L'", "D'"])
        solver = SolverBeginner(cube)
        result = solver.solve_cube()
        self.assertTrue(result)


    def test_eight(self):
        cube = CubeBeginner()
        cube.run_moves(['F', 'D', 'U2', "F'", 'B2', 'R', 'U', 'L', 'D2', "U'", 'D2', "B'", 'F2', 'L', 'D'])
        solver = SolverBeginner(cube)
        result = solver.solve_cube()
        self.assertTrue(result)


    def test_nine(self):
        cube = CubeBeginner()
        cube.run_moves(['L', "D'", "U'", 'L2', 'R', 'B', "F'", "U'", 'B2', 'F', "U'", "R'", 'D2', "F'", 'L2', 'R2', 'U', "L'", 'B2', 'F', "L'", 'R', 'D', "U'", 'L', "R'", "D'", 'U2', 'B', 'F2'])
        solver = SolverBeginner(cube)
        result = solver.solve_cube()
        self.assertTrue(result)


    def test_ten(self):
        cube = CubeBeginner()
        cube.run_moves(["R'", 'B', 'L', 'R2', 'D', "R'", "D'", 'U2', "F'", 'R', "B'", "L'", "R'", 'B', 'D2', "L'", 'B2', 'F', "D'", 'L', 'R', 'D', 'U2', 'L2', "R'", "B'", "F'", 'L', 'R2', 'F2'])
        solver = SolverBeginner(cube)
        result = solver.solve_cube()
        self.assertTrue(result)


    def test_eleven(self):
        cube = CubeBeginner()
        cube.run_moves(['U', "F'", 'R', 'B2', "F'", 'D2', 'F', 'D2', "L'", "U'", "F'", 'U2', "L'", 'D', 'F2', "L'", 'F', "R'", "D'", 'U2', "B'", "F'", 'U2', 'R', 'B', "F'", "D'", "R'", "B'", 'F', 'L', "B'", "F'", "D'", 'U2', "F'", 'D', "U'", 'L2', "B'"])
        solver = SolverBeginner(cube)
        result = solver.solve_cube()
        self.assertTrue(result)


    def test_twelve(self):
        cube = CubeBeginner()
        cube.run_moves(['R', "U'", "R'", 'B2', 'F2', "L'", 'U2', "L'", 'B2', "F'", 'L', "R'", 'F2', 'L2', 'R', 'D2', "U'", 'F', 'L', "R'", "B'", "L'", 'R', 'B', "F'", 'U', "R'", 'D2', "B'", "F'", "D'", 'U2', 'B', "F'", 'U', 'R', 'U2', "R'", 'U', 'L2'])
        solver = SolverBeginner(cube)
        result = solver.solve_cube()
        self.assertTrue(result)


    def test_thirteen(self):
        cube = CubeBeginner()
        cube.run_moves(['L2', "U'", 'F2', "U'", "B'", "F'", 'U2', 'B2', 'U2', 'L', 'R', 'D2', 'B2', 'L', 'R', 'F2', "D'", 'U2', 'F', "L'", 'U', 'L2', "R'", "U'", "F'", "D'", 'R2', "F'", 'L2', 'U2', "L'", 'D2', "F'", 'R2', 'D2', "B'", 'F', "L'", "R'", 'B2'])
        solver = SolverBeginner(cube)
        result = solver.solve_cube()
        self.assertTrue(result)


    def test_fourteen(self):
        cube = CubeBeginner()
        cube.run_moves(['R2', "U'", "B'", "D'", 'B2', 'F2', 'R2', 'F2', "L'", 'B2', "F'", 'U2', 'B', 'D', "U'", "F'", 'L2', 'R', "B'", "L'", 'U', 'B2', 'F2', 'D', 'B2', "F'", 'L', "B'", "D'", 'F2', 'D2', "U'", "B'", "R'", 'D', 'U', 'F2', "U'", 'B', 'D2', 'L2', 'B', 'L2', 'R2', "U'", 'L', "B'", 'F', 'D2', "U'"])
        solver = SolverBeginner(cube)
        result = solver.solve_cube()
        self.assertTrue(result)


if __name__ ==  '__main__':
    unittest.main()
