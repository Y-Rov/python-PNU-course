# --------------------------------------------------------------------------------------------------
# Task 1

from typing import List
from math import sqrt

def count_the_largest_number_of_consecutive_digits(row: str) -> int:
    digit_to_compare: str = '0'
    result, counter = 1, 1
    for digit in row:
        if digit_to_compare == digit:
            counter += 1
        else:
            digit_to_compare = digit
            result = max(counter, result)
            counter = 1
    
    result = max(counter, result)
    return result

print(count_the_largest_number_of_consecutive_digits('123444555566667777'))

# --------------------------------------------------------------------------------------------------
# Task 2

class Address:
    def __init__(self, street: str, house: str, apartment_number: int) -> None:
        self._street = street
        self._house = house
        self._apartment_number = apartment_number
    
    @property
    def street(self):
        return self._street
    
    @property
    def house(self):
        return self._house
    
    @property
    def apartment_number(self):
        return self._apartment_number

    def __eq__(self, other) -> bool:
        return self.street == other.street and self.house == other.house and self.apartment_number == other.apartment_number

    def __str__(self) -> str:
        return f'Address - {self.street}, house - {self.house}, apartment - {self.apartment_number}'


class Citizen:
    def __init__(self, surname: str, city: str, address: Address) -> None:
        self._surname = surname
        self._city = city
        self._address = address
    
    @property
    def surname(self):
        return self._surname
    
    @property
    def city(self):
        return self._city
    
    @property
    def address(self):
        return self._address
    
    def __str__(self) -> str:
        return f'Citizen - {self.surname}; city - {self.city}; address - {self.address}.'

def find_citizens_who_have_the_same_address(citizens_list: List[Citizen], address: Address):
    iter = filter(lambda citizen: citizen.address == address, citizens_list)
    return (next(iter), next(iter))

citizens: List[Citizen] = [
    Citizen('Pavliuk', 'Ivano-Frankivsk', Address('Mazepy', '12A', 5)),
    Citizen('Rovinskyi', 'Lviv', Address('Nezalezhnosti', '12A', 5)),
    Citizen('Hrynkiv', 'Lviv', Address('Mazepy', '12A', 5))]

citizen1, citizen2 = find_citizens_who_have_the_same_address(citizens, Address('Mazepy', '12A', 5))
print(citizen1)
print(citizen2)

# --------------------------------------------------------------------------------------------------
# Task 3

class SumIterator:
    def __init__(self, range: int) -> None:
        self.range = range
    
    def __iter__(self):
        self.current_number: int = 1
        return self

    def __next__(self):
        if self.current_number <= self.range:
            result_sum = sum(range(1, self.current_number + 1))
            self.current_number += 1
            return result_sum
        else:
            raise StopIteration
        
obj = SumIterator(5)
sum_iter = iter(obj)
for sum_res in sum_iter:
    print(sum_res)

# --------------------------------------------------------------------------------------------------
# Task 4

class Complex:
    def __init__(self, real: float = 0, imag: float = 0) -> None:
        self._real_part = real
        self._imag_part = imag

    def __str__(self) -> str:
        return f'{self._real_part:+}{self._imag_part:+}i'
    
    def __add__(self, other):
        self._real_part += other._real_part
        self._imag_part += other._imag_part
        return self
    
    def __sub__(self, other):
        self._real_part -= other._real_part
        self._imag_part -= other._imag_part
        return self

    def __mul__(self, other):
        self._real_part = self._real_part * other._real_part - self._imag_part * other._imag_part
        self._imag_part = self._real_part * other._imag_part + self._imag_part * other._real_part
        return self
    
    @property
    def modulus(self) -> float:
        return sqrt(pow(self._real_part, 2) + pow(self._imag_part, 2))


complex1 = Complex(3, 7)
complex2 = Complex(8, 11)
print(complex1)

complex1 = complex1 + complex2
print(complex1)

complex3 = Complex(7, 9)
complex4 = Complex(3, 4)
complex1 = complex3 - complex4
print(complex1)

complex5 = Complex(1, 4)
complex6 = Complex(5, 1)
complex1 = complex5 * complex6
print(complex1)
complex7 = Complex(0, 3)
print(complex7.modulus)
