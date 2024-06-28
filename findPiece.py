def find(type, colour, scramble, secondarycolour=None, tertiarycolour=None, confirm=0):
    locations = []
    neighbouring = [[3, 4, 2, 1],[5, 2, 4, 0],[3, 0, 5, 1],[5, 4, 2, 0],[3, 5, 0, 1],[3, 2, 4, 1]]
    for i in range(6):
        for j in range(9):
            if (scramble[i][j] == colour):
                if ((type == 0)and(j%2 == 1)): #Edge
                    if (secondarycolour==None):
                        locations.append([i, j])
                    else:
                        pass
                elif (((type == 1)and(j%2 == 0))and(j!=4)): #Corner
                    if (secondarycolour==None):
                        locations.append([i, j])
    if (confirm == 1):
        if (len(locations)>4):
            print(f"Too many matches in cube for type={type}, color={colour}, secondarycolour={secondarycolour}, tertiarycolour={tertiarycolour}")
            return 0
    elif (confirm == 0):
        return locations