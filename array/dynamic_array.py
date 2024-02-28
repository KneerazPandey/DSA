import ctypes
import math


class DynamicArray(object):
    def __init__(self):
        self.capacity = 1
        self.count = 0
        self.array = self._create_array(self.capacity) 
        
    def append(self, item):
        if self.count >= self.capacity:
            self._resize_array() 
            
        self.array[self.count] = item
        self.count += 1 
        
    def insert(self, item, index):
        if index < 0 or index > self.count:
            raise Exception('Invalid Index') 
        
        if self.count >= self.capacity:
            self._resize_array()
        
        for i in range(self.count - 1, index - 1, -1):
            self.array[i + 1] = self.array[i]
            
        self.array[index] = item
        self.count += 1    
        
    def pop(self, index=None):
        if not index: index = self.count - 1    
        
        if index < 0 or index > self.count:
            raise Exception('Invalid Index')
        
        val = self.array[index]
        for i in range(index, self.count - 1):
            self.array[i] = self.array[i + 1] 
            
        self.count -= 1
        return val
    
    def remove_at(self, index):
        return self.pop(index) 
    
    def delete(self, item):
        index = self.index_of(item)
        if index == -1:
            raise Exception('Element does not exists')
        
        return self.pop(index) 
    
    def index_of(self, item):
        counter = 0
        for i in range(self.count):
            if self.array[i] == item:
                return counter
            counter += 1
        return -1
        
    def __len__(self) -> int:
        return self.count
    
    def __getitem__(self, index):
        if index < 0 or index >= self.count:
            raise Exception('Invalid Index') 
        
        return self.array[index]
    
    def __setitem__(self, index, item):
        if index < 0 or index >= self.count:
            raise Exception('Invalid Index')
        self.array[index] = item
    
    def __str__(self) -> str:
        if self.count == 0:
            return '[ ]'
        
        output = '[ '
        for i in range(self.count - 1):
            output += f'{self.array[i]}, '
        output += f'{self.array[self.count - 1]} ]'
        
        return output
    
    def _create_array(self, capacity: int) -> ctypes.Array:
        return (capacity * ctypes.py_object)()
    
    def _resize_array(self):
        new_capacity = math.ceil(self.capacity * 1.5)
        new_array = self._create_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        
        self.array = new_array 
        self.capacity = new_capacity
        
    