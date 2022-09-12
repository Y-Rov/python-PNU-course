from random import randrange

# Task 1 
# Create an empty list. Add items from the keyboard. Display the list. 
# Display the length of the list. Remove the first element.

first_list = []
for i in range(int(input())):
    first_list.append(int(input()))

print(first_list)
print(f"Length = {len(first_list)}")
first_list.pop(0)
print(first_list)

# Task 2
# Specify a list created by random numbers from 1 to 9 and print.
# Add it to the end of the previous list

second_list=[]
n = int(input())
for i in range(n):
    second_list.append(randrange(1, 10))

print(second_list)
first_list += second_list
print(first_list)

# Task 3
# Enter a word from the keyboard.
# Turn it into a list.

word = input()
symbols = list(word)
print(symbols)

# Task 4
# The number x is entered from the keyboard. Calculate the fraction 1/x.
# The possibility of a "division by zero" error is determined by a block "Division by zero is not possible"

x = int(input())
try:
    result = 1 / x
    print(result)
except ZeroDivisionError:
    print("Ділити на нуль не можна")
