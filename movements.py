def turn(notation, scramble):
    if len(notation) == 2:
        editscramble = scramble
        for i in range(3):
            editscramble = turn(notation[0], scramble) #Needs to be set to a variable
        return editscramble
    else:
        colours = ["w", "r", "g", "o", "b", "y"]
        notationbasic = ["f", "u", "r", "d", "l", "b"]

        scramble[notationbasic.index(notation)] = rotatefaceclockwise(scramble[notationbasic.index(notation)])

        if ((notation == "f")):
            temp = scramble.copy()
            #Rotate all the relevant pieces

            finaltemp = (scramble[1][0], scramble[1][1], scramble[1][2])
            (temp[1][0], temp[1][1], temp[1][2]) = (scramble[4][0], scramble[4][1], scramble[4][2])
            (temp[4][0], temp[4][1], temp[4][2]) = (scramble[3][0], scramble[3][1], scramble[3][2])
            (temp[3][0], temp[3][1], temp[3][2]) = (scramble[2][0], scramble[2][1], scramble[2][2])
            (temp[2][0], temp[2][1], temp[2][2]) = finaltemp

        return temp


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

if __name__ == "__main__":
    pass