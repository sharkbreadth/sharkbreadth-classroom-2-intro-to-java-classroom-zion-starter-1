# Python Template for Basic Tuple Operations

def create_tuple():
    """
    Function to create a tuple from user input.
    """
    tuple_elements = input("Enter the elements of the tuple (comma-separated): ").split(',')
    tuple_elements = tuple(map(str.strip, tuple_elements))
    return tuple_elements

def access_element(t, index):
    """
    Function to access an element from the tuple.
    """
    # Fill in the code to access the element at the given index
    element = None
    return element

def slice_tuple(t, start, end):
    """
    Function to slice a tuple.
    """
    # Fill in the code to return the sliced tuple from start to end
    sliced_tuple = None
    return sliced_tuple

def find_index(t, element):
    """
    Function to find the index of an element in the tuple.
    """
    # Fill in the code to return the index of the element in the tuple
    index = None
    return index

def main():
    """
    Main function to perform the operations.
    """
    t = create_tuple()
    
    index_to_access = int(input("Enter the index to access: "))
    element = access_element(t, index_to_access)
    print(f"The element at index {index_to_access} is: {element}")
    
    start_index = int(input("Enter the start index for slicing: "))
    end_index = int(input("Enter the end index for slicing: "))
    sliced_t = slice_tuple(t, start_index, end_index)
    print(f"The sliced tuple from index {start_index} to {end_index} is: {sliced_t}")
    
    element_to_find = input("Enter the element to find its index: ")
    element_index = find_index(t, element_to_find)
    print(f"The index of the element '{element_to_find}' is: {element_index}")

if __name__ == "__main__":
    main()
