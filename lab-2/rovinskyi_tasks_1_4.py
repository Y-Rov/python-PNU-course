# Task 1 - Create an empty list. Add items from the keyboard. Display the list. 
# Display the length of the list. Remove the first element.

new_list = []
for i in range(int(input())):
    new_list.append(int(input()))

print(new_list)
print(f"Length = {len(new_list)}")
new_list.pop(0)
print(new_list)