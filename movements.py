def applySolve(moveset, scramblearray):
    currentscramble = scramblearray
    for i in range(len(moveset)):
        currentscramble = turn(moveset[i], currentscramble)
    return currentscramble

def turn(notation, scramble):
    if len(notation) == 2:
        editscramble = scramble
        for i in range(3):
            editscramble = turn(notation[0], scramble) #Needs to be set to a variable
        return editscramble
    else:
        colours = ["w", "r", "g", "o", "b", "y"]
        notationbasic = ["f", "u", "r", "d", "l", "b"]

        #scramble[notationbasic.index(notation)] = rotatefaceclockwise(scramble[notationbasic.index(notation)])

        temp = scramble.copy()

        if (notation == "f"):
            
            finaltemp = [scramble[1][0], scramble[1][1], scramble[1][2]]
            [temp[1][0], temp[1][1], temp[1][2]] = [scramble[4][0], scramble[4][1], scramble[4][2]]
            [temp[4][0], temp[4][1], temp[4][2]] = [scramble[3][0], scramble[3][1], scramble[3][2]]
            [temp[3][0], temp[3][1], temp[3][2]] = [scramble[2][0], scramble[2][1], scramble[2][2]]
            [temp[2][0], temp[2][1], temp[2][2]] = finaltemp
            rotatefaceclockwise(scramble[0])
        
        elif (notation == "u"):
            finaltemp = [scramble[0][0], scramble[0][1], scramble[0][2]]
            [temp[0][0], temp[0][1], temp[0][2]] = [scramble[2][0], scramble[2][1], scramble[2][2]]
            [temp[2][0], temp[2][1], temp[2][2]] = [scramble[5][0], scramble[5][1], scramble[5][2]]
            [temp[5][0], temp[5][1], temp[5][2]] = [scramble[4][0], scramble[4][1], scramble[4][2]]
            [temp[4][0], temp[4][1], temp[4][2]] = finaltemp
            rotatefaceclockwise(scramble[1])
        
        elif (notation == "r"):
            finaltemp = [scramble[0][2], scramble[0][5], scramble[0][8]]
            [temp[0][2], temp[0][5], temp[0][8]] = [scramble[3][2], scramble[3][5], scramble[3][8]]
            [temp[3][2], temp[3][5], temp[3][8]] = [scramble[5][6], scramble[5][3], scramble[5][0]]
            [temp[5][6], temp[5][3], temp[5][0]] = [scramble[1][2], scramble[1][5], scramble[1][8]]
            [temp[1][2], temp[1][5], temp[1][8]] = finaltemp
            rotatefaceclockwise(scramble[2])
        
        elif (notation == "d"):
            finaltemp = [scramble[0][6], scramble[0][7], scramble[0][8]]
            [temp[0][6], temp[0][7], temp[0][8]] = [scramble[4][6], scramble[4][7], scramble[4][8]]
            [temp[4][6], temp[4][7], temp[4][8]] = [scramble[5][6], scramble[5][7], scramble[5][8]]
            [temp[5][6], temp[5][7], temp[5][8]] = [scramble[2][6], scramble[2][7], scramble[2][8]]
            [temp[2][6], temp[2][7], temp[2][8]] = finaltemp
            rotatefaceclockwise(scramble[3])
        
        elif (notation == "l"):
            finaltemp = [scramble[0][0], scramble[0][3], scramble[0][6]]
            [temp[0][0], temp[0][3], temp[0][6]] = [scramble[1][0], scramble[1][3], scramble[1][6]]
            [temp[1][0], temp[1][3], temp[1][6]] = [scramble[5][8], scramble[5][5], scramble[5][2]]
            [temp[5][8], temp[5][5], temp[5][2]] = [scramble[3][0], scramble[3][3], scramble[3][6]]
            [temp[3][0], temp[3][3], temp[3][6]] = finaltemp
            rotatefaceclockwise(scramble[4])
        
        elif (notation == "b"):
            finaltemp = [scramble[1][0], scramble[1][3], scramble[1][6]]
            [temp[1][0], temp[1][3], temp[1][6]] = [scramble[2][2], scramble[2][5], scramble[2][8]]
            [temp[2][2], temp[2][5], temp[2][8]] = [scramble[3][8], scramble[3][7], scramble[3][6]]
            [temp[3][8], temp[3][7], temp[3][6]] = [scramble[4][6], scramble[4][3], scramble[4][0]]
            [temp[4][6], temp[4][3], temp[4][0]] = finaltemp
            rotatefaceclockwise(scramble[5])
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