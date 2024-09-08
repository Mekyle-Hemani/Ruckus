import findPiece
import movements
import displayCube
import colourprint

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
            #Case 0, checks if edge is solved
            if (((scramble[i][j] == 0)and(j%2 == 1))and(i!=0)):
                locations.append([i, j])
                listconverted = int((j-1)/2)

                if findPiece.findsecondaryface(0, [i, listconverted], 0) == True:
                    #Case 1, edge is flipped on white
                    colourprint.print_colored("Case 1, edge is flipped on white", colourprint.YELLOW)

                    #Rotate its face counter-clockwise
                    moves.append(notation[i]+"'")

                    #Rotate F clockwise
                    moves.append("f")

                    #Rotate the secondary face of the edge after the first move counter-clockwise
                    moves.append((notation[findPiece.findsecondaryface(0, ([i, findPiece.fakemovecounterclockwise(listconverted)]))])+"'")

                    #Rotate F counter-clockwise
                    moves.append("f'")

                    colourprint.print_colored(f"Piece [{i, j}] was solved using case 1", colourprint.BLUE)

                elif i == 5:
                    #Case 2, edge is on yellow
                    colourprint.print_colored("Case 2, edge is on yellow", colourprint.YELLOW)

                elif (findPiece.findsecondaryface(0, [i, listconverted]) == 5):
                    #Case 3, edge is flipped on yellow
                    colourprint.print_colored("Case 3, edge is flipped on yellow", colourprint.YELLOW)

                else:
                    #Case 4, edge is on middle row
                    colourprint.print_colored("Case 4, edge is on middle row", colourprint.YELLOW)

                    if scramble[0][findPiece.grabindex(neighbouring[0], findPiece.findsecondaryface(0, [i, listconverted]))] != 0:
                        #Rotate that face
                        pass
                    else:
                        #Rotate white and try again
                        pass

    return moves


def solve(scramble):
    #Solve for white cross
    turns = (cross(scramble))
    return turns