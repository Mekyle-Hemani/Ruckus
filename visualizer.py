COLORS = {
    0: "\033[47m",       # White
    1: "\033[48;5;208m", # Orange (ANSI 208)
    2: "\033[42m",       # Green
    3: "\033[41m",       # Red
    4: "\033[44m",       # Blue
    5: "\033[43m",       # Yellow (normal)
    6: "\033[40m",       # Black
}

RESET = "\033[0m"

def spinArrayClockwise(array):
    import copy
    arrayClone=copy.deepcopy(array)
    #Corners
    arrayClone[0]=array[6]
    arrayClone[6]=array[8]
    arrayClone[8]=array[2]
    arrayClone[2]=array[0]
    #Edges
    arrayClone[1]=array[3]
    arrayClone[3]=array[7]
    arrayClone[5]=array[1]
    arrayClone[7]=array[5]

    return arrayClone

def visualizeCube(cubeArray):
    cubeArray[1]=spinArrayClockwise(cubeArray[1])
    cubeArray[1]=spinArrayClockwise(cubeArray[1])

    cubeArray[2]=spinArrayClockwise(cubeArray[2])

    cubeArray[4]=spinArrayClockwise(cubeArray[4])
    cubeArray[4]=spinArrayClockwise(cubeArray[4])
    cubeArray[4]=spinArrayClockwise(cubeArray[4])
    #wogrby
    for i in range(3):
        for j in range(3):
            print(f"{COLORS[6]}  {RESET}", end="")
        for j in range(3):
            print(f"{COLORS[cubeArray[1][(i*3)+j]]}  {RESET}",end="")
        for j in range(3):
            print(f"{COLORS[6]}  {RESET}", end="")
        print()
    for j in range(3):
        for i in range(3):
            print(f"{COLORS[cubeArray[2][i+(j*3)]]}  {RESET}",end="")
        for i in range(3):
            print(f"{COLORS[cubeArray[0][i+(j*3)]]}  {RESET}",end="")
        for i in range(3):
            print(f"{COLORS[cubeArray[4][i+(j*3)]]}  {RESET}",end="")
        print()
    for i in range(3):
        for j in range(3):
            print(f"{COLORS[6]}  {RESET}", end="")
        for j in range(3):
            print(f"{COLORS[cubeArray[3][(i*3)+j]]}  {RESET}",end="")
        for j in range(3):
            print(f"{COLORS[6]}  {RESET}", end="")
        print()
    for i in range(3):
        for j in range(3):
            print(f"{COLORS[6]}  {RESET}", end="")
        for j in range(3):
            print(f"{COLORS[cubeArray[5][(i*3)+j]]}  {RESET}",end="")
        for j in range(3):
            print(f"{COLORS[6]}  {RESET}", end="")
        print()

if __name__ == "__main__":
    import cubeStateManagement
    cube = cubeStateManagement.resetCube()
    visualizeCube(cube)