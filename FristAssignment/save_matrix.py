import numpy as np

# Creating 15x15 matrix with random values
matrix = np.random.rand(15, 15)
print(matrix)

# Saving matrix to file
np.savetxt('FristAssignment/matrix.txt', matrix)

# print the shape of the matrix
print(matrix.shape)