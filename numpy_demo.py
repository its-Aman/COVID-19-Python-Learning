import numpy as np

print(np.__version__)

arr_1D = np.array([1, 2, 3, 4, 5], ndmin=5)
print(arr_1D)
print(arr_1D.ndim)

arr_2D = np.array([['a', 'b'], ['x', 'y']])
print(arr_2D.ndim)
print(arr_2D[0, 0], arr_2D[0, 1], arr_2D[1, 0], arr_2D[1, 1])

arr_3D = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr_3D.ndim)

arr_4D = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr_4D.ndim)
