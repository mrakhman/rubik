## rubik

### Valid spins for rubik are:
F  R  U  B  L  D
F' R' U' B' L' D'
F2 R2 U2 B2 L2 D2


To launch solver with algorithm speed timer (with any valid string of shuffle spins):
`python3 main.py "R F L B"`


To launch solver with N random shuffle spins (N is a number of spins, from 1 to 300):
`python3 main.py random 30`


To solve rubik step by step (beginner method):
`python3 solve_step_by_step.py "R F L B"`
`python3 solve_step_by_step.py random 12`


To launch solver and then apply the same shuffle and solving moves on a new cube:
`python3 solve_and_test_on_new_cube.py "R F L B"`
`python3 solve_and_test_on_new_cube.py random 12`


To launch auto tests:
`python3 test_rubik.py`
