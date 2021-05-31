import random 
import sys 

def is_sorted(values):
    for index in range(len(values) - 1): 
        if values[index] > values[index + 1]:
            return False 
    return True 

def bogo_sort(values):
    attempts = 0
    while not is_sorted(values):
        random.shuffle(values)
        attempts += 1
    return values, attempts

values = [5, 4, 8, 7, 111, 45, 9, 1, 0]
values, attempts = bogo_sort(values)

print(values)
print("The number of steps taken to sort the list is: {}".format(attempts))