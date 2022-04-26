number1 = float(input("Write the first number: "))
number2 = float(input("Write the second number: "))
option = 0

while (option != 5):
    print("\nMenu: ")
    print("1.- Sum of the two numbers")
    print("2.- Substraction of the two numbers")
    print("3.- Multiplication of the two numbers")
    print("4.- Division of two numbers")
    print("5.- Exit")
    option = int(input("Option: "))

    if option > 5 or option < 1:
        print(option, "is not an option, try again")
    elif option == 5:
        print("Good bye!")
    else:
        if option == 1:
            result = number1 + number2
        if option == 2:
            result = number1 - number2
        if option == 3:
            result = number1 * number2
        if option == 4:
            result = number1 / number2
        print("Result is: ", result)
