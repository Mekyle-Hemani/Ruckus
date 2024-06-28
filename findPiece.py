def find(type, colour, scramble, secondarycolour=None, tertiarycolour=None, confirm=0):
    locations = []
    neighbouring = [
        [3, 4, 2, 1], #White
        [5, 2, 4, 0], #Orange
        [3, 0, 5, 1], #Green
        [5, 4, 2, 0], #Red
        [3, 5, 0, 1], #Blue
        [3, 2, 4, 1] #Yellow
    ]
    for i in range(6):
        for j in range(9):
            if (scramble[i][j] == colour):
                if ((type == 0)and(j%2 == 1)): #Edge
                    locations.append([i, len(locations)])        
                elif (((type == 1)and(j%2 == 0))and(j!=4)): #Corner
                    if (secondarycolour==None):
                        locations.append([i, j])
    
    if ((type == 0)and(secondarycolour!=None)): #Edge and second colour is applied
        for i in range(4):
            if (neighbouring[locations[i][0]][locations[i][1]] == secondarycolour):
                return [[locations[i][0], locations[i][1]], [neighbouring[locations[i][0]][locations[i][1]], neighbouring[neighbouring[locations[i][0]][locations[i][1]]][locations[i][0]]]]

    if (confirm == 1):
        if (len(locations)>4):
            print(f"Too many matches in cube for type={type}, color={colour}, secondarycolour={secondarycolour}, tertiarycolour={tertiarycolour}")
            return 0
    elif (confirm == 0):
        return locations


 
def findsecondarycolor(type, colour, face, scramble, confirm=0):
    locations = []
    neighbouring = [
        [3, 4, 2, 1], #White
        [5, 2, 4, 0], #Orange
        [3, 0, 5, 1], #Green
        [5, 4, 2, 0], #Red
        [3, 5, 0, 1], #Blue
        [3, 2, 4, 1] #Yellow
    ]
    for i in range(6):
        for j in range(9):
            if (scramble[i][j] == colour):
                if ((type == 0)and(j%2 == 1)): #Edge
                    locations.append([i, len(locations)])

                    if (i == face):
                        pass
    print(locations)

    if (confirm == 1):
        if (len(locations)>4):
            print(f"Too many matches in cube for type={type}, color={colour}, secondarycolour={face}")
            return 0
    elif (confirm == 0):
        return locations