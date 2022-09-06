# Task 7 - For the given number n < 100, complete the phrase "Zalik zdalo..."
# with the sentences "n studentiv", "n studenty" or "n student",
# using the correct endings

n = int(input('Enter the quantity of students: '))
phrase = "Zalik zdalo"

if n % 10 >= 5 or n % 10 == 0 or 11 <= n <= 14:
    print(f"{phrase} {n} studentiv")
elif 2 <= n % 10 <= 4:
    print(f"{phrase} {n} studenty")
else:
    print(f"{phrase} {n} student")