class Stack(object):
    def __init__(self) -> None:
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
        
    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty. Cannot pop')
        item = self.stack.pop()
        return item

    
    def peek(self):
        if self.is_empty():
            raise Exception('Stack is empty. Cannot peek')
        item = self.stack[-1]
        return item
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def __str__(self) -> str:
        return f'{self.stack}'
    

if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(f"Top element is: {s.peek()}")
    print(f"Stack size is: {s.size()}")
    s.pop()
    s.pop()
    
    print(s)