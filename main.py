import SimpleSerial.SimpleSerialMain
import grabScramble
import solve
import SimpleSerial
import colourprint

scramble = grabScramble.grabScramble()

solution = solve.solve(scramble)

colourprint.print_colored(solution, colourprint.GREEN)

#Establishing communication with microcontroller
while True:
    if "testing" in (SimpleSerial.SimpleSerialMain.readDataOnce(debug=1)):
        break
while True:
    SimpleSerial.SimpleSerialMain.writeDataOnce("sending")
    if "recieved" in (SimpleSerial.SimpleSerialMain.readDataOnce(debug=1)):
        break
colourprint.print_colored("Communication established", colourprint.BLUE)

SimpleSerial.SimpleSerialMain.writeDataOnce(solution)

while True:
    if "testing" in (SimpleSerial.SimpleSerialMain.readDataOnce(debug=1)):
        break

colourprint.print_colored(("Cube solved using "+solution), colourprint.GREEN)