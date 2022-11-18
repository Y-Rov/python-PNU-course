import numpy as np

# Task 1
month_temperature = np.array(
    [4, 1, 0, -2, 5, 7, -3, 0, 0, 5, 0, -1, 3, 6, 9, 5, 7, 11, 9, 6, 0])
print(f'The number of days when the temperature was < 0: {len(month_temperature[month_temperature < 0])}')

# Task 2
print(f'The max degree: {month_temperature.max()}')

# Task 3
print(f'The number of day with the max degree: {month_temperature.argmax()}')

# Task 4
print(f'Was the temperature greater than +10? {np.any(month_temperature > 10)}')
print(f'Was the temperature greater than +20? {np.any(month_temperature > 20)}')

# Task 5
print(f'Was the temperature always greater than +10? {np.all(month_temperature < 10)}')

# Task 6
frozen_days = month_temperature[month_temperature < 0].copy()
print(frozen_days)

# Task 7
frozen_days.sort()
print(frozen_days)

# Task 8
print(f'The number of days when the temperature was > 0: {len(month_temperature[month_temperature > 0])}')

# Task 9
matrix_days_temperature = month_temperature.reshape(3, 7)
print(matrix_days_temperature)

# Task 10
print((matrix_days_temperature * 9 / 5) + 32)
