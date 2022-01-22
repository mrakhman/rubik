# rubik

### Valid spins:
F  R  U  B  L  D (Front, Right, Up, Back, Left, Down)

F' R' U' B' L' D' (prime spins)

F2 R2 U2 B2 L2 D2 (double spins)


### Instructions:

#### Launch solver with algorithm speed timer (with any valid string of shuffle spins):

`python3 main.py "R F L B"`


#### Launch solver with N random shuffle spins (N is a number of spins, from 1 to 300):
`python3 main.py random 30`



#### Solve rubik step by step (beginner method):
`python3 solve_step_by_step.py "R F L B"`

`python3 solve_step_by_step.py random 12`


#### Launch solver and then apply the same shuffle and solving moves on a new cube:
`python3 solve_and_test_on_new_cube.py "R F L B"`

`python3 solve_and_test_on_new_cube.py random 12`


#### Launch auto tests:
`python3 test_rubik.py`
