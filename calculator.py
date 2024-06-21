"""Design a simple calculator with basic arithmetic operations.
Prompt the user to input two numbers and an operation choice."""

import time
# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Main function to run the calculator
def calculator():
    print("Welcome to Simple Calculator!")
    time.sleep(2)
    print("Operations available:")
    time.sleep(1)
    print("1. Addition (+)")
    time.sleep(1)
    print("2. Subtraction (-)")
    time.sleep(1)
    print("3. Multiplication (*)")
    time.sleep(1)
    print("4. Division (/)")
    time.sleep(1)

    # Take input from the user
    choice = int(input("Enter operation choice (1/2/3/4): "))

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = 0
    if choice == 1:
        result = add(num1, num2)
    elif choice == 2:
        result = subtract(num1, num2)
    elif choice == 3:
        result = multiply(num1, num2)
    elif choice == 4:
        result = divide(num1, num2)
    else:
        print("Invalid input. Please enter a valid operation choice.")

    print("Result:", result)

# Run the calculator
calculator()

