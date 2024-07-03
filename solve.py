import findPiece
import movements
import displayCube

def cross(type, colour, gotscramble):
    scramble = gotscramble
    pieces = findPiece.find(type, colour, scramble)
    moves = ["f", "f'"]

    colors = ["w", "o", "g", "r", "b", "y"]
    notation = ["f", "d", "r", "l", "b"]

    solvingfor = []
    for i in range(4):
        if (pieces[i][0] == colour):
            pass
        else:
            solvingfor.append([pieces[i][0], pieces[i][1]])
    if (len(solvingfor) == 0):
        return moves
    else:
        for i in range(len(solvingfor)):
            #If its secondary colour is connected to yellow
            if (findPiece.findsecondaryface(0, solvingfor[i], 5) == True):
                if (gotscramble[0][solvingfor[i][1]] != 0):
                    #Rotate its face
                    pass


def solve(scramble):
    #Solve for white cross
    turns = (cross(0, 0, scramble))
    return turns