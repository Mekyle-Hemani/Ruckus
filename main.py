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

ser = serial.Serial('COM4', 9600)
data = "a"+solution
try:
    ser.write((data + "\n").encode())
    time.sleep(1)
except Exception as e:
    print("Error sending data:", e)
finally:
    ser.close()