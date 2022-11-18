import numpy as np

# Vectors part - Task 1
a = np.array([2, 1, 5])
b = np.array([5, 6, 7])

# Task 1.1
print(f'Vector A length = {np.linalg.norm(a)}')
print(f'Vector B length = {np.linalg.norm(b)}')

# Task 1.2
print(f'The dot product of vectors A and B = {np.dot(a, b)}')

# Task 1.3
cos_between_a_and_b = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)) 
print(f'The angle between vector A and B = {np.degrees(np.arccos(cos_between_a_and_b))}')

# Matrix part - Task 2
coeff_matrix = np.array([[2, 3, -1], [3, 2, -2], [4, 3, 1]])
equation_vector = np.array([5, 1, 13])
row_size = 3
print(coeff_matrix)

# Task 2.1 - Solve with the inverse matrix
main_det = np.linalg.det(coeff_matrix)
if (main_det == 0):
    print("There is no inverse matrix for this equation!")
    exit(1)

inverse_matrix = np.linalg.inv(coeff_matrix)
print(inverse_matrix)
first_result = np.dot(inverse_matrix, equation_vector)
print(first_result)

# Task 2.2 - Solve with Cramer's rule
main_det = np.linalg.det(coeff_matrix)
if (main_det == 0):
    print("There is no solutions or a lot of!")
    exit(1)

three_parts = [coeff_matrix.copy() for _ in range(row_size)]

for i in range(row_size):
    three_parts[i][:,i] = equation_vector

second_result = np.array([np.linalg.det(matrix) / main_det for matrix in three_parts])
print(second_result)

# Task 2.3 - Solve with np.linalg.solve
third_result = np.linalg.solve(coeff_matrix, equation_vector)
print(third_result)
