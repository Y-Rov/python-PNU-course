# Task 1 
# Display the list of available products for the user.
# Create a cycle where the name of the product and its quantity are entered from the keyboard.
# If the product is not in the list - inform the user and offer to choose the next product.
# The purchase process-cycle stops when the final word is entered ("enough").
# After that, user's check is created and "printed".

products = [ 
    ['apple', 12], ['banana', 38.5], ['bread', 20.3], 
    ['potato', 40], ['cucumber', 18.2], ['tomato', 10]
]

sum_of_purchase = 0.0

print("Welcome to our shop!\nHere is the assortment:")
for product in products:
    for info in product:
        print(info, end = ' ')
    print('UAH/kg')

chosen_product = input("Please enter the product name (enough - to stop): ").lower()
purchase = []
while chosen_product != 'enough':
    previous_sum = sum_of_purchase
    for product in products:
        if chosen_product in product:
            quantity_flag = False
            while quantity_flag == False:
                try:
                    quantity = float(input("Please enter the quantity in kilos: "))
                    if quantity <= 0.0:
                        print("Product quantity should be a positive number!")
                        continue
                    quantity_flag = True
                except ValueError:
                    print("Product quantity should be a positive number!")
            partial_sum = product[1] * quantity
            sum_of_purchase += partial_sum
            purchase.append((chosen_product, quantity, partial_sum))
  
    if previous_sum == sum_of_purchase:
        print("This product is not for sale! Choose something else!")
  
    chosen_product = input("Please enter the product name (enough - to stop): ").lower()

if sum_of_purchase != 0.0:
    print("Here is your purchase: ")
    print("------------------------")
    for item, amount, total in purchase:
        print(f'{item} x {amount} = {total}')
    print("------------------------")
    print(f"To pay: {sum_of_purchase} UAH")
    print("Have a nice day!")

# Task 2
# 1. Create a dictionary where the key is the student's last name, the key value is a list of his grades.
# Students may have a different number of grades. Dictionary minimum - 5 students.

grade_book = { 
    "Doroshenko": [5, 4, 4, 5, 4], "Pavliv": [3, 4, 5, 4], "Kapush": [3, 3, 2], 
    "Ugrynia": [5, 4, 3, 2, 1], "Koropetskyi": [2, 2, 3, 3, 3, 1], 
    "Pavliuk": [5, 5, 4, 5], "Bodnar": [2, 1, 2]
}

# 2. Calculate the average score for each student.
# 3. Calculate how much debt there will be (average score less than 3).
zaborgovanist = 0
for student, marks in grade_book.items():
    average = sum(marks) / len(marks)
    if average < 3.0:
        zaborgovanist += 1
  
    print(f"{student}'s {average = }")

# 4. Create a new dictionary: student's last name and his/her average score.
zalik = { student: sum(marks) / len(marks) for student, marks in grade_book.items() }
print(f"{zaborgovanist = }")
print(zalik)

# Task 3
# 1. Create a group list, enter the data of students (at least 5). 
# The data of one student is in the dictionary.
group = [
    {"surname": "Shevchenko", "name": "Petro", "marks": [5, 2, 5]},
    {"surname": "Kolomiets", "name": "Mariia", "marks": [4, 3, 4, 5]},
    {"surname": "Kril", "name": "Oleksandr", "marks": [4, 3, 3, 4, 3]},
    {"surname": "Ivantsiv", "name": "Tetyana", "marks": [3, 4]},
    {"surname": "Korop", "name": "Vasyl", "marks": [5, 5, 5, 4, 4, 4]}
]

# 2. Display the data of the first student
print(group[0]["name"], group[0]["surname"], group[0]["marks"])

# 3. Format group output
for i in group:
    print(i["surname"].ljust(12),i["name"].ljust(10),i["marks"])

# 4. Calculate for each student his/her average score according to the given grades.
for student in group:
    average = sum(student["marks"]) / len(student["marks"])
    print(f"{student['surname']}'s {average = }")

# 5. Create a new dictionary: surname and the average of grades.
zalik = { s["surname"]:sum(s["marks"]) / len(s["marks"]) for s in group }
print(zalik)

# 6. Create a list of surnames
surnames = [ student["surname"] for student in group ]
print(surnames)

# 7. Calculate the average value of all average scores
print(f'Total average = {(sum(list(zalik.values())) / len(zalik))}')
