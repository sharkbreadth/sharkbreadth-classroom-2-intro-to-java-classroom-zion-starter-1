# Python Template for Basic String Operations

def get_input():
    """
    Function to get user input for two strings.
    """
    str1 = input("Enter the first string (str1): ")
    str2 = input("Enter the second string (str2): ")
    return str1, str2

def concatenate(str1, str2):
    """
    Function to concatenate two strings.
    """
    # Fill in the code to return the concatenation of str1 and str2
    result = None
    return result

def length_of_string(str1, str2):
    """
    Function to find the length of two strings.
    """
    # Fill in the code to return the lengths of str1 and str2
    length_str1 = None
    length_str2 = None
    return length_str1, length_str2

def to_uppercase(str1, str2):
    """
    Function to convert two strings to uppercase.
    """
    # Fill in the code to return str1 and str2 in uppercase
    uppercase_str1 = None
    uppercase_str2 = None
    return uppercase_str1, uppercase_str2

def is_substring(str1, str2):
    """
    Function to check if one string is a substring of the other.
    """
    # Fill in the code to check if str1 is a substring of str2 or vice versa
    result = None
    return result

def main():
    """
    Main function to perform the operations.
    """
    str1, str2 = get_input()
    
    print(f"The concatenation of '{str1}' and '{str2}' is: '{concatenate(str1, str2)}'")
    length_str1, length_str2 = length_of_string(str1, str2)
    print(f"The length of '{str1}' is: {length_str1}")
    print(f"The length of '{str2}' is: {length_str2}")
    uppercase_str1, uppercase_str2 = to_uppercase(str1, str2)
    print(f"The uppercase version of '{str1}' is: '{uppercase_str1}'")
    print(f"The uppercase version of '{str2}' is: '{uppercase_str2}'")
    print(f"Is one string a substring of the other? {is_substring(str1, str2)}")

if __name__ == "__main__":
    main()
