import time 

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " took " + str((end-start)*1000) + " mil sec")
        return result
    return wrapper

@time_it
def linear_search(numbers_list, number_to_find):
    for index, number in enumerate(numbers_list):
        if number == number_to_find:
            return index
    return -1

@time_it
def binary_search(numbers_list, number_to_find):
    left_index = 0
    right_index = len(numbers_list) - 1
    mid_index = 0

    while left_index < right_index: 
        mid_index = (left_index + right_index) // 2
        mid_number = numbers_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index + 1
        
        else:
            right_index = mid_index - 1
        
    return -1

def binary_search_recursive(numbers_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1
    
    mid_index = (left_index + right_index) // 2

    if mid_index >= len(numbers_list) or mid_index < 0:
        return -1

    mid_number = numbers_list[mid_index] 

    if mid_number == number_to_find:
        return mid_index 
    
    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1
        
    return binary_search_recursive(numbers_list, number_to_find, left_index, right_index)

def count_element_in_array(numbers, number_to_find):
    # count = 0

    # for i in numbers_list:
    #     if i == number_to_count:
    #         count += 1
        
    index = binary_search(numbers, number_to_find)
    indices = [index]
    # find indices on left hand side
    i = index-1
    while i >=0:
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i - 1

    # find indices on right hand side
    i = index + 1
    while i<len(numbers):
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i + 1

    return sorted(indices)

 
if __name__ == '__main__':
    # numbers_list = [12, 15, 17, 19, 21, 24, 45, 67]
    # number_to_find =  12
    
    numbers_list = [1,4,6,9,11,15,15,15,17,21,34,34,56]
    number_to_count = 34

    # numbers_list = [1,4,6,9,10,5,7]
    # number_to_find = 5

    # numbers_list = [i for i in range(1000000)]
    # number_to_find = 1000000

    # index = linear_search(numbers_list, number_to_find)
    # index_binary = binary_search(numbers_list, number_to_find)
    # print("Number found at index {} using binary search".format(index_binary))

    # index_linear = linear_search(numbers_list, number_to_find)
    # print("Number found at index {} using linear search".format(index_linear))

    # index_binary_recursive = binary_search_recursive(numbers_list, number_to_find, 0, len(numbers_list))
    # print("Number found at index {} using linear search".format(index_binary_recursive))

    print("The {} is present {} times in array".format(number_to_count, count_element_in_array(numbers_list, number_to_count)))