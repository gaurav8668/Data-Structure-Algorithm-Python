def merge_sort(list):
    """ 
    Sorts a list in a ascending order 
    Returs a new sorted list
    
    Divide: Find the midpoint of the list and divide into sublists
    Conquer: Recursiveely sort the sublists created in previous step
    Combbine: Merge the sorted sublists created in previous step
    
    Takes O(kn log n) time
    """
    
    if len(list) <= 1:
        return list 
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    return merge(left, right)
    
def split(list):
    """
    Divide the unsorted list at midpoint into sublists 
    Returns two sublists - left and right 
    
    Takes overall O(k log n) time
    """
    midpoint = len(list) // 2
    left = list[:midpoint]
    right = list[midpoint:]

    return left, right
        
def merge(left, right):
    """
    Merges two lists (arrays) sorting them in the process 
    Returns a new merged list
    
    Runs in overall O(n) time 
    """
    
    l = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            l.append(right[j])
            j += 1
        else:
            l.append(left[i])
            i += 1
        
    while i < len(left):
        l.append(left[i])
        i += 1
        
    while j < len(right):
        l.append(right[j])
        j += 1
    
    # l += left[i:]
    # l += right[j:]
    return l


def verify(list):
    n = len(list)
    
    if n == 0 or n == 1:
        return True 
        
    return list[0] < list[1] and verify(list[1:])
        
    

alist = [54, 62, 93, 17, 77, 31 , 44, 55, 20]
result = merge_sort(alist)
print(result)
print(verify(result))