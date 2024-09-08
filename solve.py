import pieceFunctions
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
            #Checks if solved
            if (((scramble[i][j] == 0)and(j%2 == 1))and(i!=0)):
                locations.append([i, j])

    edgessolved = 0
    edgesnotsolved = len(locations)
    totalmoves = []
                
    while edgessolved != edgesnotsolved:
        for i in range(6):
            for j in range(9):
                #Case 0, checks if edge is solved
                print(locations)
                if (((scramble[i][j] == 0)and(j%2 == 1))and(i!=0)):
                    listconverted = int((j-1)/2)

                    if pieceFunctions.findsecondaryface(0, [i, listconverted], 0) == True:
                        #Case 1, edge is flipped on white
                        colourprint.print_colored("Case 1, edge is flipped on white", colourprint.YELLOW)

                        #Rotate its face counter-clockwise
                        moves.append(notation[i]+"'")

                        #Rotate F clockwise
                        moves.append("f")

                        #Rotate the secondary face of the edge after the first move counter-clockwise
                        moves.append((notation[pieceFunctions.findsecondaryface(0, ([i, pieceFunctions.fakemovecounterclockwise(listconverted)]))])+"'")

                        #Rotate F counter-clockwise
                        moves.append("f'")


                        #Resets the moves for the solve and prepares the total moves
                        totalmoves+=moves
                        scramble = movements.applySolve(moves, scramble)
                        edgessolved += 1
                        moves = []

                        locations.remove([i,j])

                        colourprint.print_colored(f"Piece [{i, j}] was solved using case 1", colourprint.BLUE)

                    elif i == 5:
                        #Case 2, edge is on yellow
                        colourprint.print_colored("Case 2, edge is on yellow", colourprint.YELLOW)

                    elif (pieceFunctions.findsecondaryface(0, [i, listconverted]) == 5):
                        #Case 3, edge is flipped on yellow
                        colourprint.print_colored("Case 3, edge is flipped on yellow", colourprint.YELLOW)

                    else:
                        #Case 4, edge is on middle row
                        colourprint.print_colored("Case 4, edge is on middle row", colourprint.YELLOW)

                        if scramble[0][pieceFunctions.grabindex(neighbouring[0], pieceFunctions.findsecondaryface(0, [i, listconverted]))] != 0:
                            #Rotate that face
                            pass
                        else:
                            #Rotate white and try again
                            pass
                

    return totalmoves


def solve(scramble):
    #Solve for white cross
    turns = (cross(scramble))
    return pieceFunctions.algorithmrefine(turns) #Refines any redundancy to send off to the arduino