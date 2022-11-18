from math import sqrt, exp
from random import randint

# Task 7
# For the given number n < 100, complete the phrase "Zalik zdalo..."
# with the sentences "n studentiv", "n studenty" or "n student",
# using the correct endings.

n = input("Enter the quantity of students: ")
phrase = "Zalik zdalo"

if n.isnumeric():
    if n[-1] in "234":
        if len(n) > 1 and n[-2] == "1":
            result = f"{phrase} {n} studentiv"
        else:
            result = f"{phrase} {n} studenty"
    elif n[-1] == "1":
        if len(n) > 1 and n[-2] != "1" or n == "1":
            result = f"{phrase} {n} student"
        else:
            result = f"{phrase} {n} studentiv"
    else:
        result = f"{phrase} {n} studentiv"

print(result)

# Task 8
# Input: 2 non-negative real numbers a and b. b is not equal to 0.
# Output: a real number - the result of formula calculation.

a = float(input())
b = float(input())

x = sqrt(a * b) / (exp(a) * b) + (a * exp(2 * a / b))
print(x)

# Task 9
# Without using the arithmetic progression sum formula, calculate 1+x+x^2+...+x^n.
# The program receives an integer n and a real number x as input.

n = int(input())
x = float(input())
result = 0

for i in range(n + 1):
    result += x**i

print(result)

# Task 10
# Write a cycle which generates 10 random natural numbers

for i in range(10):
    print(randint(1,10))

# Task 11
# Create a program that asks the student to guess a number from 0 to 100.
# The machine tries to guess it by dividing the range of acceptable numbers in half.

print("Guess a number from 0 to 100!")
input("Are you ready? ")
game_end = False
left_border = 0
right_border = 100
while game_end == False:
    number_to_guess = (left_border + right_border) // 2
    result = input(f"Is your number - {number_to_guess}? (y - for yes, n - for no) ")
    if result == "y":
        print("Game Over!")
        game_end = True
    elif result == "n":
        answer = input(f"Is your number 'less' or 'greater' than {number_to_guess}? ")
        if answer == "less":
            right_border = number_to_guess
        elif answer == "greater":
            left_border = number_to_guess
