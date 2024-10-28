import grabScramble
import solve
import SimpleSerial

scramble = grabScramble.grabScramble()

print(solve.solve(scramble))