# Python Template for Basic List Operations

def get_input():
    """
    Function to get user input for two lists.
    """
    list1 = input("Enter the first list of numbers (comma-separated): ").split(',')
    list2 = input("Enter the second list of numbers (comma-separated): ").split(',')
    list1 = [int(num.strip()) for num in list1]
    list2 = [int(num.strip()) for num in list2]
    return list1, list2

def merge_lists(list1, list2):
    """
    Function to merge two lists.
    """
    # Fill in the code to return the merged list of list1 and list2
    merged_list = None
    return merged_list

def common_elements(list1, list2):
    """
    Function to find common elements in two lists.
    """
    # Fill in the code to return a list of common elements
    common_list = None
    return common_list

def sum_of_elements(list1, list2):
    """
    Function to find the sum of all elements in two lists.
    """
    # Fill in the code to return the sum of elements in list1 and list2
    sum_list1 = None
    sum_list2 = None
    return sum_list1, sum_list2

def max_element(list1, list2):
    """
    Function to find the maximum element in two lists.
    """
    # Fill in the code to return the maximum element in list1 and list2
    max_list1 = None
    max_list2 = None
    return max_list1, max_list2

def main():
    """
    Main function to perform the operations.
    """
    list1, list2 = get_input()
    
    print(f"The merged list of {list1} and {list2} is: {merge_lists(list1, list2)}")
    print(f"The common elements between {list1} and {list2} are: {common_elements(list1, list2)}")
    sum_list1, sum_list2 = sum_of_elements(list1, list2)
    print(f"The sum of elements in {list1} is: {sum_list1}")
    print(f"The sum of elements in {list2} is: {sum_list2}")
    max_list1, max_list2 = max_element(list1, list2)
    print(f"The maximum element in {list1} is: {max_list1}")
    print(f"The maximum element in {list2} is: {max_list2}")

if __name__ == "__main__":
    main()
