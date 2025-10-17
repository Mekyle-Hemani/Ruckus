import cubeStateManagement
import transformations
import visualizer

cubeArray = []

cubeArray=cubeStateManagement.resetCube()
cubeArray=transformations.applyTransformations(["f","r","u","r'","u'","f'"], cubeArray)
print(cubeArray)
visualizer.visualizeCube(cubeArray)