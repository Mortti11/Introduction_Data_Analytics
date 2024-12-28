import numpy as np

# Creating 15x15 matrix with random values
matrix_saved = np.random.rand(15, 15)
print(matrix_saved)

# Saving matrix to file
np.savetxt('FristAssignment/matrix.txt', matrix_saved)

# print the shape of the matrix
print(matrix_saved.shape)