def quicksort(values):
    if len(values) <= 1:
        return values
        
    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]
    
    for j in range(1, len(values)):
        if pivot >= values[j]:
            less_than_pivot.append(values[j])
        else:
            greater_than_pivot.append(values[j])

    print("%15s %1s %15s" % (less_than_pivot, pivot, greater_than_pivot))
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)
    
numbers = [5, 7, 1, 2, 6, 8, 6, 3]
sorted_numbers = quicksort(numbers)
print(sorted_numbers)


# --------------------------------------------------------------------------------------------------------------------------------------------

# def swap(a, b, arr):
#     if a != b:
#         tmp = arr[a]
#         arr[a] = arr[b]
#         arr[b] = tmp 

# def partition(elements, start, end):
#     pivot_index = start
#     pivot = elements[pivot_index]

#     while start < end:
#         while start < len(elements) and elements[start] <= pivot:
#             start += 1
        
#         while elements[end] > pivot:
#             end -= 1

#         if start < end:
#             swap(start, end, elements)
    
#     swap(pivot_index, end, elements)

#     return end

# def quick_sort(elements, start, end):
#     if start < end:
#         pi = partition(elements, start, end)
#         quick_sort(elements, start, pi - 1)     # left partition
#         quick_sort(elements, pi + 1, end)       # right partition

# if __name__ == '__main__':
#     elements = [11, 9, 29, 7, 2, 15, 28]
#     quick_sort(elements, 0, len(elements) - 1)
#     print(elements)



