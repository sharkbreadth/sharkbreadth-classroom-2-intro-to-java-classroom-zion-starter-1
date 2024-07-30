# Python Template for Basic Operations with Two Numbers

def get_input():
    """
    Function to get user input for two numbers.
    """
    a = float(input("Enter the first number (a): "))
    b = float(input("Enter the second number (b): "))
    return a, b

def add(a, b):
    """
    Function to add two numbers.
    """
    # Fill in the code to return the sum of a and b
    result = None
    return result

def subtract(a, b):
    """
    Function to subtract two numbers.
    """
    # Fill in the code to return the difference of a and b
    result = None
    return result

def multiply(a, b):
    """
    Function to multiply two numbers.
    """
    # Fill in the code to return the product of a and b
    result = None
    return result

def divide(a, b):
    """
    Function to divide two numbers.
    """
    # Fill in the code to return the division of a by b
    # Make sure to handle the case when b is zero
    result = None
    return result

def main():
    """
    Main function to perform the operations.
    """
    a, b = get_input()
    
    print(f"The sum of {a} and {b} is: {add(a, b)}")
    print(f"The difference of {a} and {b} is: {subtract(a, b)}")
    print(f"The product of {a} and {b} is: {multiply(a, b)}")
    print(f"The division of {a} by {b} is: {divide(a, b)}")

if __name__ == "__main__":
    main()
