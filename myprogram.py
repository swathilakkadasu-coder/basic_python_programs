def swap_numbers(a,b):
    """In python swapping two numbers can be done in a single line without using a temporary variable"""
    a, b = b, a  #swapping the values
    return b, a  #returns swapped values


#example usage
a = 5
b = 2
a, b = b, a
print(swap_numbers(a,b))  #output: (2,5)


