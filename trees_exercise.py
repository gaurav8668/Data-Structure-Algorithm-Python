# class TreeNode:
#     def __init__(self, name, designation):
#         self.name = name
#         self.designation = designation
#         self.childern = []
#         self.parent = None 
    
#     def add_child(self, child):
#         child.parent = self
#         self.childern.append(child)
    
#     def get_level(self):
#         level = 0
#         p = self.parent

#         while p:
#             level += 1
#             p = p.parent
#         return level

#     def print_tree(self, property_name):
#         if property_name == 'both':
#             value = self.name + " (" + self.designation + ")"
#         elif property_name == 'name':
#             value = self.name
#         else:
#             value = self.designation

#         spaces = ' ' * self.get_level() * 3
#         prefix = spaces + "|_" if self.parent else ""
#         print(prefix + value)

#         if self.childern:  # or len(self.children) > 0
#             for child in self.childern:
#                 child.print_tree(property_name)

# def build_product_tree():
#     head = TreeNode('Vishwa', 'Infrastructure Haad')
#     head.add_child(TreeNode('Dhaval', 'Cloud Manager'))
#     head.add_child(TreeNode('Abhijit', 'App Manager'))
    
#     cto = TreeNode('Chinmay', 'CTO')
#     cto.add_child(head)
#     cto.add_child(TreeNode('Aamir', 'Application Head'))

#     gels = TreeNode('Gels', 'HR Head')
#     gels.add_child(TreeNode('Peter', 'Recruitment Manager'))
#     gels.add_child(TreeNode('Waqas', 'Policy Manager'))

#     ceo = TreeNode('Nilpul', 'CEO')
#     ceo.add_child(cto)
#     ceo.add_child(gels)

#     return ceo


# if __name__ == '__main__':
#     root = build_product_tree()
#     root.print_tree("name")
#     root.print_tree("designation")
#     root.print_tree("both")





class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None 
    
    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        level = 0
        p = self.parent 
        while p:
            level += 1
            p = p.parent
        return level 

    def print_tree(self, level):
        if level == 0:
            print(self.parent)
        spaces = ' ' * self.get_level() * 3
        prefix = spaces +  '|__' if self.parent else ""
        print(prefix + self.data) 

        if self.children:
            for child in self.children:
                child.print_tree()
    
def buld_location_tree():
    guj = TreeNode('Gujraj')
    guj.add_child(TreeNode('Ahmedabad'))
    guj.add_child(TreeNode('Baroda'))

    kar = TreeNode('Karnataka')
    kar.add_child(TreeNode('Bangluru'))
    kar.add_child(TreeNode('Mysore'))

    ind = TreeNode('India')
    ind.add_child(guj)
    ind.add_child(kar)

    new_je = TreeNode('New Jersy')
    new_je.add_child(TreeNode('Princeton'))
    new_je.add_child(TreeNode('Trenton'))

    cal = TreeNode('California')
    cal.add_child(TreeNode('San Francisco'))
    cal.add_child(TreeNode('Mountain View'))
    cal.add_child(TreeNode('Palo Alto'))

    usa = TreeNode('USA')
    usa.add_child(new_je)
    usa.add_child(cal)

    glb = TreeNode('Global')
    glb.add_child(ind)
    glb.add_child(usa)

    return glb




if __name__ == '__main__':
    r = buld_location_tree()
    r.print_tree()
