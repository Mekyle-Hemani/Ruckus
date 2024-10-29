import kociemba

def solve(scramble):
    try:
        solution = kociemba.solve(scramble)
        return solution
    except Exception as e:
        return (f"Error solving the cube: {e}")