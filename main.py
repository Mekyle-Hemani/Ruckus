import displayCube
import movements
import convertScramble
import solve

userturns = ["r"]

userscramble = [
    [0, 0, 0,
     0, 0, 0,
     0, 0, 0], #White
     
    [1, 1, 1,
     1, 1, 1,
     1, 1, 1], #Orange

    [2, 2, 2,
     2, 2, 2,
     2, 2, 2], #Green

    [3, 3, 3,
     3, 3, 3,
     3, 3, 3], #Red

    [4, 4, 4,
     4, 4, 4,
     4, 4, 4], #Blue

    [5, 5, 5,
     5, 5, 5,
     5, 5, 5] #Yellow
]

userscramble = movements.applySolve(userturns, userscramble)

displayCube.displayCube(userscramble)

convertScramble.convertScramble(userscramble)

#print(solve.solve(convertScramble.convertScramble(result)))