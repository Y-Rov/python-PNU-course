from collections import Counter
from typing import Dict

def reverse(get_list):
    def wrapper():
        result_list = get_list()
        result_list.reverse()
        return result_list
    return wrapper

@reverse
def generate_list() -> list:
    return [1, 2, 3, 4, 5]

print(generate_list())

def check_duplicate_values(swap):
    def wrapper(input_dict: dict):
        values = list(input_dict.values())
        if (len(values) != len(set(values))):
            raise ValueError
        else:
            return swap(input_dict)
    
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

def check_unsuitable_values(get_session_result):
    def wrapper(students: dict):
        marks = ["Незадовільно", "Задовільно", "Добре", "Відмінно"]
        for value in students.values():
            if value not in marks:
                return 'Сесія ще не завершена'
        
        return get_session_result(students)

    return wrapper

@check_unsuitable_values
def get_session_results(students: Dict[str, str]) -> Counter:
    return Counter(students.values())

test_result = {
    "Hrynkiv": "Добре", "Maksymchuk": "Задовільно", "Ivanov": "Незадовільно",
    "Rovinskyi": "Добре", "Pavliuk": "Відмінно"
}
print(get_session_results(test_result))
