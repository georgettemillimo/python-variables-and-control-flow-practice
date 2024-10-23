# inputs from the user
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
operation = input("Enter your desired operation (+, -, *, /): ")

# Perform operation is desired by the user
if operation == "+":
    print("Result:", number1 + number2)
elif operation == "-":
    print("Result:", number1 - number2)
elif operation == "*":
    print("Result:", number1 * number2)
elif operation == "/":
    if number2 != 0:
        print("Result:", number1 / number2)
    else:
        print("Error: You cannot divide the number by zero")
else:
    print("Error: Invalid operation")
