def reverse_array(arr):
    """
    Reverses the given array.
    By using this slicing method, we can reverse the array efficiently.
    """
    return arr[::-1]    #it returns a new array that is the reverse of the input array

#Example usage
arr = [10,20,30,40,50]
print(reverse_array(arr))  #output: [50, 40, 30, 20, 10]


    
    