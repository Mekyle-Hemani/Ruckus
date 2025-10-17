import cubeStateManagement
import transformations
import visualizer

cubeArray = []

cubeArray=cubeStateManagement.resetCube()
cubeArray=transformations.applyTransformations(["r2","u2"])
print(cubeArray)
visualizer.visualizeCube(cubeArray)