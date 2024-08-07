import grabScramble
import displayCube
import movements
import findPiece
import solve

#userturns = grabScramble.grabscramble()
userturns = ["r", "u"]

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

'''
print(findPiece.find(0, 2, userscramble, 3))

userscramble = movements.debugmode(userscramble, 1)'''

userscramble = movements.applySolve(userturns, userscramble)

#print(findPiece.findsecondarycolor(0, [3, 0], userscramble))

displayCube.displayCube(userscramble)

print(solve.solve(userscramble))