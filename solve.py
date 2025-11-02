import transformations
import trainingProgress
import visualizer
import cubeStateManagement
import random

MOVES = ["f","f'","r","r'","u","u'","l","l'","d","d'","b","b'"]

Q={}

def chooseMove(state, randomness=1.0):
    if state not in Q:
        Q[state]= {}
        for move in MOVES:
            Q[state][move]= 0.0

    if random.random() < randomness:
        return random.choice(MOVES)
    else:
        bestMove = None #No best move yet
        bestValue = -float('inf') #Anything better than -infinity is the next best move
        for move, value in Q[state].items():
            if value > bestValue:
                bestValue = value
                bestMove = move
        return bestMove
    
def applyMove(cubeArray, state, move, alpha=0.1, gamma=0.9):
    import trainingProgress

    cubeArray = transformations.applyTransformations([move], cubeArray)

    newState = round(trainingProgress.calculateConnectingPieces(cubeArray), 2)
    reward = newState - state

    if state not in Q:
        Q[state] = {}
        for move in MOVES:
            Q[state][move] = 0.0
            
    if newState not in Q:
        Q[newState] = {}
        for move in MOVES:
            Q[newState][move] = 0.0

    bestFuture = max(Q[newState].values())
    Q[state][move] += alpha * (reward + gamma * bestFuture - Q[state][move])

    return cubeArray, newState

def solve(cubeArray, scrambleLength=2, maxSteps=20, initialRandomness=1.0):
    import trainingProgress

    #Small scramble
    scrambleMoves = random.choices(MOVES, k=scrambleLength)
    cubeArray = transformations.applyTransformations(scrambleMoves, cubeArray)

    #Initial state
    state = round(trainingProgress.calculateConnectingPieces(cubeArray), 2)
    randomness = initialRandomness

    for stepNum in range(maxSteps):
        move = chooseMove(state, randomness)
        cubeArray, state = applyMove(cubeArray, state, move)

        #Visualize progress
        visualizer.visualizeCube(cubeArray)
        print(f"Step {stepNum+1}: Move={move}, Progress={state}")

        randomness = max(0.1, randomness * 0.95)

    return cubeArray
    
if __name__ == "__main__":
    cubeArray = cubeStateManagement.resetCube()
    #cubeArray=transformations.applyTransformations(["u2","r'","l2","f2","d'","f2","d'","l2","d2","u'","f","d'","b'","f'","l'","u'","l2","r2"], cubeArray)
    # cubeArray=transformations.applyTransformations(["u","r"], cubeArray)
    # visualizer.visualizeCube(cubeArray)
    cubeArray=solve(cubeArray)
    visualizer.visualizeCube(cubeArray)