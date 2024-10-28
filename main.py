import SimpleSerial.SimpleSerialMain
import grabScramble
import solve
import SimpleSerial

scramble = grabScramble.grabScramble()

print(solve.solve(scramble))


#Establishing communication with microcontroller
while True:
    if "testing" in (SimpleSerial.SimpleSerialMain.readDataOnce):
        break
while True:
    SimpleSerial.SimpleSerialMain.writeDataOnce("sending")
    if "recieved" in (SimpleSerial.SimpleSerialMain.readDataOnce):
        break