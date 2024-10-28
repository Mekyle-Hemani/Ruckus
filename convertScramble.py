import grabScramble
import colourprint

def fromCubestring(string):
    dict = {'F': "W", 
        'L': "O", 
        'D': "G", 
        'R': "R", 
        'U': "B", 
        'B': "Y", 
        ",":","}
    converted_string = ""
    for char in string:
        converted_char = dict.get(char, char)
        converted_string += converted_char
    colourprint.print_colored(converted_string, colourprint.BLUE)
    return converted_string

def toCubestring(string):
    dict = {'W': "F", 
        'O': "L", 
        'G': "D", 
        'R': "R", 
        'B': "U", 
        'Y': "B", 
        ",":","}
    converted_string = ""
    for char in string:
        converted_char = dict.get(char, char)
        converted_string += converted_char
    colourprint.print_colored(converted_string, colourprint.BLUE)
    return converted_string