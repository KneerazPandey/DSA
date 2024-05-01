class Node(object):
    def __init__(self, val=0, next=None) -> None:
        self.val = val 
        self.next = next 
        
        

class Solution(object):
    def merge_two_lists(self, list1, list2):
        dummy = Node()
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1 
                list1 = list1.next 
            else:
                tail.next = list2
                list2 = list2.next 
            
            tail = tail.next 
            
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
            
        return dummy.next   
    
    @staticmethod
    def print_list(data):
        current = data
        if data == None:
            print("[ ]")
            return
        
        output = []
        while current:
            output.append(current.val)
            current = current.next 
            
        print(output)
    
    
    
list1 = Node(1)
a = Node(2)
b = Node(4)
list1.next = a 
a.next = b

list2 = Node(1)
x = Node(3)
y = Node(4)
list2.next = x 
x.next = y


s = Solution()
s.print_list(s.merge_two_lists(list1, list2))