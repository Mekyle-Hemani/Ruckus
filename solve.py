import findPiece
import movements
import displayCube

def cross(gotscramble):
    scramble = gotscramble
    moves = ["f", "f'"]
    movestotal = moves

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

                print(locations)

                if (findPiece.findsecondaryface(0, [i, send]) == 0): #This checks if the secondary colour has its edge on the white face

                    if (findPiece.grabindex(neighbouring[0], i) == 0): #This checks if the piece's edge is connected to white

                        #Rotate its face counter clockwise, rotate white clockwise, rotate its secondary face counter clockwise, rotate white counter clockwise
                        moves.append(notation[i]+"'")

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

                        moves.append("piece solved")
                
                        #scramble = movements.applySolve(moves, scramble)

                        #displayCube.displayCube(scramble)

                        print(moves)

                        exit()

                        for k in range(len(moves)):
                            movestotal.append(moves[k])
                        moves = ["f", "f'"]
    return movestotal


def solve(scramble):
    #Solve for white cross
    turns = (cross(scramble))
    return turns