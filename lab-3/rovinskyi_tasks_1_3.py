products = [['apple', 12], ['banana', 38.5], ['bread', 20.3],
            ['potato', 40], ['cucumber', 18.2], ['tomato', 10]]
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
  for item, amount, sum in purchase:
    print(f'{item} x {amount} = {sum}')
  print("------------------------")
  print(f"To pay: {sum_of_purchase} UAH")
print("Have a nice day!")