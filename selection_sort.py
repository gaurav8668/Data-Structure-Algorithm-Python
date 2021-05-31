def find_min_elements(arr):
    min = 1000000
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
    return min

def selection_sort(arr):
    size = len(arr)

    for i in range(size - 1):
        min_index = i
        for j in range(min_index + 1, size):
            if arr[j]['First Name'] < arr[min_index]['First Name']:
                min_index = j 
        if i != min_index:
            arr[i]['First Name'], arr[min_index]['First Name'] = arr[min_index]['First Name'], arr[i]['First Name']

if __name__ == '__main__':
    # elements = [78, 12, 15, 8, 61, 53, 23, 27]
    elements = [
        {'First Name': 'Raj', 'Last Name': 'Nayyar'},
        {'First Name': 'Suraj', 'Last Name': 'Sharma'},
        {'First Name': 'Karan', 'Last Name': 'Kumar'},
        {'First Name': 'Jade', 'Last Name': 'Canary'},
        {'First Name': 'Raj', 'Last Name': 'Thakur'},
        {'First Name': 'Kiran', 'Last Name': 'Sharma'},
        {'First Name': 'Armaan', 'Last Name': 'Kumar'},
        {'First Name': 'Jaya', 'Last Name': 'Sharma'},
        {'First Name': 'Ingrid', 'Last Name': 'Galore'},
        {'First Name': 'Armaan', 'Last Name': 'Seth'},
        {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
        {'First Name': 'Aahana', 'Last Name': 'Arora'}
    ]
    selection_sort(elements)
    print(elements)
    # print(find_min_elements(elements))

# --------------------------------------------------------------------------------------------------------------------------------------------

# a = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
a = [1, 2, 3, 4, 5]
sorted = []

def find_min(values):
    
    min_value = values[0]

    for i in range(1, len(a)):
        if values[i] < min_value:
            min_value = values[i]

    return min_value
    
def selection_sort(values):

    if len(values) == 0:
        return values
    
    if len(values) == 1:
        return sorted.append(values[0])
        
    min_value = find_min(values)
    
    sorted.append(min_value)
    values.remove(min_value)
    selection_sort(values)

    return sorted

test_cases = [
    [8, 5, 1, 4, 7, 3, 14, 156, 10, 45654, 500],
    # [],
    # [1, 2, 3, 4, 5],
    # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    ]
# for i in test_cases:
#     print(i)
#     print(selection_sort(i))
print(selection_sort(a))
