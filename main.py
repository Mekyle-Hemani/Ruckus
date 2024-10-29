import SimpleSerial.SimpleSerialMain
import grabScramble
import solve
import SimpleSerial
import colourprint
import time
import serial

scramble = grabScramble.grabScramble()

solution = solve.solve(scramble)

colourprint.print_colored(solution, colourprint.GREEN)

colourprint.print_colored("Communication to microcontroller established", colourprint.BLUE)

SimpleSerial.SimpleSerialMain.writeDataOnce("a"+solution, debug=1)