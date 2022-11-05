# This script contains the solution for task №5

import pickle

class Person:
    def __init__(self) -> None:
        self.name = None
        self.byear = None

    def input(self):
        self.name = input('Прізвище: ')
        self.byear = input('Рік народження: ')

    def print(self):
        print(self.name, self.byear, end=' ')

class Familiar(Person):
    def __init__(self) -> None:
        super().__init__()
        self.phone = None

    def input(self):
        super().input()
        self.phone = input('Номер телефону: ')

    def print(self):
        super().print()
        print(self.phone, end=' ')

class PhoneDir:
    def __init__(self) -> None:
        self.contact_list: list = []

    def add_number(self, someone: Familiar) -> None:
        """Adds a new contact to the current list"""
        self.contact_list.append(someone)
        self.save_to_file()

    def find_phones_by_surname(self, surname: str) -> str:
        """Returns all phones that person with 'surname' has"""
        self.read_from_file()
        iter = filter(lambda familiar: (familiar.name == surname), self.contact_list)
        return " ".join([familiar.phone for familiar in iter])
    
    def replace_old_phone_for_someone(self, surname: str, new_phone: str) -> None:
        """Updates the phone number for the first occured person with 'surname'"""
        someone = next(filter(lambda familiar: (familiar.name == surname), self.contact_list))
        someone.phone = new_phone
        self.save_to_file()
    
    def save_to_file(self) -> None:
        with open('phones.txt', 'wb') as phones_file:
            pickle.dump(self, phones_file)
    
    def read_from_file(self) -> None:
        with open('phones.txt', 'rb') as phones_file:
            self = pickle.load(phones_file)

f1 = Familiar()
f1.input()
f2 = Familiar()
f2.input()
f3 = Familiar()
f3.input()
phones = PhoneDir()
phones.add_number(f1)
phones.add_number(f2)
phones.add_number(f3)

phones.find_phones_by_surname('Rovinskyi')
phones.replace_old_phone_for_someone('Pavliuk', '+380667654321')
