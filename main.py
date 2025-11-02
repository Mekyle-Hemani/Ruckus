import cubeStateManagement
import transformations
import visualizer
import solve

cubeArray = []

cubeArray=cubeStateManagement.resetCube()
cubeArray=transformations.applyTransformations(["u2","r'","l2","f2","d'","f2","d'","l2","d2","u'","f","d'","b'","f'","l'","u'","l2","r2"], cubeArray)
print(cubeArray)
visualizer.visualizeCube(cubeArray)
solve.solve(cubeArray)