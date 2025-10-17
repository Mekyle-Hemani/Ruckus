def applyTransformations(moves=["f","r","u","r'","u'","f'"],cubeArray=None):
    if cubeArray == None:
        import cubeStateManagement
        cubeArray=cubeStateManagement.resetCube()

    for move in range(len(moves)):
        prime=("'" in moves[move])
        dual=("2" in moves[move])
        print(dual)

        cubeArrayClone=[]
        import copy
        cubeArrayClone=copy.deepcopy(cubeArray)
        faces=["f","u","l","d","r","b"]
        face=faces.index(moves[move][0])

        neighbours = [[1,4,3,2],
                      [0,2,5,4],
                      [0,3,5,1],
                      [0,4,5,2],
                      [0,1,5,3],
                      [3,4,1,2]]
        
        neighbourIndices=[[[0,1,2],[0,1,2],[0,1,2],[0,1,2]], #White
                          [[0,1,2],[6,3,0],[8,7,6],[2,5,8]], #Orange
                          [[0,3,6],[0,3,6],[0,3,6],[8,5,2]], #Green
                          [[6,7,8],[0,3,6],[2,1,0],[8,5,2]], #Red
                          [[2,5,8],[6,3,0],[2,5,8],[2,5,8]], #Blue
                          [[6,7,8],[6,7,8],[6,7,8],[6,7,8]]] #Yellow

        for i in range(3):
            if prime:
                cubeArrayClone[neighbours[face][0]][neighbourIndices[face][0][i]]=cubeArray[neighbours[face][1]][neighbourIndices[face][1][i]]
                cubeArrayClone[neighbours[face][1]][neighbourIndices[face][1][i]]=cubeArray[neighbours[face][2]][neighbourIndices[face][2][i]]
                cubeArrayClone[neighbours[face][2]][neighbourIndices[face][2][i]]=cubeArray[neighbours[face][3]][neighbourIndices[face][3][i]]
                cubeArrayClone[neighbours[face][3]][neighbourIndices[face][3][i]]=cubeArray[neighbours[face][0]][neighbourIndices[face][0][i]]
            else:
                for j in range(1+dual):
                    cubeArrayClone[neighbours[face][1]][neighbourIndices[face][1][i]]=cubeArray[neighbours[face][0]][neighbourIndices[face][0][i]]
                    cubeArrayClone[neighbours[face][2]][neighbourIndices[face][2][i]]=cubeArray[neighbours[face][1]][neighbourIndices[face][1][i]]
                    cubeArrayClone[neighbours[face][3]][neighbourIndices[face][3][i]]=cubeArray[neighbours[face][2]][neighbourIndices[face][2][i]]
                    cubeArrayClone[neighbours[face][0]][neighbourIndices[face][0][i]]=cubeArray[neighbours[face][3]][neighbourIndices[face][3][i]]
                    cubeArray=copy.deepcopy(cubeArrayClone)

        for i in range(1+(prime*2)+(dual)):
            #Corners
            cubeArrayClone[face][0]=cubeArray[face][6]
            cubeArrayClone[face][6]=cubeArray[face][8]
            cubeArrayClone[face][8]=cubeArray[face][2]
            cubeArrayClone[face][2]=cubeArray[face][0]
            #Edges
            cubeArrayClone[face][1]=cubeArray[face][3]
            cubeArrayClone[face][3]=cubeArray[face][7]
            cubeArrayClone[face][5]=cubeArray[face][1]
            cubeArrayClone[face][7]=cubeArray[face][5]

            cubeArray=copy.deepcopy(cubeArrayClone)
    return cubeArray