def get_array_elements():
    """
    This function takes array elements from the user.
    """
    array_size = int(input("Enter the number of elements in the array: "))
    array = []
    for i in range(array_size):
        element = int(input("Enter element {}: ".format(i + 1)))
        array.append(element)
    return array


array = get_array_elements()
print("The array is: ", array)
