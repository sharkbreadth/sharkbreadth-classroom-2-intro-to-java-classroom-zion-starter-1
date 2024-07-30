# Python Template for Basic Dictionary Operations

def get_input():
    """
    Function to get user input for two dictionaries.
    """
    dict1 = eval(input("Enter the first dictionary (in the form {'key': value, ...}): "))
    dict2 = eval(input("Enter the second dictionary (in the form {'key': value, ...}): "))
    return dict1, dict2

def add_key_value(dictionary, key, value):
    """
    Function to add a key-value pair to a dictionary.
    """
    # Fill in the code to add the key-value pair to the dictionary
    return dictionary

def remove_key(dictionary, key):
    """
    Function to remove a key from a dictionary.
    """
    # Fill in the code to remove the key from the dictionary
    return dictionary

def merge_dictionaries(dict1, dict2):
    """
    Function to merge two dictionaries.
    """
    # Fill in the code to return the merged dictionary
    merged_dict = None
    return merged_dict

def find_value(dictionary, key):
    """
    Function to find the value associated with a given key in a dictionary.
    """
    # Fill in the code to return the value associated with the key
    value = None
    return value

def main():
    """
    Main function to perform the operations.
    """
    dict1, dict2 = get_input()
    
    key_to_add = input("Enter the key to add: ")
    value_to_add = input("Enter the value to add: ")
    dict1 = add_key_value(dict1, key_to_add, value_to_add)
    print(f"The dictionary after adding the key-value pair is: {dict1}")
    
    key_to_remove = input("Enter the key to remove: ")
    dict1 = remove_key(dict1, key_to_remove)
    print(f"The dictionary after removing the key is: {dict1}")
    
    merged_dict = merge_dictionaries(dict1, dict2)
    print(f"The merged dictionary is: {merged_dict}")
    
    key_to_find = input("Enter the key to find its value: ")
    value = find_value(merged_dict, key_to_find)
    print(f"The value associated with the key '{key_to_find}' is: {value}")

if __name__ == "__main__":
    main()
