class Node(object):
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        
    def __str__(self) -> str:
        return f'{self.val}'



class LinkedList(object):
    def __init__(self) -> None:
        self.head = None 
        self.count = 0
        
    def add_first(self, val) -> None:
        node = Node(val)
        if self.is_empty:
            self.head = node
        else:
            node.next = self.head
            self.head = node
            
        self.count += 1  
    
    def add_last(self, val) -> None:
        node = Node(val)
        if self.is_empty:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node 
        
        self.count += 1  
    
    def insert(self, index, val) -> None:
        if index < 0 or index > self.count:
            raise Exception('IndexOutOfBounds Exception') 
        if index == 0:
            self.add_first(val)
        elif index == self.count:
            self.add_last(val)
        else:
            counter = 1
            current = self.head
            while current:
                if index == counter:
                    break
                current = current.next
                counter += 1
                
            node = Node(val)
            _next = current.next
            current.next = node
            node.next = _next 
            
            self.count += 1 
    
    def remove_first(self) -> None:
        if self.is_empty:
            raise Exception('EmptyList Exception. List is already empty.')
        
        if self.head.next is None:
            self.head = None
        else:
            _next = self.head.next
            self.head.next = None
            self.head = _next
        
        self.count -= 1  
    
    def remove_last(self) -> None:
        if self.is_empty:
            raise Exception('EmptyList Exception. List is already empty.')
        
        if self.head.next is None:
            self.head = None 
        else:
            current = self.head
            while current.next.next:
                current = current.next 
            current.next = None 
        
        self.count -= 1
    
    def remove(self, val) -> None:
        index = self.index_of(val)
        if index == -1:
            raise Exception('The value does not exists in a list')
        self.remove_at(index)  
    
    def remove_at(self, index) -> None:
        if index < 0 or index >= self.count:
            raise Exception("IndexOutOfBounds Exception.") 
        if index == 0:
            self.remove_first()
        elif index == self.count:
            self.remove_last()
        else:
            counter = 1
            current = self.head
            while current:
                if counter == index:
                    break
                current = current.next
                counter += 1
            to_remove = current.next
            _next = to_remove.next 
            to_remove.next = None
            current.next = _next
            self.count -= 1
    
    def index_of(self, val) -> None:
        counter = 0
        current = self.head
        while current:
            if current.val == val:
                return counter
            current = current.next
            counter += 1 
            
        return -1
    
    def contains(self, val) -> bool:
        current = self.head
        while current:
            if current.val == val:
                return True
            current = current.next
        
        return False  
    
    def reverse(self):
        prev = None 
        current = self.head
        
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next 
            
        self.head = prev
    
    @property
    def is_empty(self):
        return self.head == None 
    
    def __len__(self) -> int:
        return self.count 
    
    def size(self):
        return self.count
    
    def __str__(self) -> str:
        if self.is_empty:
            return '[ ]'
        
        output = '[ '
        current = self.head
        while current:
            if current.next is None:
                break
            else:
                output += f'{current.val}, '
            current = current.next
            
        output += f'{current.val} ]'
        
        return output
    



if __name__ == '__main__':
    l = LinkedList()
    l.add_first(5)
    l.add_first(4)
    l.add_first(3)
    l.add_first(2)
    l.add_first(1)

    l.add_last(6)
    l.add_last(7)
    l.insert(1, 1.5)
    l.insert(5, 4.5)

    l.remove_last()
    l.remove_last()
    l.remove_at(1)
    l.remove_at(0)
    l.remove_at(3)
    l.remove_at(3)

    l.reverse()
    l.add_last(1)

    print(l)
    print(f'The size of Linked List is: {len(l)}')