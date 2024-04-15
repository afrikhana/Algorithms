def linearSearch(arr):
    n = len(arr)
    for i in range(n):
        if arr[i] == 'x':  # Use if condition to check if arr[i] is 'x'
            return True
    return False 
# Test the function with the array provided
arr = ['a', 'b', 'c', 'd', 'e', 'x']
result = linearSearch(arr)
print(f"Is 'x' in the array? {result}")
    