import numpy as np

# Function to Get Matrix Input
def get_matrix():
    try:
        rows = int(input("Enter number of rows : "))
        cols = int(input("Enter number of columns : "))

        print("Enter the elements of the matrix : ")

        matrix_list = []
        for i in range(rows):
            row = list(map(int, input().split()))
            matrix_list.append(row)
        return np.array(matrix_list)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
        return None

# Matrix Operation
def matrix_operations(A, B):
    print("\n=== Matrix Operations ===")    
    try:
        print("\nAddition : \n", A+B)
    except ValueError:
        print("Error : Invalid input. Please enter valid numbers.")
    try:
        print("\nSubtraction : \n", A-B)
    except ValueError:
        print("Error : Invalid input. Please enter valid numbers.")
    try:
        print("\nMultiplication : \n", A*B)
    except ValueError:
        print("Error : Invalid input. Please enter valid numbers.")
    try:
        print("\nDot Product : \n", np.dot(A, B))
    except ValueError:
        print("Error : Invalid input. Please enter valid numbers.")
    try:
        print("\nDeterminant : \n", np.linalg.det(A))
    except ValueError:
        print("Error : Invalid input. Please enter valid numbers.")
    try:
        print("\nInverse : \n", np.linalg.inv(A))
        print("\nEigenvalue : \n", np.linalg.eig(A))
    except ValueError:
        print("Error : Invalid input. Please enter valid numbers.")    
    

# Main Program
if __name__ == "__main__":
    print("Matrix Calculator")
    A = get_matrix()
    if A is None:
        exit()
    B = get_matrix()
    if B is None:
        exit()
    if A is not None and B is not None:
        matrix_operations(A, B)