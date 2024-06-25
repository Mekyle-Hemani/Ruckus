userturns = ["f", "r", "u"]

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

def turn(notation, scramble):
    if len(notation) == 2:
        for i in range(3):
            turn(notation[0])
    else:
        colours = ["w", "r", "g", "o", "b", "y"]
        notationbasic = ["f", "u", "r", "d", "l", "b"]

        rotatefaceclockwise(notationbasic.index(notation))

        if (notation == "f"):
            pass


def findpair(givenpair):
    pairs = [
        ["f", "b"],
        ["l", "r"],
        ["u", "d"]
    ]
    for i in range(3):
        for j in range(2):
            if ((pairs[i][j]) == givenpair):
                if (j == 0):
                    return pairs[i][1]
                elif (j == 1):
                    return pairs[i][0]
    return

def debugmode(scramble, tile):
    tempscramble = scramble
    for i in range(6):
        tempscramble[i][tile] = 6
    return tempscramble

def rotatefaceclockwise(face):
    tempface = face.copy()

    tempface[0] = face[6]
    tempface[1] = face[3]
    tempface[2] = face[0]

    tempface[3] = face[7]
    #Tile 4 will stay the same
    tempface[5] = face[1]

    tempface[6] = face[8]
    tempface[7] = face[5]
    tempface[8] = face[2]

    return tempface

print(rotatefaceclockwise([0, 1, 2, 3, 4, 5, 6, 7, 8]))

'''
for i in range(len(userturns)):
    turn(userturns[i])'''