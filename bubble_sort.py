def bubble_sort(elements, key=None):
    size = len(elements)

    if key == 'transaction_amount':
        for i in range(size - 1):
            swapped = False
            for j in range(size - 1 - i):
                if elements[j]['transaction_amount'] > elements[j + 1]['transaction_amount']:
                    tmp = elements[j]['transaction_amount']
                    elements[j]['transaction_amount'] = elements[j + 1]['transaction_amount']
                    elements[j + 1]['transaction_amount'] = tmp 
                    swapped = True

            if not swapped:
                break
            
    elif key == 'name':
        for i in range(size - 1):
            swapped = False
            for j in range(size - 1 - i):
                if elements[j]['name'] > elements[j + 1]['name']:
                    tmp = elements[j]['name']
                    elements[j]['name'] = elements[j + 1]['name']
                    elements[j + 1]['name'] = tmp 
                    swapped = True

            if not swapped:
                break

if __name__ == '__main__':
    # elements = [5, 9, 2, 1, 67, 34, 88, 34]
    # elements = [1, 2, 4]
    elements = [
        {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
        {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
        {'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
        {'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'}
    ]

    bubble_sort(elements, key='name')
    print(elements)