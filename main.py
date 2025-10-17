import cubeStateManagement
import transformations
import visualizer

cubeArray = []

cubeArray=cubeStateManagement.resetCube()
cubeArray=transformations.applyTransformations()
print(cubeArray)
visualizer.visualizeCube(cubeArray)