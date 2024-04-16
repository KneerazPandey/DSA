class Node(object):
    def __init__(self, val) -> None:
        self.val = val
        
    def __str__(self) -> str:
        return f'{self.val}'
    


class CircularLinkedList(object):
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0
        
    def add_first(self, val): # O(1)
        node = Node(val)
        if self.is_empty:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        
        self.tail.next = self.head # maintaining the circular reference
        self.count += 1  
    
    def add_last(self, val): # O(1)
        node = Node(val)
        if self.is_empty:
            self.head = self.tail = node 
            self.tail.next = self.head 
        else:
            self.tail.next = None
            self.tail.next = node
            self.tail = node
        
        self.tail.next = self.head # maintaing the circular reference
        self.count += 1
    
    def insert(self, index, val): # O(n)
        if index < 0 or index > self.count:
            raise Exception('Invalid Index. Index out of bounds')
        if index == 0:
            self.add_first(val)
        elif index == self.count:
            self.add_last(val) 
        else:
            node = Node(val)
            current = self.head
            for _ in range(index - 1):
                current = current.next 
            
            _next = current.next 
            current.next = node
            node.next = _next
            self.count += 1
    
    def remove_first(self): # O(1)
        if self.is_empty:
            raise Exception('List is empty. Cannot remove element.')
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            _next = self.head.next 
            self.head.next = None
            self.head = _next
            self.tail.next = self.head # maintaing the circular reference. 
        
        self.count -= 1

    def remove_last(self): # O(n)
        if self.is_empty:
            raise Exception('List is empty. Cannot remove an element.')
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            current = self.head
            while current.next.next != self.head:
                current = current.next  
            current.next = None
            self.tail = current
            self.tail.next = self.head # maintaining the circular reference.
            
        self.count -= 1
    
    def remove(self, val):
        index = self.index_of(val)
        if index == -1:
            raise Exception('The element does not exists to be removed.')
        
        self.remove_at(index) 
    
    def remove_at(self, index): # O(n)
        if index < 0 or index >= self.count:
            raise Exception('Invalid Index. Index out of bounds.')
        if index == 0:
            self.remove_first()
        elif index == self.count - 1:
            self.remove_last()
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
                
            to_remove = current.next 
            _next = to_remove.next 
            to_remove = None
            current.next = _next
                
            self.count -= 1
    
    def contains(self, val): # O(n)
        current = self.head
        if self.head is not None:
            while True:
                if current.val == val:
                    return True 
                current = current.next 
                if current == self.head:
                    break
        
        return False  
    
    def index_of(self, val): # O(n)
        counter = 0
        current = self.head 
        if self.head is not None:
            while True:
                if current.val == val:
                    return counter
                current = current.next
                counter += 1
                if current == self.head:
                    break 
                
        return -1   
    
    @property
    def is_empty(self):
        return self.head == self.tail == None 
        
    def __str__(self) -> str:
        if self.is_empty:
            return '[ ]'
        
        output = '[ '
        current = self.head
        while current.next != self.head:
            output += f'{current.val}, '
            current = current.next
        output += f'{current.val} ]'
        
        return output
    
    def __len__(self) -> int:
        return self.count
    
    
    
if __name__ == '__main__':
    c = CircularLinkedList()
    
    c.add_first(3)
    c.add_first(2)
    c.add_first(1)
    
    c.add_last(4)
    c.add_last(5)
    
    c.remove_first()
    
    c.remove_last()
    
    c.insert(1, 9)
    c.insert(3, 6)
    
    c.remove_at(3)
    c.remove_at(1)
    
    print(c)
    print(f'The length of curcular linked list is: {len(c)}')