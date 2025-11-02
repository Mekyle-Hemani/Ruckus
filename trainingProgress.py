import cubeStateManagement
import transformations
import visualizer

MOVES = ["f","f'","r","r'","u","u'","l","l'","d","d'","b","b'"]

def calculateConnectingPieces(cubeArray):
    value=0
    for i in range(6):
        for j in range(9):
            if cubeArray[i][j]==cubeArray[i][4]:
                value+=1
    correct=value-6
    return correct/48

if __name__ == "__main__":
    cubeArray = cubeStateManagement.resetCube()
    cubeArray=transformations.applyTransformations(["u", "u'"], cubeArray)
    visualizer.visualizeCube(cubeArray)
    print(calculateConnectingPieces(cubeArray))