class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def add_child(self, data):
        if data == self.data:
            return 
        
        if data < self.data:
            ## add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            ## add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)
            
    def in_order_traversal(self):
        element = []
    
        # visit left tree
        if self.left:
            element += self.left.in_order_traversal()
        
        ## visit base tree
        element.append(self.data)

        # visit right tree
        if self.right:
            element += self.right.in_order_traversal()

        return element
    
    def pre_oder_traversal(self):
        ## root left right
        element = []
        element.append(self.data)

        if self.left:
            element += self.left.pre_oder_traversal()
        
        if self.right:
            element += self.right.pre_oder_traversal()
        
        return element
    
    def post_tree_traversel(self):
        element = []

        if self.left:
            element += self.left.post_tree_traversel()
        if self.right:
            element += self.right.post_tree_traversel()
        element.append(self.data)

        return element
    
    def search(self, val):
        if self.data == val:
            return True
        
        if val < self.data:
            # value might be in left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False
        
        if  val > self.data:
            # value might be in right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False
        
    def min_value(self):
        element = self.in_order_traversal()
        return min(element)
    
    def max_value(self):
        element = self.in_order_traversal()
        return max(element)
    
    # def calculate_sum(self):
    #     left_sum = self.left.calculate_sum() if self.left else 0
    #     right_sum = self.right.calculate_sum() if self.right else 0
    #     print(self.data)
    #     return self.data + left_sum + right_sum
    
    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None 
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right
            # min_val = self.right.min_value()
            # self.data = min_val
            # self.right = self.right.delete(min_val)
            max_val = self.left.max_value()
            self.data = max_val
            self.left = self.left.delete(max_val)
        return self 

def build_tree(element):
    root = BinarySearchTree(element[0])

    for i in range(1, len(element)):
        root.add_child(element[i])
        
    return root 


if __name__ == '__main__':
    numbers  = [17, 4, 1, 20, 9, 23, 19, 34, 34, 9, 23]
    # countries = ["India", "Pakistan", "Germany", "USA", "China", "India", "UK","USA"]
    numbers_tree = build_tree(numbers)
    # countries_tree = build_tree(countries)
    # print(numbers_tree.in_order_traversal())
    # # print(numbers_tree.search(4))
    # print("The minimum value in the tree is: ", numbers_tree.min_value())
    # print("The maximum value in the tree is: ",  numbers_tree.max_value())
    # print("Thre in in-order-traversal tree is: ", numbers_tree.in_order_traversal())
    # print("The pre-traversal-tree is: ", numbers_tree.pre_oder_traversal())
    # print("The post-traversal-tree is: ", numbers_tree.post_tree_traversel())
    # print("The total sum of the tree is: ", numbers_tree.calculate_sum())
    # print(countries_tree.in_order_traversal())
    # print("UK is in the list? ", countries_tree.search("UK"))
    # print("Sweden is in the list? ", countries_tree.search("Sweden"))
    numbers_tree.delete(20)
    print("After deleting 20 ", numbers_tree.in_order_traversal())
 