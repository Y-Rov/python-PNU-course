from random import randint
from typing import Dict, Tuple

# Task 1
def get_amount_of_one_letter_words(text: str) -> int:
    return len(tuple(filter(lambda word: (len(word) == 1), text.split(' '))))

print(f'Quantity = {get_amount_of_one_letter_words("I me a bc d efg h i")}')

# Task 2
def get_amount_of_vowels(text: str) -> int:
    return len(tuple(filter(lambda symbol: (symbol.lower() in ('a', 'e', 'i', 'o', 'u')), text)))

print(f'Quantity = {get_amount_of_vowels("Hello Python!")}')

# Task 3
def swap_keys_and_values(dictionary: dict) -> dict:
    return dict([(value, key) for key, value in dictionary.items()])

people = {"Adam": 30, "Bob": 12, "John": 34, "Jack": 45, "Liza": 22}
people = swap_keys_and_values(people)
print(people)

# Task 4
def generate_student_marks(people: Tuple[str, ...]) -> Dict[str, int]:
    return dict(zip(students, (randint(1, 100) for _ in range(len(people)))))

students = ("Hrynkiv", "Maksymchuk", "Luchynskyi", "Rovinskyi", "Pavliuk")
journal = generate_student_marks(students)
print(journal)
