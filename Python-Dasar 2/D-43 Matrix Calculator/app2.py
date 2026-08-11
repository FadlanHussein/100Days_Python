import numpy as np

# Function to create matrix from user input
def get_matrix():
    rows = int(input("Enter number of rows : "))
    cols = int(input("Enter number of columns : "))

    print("Enter the elements of the matrix : ")

    matrix_list = []
    for i in range(rows):
        row = list(map(int, input().split()))
        matrix_list.append(row)
    return np.array(matrix_list)

# Example Usage
matrix = get_matrix()
print("Matrix : ", matrix)
