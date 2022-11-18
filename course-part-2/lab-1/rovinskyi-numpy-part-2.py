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
