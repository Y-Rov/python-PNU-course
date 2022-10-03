# Task 1
from typing import Dict


def get_amount_of_one_letter_words(text: str) -> int:
    """Returns the quantity of one letter words."""
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