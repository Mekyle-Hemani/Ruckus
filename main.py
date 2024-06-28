import grabScramble
import displayCube
import movements
#import findPiece

#userturns = grabScramble.grabscramble()
userturns = ["u"]

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

#print(findPiece.find(0, 0, userscramble))

userscramble = movements.debugmode(userscramble, 1)

userscramble = movements.applySolve(userturns, userscramble)

displayCube.displayCube(userscramble)