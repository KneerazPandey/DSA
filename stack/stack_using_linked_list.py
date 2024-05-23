class Node(object):
    def __init__(self, val) -> None:
        self.val = val 
        self.next = None

class Stack(object):
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0
        
    def push(self, val):
        node = Node(val)
        if self.is_empty():
            self.head = self.tail = node 
        else:
            self.tail.next = node
            self.tail =node
        
        self.count += 1
    
    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty. Cannot pop an element from an empty stack')
        if self.head.next is None:
            self.head = self.tail = None
        else:
            current = self.head
            while current:
                if current.next == self.tail:
                    break
                current = current.next
            current.next = None
            self.tail = current 
        
        self.count -= 1 
    
    def peek(self):
        if self.is_empty():
            raise Exception('Stack is empty. Cannot peek an element from empty stack') 
        return self.tail.val 
        
    def is_empty(self):
        return self.head == self.tail == None
    
    def size(self):
        return self.cout
    
    def __len__(self):
        return self.count
    
    def __str__(self) -> str:
        if self.is_empty():
            return '[ ]'
        
        output = '[ '
        current = self.head
        while current:
            if current.next is None:
                output += f'{current.val} ]'
            else:
                output += f'{current.val}, '
            current = current.next 
    
        return output
    
    
    

if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    
    s.pop()
    s.pop()
    
    print(s)
    print(f'The peek element is: {s.peek()}')
    print(f'The length of the stack is: {len(s)}')