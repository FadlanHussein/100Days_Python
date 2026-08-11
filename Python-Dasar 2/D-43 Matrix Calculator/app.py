import numpy as np

# create a 2x2 Matrix
matrix = np.array([[1,2],[3,4]])
print(matrix)

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])

print("Addition : ", A+B)
print("Subtraction : ", A-B)
print("Multiplication : ", A*B)
print("Dot Product : ", np.dot(A, B))
print("Determinant : ", np.linalg.det(A))
print("Inverse : ", np.linalg.inv(A))
print("Eigenvalue : ", np.linalg.eig(A))
