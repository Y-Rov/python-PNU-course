# This script contains the solution for task №1 that consists of 2 parts

def count_different_digits_in(number: int) -> int:
    """Counts the amount of different digits in integer"""
    return len(set(str(number)))

def print_all_digits_that_not_in(number: int) -> None:
    """Prints all digits thar are not presented in integer"""
    digits = list(set('0123456789').difference(set(str(number))))
    digits.sort()
    print(digits)


first_number: int = 133
second_number: int = 12345
print(count_different_digits_in(first_number))
print(count_different_digits_in(second_number))
print_all_digits_that_not_in(first_number)
