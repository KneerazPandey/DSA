class Node(object):
    def __init__(self, val) -> None:
        self.val = val
        self.prev = None
        self.next = None
        
        

class DoublyLinkedList(object):
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0
        
    def add_first(self, val):
        node = Node(val)
        if self.is_empty:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.count += 1   
    
    def add_last(self, val):
        node = Node(val)
        if self.is_empty:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.count += 1 
    
    def insert(self, index, val):
        if index < 0 or index > self.count:
            raise Exception('Index out of bounds. IndexError')
        if index == 0:
            self.add_first(val)
        elif index == self.count:
            self.add_last(val)
        else:
            node = Node(val)
            current = self.head
            counter = 1
            while current:
                if counter == index:
                    break
                current = current.next
                counter += 1
            _next = current.next
            current.next = node
            node.prev = current
            node.next = _next
            _next.prev = node
            self.count += 1 
    
    def remove_first(self):
        if self.is_empty:
            raise Exception('List is empty')
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            _next = self.head.next
            _next.prev = None
            self.head.next = None
            self.head = _next 
        self.count -= 1 
    
    def remove_last(self):
        if self.is_empty:
            raise Exception('List is empty.')
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            _prev = self.tail.prev
            self.tail.prev = None
            _prev.next = None
            self.tail = _prev
        self.count -= 1 
    
    def remove(self, val):
        index = self.index_of(val)
        if index == -1:
            raise Exception('Element does not exist in a list to be removed.')
        self.remove_at(index) 
    
    def remove_at(self, index):
        if index < 0 or index >= self.count:
            raise Exception("IndexError. Index out of bounds")
        if index == 0:
            self.remove_first()
        elif index == self.count - 1:
            self.remove_last()
        else:
            counter = 0
            current = self.head
            while current:
                if counter == index:
                    break
                current = current.next
                counter += 1
            _prev = current.prev
            _next = current.next
            current.next = None
            current.prev = None
            _prev.next = _next
            _next.prev = _prev
            self.count -= 1 
    
    def contains(self, val):
        current = self.head
        while current:
            if current.val == val:
                return True 
            current = current.next
            
        return False  
    
    def index_of(self, val):
        counter = 0
        current = self.head
        
        while current:
            if current.val == val:
                return counter
            current = current.next
            counter += 1 
            
        return -1
    
    def reverse(self):
        current = self.head
        temp = None
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp:
            self.head = temp.prev 
        
    @property
    def is_empty(self):
        return self.head == None
    
    def size(self) -> int:
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
    
    def __len__(self) -> int:
        return self.count
    
    
    
    

if __name__ == '__main__':
    d = DoublyLinkedList()
    
    d.add_first(3)
    d.add_first(2)
    d.add_first(1)
    d.add_first(2)
    
    d.add_last(4)
    d.add_last(5)
    
    d.remove_first()
    d.remove_first()
    d.remove_first()
    
    d.remove_last()
    d.remove_last()
    d.remove_last()
    
    d.insert(0, 1)
    d.insert(1, 4)
    d.insert(1, 3)
    d.insert(1, 2)
    d.insert(len(d), 5)
    d.insert(0, 0)
    d.insert(4, 3.5)
    d.insert(len(d), 6)
    
    d.remove_at(4)
    d.remove_at(6)
    d.remove_at(0)
    
    d.remove(4)
    
    d.insert(3, 4)

    
    print(d)
    d.reverse()
    print(d)
    print(f'The size of double linked list is: {len(d)}')