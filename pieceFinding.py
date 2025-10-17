import cubeStateManagement
neighbours = [[1,4,3,2],[0,2,5,4],[0,3,5,1],[0,4,5,2],[0,1,5,3],[3,4,1,2]]

pieceToEdge = {1:0,
            3:3,
            5:1,
            7:2}
    
edgeToPiece = {0:1,
            3:3,
            1:5,
            2:7}

def findEdgeColour(face=0, piece=0, edgeNotation=False):
    if edgeNotation:
        out = [neighbours[face][piece],neighbours[neighbours[face][piece]].index(face)]
    else:
        out = [neighbours[face][pieceToEdge[piece]],edgeToPiece[neighbours[neighbours[face][pieceToEdge[piece]]].index(face)]]
    
    return out

def findEdgeByColor(coloura, colourb, cubeArray=cubeStateManagement.resetCube()):
    for i in range(6):
        for j in range(4):
            if cubeArray[i][edgeToPiece[j]] == coloura:
                coordinates = findEdgeColour(i, edgeToPiece[j])
                if cubeArray[coordinates[0]][coordinates[1]] == colourb:
                    return [coordinates[0],coordinates[1]],[i,edgeToPiece[j]]

#def findCornerColour(face=0, piece=0):

if __name__ == "__main__":
    #print(findEdgeColour(5,5))
    print(findEdgeByColor(5,3))