def linear_search(array, target):
    for i in range(0, len(array)):
        if array[i] == target:
            return i 
        
    return -1

array = [2, 4, 0, 1, 9]
target = 1

result = linear_search(array, target)
if result == -1:
    print('Element not found')
else:
    print(f'Element found at index: {result}')