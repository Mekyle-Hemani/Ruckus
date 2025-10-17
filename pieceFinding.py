neighbours = [[1,4,3,2],[0,2,5,4],[0,3,5,1],[0,4,5,2],[0,1,5,3],[3,4,1,2]]

def findEdgeColour(face=0, piece=0, edgeNotation=False):
    pieceToEdge = {1:0,
                3:3,
                5:1,
                7:2}
    
    edgeToPiece = {0:1,
                3:3,
                1:5,
                2:7}
    
    if edgeNotation:
        out = [neighbours[face][piece],neighbours[neighbours[face][piece]].index(face)]
    else:
        out = [neighbours[face][pieceToEdge[piece]],edgeToPiece[neighbours[neighbours[face][pieceToEdge[piece]]].index(face)]]
    
    return out

#def findCornerColour(face=0, piece=0):

if __name__ == "__main__":
    print(findEdgeColour(5,5))