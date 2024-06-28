import grabScramble
import displayCube
import movements

#userturns = grabScramble.grabscramble()
userturns = ["u", "r"]

userscramble = [
    [0, 0, 0,
     0, 0, 0,
     0, 0, 0], #White
     
    [1, 1, 1,
     1, 1, 1,
     1, 1, 1], #Red

    [2, 2, 2,
     2, 2, 2,
     2, 2, 2], #Green

    [3, 3, 3,
     3, 3, 3,
     3, 3, 3], #Orange

    [4, 4, 4,
     4, 4, 4,
     4, 4, 4], #Blue

    [5, 5, 5,
     5, 5, 5,
     5, 5, 5] #Yellow
]

#userscramble = movements.debugmode(userscramble, 1)

userscramble = movements.applySolve(userturns, userscramble)

displayCube.displayCube(userscramble)