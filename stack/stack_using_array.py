import ctypes

class Stack(object):
    def __init__(self, capacity) -> None:
        self.top = -1
        self.capacity = capacity
        self.stack = self.create_array(self.capacity)
        
    def push(self, item):
        self.top += 1
        if self.top >= self.capacity:
            raise Exception('Stack is full. Cannot add more element.')
        self.stack[self.top] = item 
    
    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty. Cannot pop an elment from an empty stack')
        data = self.stack[self.top]
        self.top -= 1
        return data 
    
    def is_full(self):
        return self.top + 1 == self.capacity  
    
    def peek(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.stack[self.top] 
    
    def create_array(self, size):
        return (size * ctypes.py_object)() 
    
    def is_empty(self):
        return self.top == -1
    
    def __str__(self) -> str:
        if self.is_empty():
            return '[ ]'
        
        output = []
        for index in range(self.top + 1):
            output.append(self.stack[index])
        
        return f'{output}'
    
    
    
    

if __name__ == '__main__':
    s = Stack(capacity=4)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    print(s)  