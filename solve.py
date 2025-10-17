import transformations
import pieceFinding
import cubeStateManagement

def solve(cubeArray):
    whiteEdges = []
    for i in range(4):
        whiteEdges.append(pieceFinding.findEdgeByColor(0,i+1,cubeArray))
    print(whiteEdges)
    #Gets all the white edges and places them in the following format;
    #[[[face 0, face 1], [piece 0, piece 1]], [[face 0, face 1], [piece 0, piece 1]], [[face 0, face 1], [piece 0, piece 1]], [[face 0, face 1], [piece 0, piece 1]]]

if __name__ == "__main__":
    cubeArray = cubeStateManagement.resetCube()
    cubeArray=transformations.applyTransformations(["f","r","u","r'","u'","f'"], cubeArray)
    solve(cubeArray)