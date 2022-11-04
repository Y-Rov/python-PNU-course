def print_vowels_that_are_everywhere(text: str) -> None:
    print(*set(filter(lambda symbol: (symbol in 'aeuio'), text.lower())))

def print_vowels_that_are_nowhere(text: str) -> None:
    founded_vowels = set(filter(lambda symbol: (symbol in 'aeuio'), text.lower()))
    print(*set(str('aueio')).difference(founded_vowels))

print_vowels_that_are_everywhere('Hello world.')
print_vowels_that_are_nowhere('Hello amazing world.')