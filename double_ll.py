class Node:
    def __init__(self, prev=None, next=None, data=None):
        self.prev = prev
        self.next = next
        self.data = data
    

class DoubleLL:
    def __init__(self):
        self.head = None
    
    def add_element_beg(self, data):
        node = Node(data, self.head, self.head)
        self.head = node
    
    def print(self):
        if self.head == None:
            return
        
        itr = self.head 
        s = ''
        while itr:
            s += str(itr.data) + ' ---> '
            itr = itr.next
        print(s)
    
if __name__ == '__main__':
    dll = DoubleLL()
    dll.add_element_beg(5)
    dll.print()
