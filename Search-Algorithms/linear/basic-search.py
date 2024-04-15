def linearSearch(arr):
    n = len(arr)
    for i in range(n):
        if arr[i] == 'z':  # Use if condition to check if arr[i] is 'x'
            return True
    return False 
# Test the function with the array provided
arr = ['a', 'b', 'c', 'd', 'e', 'x']
result = linearSearch(arr)
print(f"Is 'x' in the array? {result}")

def linearSearchName(names,name):
    n = len(names)
    for i in range(n):
        if name == names[i]:
            return names[i]
    return  'Name not found'   # Else if name doesnt exist then return none
# Define the list of names
names = ['a', 'b', 'c', 'd', 'e', 'x']

# Promt user to enter name
name = input("Enter the name you want to search for: ")

# Call the prompt
result = linearSearchName(names, name)

# Print whether the name was found or not
print(f'{result}')