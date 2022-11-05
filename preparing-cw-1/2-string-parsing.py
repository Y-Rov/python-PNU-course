# This script contains the solution for tasks №3 and №4

from collections import Counter

def if_brackets_are_correctly_placed_in(text: str) -> str:
    """Checks if text contains all '(' and ')'"""
    modified = "".join(filter(lambda symbol: (symbol == '(' or symbol == ')'), text))
    return "так" if text.count('(') == text.count(')') and modified.endswith(')') and modified.startswith('(') else "ні"

print(if_brackets_are_correctly_placed_in("sw(ss(sd)sd)"))

def print_vowels_that_are_everywhere(text: str) -> None:
    """Prints all vowels which are in each word"""
    print(*set(filter(lambda symbol: (symbol in 'aeuio'), text.lower())))

def print_vowels_that_are_nowhere(text: str) -> None:
    """Prints all vowels that are not a part of any word"""
    founded_vowels = set(filter(lambda symbol: (symbol in 'aeuio'), text.lower()))
    print(*set(str('aueio')).difference(founded_vowels))

def print_letters_that_are_in(text: str) -> None:
    """Prints the first occurrences of letters in the text, keeping the initial mutual order"""
    words = text.lower().rstrip('.').split(' ')
    print(list(dict.fromkeys(list("".join(words)))))

def print_two_times_and_more_letters_in(text: str) -> None:
    """Prints all letters included in the text at least twice"""
    words = text.lower().rstrip('.').split(' ')
    letter_counter = Counter("".join(words))
    print([key for key, value in letter_counter.items() if value >= 2])

def print_one_time_letters_in(text: str) -> None:
    """Prints all letters included in the text once"""
    words = text.lower().rstrip('.').split(' ')
    letter_counter = Counter("".join(words))
    print([key for key, value in letter_counter.items() if value == 1])

print_vowels_that_are_everywhere('Hello world.')
print_vowels_that_are_nowhere('Hello amazing world.')
print_letters_that_are_in('Hello incredible world.')
print_two_times_and_more_letters_in('Hello lollipop')
print_one_time_letters_in('Hello world.')
