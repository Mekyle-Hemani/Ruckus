def resetCube():
    array=[]
    for i in range(6):
        temparray=[]
        for j in range(9):
            temparray.append(i)
        array.append(temparray)
    return array