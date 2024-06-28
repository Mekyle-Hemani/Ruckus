def find(type, colour, scramble, secondarycolour=None, confirm=0):
    locations = []
    for i in range(6):
        for j in range(9):
            if (scramble[i][j] == colour):
                if ((type == 0)and(j%2 == 1)): #Edge
                    locations.append([i, j])
                elif (((type == 1)and(j%2 == 0))and(j!=4)): #Corner
                    locations.append([i, j])
    if (confirm == 1):
        if (len(locations)>4):
            print(f"Too many matches in cube for type={type}, color={colour}, secondarycolour={secondarycolour}")
            return 0
    elif (confirm == 0):
        return locations