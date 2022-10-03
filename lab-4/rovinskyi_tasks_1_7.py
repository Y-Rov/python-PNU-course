from random import randint
from typing import Dict, List, Tuple

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

# Task 5

def generate_all_combinations_of(symbols: str) -> List[str]:
    return [first_symb + second_symb for first_symb in symbols for second_symb in symbols]

print(generate_all_combinations_of("01"))

# Task 6

def get_every_word_occurence(text: str) -> Dict[str, int]:
    words = "".join(filter(lambda ch: ch not in ",?.!-:", text)).lower().split(' ')
    return {word : words.count(word) for word in words}

print(get_every_word_occurence("Hello - hello, hi! What's up?"))
