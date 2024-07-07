import findPiece
import movements
import displayCube

def cross(gotscramble):
    scramble = gotscramble
    moves = ["f", "f'"]

    colors = ["w", "o", "g", "r", "b", "y"]
    notation = ["f", "d", "r", "u", "l", "b"]

    neighbouring = [
        [3, 4, 2, 1], #White
        [5, 2, 4, 0], #Orange
        [3, 0, 5, 1], #Green
        [5, 4, 2, 0], #Red
        [3, 5, 0, 1], #Blue
        [3, 2, 4, 1] #Yellow
    ]

    locations = []

    for i in range(6):
        for j in range(9):
            if (((gotscramble[i][j] == 0)and(j%2 == 1))and(i!=0)):
                locations.append([i, j])
                send = int((j-1)/2)
                if (findPiece.findsecondaryface(0, [i, send]) == 0):
                    if (findPiece.grabindex(neighbouring[0], i) == 0):
                        #Rotate its face clockwise, rotate white clockwise, rotate its secondary face counter clockwise, rotate white counter clockwise
                        moves.append(notation[i])
                        if (send == 3):
                            send=2
                        elif (send == 2):
                            send=0
                        elif (send == 0):
                            send=1
                        elif (send == 1):
                            send=3
                        moves.append("f")
                        moves.append(notation[neighbouring[i][send]]+"'")
                        moves.append("f'")
                        pass
    return moves


def solve(scramble):
    #Solve for white cross
    turns = (cross(scramble))
    return turns