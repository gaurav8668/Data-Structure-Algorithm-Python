class Node:
    """
        This is the class node, because every element in the linked list stores in the form of node
    """

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next    

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self, data):
        """
            This function will insert the node at the begnining of the linked list
        """

        node = Node(data, self.head)
        self.head = node  
    
    def print(self):
        """
            This function will print the values that are present inside linked list
        """

        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + ' ----> '
            itr = itr.next
        
        return llstr
    
    def reverse_linked_list(self):
        """
            This function will reverse the linked list
        """

        l = []
        current = self.head 
        
        while current:
            l.append(current.data)
            current = current.next
        print("Linked List after reversing the values: ", end=" ")
        for i in reversed(l):
            print(i, end=" ----> ")
        
        # return rllstr
    
    def swap_at_k(self, k):
        """
            This function will swap the value of the (start + k) to (end - k) and viseversa
        """

        size = self.get_length()

        a = self.head
        b = self.head
        
        y = []
        x = []

        i = 0
        j = 0

        if k > size or k <= 0:
            print("Invalid index: {}".format(k))
    
        elif self.head == None:
            print("Linked List is Empty")

        elif  size == 1:
            return self.head

        else:
            while a:
                if i == k  - 1:
                    x.append(a.data)
                    break
                a = a.next
                i += 1
            
            while b:
                if j == (size - k):
                    y.append(b.data)
                    break
                b = b.next 
                j += 1
            
            while a:
                if i == k - 1:
                    a.data = y[0]
                    break
                a = a.next 
                i += 1
            
            while b:
                if j == (size - k):
                    b.data = x[0]
                    break 
                b = b.next
                j +=1

    def insert_at_end(self, data):
        """
            This function will insert the node at the end of the linked list
        """

        if self.head == None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)

    def insert_value(self, data_lst):
        """
            This function will insert the list of value at the end of the linked list
        """

        self.head = None
        for data in data_lst:
            self.insert_at_end(data)

    def get_length(self):
        """
            This function will calculate the length of the linked list
        """

        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def remove_at(self, index):
        """
            This function will remove the node from the kth index
        """

        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
        
    def insert_at(self, index, data):
        """
            This function will insert the node at the kth index
        """

        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
        
        if index == 0:
            self.insert_at_begining(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break                

            itr = itr.next
            count += 1
        
    def insert_after_value(self, data_after, data_to_insert):
        """
            This function will insert the node after the value
        """

        if data_after not in ["banana", "mango", "grapes", "orange"]:
            print("Please enter a valid data")

        else:
            itr = self.head
            while itr:
                if itr.data == data_after:
                    itr.next = Node(data_to_insert, itr.next)
                    break
                itr = itr.next
            
    def remove_by_value(self, data):
        """
            This function will remove the the node by value
        """

        if data == 'banana':
            self.head = self.head.next
        else:
            itr = self.head
            while itr:
                if itr.next.data == data:
                    itr.next  = itr.next.next
                    break

                itr = itr.next



if __name__ == '__main__':
    ll = LinkedList()
    # ll.insert_at_begining(1)
    # ll.insert_at_begining(2)
    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)
    ll.insert_at_end(4)
    ll.insert_at_end(5)
    ll.insert_at_end(6)
    ll.insert_at_end(7)
    ll.insert_at_end(8)
    ll.insert_at_end(9)
    print("Original Linked list: ", ll.print())
    ll.swap_at_k(2)
    print()
    print("Linked List after swapping the values: ", ll.print())
    print()
    ll.reverse_linked_list()


    # ll.insert_at_end(79)
    # ll.insert_at_end(1)
#     # ll.insert_at_end(65)
#     ll.insert_value(["banana", "mango", "grapes", "orange"])
    # ll.print()
#     # print("Length: ", ll.get_length())
#     # ll.remove_at(1)
#     # print(ll.insert_at(2, "figs"))
#     # ll.print()
#     # ll.insert_after_value("banana", "apple")
#     ll.remove_by_value('mango')
#     ll.print()

## ============================================================================================================================================

# class Node:
#     """
#      An object for storing a single node of a linked list.
#      Model two attributes - data and the link to the next node in the list 
#      """
#     data = None 
#     next_node = None
     
#     def __init__(self, data):
#         self.data = data
    
#     # def __repr__(self):
#         # return "Node data: {}".format(self.data)
        
#     def __str__(self):
#         return "Node data: {}".format(self.data)
    
# class LinkedList:
#     """
#     Single Linked List
#     """
    
#     def __init__(self):
#         self.head = None
    
#     def is_empty(self):
#         return self.head == None 
    
#     def add(self, data):
#         """ 
#         Adds a new node containing data at head of the list 
#         """
#         new_node = Node(data)
#         new_node.next_node = self.head
#         self.head = new_node
    
#     def print_val(self):
#         if self.head == None:
#             return "Linked LIst is empty"
        
#         current = self.head
#         s = ""
#         while current:
#             s += str(current.data) + "---->"
#             current = current.next_node
        
#         return s
    
#     def search(self, key):
#         """
#         Search for the first node that mathces a key
#         Returns the node or 'None' if not found
#         Takes 0(n) time
#         """
        
#         current = self.head
        
#         while current:
#             if current.data == key:
#                 return current
#             else:
#                 current = current.next_node
#         return None 
    
#     def insert(self, data, index):
#         """
#         Inserts a new Node containing data at index position 
#         Insertion takes O(1) time but finding the node at the 
#         insertion point takes O(n) time.
#         Takes overall O(n) times
#         """
#         if index == 0:
#             self.add(data)
            
#         # if index > 0:
            
#         current = self.head
#         i = 0
#         while current:
#             if i == index - 1:
#                 new_node = Node(data)
#                 new_node.next_node = current.next_node
#                 current.next_node = new_node
#                 # new_node.next_node = current.next_node.next_node
#                 break
            
#             current = current.next_node
#             i = i + 1
    
#     def delete(self, index):
#         """
#         Removes Node containing data that mathces the key
#         Returns the node or None if key doesn't exist 
#         Takes O(n) time
#         """
        
#         if self.head == None:
#             raise Exception("Linked List is Empty")
#         if index == 0:
#             self.head = self.head.next_node
#         current = self.head
#         count = 0
#         while current:
#             if count == index - 1:
#                 current.next_node = current.next_node.next_node
#                 break
#             current = current.next_node
#             count += 1
        
#     def node_at_index(self, index):
#         if index == 0:
#             return self.head 
#         else:
#             current = self.head 
#             i = 0

#             while i < index: 
#                 current = current.next_node
#                 i += 1
            
#             return current

#     def __str__(self):
#         nodes = []
#         current = self.head
        
#         while current:
#             if current is self.head:
#                 nodes.append("[Head: %s]" % current.data)
#             elif current.next_node is None:
#                 nodes.append("[Tail: %s]" % current.data)
#             else:
#                 nodes.append("[%s]" % current.data)
#             current = current.next_node
        
#         return '--> '.join(nodes)
        
#     def size(self):
#         """
#         Returns the number of nodes in the list
#         Take 0(n) time
#         """
        
#         current = self.head
#         count = 0
        
#         while current:
#             count += 1
#             current = current.next_node
        
#         return count
            
    
    
    
# l = LinkedList()
# l.add(10)
# l.add(200)
# l.add(45)
# l.add(50)
# l.add(78)
# print(l.print_val())
# print(l.search(10))
# search = l.search(200)
# print(search)
# print(l)
# print(l.insert(1, 2))
# print(l.node_at_index(3))
# print(l)
# print(l.size())
        