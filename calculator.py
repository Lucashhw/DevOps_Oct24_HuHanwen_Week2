import math

def calculator():
    choice = input("Enter choice: 1-Addition, 2-Subtraction: ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", num1 + num2)
    elif choice == "2":
        print("Result:", num1 - num2)
    else:
        print("Invalid Choice")

calculator()
