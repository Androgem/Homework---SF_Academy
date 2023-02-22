while True:
    # Display available operations
    print("Please choose an operation: \n 1 = ADD \n 2 = SUBTRACT \n 3 = MULTIPLY \n 4 = DIVIDE")

    # Ask user to choose an operation
    operation = input("Enter operation number (1-4): ")

    # Validate operation input
    if operation.isdigit() and 1 <= int(operation) <= 4:
        operation = int(operation)
    else:
        print("Invalid operation number. Please try again.")
        continue

    # Ask user to input two numbers
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    # Validate number inputs
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("Invalid number input. Please try again.")
        continue

    # Perform selected operation
    if operation == 1:
        result = num1 + num2
        print(num1, "+", num2,"= ", result)
    elif operation == 2:
        result = num1 - num2
        print( num1, "-",num2,"= ", result)
    elif operation == 3:
        result = num1 * num2
        print(num1,"*",num2,"= ", result)
    elif operation == 4:
        if num2 == 0:
            print("Cannot divide by zero. Please enter a non-zero second number.")
            continue
        else:
            result = num1 / num2
            print( num1,"/",num2,"= ", result)

    # Ask user if they want to perform another calculation
    choice = input("Would you like to do a new calculation? (yes/no): ")
    if choice.lower() != "yes":
        break
