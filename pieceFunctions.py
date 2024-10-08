import colourprint

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
            colourprint.print_colored(f"Too many matches in cube for type={type}, color={colour}, secondarycolour={secondarycolour}, tertiarycolour={tertiarycolour}", colourprint.RED)
            return 0
    elif (confirm == 0):
        return locations

def findsecondaryface(type, location, checkingfor=None):
    neighbouring = [
        [3, 4, 2, 1], #White
        [5, 2, 4, 0], #Orange
        [3, 0, 5, 1], #Green
        [5, 4, 2, 0], #Red
        [3, 5, 0, 1], #Blue
        [3, 2, 4, 1] #Yellow
    ]
    if (type == 0):
        if (checkingfor == None):
            return neighbouring[location[0]][location[1]] #Finds what face the edge is on
        else:
            return (neighbouring[location[0]][location[1]] == checkingfor) #Returns if its on the right face the user gave

def grabindex(list, item):
    results = []
    for i in range(len(list)):
        if (list[i] == item):
            results.append(i)
    if (len(results)==1):
        return results[0]
    else:
        return results

def findsecondarycolor(type, location, scramble):
    neighbouring = [
        [3, 4, 2, 1], #White
        [5, 2, 4, 0], #Orange
        [3, 0, 5, 1], #Green
        [5, 4, 2, 0], #Red
        [3, 5, 0, 1], #Blue
        [3, 2, 4, 1] #Yellow
    ]

    if (type == 0):
        return scramble[neighbouring[location[0]][location[1]]][(grabindex((neighbouring[(neighbouring[location[0]][location[1]])]), location[0]))]
    
def fakemovecounterclockwise(piece):
    if piece == 3:
        return 2
    elif piece == 2:
        return 0
    elif piece == 0:
        return 1
    elif piece == 1:
        return 3
    
def fakemoveclockwise(piece):
    if piece == 3:
        return 1
    elif piece == 1:
        return 0
    elif piece == 0:
        return 2
    elif piece == 2:
        return 3
    
def inversenotation(notation):
    if len(notation) == 2:
        notationsplit = list(notation)
        if notationsplit[1] == "'":
            return notationsplit[0]
        elif notationsplit[1] == "2":
            return notation
    else:
        return notation+"'"
    
def algorithmrefine(notations):
    lastitem = "pass"
    removes = []
    for i in range(len(notations)):
        if lastitem == inversenotation(notations[i]):
            removes.append(i-1)
            removes.append(i)
            i+=1
        lastitem = notations[i]

    returnlist = []

    for i in range(len(notations)):
        if i in removes:
            pass
        else:
            returnlist.append(notations[i])
    return returnlist