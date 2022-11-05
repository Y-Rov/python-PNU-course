def reverse(func):
    def wrapper():
        result_list = func()
        result_list.reverse()
        return result_list
    return wrapper

@reverse
def generate_list() -> list:
    return [1, 2, 3, 4, 5]

print(generate_list())

def check_duplicate_values(func):
    def wrapper(input_dict: dict):
        values = list(input_dict.values())
        if (len(values) != len(set(values))):
            raise ValueError
        else:
            return func(input_dict)
    
    return wrapper

@check_duplicate_values
def swap_keys_and_values(dictionary: dict) -> dict:
    return dict([(value, key) for key, value in dictionary.items()])

people = {"Adam": 30, "Bob": 12, "John": 34, "Jack": 45, "Liza": 22}
people = swap_keys_and_values(people)
print(people)

def remove_digits_and_punctuation(get_text):
    def wrapper():
        text = get_text()
        return "".join(filter(lambda symbol: (symbol not in '.,!?:;-\"\'()'), text))
    
    return wrapper

@remove_digits_and_punctuation
def generate_text() -> str:
    return "The winner takes it all! I don't wanna talk if it makes you feel sad..."

print(generate_text())