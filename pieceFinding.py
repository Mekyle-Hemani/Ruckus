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
                    return [[coordinates[0],coordinates[1]],[i,edgeToPiece[j]]]

def cornerLocation(edges):
    if edges == [1,5] or edges == [5,1]:
        return 2
    if edges == [5,7] or edges == [7,5]:
        return 8
    if edges == [7,3] or edges == [3,7]:
        return 6
    if edges == [3,1] or edges == [1,3]:
        return 0

def findCornerColour(facea, faceb, facec):
    ab = edgeToPiece[neighbours[facea].index(faceb)]
    ac = edgeToPiece[neighbours[facea].index(facec)]

    ba = edgeToPiece[neighbours[faceb].index(facea)]
    bc = edgeToPiece[neighbours[faceb].index(facec)]

    ca = edgeToPiece[neighbours[facec].index(facea)]
    cb = edgeToPiece[neighbours[facec].index(faceb)]

    aCornerLocation = (cornerLocation([ab,ac]))
    bCornerLocation = (cornerLocation([ba,bc]))
    cCornerLocation = (cornerLocation([ca,cb]))

    return([aCornerLocation,bCornerLocation,cCornerLocation])

def findCornerByColour(coloura, colourb, colourc, cubeArray=cubeStateManagement.resetCube()):
    combinedColourGoal = [coloura, colourb, colourc]
    for i in range(6):
        for j in range(4):
            indexToCorners = {0:0,
                              1:2,
                              2:6,
                              3:8}
            if cubeArray[i][indexToCorners[j]] == coloura:
                corner = indexToCorners[j]
                edges=None
                if corner == 2:
                    edges = [1,5]
                if corner == 8:
                    edges = [5,7]
                if corner == 6:
                    edges = [7,3]
                if corner == 0:
                    edges = [1,3]
                faceb = neighbours[i][pieceToEdge[edges[0]]]
                facec = neighbours[i][pieceToEdge[edges[1]]]

                result = findCornerColour(i, faceb, facec)
                colours = [cubeArray[i][result[0]],cubeArray[faceb][result[1]],cubeArray[facec][result[2]]]
                if sorted(colours) == sorted(combinedColourGoal):
                    return [[i,result[0]],[faceb,result[1]],[facec,result[2]]]
    print("No corner found with the supplied colours")
    return None
                
if __name__ == "__main__":
    #print(findEdgeColour(5,5))
    #print(findEdgeByColor(5,3))
    #print(findCornerColour(0,1,4))
    print(findCornerByColour(0,1,5))