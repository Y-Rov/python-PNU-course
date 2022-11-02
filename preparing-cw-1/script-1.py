
def count_different_digits_in(number: int) -> int:
     return len(set(str(number)))

first_number: int = 133
second_number: int = 12345
print(count_different_digits_in(first_number))
print(count_different_digits_in(second_number))