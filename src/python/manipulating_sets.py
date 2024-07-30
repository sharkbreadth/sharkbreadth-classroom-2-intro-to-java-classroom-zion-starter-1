# Python Template for Basic Set Operations

def get_input():
    """
    Function to get user input for two sets.
    """
    set1 = set(input("Enter the first set of elements (comma-separated): ").split(','))
    set2 = set(input("Enter the second set of elements (comma-separated): ").split(','))
    return set1, set2

def add_element(s, element):
    """
    Function to add an element to a set.
    """
    # Fill in the code to add the element to the set
    return s

def remove_element(s, element):
    """
    Function to remove an element from a set.
    """
    # Fill in the code to remove the element from the set
    # Make sure to handle the case when the element is not present in the set
    return s

def union_sets(set1, set2):
    """
    Function to find the union of two sets.
    """
    # Fill in the code to return the union of set1 and set2
    union_set = None
    return union_set

def intersection_sets(set1, set2):
    """
    Function to find the intersection of two sets.
    """
    # Fill in the code to return the intersection of set1 and set2
    intersection_set = None
    return intersection_set

def main():
    """
    Main function to perform the operations.
    """
    set1, set2 = get_input()
    
    element_to_add = input("Enter the element to add to the first set: ")
    set1 = add_element(set1, element_to_add)
    print(f"The first set after adding the element is: {set1}")
    
    element_to_remove = input("Enter the element to remove from the first set: ")
    set1 = remove_element(set1, element_to_remove)
    print(f"The first set after removing the element is: {set1}")
    
    union_set = union_sets(set1, set2)
    print(f"The union of the sets is: {union_set}")
    
    intersection_set = intersection_sets(set1, set2)
    print(f"The intersection of the sets is: {intersection_set}")

if __name__ == "__main__":
    main()
