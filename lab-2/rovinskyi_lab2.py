print("Program menu:\n1. Create an empty list\n2. Add new element to the existing list\n3. List preview")
print("4. Create an automatic list of natural numbers with a certain length\n5. Change the list item by its index")
print("6. Insert an element at the specified position")
print("7. Remove a list item by its index\n8. Help (prints this menu again)\n9. Exit the program")
while True:
    print("-----------------------------")
    choice = input("You choice: ")
    try:
        if choice == '1':
            user_list = []
            print("Done")
        elif choice == '2':
            new_element = input("Element: ")
            user_list.append(new_element)
            print("Done")
        elif choice == '3':
            print(user_list)
        elif choice == '4':
            try:
                list_length = int(input("Length: "))
                if list_length <= 0:
                    print("An empty list is creating...")
                user_list = list(range(1, list_length + 1))
                print("Done")
            except ValueError:
                print("Length should be an integer!")
        elif choice == '5':
            index = int(input("Index: "))
            value = input("Value: ")
            user_list[index] = value
            print("Done")
        elif choice == '6':
            index = int(input("Index: "))
            value = input("Value: ")
            if index <= 0:
                print("Inserting at the beginning...")
            elif index >= len(user_list):
                print("Inserting at the end...")
            user_list.insert(index, value)
            print("Done")
        elif choice == '7':
            index = int(input("Index: "))
            user_list.pop(index)
            print("Done")
        elif choice == '8':
            print("Program menu:\n1. Create an empty list\n2. Add new element to the existing list\n3. List preview")
            print("4. Create an automatic list of natural numbers with a certain length")
            print("5. Change the list item by its index\n6. Insert an element at the specified position")
            print("7. Remove a list item by its index\n8. Help (prints this menu again)\n9. Exit the program")
        elif choice == '9':
            print("Have a nice day!")
            break
        else:
            print("This command is not supported! Command for help: '8'")
    except NameError:
        print("List is undefined, you need to create it firstly (command: '1')")
    except IndexError:
        print("Index is out of range, check the list content, how many elements it has etc.")
    except ValueError:
        print("Index should be an integer!")
    except OverflowError:
        print("The entered value is too big for integer!")
