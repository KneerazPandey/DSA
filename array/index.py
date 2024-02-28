from dynamic_array import DynamicArray


a = DynamicArray()

a.append(1)
a.append(2)
a.append(3)
a.insert(0, 0)
a.insert(1.5, 2)
a.insert(4, 5)

print(a.pop(2))
print(a.remove_at(1))
print(a.delete(3))

a[0] = 1
a[2] = 3

print(a)
print(f'The size of an array is: {len(a)}')
