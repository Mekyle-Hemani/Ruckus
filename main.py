import SimpleSerial.SimpleSerialMain
import grabScramble
import solve
import SimpleSerial
import colourprint

scramble = grabScramble.grabScramble()

solution = solve.solve(scramble)

colourprint.print_colored(solution, colourprint.GREEN)

colourprint.print_colored("Communication to microcontroller established", colourprint.BLUE)

print("\n")

if (SimpleSerial.SimpleSerialMain.writeDataOnce("a"+solution, debug=1) == 0):
    colourprint.print_colored("Device has not recieved scramble", colourprint.RED)
    quit()

colourprint.print_colored("Device has recieved scramble", colourprint.GREEN)