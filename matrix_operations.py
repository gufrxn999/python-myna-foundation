import numpy as np

# Define two 2x2 matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Matrix addition
add = A + B
print("Matrix Addition:\n", add)

# Element-wise multiplication
elementwise = A * B
print("\nElement-wise Multiplication:\n", elementwise)

# Matrix multiplication (dot product)
dot = A.dot(B)
print("\nMatrix Multiplication (Dot Product):\n", dot)

# Transpose of matrix A
transpose = A.T
print("\nTranspose of Matrix A:\n", transpose)
