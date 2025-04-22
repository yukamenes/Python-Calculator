from art import *
import os

def add(n1, n2):
    """Add two numbers."""
    return n1 + n2

def subtract(n1, n2):
    """Subtract n2 from n1."""
    return n1 - n2

def multiply(n1, n2):
    """Multiply two numbers."""
    return n1 * n2

def divide(n1, n2):
    """Divide n1 by n2."""
    if n2 == 0:
        raise ValueError("Cannot divide by zero!")
    return n1 / n2

# Dictionary mapping operations to their respective functions
math_operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def get_number(prompt):
    """Get a valid number from user input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def get_operation():
    """Get a valid operation from user input."""
    while True:
        op = input("+\n-\n*\n/\nPick an operation: ")
        if op in math_operations:
            return op
        print("Invalid operation. Please choose +, -, *, or /.")

def calculate_and_print_result(op, first_number, next_number):
    """Perform the operation and print the result."""
    try:
        result = math_operations[op](first_number, next_number)
        print(f"{first_number} {op} {next_number} = {result}")
        return result
    except ValueError as e:
        print(e)
        return None

def get_continue_choice(result):
    """Get user's choice to continue or start new calculation."""
    while True:
        choice = input(f"Type 'y' to continue calculating with {result}, 'n' to start a new calculation, or 'e' to exit: ").lower()
        if choice in ['y', 'n', 'e']:
            return choice
        print("Please enter 'y', 'n', or 'e'.")

# Main program
print(logo)
while True:
    first_number = get_number("What's the first number?: ")
    operation = get_operation()
    next_number = get_number("What's the next number?: ")

    result = calculate_and_print_result(operation, first_number, next_number)
    if result is None:
        continue

    nextCalc = get_continue_choice(result)
    if nextCalc == 'e':
        print("Goodbye!")
        break
    while nextCalc == 'y':
        operation = get_operation()
        next_number = get_number("What's the next number?: ")
        result = calculate_and_print_result(operation, result, next_number)
        if result is None:
            break
        nextCalc = get_continue_choice(result)
    os.system('cls||clear')
    print(logo)