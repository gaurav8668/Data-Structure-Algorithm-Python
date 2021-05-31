class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
        self.prev = None 
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None 
    
    def insert_node_at_beg(self, data):
        new_node = Node(data)
        new_node.prev = self.head
        new_node.next = self.head
        self.head = new_node
    
    def insert_node_at_end(self, data):
        if self.head == None:
            self.insert_node_at_beg(data)
            return
        
        current = self.head 
        while current.next:
            current = current.next 
        
        new_node = Node(data)
        current.next = new_node 
        new_node.next = None 
        new_node.prev = current.next 
    
    def size(self):
        try:
            if self.head == None:
                return 
            count = 0
            current = self.head
            while current:
                count += 1
                current = current.next 
            return count

        except Exception as e:
            print("Exception is: ", e)

    
    def insert_node_at_index(self, data, index):
        try:
            if index > self.size():
                print("Please give the valid index")
            if index == 0:
                new_node = Node(data)
                new_node.prev = None
                new_node.next = self.head 
                self.head = new_node
                return

            current = self.head 
            count = 0
            while current:
                if count == index - 1:
                    new_node = Node(data)
                    new_node.next = current.next
                    new_node.prev = current
                    break
                else:
                    count += 1
                    current = current.next

        except Exception as e:
            print("Exception is: ", e)
        


    def print(self):
        if self.head == None:
            print("Doubly Linked List is empty")
        c = self.head 
        str_dll = ''
        while c:
            str_dll += str(c.data) + "----->"
            c = c.next
        return str_dll
    
    def __str__(self):
        return "This is Doubly Linked List Class"

dll = DoublyLinkedList()
# dll.insert_node_at_beg(45)
# dll.insert_node_at_beg(50)
# dll.insert_node_at_beg(78)
# dll.insert_node_at_end(42)
# dll.insert_node_at_end(10)
# dll.insert_node_at_end(56)
# dll.insert_node_at_index(100, 1)
# print(dll.size())
# print(dll.print())
print(dll)