import grabScramble
import displayCube
import movements
import pieceFunctions
import solve
import colourprint

#userturns = grabScramble.grabscramble()
userturns = ["r2", "f"]

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

colourprint.print_colored(solve.solve(userscramble), colourprint.GREEN)